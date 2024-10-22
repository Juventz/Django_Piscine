from sys import argv
import settings


def render_template(file_path):

    surname = "The Hitchhiker's Guide"
    age = 42
    profession = "No one knows"

    if not file_path.endswith('.template'):
        raise TypeError(f' {file_path} file is not a .template')

    output = file_path.replace('.template', '.html')

    try:
        with open(file_path, 'r') as file:
            template = file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f'{file_path} file not found')

    rendered_content = template.replace('{name}', settings.name)

    html_structure = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> {settings.name}'s CV </title>
</head>
<body>
    <header>
        <h1> {settings.name} </h1>
        <p> {surname} </p>
        <p> Age: {age} </p>
        <p> Profession: {profession} </p>
    </header>
    <h2> Exo 00 </h2>
    {rendered_content}
</body>
</html>"""

    with open(output, 'w') as file:
        file.write(html_structure)

    print(f'File {output} has been created')


def main():
    try:
        if len(argv) != 2:
            print('Usage: python3 render.py <.template>')
        else:
            render_template(argv[1])

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == '__main__':
    main()
