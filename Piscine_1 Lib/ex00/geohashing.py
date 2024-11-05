from antigravity import geohash
from sys import argv


def main():
    try:
        if len(argv) != 4:
            raise ValueError("Usage : python3 geohashing.py <latitude> <longitude> <date>")

        latitude = float(argv[1])
        longitude = float(argv[2])
        date = argv[3].encode("utf-8")

        geohash(latitude, longitude, date)

    except Exception as e:
        print(f"{type(e).__name__} : {e}")
        return


if __name__ == "__main__":
    main()
