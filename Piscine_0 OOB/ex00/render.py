from sys import argv
import settings


def render_template(file_path):

    if not file_path.endswith('.template'):
        raise TypeError(f' {file_path} file is not a template')

    output = file_path.replace('.template', '.html')

    try:
        with open(file_path, 'r') as file:
            template = file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f'{file_path} file not found')

    rendered_content = template.replace('{name}', settings.name)

    with open(output, 'w') as file:
        file.write(rendered_content)


def main():
    try:
        if len(argv) != 2:
            print('Usage: python3 render.py <file_path>"')
        else:
            render_template(argv[1])

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return

    finally:
        print('Rendering complete')


if __name__ == '__main__':
    main()
