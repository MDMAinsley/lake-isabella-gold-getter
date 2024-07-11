import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

ENTER = 0x1C
NUMPADEIGHT = 0x48
NUMPADFIVE = 0x4C
NUMPADTWO = 0x50

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

# // Listed are keyboard scan code constants, taken from dinput.h

# define DIK_ESCAPE          0x01
DIK_1 = 0x02
DIK_2 = 0x03
DIK_3 = 0x04
DIK_4 = 0x05
DIK_5 = 0x06
DIK_6 = 0x07
DIK_7 = 0x08
DIK_8 = 0x09
DIK_9 = 0x0A
DIK_0 = 0x0B
DIK_MINUS = 0x0C  # /* - on main keyboard */
# define DIK_EQUALS          0x0D
# define DIK_BACK            0x0E    /* backspace */
# define DIK_TAB             0x0F
DIK_Q = 0x10
DIK_W = 0x11
DIK_E = 0x12
DIK_R = 0x13
DIK_T = 0x14
DIK_Y = 0x15
DIK_U = 0x16
DIK_I = 0x17
DIK_O = 0x18
DIK_P = 0x19
DIK_LBRACKET = 0x1A
# define DIK_RBRACKET        0x1B
# define DIK_RETURN          0x1C    /* Enter on main keyboard */
# define DIK_LCONTROL        0x1D
DIK_A = 0x1E
DIK_S = 0x1F
DIK_D = 0x20
DIK_F = 0x21
DIK_G = 0x22
DIK_H = 0x23
DIK_J = 0x24
DIK_K = 0x25
DIK_L = 0x26
DIK_SEMICOLON = 0x27
DIK_APOSTROPHE = 0x28
# define DIK_GRAVE           0x29    /* accent grave */
DIK_LSHIFT = 0x2A
# define DIK_BACKSLASH       0x2B
DIK_Z = 0x2C
DIK_X = 0x2D
DIK_C = 0x2E
DIK_V = 0x2F
DIK_B = 0x30
DIK_N = 0x31
DIK_M = 0x32
DIK_COMMA = 0x33
DIK_PERIOD = 0x34  # /* . on main keyboard */
DIK_SLASH = 0x35  # /* / on main keyboard */
# define DIK_RSHIFT          0x36
# define DIK_MULTIPLY        0x37    /* * on numeric keypad */
# define DIK_LMENU           0x38    /* left Alt */
DIK_SPACE = 0x39
# define DIK_CAPITAL         0x3A
# define DIK_F1              0x3B
# define DIK_F2              0x3C
# define DIK_F3              0x3D
# define DIK_F4              0x3E
# define DIK_F5              0x3F
# define DIK_F6              0x40
# define DIK_F7              0x41
# define DIK_F8              0x42
# define DIK_F9              0x43
# define DIK_F10             0x44
# define DIK_NUMLOCK         0x45
# define DIK_SCROLL          0x46    /* Scroll Lock */
# define DIK_NUMPAD7         0x47
# define DIK_NUMPAD8         0x48
# define DIK_NUMPAD9         0x49
# define DIK_SUBTRACT        0x4A    /* - on numeric keypad */
# define DIK_NUMPAD4         0x4B
# define DIK_NUMPAD5         0x4C
# define DIK_NUMPAD6         0x4D
# define DIK_ADD             0x4E    /* + on numeric keypad */
# define DIK_NUMPAD1         0x4F
# define DIK_NUMPAD2         0x50
# define DIK_NUMPAD3         0x51
# define DIK_NUMPAD0         0x52
# define DIK_DECIMAL         0x53    /* . on numeric keypad */
# define DIK_F11             0x57
# define DIK_F12             0x58
# define DIK_F13             0x64    /*                     (NEC PC98) */
# define DIK_F14             0x65    /*                     (NEC PC98) */
# define DIK_F15             0x66    /*                     (NEC PC98) */

# define DIK_KANA            0x70    /* (Japanese keyboard)            */
# define DIK_CONVERT         0x79    /* (Japanese keyboard)            */
# define DIK_NOCONVERT       0x7B    /* (Japanese keyboard)            */
# define DIK_YEN             0x7D    /* (Japanese keyboard)            */
# define DIK_NUMPADEQUALS    0x8D    /* = on numeric keypad (NEC PC98) */
# define DIK_CIRCUMFLEX      0x90    /* (Japanese keyboard)            */
# define DIK_AT              0x91    /*                     (NEC PC98) */
# define DIK_COLON           0x92    /*                     (NEC PC98) */
# define DIK_UNDERLINE       0x93    /*                     (NEC PC98) */
# define DIK_KANJI           0x94    /* (Japanese keyboard)            */
# define DIK_STOP            0x95    /*                     (NEC PC98) */
# define DIK_AX              0x96    /*                     (Japan AX) */
# define DIK_UNLABELED       0x97    /*                        (J3100) */
# define DIK_NUMPADENTER     0x9C    /* Enter on numeric keypad */
# define DIK_RCONTROL        0x9D
# define DIK_NUMPADCOMMA     0xB3    /* , on numeric keypad (NEC PC98) */
# define DIK_DIVIDE          0xB5    /* / on numeric keypad */
# define DIK_SYSRQ           0xB7
# define DIK_RMENU           0xB8    /* right Alt */
# define DIK_HOME            0xC7    /* Home on arrow keypad */
# define DIK_UP              0xC8    /* UpArrow on arrow keypad */
# define DIK_PRIOR           0xC9    /* PgUp on arrow keypad */
# define DIK_LEFT            0xCB    /* LeftArrow on arrow keypad */
# define DIK_RIGHT           0xCD    /* RightArrow on arrow keypad */
# define DIK_END             0xCF    /* End on arrow keypad */
# define DIK_DOWN            0xD0    /* DownArrow on arrow keypad */
# define DIK_NEXT            0xD1    /* PgDn on arrow keypad */
# define DIK_INSERT          0xD2    /* Insert on arrow keypad */
# define DIK_DELETE          0xD3    /* Delete on arrow keypad */
# define DIK_LWIN            0xDB    /* Left Windows key */
# define DIK_RWIN            0xDC    /* Right Windows key */
# define DIK_APPS            0xDD    /* AppMenu key */

if __name__ == "__main__":
    while True:
        time.sleep(1)
