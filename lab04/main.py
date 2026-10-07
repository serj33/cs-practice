import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    valid_records, errors_count = read_valid(lines)

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
