"""Autonomus API default settings."""

import os
from pathlib import Path

# Server environment and application settings.
DEBUG = not os.getenv("GAE_ENV", "").startswith("standard")
APP_NAME = "Autonomus"
PROJECT_ID = APP_NAME.lower()
NAMESPACE = "development"

# Miscellaneous.
TIMEOUT = 10
ENCODING = "utf-8"

# Paths.
PROJECT_DIR = Path(__file__).parent.parent
WORK_DIR = Path(f"~/Work/{APP_NAME}").expanduser()
