import os  
  
def generate_menu(directory):  
    menu = []  
    dirs = os.listdir(directory)  
    for dir in dirs:  
        menu.append([dir])  
        menu.append(['\n- [{}]'.format(dir)])  
        for root, files in os.walk(dir):  
            for file in files:  
                if file.endswith('.md'):  
                    file_path = os.path.join(root, file)  
                    relative_path = os.path.relpath(file_path, directory)  
                    menu.append('\n- [{0}]({1})'.format(os.path.basename(file), relative_path))  
    return '\n'.join(menu)  
  
# 注意使用原始字符串来处理路径中的反斜杠  
directory = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'  
  
if __name__ == "__main__":  
    menu = generate_menu(directory)  
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book\_sidebar.md'  
    with open(location, 'w', encoding='utf-8') as f:  
        f.write(menu)