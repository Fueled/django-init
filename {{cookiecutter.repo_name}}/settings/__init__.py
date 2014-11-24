# -*- coding: utf-8 -*-

import sys

if "test" in sys.argv:
    print("\033[1;91mNo django tests.\033[0m")
    print("Try: \033[1;33mpy.test\033[0m")
    sys.exit(0)

from .development import Development  # noqa
from .production import Production  # noqa
from .testing import Testing  # noqa
