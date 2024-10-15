from sys import argv


def get_state_abbr(state, state_dict):
    """Get the abbreviation of a state from a dictionary of states.
    """
    return state_dict.get(state)


def get_capital_city(state_abbr, capitals_dict):
    """Get the capital city of a state from a dictionary of capitals.
    """
    return capitals_dict.get(state_abbr)


def main():
    states = {
        'Oregon': 'OR',
        'Alabama': 'AL',
        'New Jersey': 'NJ',
        'Colorado': 'CO'
    }

    capital_cities = {
        'OR': 'Salem',
        'AL': 'Montgomery',
        'NJ': 'Trenton',
        'CO': 'Denver'
    }

    if len(argv) != 2:
        return

    state_name = argv[1]
    state_abbr = get_state_abbr(state_name, states)

    if state_abbr is None:
        print('Unknown state')
    else:
        capital = get_capital_city(state_abbr, capital_cities)
        if capital:
            print(capital)
        else:
            print('Unknown State')


if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
