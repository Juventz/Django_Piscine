from antigravity import geohash
from sys import argv


def is_valid_date(date_str: str) -> bool:
    parts = date_str.split('-')
    if len(parts) != 3:
        return False

    day, month, year = parts

    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and day > 29:
            return False
        elif day > 28:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False

    return True


def main():
    try:
        if len(argv) != 4:
            raise ValueError("Usage : python3 geohashing.py \
<latitude> <longitude> <date>")

        latitude = float(argv[1])
        longitude = float(argv[2])
        date = argv[3].encode("utf-8")

        if not is_valid_date(argv[3]):
            raise ValueError(f"Invalid date format: {argv[3]}. Expected format\
 is 'DD-MM-YYYY'.")

        geohash(latitude, longitude, date)

    except Exception as e:
        print(f"{type(e).__name__} : {e}")
        exit(1)


if __name__ == "__main__":
    main()
