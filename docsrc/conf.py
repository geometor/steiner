"""Sphinx configuration for Jakob Steiner."""

from __future__ import annotations

import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.steiner as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "steiner"
repo_name = "steiner"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

# Restrict intersphinx_mapping strictly to offline local inventories present on disk:
for _key in list(intersphinx_mapping.keys()):  # noqa: F405
    _entry = intersphinx_mapping[_key]  # noqa: F405
    _target = _entry[1] if isinstance(_entry, tuple) and len(_entry) >= 2 else None
    _local_file = _target[0] if isinstance(_target, tuple) and _target else _target
    if not (isinstance(_local_file, str) and Path(_local_file).is_file()):
        intersphinx_mapping.pop(_key, None)  # noqa: F405

for _sister in (
    "euclid",
    "elements",
    "divine",
    "knott",
    "etc",
    "pacioli",
    "model",
    "explorer",
):
    if _sister == repo:
        continue
    _inv = _WORKSPACE_ROOT / _sister / "docs" / "objects.inv"
    if _inv.is_file():
        intersphinx_mapping[_sister] = (  # noqa: F405
            f"https://geometor.github.io/{_sister}",
            (os.fspath(_inv), None),
        )

html_theme = "foundation"
site_title = "Jakob Steiner"
html_title = f"{site_title} • {org_name}"
blog_title = site_title
project = site_title
html_static_path: list[str] = ["_static"]
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
napoleon_use_ivar = True
for _excl in ("intro.rst", "modules/api/geometor/steiner/index.rst"):
    if _excl not in exclude_patterns:  # noqa: F405
        exclude_patterns.append(_excl)  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
