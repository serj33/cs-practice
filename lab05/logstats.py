

LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
def parse_event(line):
    s = line.split(maxsplit = 2)
    if s[1] in LEVELS and len(s) == 3:
        d = {'time': s[0], 'level': s[1], 'message': s[2]}
    else:
        d = 'ValueError'
    return d

print(parse_event('2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv'))
