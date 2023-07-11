class UsageError(Exception):
    """Error in plugin usage."""

    __module__ = "builtins"


try:
    from vcr.persisters.filesystem import CassetteNotFoundError
except ImportError:

    class CassetteNotFoundError(ValueError):
        """Retain compatibility with vcr.py<5"""


try:
    from vcr.persisters.filesystem import CassetteDecodeError
except ImportError:

    class CassetteDecodeError(ValueError):
        """Retain compatibility with vcr.py<5"""


__all__ = ["UsageError", "CassetteNotFoundError", "CassetteDecodeError"]
