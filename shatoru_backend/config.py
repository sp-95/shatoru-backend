import os
from distutils.util import strtobool
from pathlib import Path

APP_ROOT = Path(str(Path(__file__).parent.parent.absolute()))
DEBUG_MODE = strtobool(os.environ.get("DEBUG", "False"))
LOG_PATH = APP_ROOT / "logs"
