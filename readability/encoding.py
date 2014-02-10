import re
import chardet


HTML_CHARSET_REGEXP = re.compile(r"meta\s+http-equiv=\"content-type\"\s+content=\"[^;]+;\s*charset=([A-Za-z0-9_\-]+)\"", re.I)
HTML5_CHARSET_REGEXP = re.compile(r"meta\s+charset=\"([A-Za-z0-9_\-]+)\"", re.I)


def get_encoding(page):
    charset = "iso-8859-1" # WEB DEFAULT CHARTE

    for regexp in [HTML_CHARSET_REGEXP, HTML5_CHARSET_REGEXP]:
        match = regexp.search(page)
        if match:
            charset = match.group(1)
            break
    else:
        detected = chardet.detect(page)
        if detected and "encoding" in detected:
            charset = detected["encoding"]

    if charset == 'MacCyrillic':
        charset = 'cp1251'

    return charset
