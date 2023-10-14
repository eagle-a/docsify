import os  
  
def generate_menu(directory):  
    menu = []  
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            if file.endswith('.md'):  
                # 获取文件的绝对路径  
                file_path = os.path.join(root, file)  
                # 获取文件名和相对路径  
                relative_path = os.path.relpath(file_path, directory)  
                # 将文件名和相对路径以特定格式添加到菜单中  
                menu.append(f'[{os.path.basename(file)}] ({relative_path})')  
    return menu  
  
# 注意使用原始字符串来处理路径中的反斜杠  
directory = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'  

if __name__ == "__main__":  
    menu = generate_menu(directory)  
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\_sidebar.md'  
    with open(location, 'w', encoding='utf-8') as f:  
        for url in menu:  
            f.write(url + '\n')  # 添加 '\n' 是为了在每个url后面都有一个新的一行