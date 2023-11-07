"""
CP1404 - Programs Objects
"""


class ProgrammingLanguage:
    """Represent program languages information"""

    def __init__(self, name, typing, reflection, year):
        """Create Languages from values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection} , Appeared in {self.year}"

    def is_dynamic(self):
        """Determined if program is typed "Dynamically"""
        return self.typing == "Dynamic"


def testing():
    """Simple testing"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    testing()
