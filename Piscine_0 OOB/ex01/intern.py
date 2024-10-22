class Intern:
    # default Builder taking character chain as a parameter and assigning it to a Name attribute
    def __init__(self, Name="My name? I’m nobody, an intern, I have no name."):
        self.Name = Name

    # method that returns the name attribute
    def __str__(self):
        return self.Name


    
