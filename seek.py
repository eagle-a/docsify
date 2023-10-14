import os


def generate_menu(directory):
    menu = []

    for dirs in os.walk(directory):
        for dirs_1 in dirs:
            menu.append('['+dirs_1+']')
            for dirs_2 in os.walk(dirs_1):
                for files in os.walk(dirs_2):
                    for root, file in files:
                        if file.endswith('.md'):
                            file_path = str(os.path.join(root, file))
                            relative_path = str(
                                os.path.relpath(file_path, directory))
                            menu.appendstr('['+dirs_2+ ']' + '('+relative_path + ')')

    return menu


directory = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'

if __name__ == "__main__":
    menu = generate_menu(directory)
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\_sidebar.md'
    f = open(location, 'w', encoding='utf-8')
    for url in menu:
        f.write(str(url)) 
        f.write('\n')
    f.close() 
