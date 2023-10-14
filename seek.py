import os


def generate_menu(directory):
    menu = []
    for root, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
            #   relative_path_with_slash = os.path.join('/', relative_path)
                menu.append( '[' + '/'.join(file) + '](/book/' + relative_path + ')')
    return menu

directory = r'./docsify/docs/book'

if __name__ == "__main__":
    menu = generate_menu(directory)
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\_sidebar.md'
    f = open(location, 'w', encoding='utf-8')
    for menu1 in menu:
        f.write(menu1)
        f.write('\n')
    f.close()
    # 打开并读取Markdown文件  
with open(location, 'r', encoding='utf-8') as file:  
    content = file.read()   
    file.write(content)
