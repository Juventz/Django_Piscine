def create_dict_from_list(couples):
    """This function takes a list of tuples and returns
    a dictionary with the year as key and the name as value.
    """
    result_dict = {}

    for musician, year in couples:
        if year not in result_dict:
            result_dict[year] = []
        result_dict[year].append(musician)

    return result_dict


def print_dict(d):
    """This function takes a dictionary and prints it in a formatted way.
    """
    for year, musicians in sorted(d.items(), reverse=True):
        print(f"{year}: {', '.join(musicians)}")


def main():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    music_dict = create_dict_from_list(d)
    print_dict(music_dict)


if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
