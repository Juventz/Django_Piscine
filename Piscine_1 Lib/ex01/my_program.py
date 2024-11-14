from sys import path


def add_sys_to_path():
    path.insert(0, './local_lib')


def main():
    try:
        add_sys_to_path()

        from path import Path

        folder = Path("my_folder")
        folder.mkdir_p()

        file_path = folder / "my_file.txt"
        file_path.write_text("Hello, this is a test file.\n")

        content = file_path.read_text()
        print("File content: ", content)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
