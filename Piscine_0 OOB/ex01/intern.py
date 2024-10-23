class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


class Intern:
    def __init__(self, Name="My name? I'm nobody, an intern, I have no name."):
        self.Name = Name

    # method that returns the name attribute
    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return Coffee()


def main():
    try:
        intern_named = Intern()
        intern_nonamed = Intern("Mark")

        print(intern_named)
        print(intern_nonamed)
        print("-" * 20)

        print(intern_nonamed.make_coffee())
        print("-" * 20)
        print(intern_named.work())

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
