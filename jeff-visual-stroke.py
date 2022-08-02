# Jeff's Visual Stroke dictionary
import re

LONGEST_KEY = 2

SHOW_STROKE_TRIGGER = 'STR*Z'

PARTS_MATCHER = re.compile(
    r'(S?)(T?)(K?)(P?)(W?)(H?)(R?)(A?)(O?)([-*]?)(E?)(U?)(F?)(R?)(P?)(B?)(L?)(G?)(T?)(S?)(D?)(Z?)'
)

UNPRESSED_KEYS = [
    "🅂🅃🄿🄷🄾🄵🄿🄻🅃🄳",
    "🅂🄺🅆🅁🄾🅁🄱🄶🅂🅉",
    "🄰🄾🄴🅄",
]

PRESSED_KEYS = [
    "🆂🆃🅿🅷🅾🅵🅿🅻🆃🅳",
    "🆂🅺🆆🆁🅾🆁🅱🅶🆂🆉",
    "🅰🅾🅴🆄",
]

SPACE_PRE_STAR = " "
SPACE_POST_STAR = " "
SPACE_PRE_VOWELS = "　　　"
SPACE_BETWEEN_VOWELS = " "
NEWLINE = "\n"

def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    if SHOW_STROKE_TRIGGER != key[0]:
        raise KeyError
    if len(key) == 1:
        return ' '

    stroke = key[1]
    match = PARTS_MATCHER.fullmatch(stroke)
    if not match:
        raise KeyError

    (s1, t1, k, p1, w, h, r1, a, o, star, e, u, f,
     r2, p2, b, l, g, t2, s2, d, z) = match.groups()

    result = []

    result.append(NEWLINE)

    # First row
    result.append(PRESSED_KEYS[0][0] if s1 != '' else UNPRESSED_KEYS[0][0])
    result.append(PRESSED_KEYS[0][1] if t1 != '' else UNPRESSED_KEYS[0][1])
    result.append(PRESSED_KEYS[0][2] if p1 != '' else UNPRESSED_KEYS[0][2])
    result.append(PRESSED_KEYS[0][3] if h != '' else UNPRESSED_KEYS[0][3])
    result.append(SPACE_PRE_STAR)
    result.append(PRESSED_KEYS[0][4] if star == '*' else UNPRESSED_KEYS[0][4])
    result.append(SPACE_POST_STAR)
    result.append(PRESSED_KEYS[0][5] if f != '' else UNPRESSED_KEYS[0][5])
    result.append(PRESSED_KEYS[0][6] if p2 != '' else UNPRESSED_KEYS[0][6])
    result.append(PRESSED_KEYS[0][7] if l != '' else UNPRESSED_KEYS[0][7])
    result.append(PRESSED_KEYS[0][8] if t2 != '' else UNPRESSED_KEYS[0][8])
    result.append(PRESSED_KEYS[0][9] if d != '' else UNPRESSED_KEYS[0][9])
    result.append(NEWLINE)

    result.append(PRESSED_KEYS[1][0] if s1 != '' else UNPRESSED_KEYS[1][0])
    result.append(PRESSED_KEYS[1][1] if k != '' else UNPRESSED_KEYS[1][1])
    result.append(PRESSED_KEYS[1][2] if w != '' else UNPRESSED_KEYS[1][2])
    result.append(PRESSED_KEYS[1][3] if r1 != '' else UNPRESSED_KEYS[1][3])
    result.append(SPACE_PRE_STAR)
    result.append(PRESSED_KEYS[1][4] if star == '*' else UNPRESSED_KEYS[1][4])
    result.append(SPACE_POST_STAR)
    result.append(PRESSED_KEYS[1][5] if r2 != '' else UNPRESSED_KEYS[1][5])
    result.append(PRESSED_KEYS[1][6] if b != '' else UNPRESSED_KEYS[1][6])
    result.append(PRESSED_KEYS[1][7] if g != '' else UNPRESSED_KEYS[1][7])
    result.append(PRESSED_KEYS[1][8] if s2 != '' else UNPRESSED_KEYS[1][8])
    result.append(PRESSED_KEYS[1][9] if z != '' else UNPRESSED_KEYS[1][9])
    result.append(NEWLINE)

    result.append(SPACE_PRE_VOWELS)
    result.append(PRESSED_KEYS[2][0] if a != '' else UNPRESSED_KEYS[2][0])
    result.append(PRESSED_KEYS[2][1] if o != '' else UNPRESSED_KEYS[2][1])
    result.append(SPACE_BETWEEN_VOWELS)
    result.append(PRESSED_KEYS[2][2] if e != '' else UNPRESSED_KEYS[2][2])
    result.append(PRESSED_KEYS[2][3] if u != '' else UNPRESSED_KEYS[2][3])
    result.append(NEWLINE)

    result.append('{^}{-|}')

    return "".join(result)
 