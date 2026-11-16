
import json


def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    lines = text.strip().splitlines()
    headers = [item.strip() for item in lines[0].split(",")]

    records = []

    for line in lines[1:]:
        if not line.strip():
            continue

        values = [item.strip() for item in line.split(",")]
        records.append(dict(zip(headers, values)))

    return records



def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    for line in lines:
        line = line.split("#")[0].strip()

        if not line:
            continue

        if line.startswith("- "):
            if current_list is not None:
                settings[current_list].append(line[2:].strip())
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            settings[key] = []
            current_list = key
            continue

        current_list = None

        if value in ("true", "yes"):
            value = True
        elif value in ("false", "no"):
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        settings[key] = value

    return settings

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        merged = {}
        if row.get(key) in extra:
            merged.update(extra[row[key]])

        merged.update(row)
        result.append(merged)

    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )
