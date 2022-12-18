#!/usr/bin/env python3
# encoding: utf-8
from fileinput import filename
import sys
import os

Languages = {
    "C": {
        "template": [            
            "#include <stdio.h>",
            "",
            "int main() {",
            "    printf(\"Hello, World!\");",
            "    return 0;",
            "}"
        ],
        "defaultFileName": "main",
        "extension": ".c"
    },
    "C++": {
        "template": [
            "#include <iostream>",
            "",
            "using namespace std;",
            "",
            "int main() {",
            "    printf(\"Hello, World!\");",
            "    return 0;",
            "}"
        ],
        "defaultFileName": "main",
        "extension": ".cpp"
    },
    "Java": {
        "template": [
            "class Main{",
            "",
            "    public static void main(String[] args) {",
            "        System.out.println(\"Hello, World!\");",
            "   }",
            "}"
        ],
        "defaultFileName": "Main",
        "extension": ".java"
    },
    "Python": {
        "template": [
            "#!/usr/bin/env python3",
            "# encoding: utf-8",
            "",
            "def main():",
            "    print(\"Hello Python!\")",
            "",
            "if(__name__ == \"__main__\"):",
            "    main()"
        ],
        "defaultFileName": "main",
        "extension": ".py"
    }
}

def print_error(message):
    clear_screen()
    print(f"Error! {message}", file=sys.stderr)

def generate_file(template, filename, ):
    file_path = f"{os.getcwd()}/{filename}"
    if(not os.path.exists(file_path)):
        with open(file_path, "w") as fout:
            fout.write("\n".join(template))
        return True
    else:
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def select_language():
    language_names = list(Languages.keys())
    clear_screen()
    print("-"*20)
    for index, language_name in enumerate(language_names):
        print(f"{index + 1}. {language_name}")
    selected_language_index = int(input("Please select a language: ")) - 1 
    if selected_language_index >= 0 and selected_language_index < len(language_names):
        return language_names[selected_language_index]
    return None

def main():
    if(len(sys.argv) > 1):
        language = sys.argv[1]
    else:
        language = select_language()
    if(language in Languages.keys()):
            template = Languages[language]["template"]
            filename = Languages[language]["defaultFileName"] + Languages[language]["extension"]
            if generate_file(template, filename):
                clear_screen()
                print(f"{filename} generated successfuly!")
            else:
                print_error("File already exist.")
    else:
        print_error("This language is not supported")
if(__name__ == "__main__"):
    main()