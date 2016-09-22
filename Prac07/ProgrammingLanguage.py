class ProgrammingLanguage:
    def __init__(self, code_name, typing, reflection, year_founded):
        self.code_name = code_name
        self.typing = typing
        self.reflection = reflection
        self.year_founded = year_founded

    def __str__(self):
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.code_name, self.typing, self.reflection, self.year_founded)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False