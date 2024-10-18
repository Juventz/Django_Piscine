from sys import argv


def clean_input(input_str):
    """Removes leading and trailing whitespace from the input string."""
    return input_str.strip().lower()


def process_input(expression, states, capitals):
    """Returns the state corresponding to the given capital."""
    input_clean = clean_input(expression)

    for state, abbr in states.items():
        if clean_input(state) == input_clean:
            capital = capitals[abbr]
            return (f"{capital} is the capital of {state}")

    for abbr, capital in capitals.items():
        if clean_input(capital) == input_clean:
            state = [st for st, code in states.items() if code == abbr][0]
            return (f"{capital} is the capital of {state}")

    return (f"{expression.strip()} is neither a capital city nor a state")


def main():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capitals = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(argv) != 2:
        return

    input_str = argv[1]

    if ",," in input_str:
        return

    expressions = input_str.split(",")

    for expression in expressions:
        expression = expression.strip()
        if expression:
            result = process_input(expression, states, capitals)
            print(result)


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
