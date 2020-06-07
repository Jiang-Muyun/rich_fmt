import bbcode

class Shortcuts():
    def bold(x):       return '\033[1m'  + str(x) + '\033[0m'
    def dim(x):        return '\033[2m'  + str(x) + '\033[0m'
    def italicized(x): return '\033[3m'  + str(x) + '\033[0m'
    def underline(x):  return '\033[4m'  + str(x) + '\033[0m'
    def blink(x):      return '\033[5m'  + str(x) + '\033[0m'
    def inverse(x):    return '\033[7m'  + str(x) + '\033[0m'
    def gray(x):       return '\033[90m' + str(x) + '\033[0m'
    def red(x):        return '\033[91m' + str(x) + '\033[0m'
    def green(x):      return '\033[92m' + str(x) + '\033[0m'
    def yellow(x):     return '\033[93m' + str(x) + '\033[0m'
    def blue(x):       return '\033[94m' + str(x) + '\033[0m'
    def magenta(x):    return '\033[95m' + str(x) + '\033[0m'
    def cyan(x):       return '\033[96m' + str(x) + '\033[0m'
    def white(x):      return '\033[97m' + str(x) + '\033[0m'


base_colors    = ['gray', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
clear_codes = {
    'reset'          : '\033[0m',
    'bold_off'       : '\033[22m',
    'italicized_off' : '\033[23m',
    'underline_off'  : '\033[24m',
    'blink_off'      : '\033[25m',
    'inverse_off'    : '\033[27m',
}
codes = {
    'b'          : '\033[1m',
    'i'          : '\033[3m',
    'u'          : '\033[4m',

    'bold'       : '\033[1m',
    'dim'        : '\033[2m',
    'italicized' : '\033[3m',
    'underline'  : '\033[4m',
    'blink'      : '\033[5m',
    'inverse'    : '\033[7m',
    'inv'        : '\033[7m',

    'gray'       : '\033[90m',
    'red'        : '\033[91m',
    'green'      : '\033[92m',
    'yellow'     : '\033[93m',
    'blue'       : '\033[94m',
    'magenta'    : '\033[95m',
    'cyan'       : '\033[96m',
    'white'      : '\033[97m',

    'b_gray'       : '\033[1m\033[90m',
    'b_red'        : '\033[1m\033[91m',
    'b_green'      : '\033[1m\033[92m',
    'b_yellow'     : '\033[1m\033[93m',
    'b_blue'       : '\033[1m\033[94m',
    'b_magenta'    : '\033[1m\033[95m',
    'b_cyan'       : '\033[1m\033[96m',
    'b_white'      : '\033[1m\033[97m',

    'i_gray'       : '\033[3m\033[90m',
    'i_red'        : '\033[3m\033[91m',
    'i_green'      : '\033[3m\033[92m',
    'i_yellow'     : '\033[3m\033[93m',
    'i_blue'       : '\033[3m\033[94m',
    'i_magenta'    : '\033[3m\033[95m',
    'i_cyan'       : '\033[3m\033[96m',
    'i_white'      : '\033[3m\033[97m',

    'u_gray'       : '\033[4m\033[90m',
    'u_red'        : '\033[4m\033[91m',
    'u_green'      : '\033[4m\033[92m',
    'u_yellow'     : '\033[4m\033[93m',
    'u_blue'       : '\033[4m\033[94m',
    'u_magenta'    : '\033[4m\033[95m',
    'u_cyan'       : '\033[4m\033[96m',
    'u_white'      : '\033[4m\033[97m',

}

parser = None

def rich_fmt(text):
    global parser
    if parser is None:
        parser = bbcode.Parser()
        for cmd in codes.keys():
            parser.add_formatter(cmd, '')

    fmt = ''
    tokens = parser.tokenize(text)
    keep = False
    for token in tokens:
        token_type, tag_name, tag_options, token_text = token
        # print('--', token_type, tag_name, tag_options, token_text)
        if token_type == parser.TOKEN_TAG_START:
            if tag_name in codes.keys():
                fmt += codes[tag_name]

            elif tag_name == 'color' and 'color' in tag_options:
                if tag_options['color'] in codes.keys():
                    fmt += codes[tag_options['color']]
                    
        elif token_type == parser.TOKEN_TAG_END:
            if tag_name == 'blink':
                fmt += clear_codes['blink_off']
            elif tag_name in ['b', 'bold']:
                fmt += clear_codes['bold_off']
            elif tag_name in ['i', 'italicized']:
                fmt += clear_codes['italicized_off']
            elif tag_name in ['u', 'underline']:
                fmt += clear_codes['underline_off']
            elif tag_name in ['inv', 'inverse']:
                fmt += clear_codes['inverse_off']
            else:
                fmt += clear_codes['reset']

        elif token_type == parser.TOKEN_NEWLINE:
            fmt += '\n'

        else:
            fmt += token_text
    return fmt

def rich_print(*args, **kwargs):
    text = ''
    for arg in args:
        text += str(arg) + ' '
    print(rich_fmt(text), **kwargs)
