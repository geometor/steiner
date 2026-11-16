"""Pytest configuration and environment bootstrapping for GEOMETOR Steiner."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent

for _p in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "divine" / "src",
    _WORKSPACE_ROOT / "pappus" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
