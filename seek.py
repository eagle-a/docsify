import os


def generate_menu(directory):
    menu = []
    for root, dirs, files in os.walk(directory):
        #for dir in dirs:
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory)  
                    menu.append(
                        '-[' + ''.join(file) + '](/book/' + relative_path + ')</br>')
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
    content = content.replace('\\', '/')  
    
    with open(location, 'w', encoding='utf-8') as f:
        f.write(content)
