

LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def parse_event(line):
    s = line.split(maxsplit = 2)
    if s[1] in LEVELS and len(s) == 3:
        d = {'time': s[0], 'level': s[1], 'message': s[2]}
    else:
        raise ValueError('негодная строка')
    return d

def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    counts["BROKEN"] = 0
    
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]]+=1
        except ValueError:
            counts["BROKEN"] += 1
            
    return counts

