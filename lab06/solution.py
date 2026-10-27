

def count_by_extension(paths):
    counts = {}
    for i in paths:
        s = i.split('.')
        if len(s)==2:
            level = s[-1].lower()
        else:
            level = ''
        counts[level] = counts.get(level, 0) + 1
    return counts

