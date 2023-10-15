# Text color
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Background color
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Formatting
RESET = '\033[0m'
BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m'  # Not widely supported
UNDERLINE = '\033[4m'
BLINK = '\033[5m'    # Slow blink, not widely supported
INVERT = '\033[7m'
CONCEAL = '\033[8m'  # Hidden

# Cursor movement and clearing
CURSOR_HOME = '\033[H'
CLEAR_SCREEN = '\033[2J'
CLEAR_TO_END_OF_LINE = '\033[K'
CURSOR_UP = '\033[A'
CURSOR_DOWN = '\033[B'
CURSOR_FORWARD = '\033[C'
CURSOR_BACKWARD = '\033[D'
