"""The ledger gate and the exercise-calibration gate."""
import os
import pathlib
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import check_exercise_calibration as cal  # noqa: E402
import check_ledger  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_repo_ledger_is_clean():
    errors, nrows = check_ledger.check([str(ROOT / "parts")])
    assert errors == []
    assert nrows > 100


def test_ledger_unknown_id_and_free_text(tmp_path):
    f = tmp_path / "x.tex"
    f.write_text("% ledger: aw:Fe, const:F (rounded; see text)\n"
                 "% ledger: nosuch:row\n"
                 "% ledger: not an id\n")
    errors, _ = check_ledger.check([str(f)])
    assert len(errors) == 2
    assert "nosuch:row has no row" in errors[0]
    assert "not a ledger id" in errors[1]


def _chapter(stars, problem_items=None):
    s = "".join("\\begin{exercise}[$%s$]\\label{exo:x:%d}\\end{exercise}\n"
                % ("\\star" * k, i) for i, k in enumerate(stars))
    if problem_items is not None:
        s += ("\\begin{problem}[{Weekend problem}]\\begin{enumerate}"
              + "\\item q\n" * problem_items
              + "\\item with parts \\begin{enumerate}\\item a \\item b\\end{enumerate}\n"
              + "\\end{enumerate}\\end{problem}\n")
    return s


def test_calibration_bands(tmp_path):
    f = tmp_path / "01-x.tex"
    f.write_text(_chapter([1] * 4 + [2] * 5 + [3] * 3, 24))     # 25 questions
    assert cal.check_file(f, cal.band("bachelor-2")) == []
    assert cal.check_file(f, cal.band("grade-11"))               # 12 exercises, wrong ramp
    f.write_text(_chapter([1] * 4 + [3] + [2] * 5 + [3] * 2, 24))
    assert any("decrease" in m for m in cal.check_file(f, cal.band("bachelor-1")))
    f.write_text(_chapter([1] * 8 + [2] * 2, 5))
    assert cal.check_file(f, cal.band("grade-3")) == ["this band has no weekend problem"]
    f.write_text("\\chapter{x}\n\\noindent\\emph{To be written.}\n")
    assert cal.check_file(f, cal.band("bachelor-3")) == []       # placeholder skipped
