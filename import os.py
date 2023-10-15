import os

def generate_menu(directory):
    menu = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            file_path = os.path.join(root, dir)
            relative_path = os.path.relpath(file_path, directory)  
            menu.append(generate_menu_item(dir, relative_path))
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)  
                (shotname,extension) = os.path.splitext(file)
                menu.append(generate_menu_item(shotname, relative_path, indent=True))
    return menu

def generate_menu_item(name, path, indent=False):
    prefix = '  ' if indent else ''
    return f'{prefix}- [{name}](/book/{path})'


directory = r'./docsify/docs/book'

menu = generate_menu(directory)
for item in menu:
    print(item)