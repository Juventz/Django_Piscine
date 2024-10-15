from sys import argv


def get_state_by_capital(capital, reversed_capitals_dict):
    """Returns the state corresponding to the given capital."""
    return reversed_capitals_dict.get(capital)


def main():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Reverse the capital_cities dictionary to map capitals to states
    reversed_capitals_dict = {capital: state for state, abbr in states.items()
                              for abbr_key, capital in capital_cities.items()
                              if abbr == abbr_key}

    if len(argv) != 2:
        return

    capital_name = argv[1]
    state_name = get_state_by_capital(capital_name, reversed_capitals_dict)

    if state_name is None:
        print("Unknown capital city")
    else:
        print(state_name)


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
