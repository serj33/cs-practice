import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    raw_lines = sys.stdin.read().splitlines()
    meaningful_lines = [line for line in raw_lines if line.strip()]
    valid_records = read_valid(raw_lines)
    errors_count = len(meaningful_lines) - len(valid_records)

    print(len(valid_records))
    print(errors_count)

    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(f"{averages[best_city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()
