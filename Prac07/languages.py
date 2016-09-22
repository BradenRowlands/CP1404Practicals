from Prac07.ProgrammingLanguage import ProgrammingLanguage

def main():
    code_languages = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                      ProgrammingLanguage("Python", "Dynamic", True, 1991),
                      ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

    print("The dynamically typed languages are:")
    for language in code_languages:
        if language.is_dynamic():
            print(language.code_name)
main()