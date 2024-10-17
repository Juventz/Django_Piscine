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
            td { border: 1px solid black; padding: 10px; width: 70px; text-align: center; }
            h4 { margin: 5px; }
            ul { padding-left: 15px; text-align: left; }
        </style>
    </head>
    <body>
    <h1>Periodic Table of Elements</h1>
    <table>
    <tr>'''
    # Build the periodic table layout
    max_columns = 18
    row_cells = [''] * max_columns
    for element in elements:
        # Fill the row cells based on the position of the element
        position = element['position']
        electron_count = len(element['electron'])
        row_cells[position] = f'''
        <td>
            <h4>{element['name']}</h4>
            <ul>
                <li>No {element['number']}</li>
                <li>{element['symbol']}</li>
                <li>{element['mass']}</li>
                <li>{electron_count} electron{'s' if electron_count > 1 else ''}</li>
            </ul>
        </td>
        '''
        # When position is 17 (rightmost), start a new row
        if position == 17:
            html_content += ''.join(row_cells) + '</tr><tr>'
            row_cells = [''] * max_columns
    # Add remaining row if not complete
    if any(row_cells):
        html_content += ''.join(row_cells) + '</tr>'
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
