"""Comprehensive test suite for ``geometor.steiner``."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.steiner import (
    __version__,
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

    # Diameter is along x-axis (y = 0), so perpendicular must be parallel to y-axis
    p1 = spg.Point(2, 1)
    p2 = spg.Point(2, 5)
    assert res.perpendicular_line.is_parallel(spg.Line(p1, p2))

    # Verify no floats in points
    for pt in res.model.points:
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_steiner_harmonic_conjugate() -> None:
    """Verify complete quadrangle construction of fourth harmonic point."""
    a_pt = (sp.Rational(0), sp.Rational(0))
    b_pt = (sp.Rational(4), sp.Rational(0))
    c_pt = (sp.Rational(3), sp.Rational(0))

    res = steiner_harmonic_conjugate(a_pt, b_pt, c_pt)
    # (A, B; C, D) = -1 -> D = 6
    assert res.d.equals(spg.Point(6, 0))
    assert res.cross_ratio == -1


def test_steiner_centers_of_similitude() -> None:
    """Verify exact centers of similitude between two circles."""
    m1 = (sp.Rational(0), sp.Rational(0))
    r1 = sp.Rational(2)
    m2 = (sp.Rational(6), sp.Rational(0))
    r2 = sp.Rational(4)

    ext_center, int_center = steiner_centers_of_similitude(m1, r1, m2, r2)

    # A = (2*6 - 4*0)/(2 - 4) = -6
    assert ext_center.equals(spg.Point(-6, 0))

    # I = (2*6 + 4*0)/(2 + 4) = 2
    assert int_center.equals(spg.Point(2, 0))


def test_steiner_radical_axis() -> None:
    """Verify exact radical axis of two circles."""
    m1 = (sp.Rational(0), sp.Rational(0))
    r1 = sp.Rational(3)
    m2 = (sp.Rational(6), sp.Rational(0))
    r2 = sp.Rational(3)

    rad = steiner_radical_axis(m1, r1, m2, r2)
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
    repo_root = Path(__file__).resolve().parents[1]
    persons_json = json.loads(
        (repo_root / "resources" / "persons.json").read_text(encoding="utf-8")
    )
    cites_json = json.loads(
        (repo_root / "resources" / "citations.json").read_text(encoding="utf-8")
    )
    glossary_json = json.loads(
        (repo_root / "resources" / "glossary.json").read_text(encoding="utf-8")
    )

    def to_slug(raw: str) -> str:
        s = raw.strip().lower()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s

    person_slugs = {to_slug(k) for k in persons_json}
    cite_slugs = {to_slug(k) for k in cites_json}
    term_slugs = {to_slug(k) for k in glossary_json}

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
                assert slug in person_slugs, (
                    f"Unresolved :person:`{raw_val}` -> '{slug}' in {rst_path}"
                )
            elif role == "cite":
                assert slug in cite_slugs, (
                    f"Unresolved :cite:`{raw_val}` -> '{slug}' in {rst_path}"
                )
            elif role == "term":
                assert slug in term_slugs, (
                    f"Unresolved :term:`{raw_val}` -> '{slug}' in {rst_path}"
                )


def test_codex_leaf_partition_and_plates() -> None:
    """Verify 5 containers, 51 4-track leaves, monotonic folios, and 26 paired plates/SVGs."""
    book_dir = Path(__file__).resolve().parents[1] / "docsrc" / "constructionen_1833"
    containers = ["overview", "chapter_01", "chapter_02", "chapter_03", "appendix"]

    leaf_dirs: list[Path] = []
    for cname in containers:
        cdir = book_dir / cname
        assert (cdir / "index.rst").exists(), f"Missing container index for {cname}"
        sub_leaves = sorted(p for p in cdir.iterdir() if p.is_dir())
        assert sub_leaves, f"No leaf directories in {cname}"
        # Sort by explicit :order: field
        sub_leaves.sort(
            key=lambda d: int(
                re.search(
                    r"^:order:\s*(\d+)",
                    (d / "index.rst").read_text(encoding="utf-8"),
                    re.M,
                ).group(1)
            )
        )
        leaf_dirs.extend(sub_leaves)

    assert len(leaf_dirs) == 51

    folios: list[int] = []
    for ldir in leaf_dirs:
        for track in ("index.rst", "de.rst", "summary.rst", "notes.rst"):
            tf = ldir / track
            assert tf.exists(), f"Missing track {tf}"
            text = tf.read_text(encoding="utf-8")
            assert ":folio:" in text, f"Missing :folio: badge in {tf}"
            assert ":layout: book" in text, f"Missing :layout: book in {tf}"
            assert ":tracks:" in text, f"Missing :tracks: header in {tf}"
        en_text = (ldir / "index.rst").read_text(encoding="utf-8")
        m = re.search(r"^:folio:\s*(\d{4})", en_text, re.M)
        assert m, f"Missing 4-digit folio in {ldir / 'index.rst'}"
        folios.append(int(m.group(1)))

    assert folios == sorted(folios), f"Non-monotonic folio progression: {folios}"

    # Verify all 26 PNG plates paired with 5-layer .euclid-graphic SVGs
    png_plates = sorted(book_dir.rglob("*.g*.png"))
    svg_plates = sorted(book_dir.rglob("*.g*.svg"))
    assert len(png_plates) == 26
    assert len(svg_plates) == 26
    for png_path in png_plates:
        svg_path = png_path.with_suffix(".svg")
        assert svg_path.exists(), f"Unpaired plate {png_path}"
        svg_text = svg_path.read_text(encoding="utf-8")
        for req_id in (
            'id="elements"',
            'id="graphics"',
            'id="highlights"',
            'id="points"',
            'id="labels"',
            'id="geom-tick-1"',
            'id="geom-tick-2"',
            'id="geom-tick-3"',
        ):
            assert req_id in svg_text, f"Missing {req_id} in {svg_path}"


def test_legacy_anchors_preserved() -> None:
    """Verify every legacy anchor from the flat 5-chapter codex still resolves cleanly."""
    book_dir = Path(__file__).resolve().parents[1] / "docsrc" / "constructionen_1833"
    all_rst = "\n".join(p.read_text(encoding="utf-8") for p in book_dir.rglob("*.rst"))
    required_anchors = [
        "constructionen_1833-index",
        "constructionen_1833-title-de",
        "steiner-01-en",
        "steiner-01-de",
        "steiner-01-summary",
        "steiner-01-notes",
        "steiner-en-s01",
        "steiner-de-s01",
        "steiner-en-s02",
        "steiner-de-s02",
        "steiner-02-en",
        "steiner-02-de",
        "steiner-02-summary",
        "steiner-02-notes",
        "steiner-en-s03",
        "steiner-de-s03",
        "steiner-en-s06",
        "steiner-de-s06",
        "steiner-en-s07",
        "steiner-de-s07",
        "steiner-03-en",
        "steiner-03-de",
        "steiner-03-summary",
        "steiner-03-notes",
        "steiner-en-s11",
        "steiner-de-s11",
        "steiner-en-s14",
        "steiner-de-s14",
        "steiner-04-en",
        "steiner-04-de",
        "steiner-04-summary",
        "steiner-04-notes",
        "steiner-en-aufgabe-1",
        "steiner-de-aufgabe-1",
        "steiner-en-aufgabe-2",
        "steiner-de-aufgabe-2",
        "steiner-en-aufgabe-3",
        "steiner-de-aufgabe-3",
        "steiner-en-aufgabe-4-5",
        "steiner-de-aufgabe-4-5",
        "steiner-05-en",
        "steiner-05-de",
        "steiner-05-summary",
        "steiner-05-notes",
        "steiner-en-aufgabe-6",
        "steiner-de-aufgabe-6",
        "steiner-en-aufgabe-7",
        "steiner-de-aufgabe-7",
        "steiner-en-aufgabe-8",
        "steiner-de-aufgabe-8",
        "steiner-en-schluss",
        "steiner-de-schluss",
    ]
    for anc in required_anchors:
        assert f".. _{anc}:" in all_rst, f"Missing legacy anchor .. _{anc}:"
