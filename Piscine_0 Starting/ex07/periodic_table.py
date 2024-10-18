def parse_periodic_table(file_path):
    elements = []
    with open(file_path, 'r') as file:
        for line in file:
            name, attributes = line.strip().split('=')
            attributes = dict(item.strip().split(':') for item
                              in attributes.split(', '))
            elements.append({
                'name': name,
                'position': int(attributes['position']),
                'number': int(attributes['number']),
                'symbol': attributes['small'],
                'mass': float(attributes['molar']),
                'electron': list(map(int, attributes['electron'].split()))
            })

    return elements


def generate_html(elements):
    html_content = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Periodic Table</title>
        <style>
            table { border-collapse: collapse; width: 100%; }
            td { padding: 10px; width: 70px; text-align: center; }
            td.filled { border: 1px solid black; }
            h4 { margin: 5px; }
            ul { padding-left: 15px; text-align: left; }
        </style>
    </head>
    <body>
    <h1>Periodic Table of Elements (Mendelïev)</h1>
    <table>
    '''

    # The structure of the periodic table per period and group
    table_structure = [
        [1, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 2],
        [3, 4, '', '', '', '', '', '', '', '', '', '', 5, 6, 7, 8, 9, 10],
        [11, 12, '', '', '', '', '', '', '', '', '', '', 13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
        [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
        [55, 56, '', 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86],
        [87, 88, '', 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]
    ]

    # Mapping atomic numbers to element details
    element_dict = {element['number']: element for element in elements}

    # Iterate over the table structure and fill the table
    for period in table_structure:
        row_cells = []
        for position in period:
            if position == '':
                # Empty cell
                row_cells.append('<td></td>')
            else:
                element = element_dict[position]
                electron_count = len(element['electron'])
                row_cells.append(f'''
                <td class="filled">
                    <h4>{element['name']}</h4>
                    <ul>
                        <li>No {element['number']}</li>
                        <li>{element['symbol']}</li>
                        <li>{element['mass']}</li>
                        <li>{electron_count} electron{'s' if electron_count > 1 else ''}</li>
                    </ul>
                </td>
                ''')
        html_content += '<tr>' + ''.join(row_cells) + '</tr>'

    html_content += '''
    </table>
    </body>
    </html>
    '''
    return html_content


def save_html(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


if __name__ == '__main__':
    try:
        elements = parse_periodic_table('periodic_table.txt')
        html_content = generate_html(elements)
        if html_content is not None:
            save_html('periodic_table.html', html_content)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)
