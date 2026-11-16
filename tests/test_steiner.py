"""Comprehensive test suite for ``geometor.steiner``."""

from __future__ import annotations

import re
import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.steiner import (
    __version__,
    clean_expr,
    exact_line_meet,
    pappus_steiner_star_points,
    run,
    steiner_centers_of_similitude,
    steiner_harmonic_conjugate,
    steiner_parallel_through_point,
    steiner_perpendicular_to_diameter,
    steiner_radical_axis,
)


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_exact_line_meet() -> None:
    """Verify exact line meet calculation without floating point."""
    l1 = spg.Line(spg.Point(0, 0), spg.Point(1, 1))
    l2 = spg.Line(spg.Point(0, 2), spg.Point(2, 0))
    pt = exact_line_meet(l1, l2)
    assert pt is not None
    assert pt.equals(spg.Point(1, 1))

    # Parallel lines meet at None
    l3 = spg.Line(spg.Point(0, 1), spg.Point(1, 2))
    assert exact_line_meet(l1, l3) is None


def test_steiner_parallel_through_point() -> None:
    """Verify Steiner Erste Aufgabe: straightedge parallel to diameter."""
    center = (sp.Rational(0), sp.Rational(0))
    radius = sp.Rational(2)
    p_ext = (sp.Rational(1), sp.Rational(3))

    res = steiner_parallel_through_point(center, radius, p_ext)

    # Verify parallel line passes through p_ext
    assert res.parallel_line.contains(spg.Point(1, 3))

    # Verify strictly parallel to diameter (meet is None)
    assert exact_line_meet(res.parallel_line, res.diameter) is None

    # Verify no floats in points
    for pt in res.model.points:
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_steiner_perpendicular_to_diameter() -> None:
    """Verify Steiner Dritte Aufgabe: straightedge perpendicular via orthocenter."""
    center = (sp.Rational(0), sp.Rational(0))
    radius = sp.Rational(5)
    p_ext = (sp.Rational(2), sp.Rational(1))

    res = steiner_perpendicular_to_diameter(center, radius, p_ext)

    # Verify perpendicular line passes through p_ext
    assert res.perpendicular_line.contains(spg.Point(2, 1))

    # Verify exact perpendicularity with diameter line (horizontal y=0 -> perp has x=constant)
    # Diameter is along x-axis (y = 0), so perpendicular must have direction parallel to y-axis
    p1 = spg.Point(2, 1)
    p2 = spg.Point(2, 5)
    assert res.perpendicular_line.is_parallel(spg.Line(p1, p2))

    # Verify no floats in points
    for pt in res.model.points:
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_steiner_harmonic_conjugate() -> None:
    """Verify complete quadrangle construction of fourth harmonic point."""
    A = (sp.Rational(0), sp.Rational(0))
    B = (sp.Rational(4), sp.Rational(0))
    C = (sp.Rational(3), sp.Rational(0))

    res = steiner_harmonic_conjugate(A, B, C)
    # (A, B; C, D) = -1
    # AC = 3, BC = -1 -> AC / BC = -3
    # AD / BD must equal 3 -> D / (D - 4) = 3 -> D = 3D - 12 -> 2D = 12 -> D = 6
    assert res.d.equals(spg.Point(6, 0))
    assert res.cross_ratio == -1


def test_steiner_centers_of_similitude() -> None:
    """Verify exact centers of similitude between two circles."""
    M1 = (sp.Rational(0), sp.Rational(0))
    R1 = sp.Rational(2)
    M2 = (sp.Rational(6), sp.Rational(0))
    R2 = sp.Rational(4)

    A, I = steiner_centers_of_similitude(M1, R1, M2, R2)

    # A = (2*6 - 4*0)/(2 - 4) = 12 / (-2) = -6
    assert A.equals(spg.Point(-6, 0))

    # I = (2*6 + 4*0)/(2 + 4) = 12 / 6 = 2
    assert I.equals(spg.Point(2, 0))


def test_steiner_radical_axis() -> None:
    """Verify exact radical axis of two circles."""
    M1 = (sp.Rational(0), sp.Rational(0))
    R1 = sp.Rational(3)
    M2 = (sp.Rational(6), sp.Rational(0))
    R2 = sp.Rational(3)

    rad = steiner_radical_axis(M1, R1, M2, R2)
    # Equal radii centered at x=0 and x=6 -> radical axis is x = 3
    assert rad.contains(spg.Point(3, 0))
    assert rad.contains(spg.Point(3, 5))


def test_pappus_steiner_star_points() -> None:
    """Verify Pappus S3 permutation family generates Steiner Star points S+, S-."""
    a_pts = (spg.Point(0, 0), spg.Point(1, 0), spg.Point(3, 0))
    b_pts = (spg.Point(0, 2), spg.Point(2, 3), spg.Point(4, 4))

    s_plus, s_minus, st_line = pappus_steiner_star_points(a_pts, b_pts)
    assert s_plus is not None
    assert s_minus is not None
    assert st_line is not None
    assert st_line.contains(s_plus)
    assert st_line.contains(s_minus)


def test_all_rst_apparatus_roles_resolve() -> None:
    """Verify all :person:, :cite:, and :term: roles in docsrc resolve to valid JSON entries."""
    import json
    from pathlib import Path

    repo_root = Path(__file__).resolve().parents[1]
    persons_json = json.loads((repo_root / "resources" / "persons.json").read_text(encoding="utf-8"))
    cites_json = json.loads((repo_root / "resources" / "citations.json").read_text(encoding="utf-8"))
    glossary_json = json.loads((repo_root / "resources" / "glossary.json").read_text(encoding="utf-8"))

    def to_slug(raw: str) -> str:
        s = raw.strip().lower()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s

    person_slugs = {to_slug(k) for k in persons_json.keys()}
    cite_slugs = {to_slug(k) for k in cites_json.keys()}
    term_slugs = {to_slug(k) for k in glossary_json.keys()}

    role_re = re.compile(r":(person|cite|term):`([^`]+)`")

    def extract_target(raw: str) -> str:
        m = re.search(r"<([^>]+)>", raw)
        target = m.group(1) if m else raw
        return to_slug(target)

    for rst_path in sorted((repo_root / "docsrc").rglob("*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        for role, raw_val in role_re.findall(text):
            slug = extract_target(raw_val)
            if role == "person":
                assert slug in person_slugs, f"Unresolved :person:`{raw_val}` -> '{slug}' in {rst_path}"
            elif role == "cite":
                assert slug in cite_slugs, f"Unresolved :cite:`{raw_val}` -> '{slug}' in {rst_path}"
            elif role == "term":
                assert slug in term_slugs, f"Unresolved :term:`{raw_val}` -> '{slug}' in {rst_path}"
