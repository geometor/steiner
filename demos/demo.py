"""Minimal demonstration script for ``geometor.steiner``."""

from __future__ import annotations

from geometor.steiner import __version__, run


def main() -> int:
    """Run the package demonstration and report version metadata.

    Returns:
        Exit status code from :func:`run`.
    """
    print(f"geometor.steiner v{__version__}")
    return run([])


if __name__ == "__main__":
    raise SystemExit(main())
