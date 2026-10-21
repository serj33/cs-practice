from collections import Counter

LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def parse_event(line):
    s = line.strip().split(maxsplit = 2)


    if len(s) != 3:
        raise ValueError("Неполная строка")
    if s[1] not in LEVELS:
        raise ValueError("Неизвестный уровень")
##    if not s[2].strip():
##        raise ValueError("Пустое сообщение")
    
    return {"time": s[0], "level": s[1], "message": s[2]}

def count_levels(lines):
    counts = {}
    
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event['level']
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts

def top_errors(lines, n):
    errors = Counter()

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                errors[event["message"]] += 1
        except ValueError:
            continue

    sorted_errors = sorted(errors.items(), key=lambda item: (-item[1], item[0]))

    return [[message, count] for message, count in sorted_errors[:n]]

def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"

