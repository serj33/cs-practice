

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

def deepest_path(paths):
    deepest = ''
    for i in paths:
        if i.count('/') > deepest.count('/'):
            deepest = i
        elif i.count('/') == deepest.count('/'):
            deepest = min(deepest, i)
    return deepest

