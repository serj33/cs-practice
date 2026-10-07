def parse_record(line: str) -> dict:
    
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей ({len(parts)} вместо 3) в строке: '{line}'")

    city, temp_str, date = parts

    # Проверка на пустые строки в полях города или даты
    if not city.strip() or not date.strip():
        raise ValueError(f"Город или дата не могут быть пустыми в строке: '{line}'")

    try:
        temp = float(temp_str)
    except ValueError as e:
        raise ValueError(f"Температура '{temp_str}' не является числом в строке: '{line}'") from e

    return {"city": city, "temp": temp, "date": date}

