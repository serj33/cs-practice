def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: {len(parts)}")

    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("Город или дата пусты")

    try:
        temperature = float(temp_str.replace(",", "."))
    except ValueError as e:
        raise ValueError(f"Не число: '{temp_str}'") from e

    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            valid_records.append(parse_record(line))
        except ValueError:
            pass
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1

    return {city: totals[city] / counts[city] for city in totals}


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    return min(averages.keys(), key=lambda city: (-averages[city], city))
