def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


def process_numbers(numbers_string):
    return numbers_string.split(',')


def display_numbers(numbers_list):
    for number in numbers_list:
        print(number)


def main():
    file_path = 'numbers.txt'
    numbers_string = read_file(file_path)

    if numbers_string:
        numbers_list = process_numbers(numbers_string)
        display_numbers(numbers_list)


if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
