# Standard Library
import sys

if 'test' in sys.argv:
    print('\033[1;91mNo django tests.\033[0m')
    print('Try: \033[1;33mpytest\033[0m')
    sys.exit(0)
