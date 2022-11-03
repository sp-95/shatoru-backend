from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

from shatoru_backend.core.logger import setup_loggers

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "shatoru-backend"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


setup_loggers()
