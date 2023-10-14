import os  
  
def generate_menu(directory):  
    menu = []  
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            if file.endswith('.md'):  
                file_path = os.path.join(root, file)  
                relative_path = os.path.relpath(file_path, directory)  # 使用 os.path.relpath 来正确地计算相对路径  
                menu.append([os.path.basename(file), relative_path])  # 仅保存文件名和相对路径  
    return menu  
 # "C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book"
directory = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'  # 注意使用原始字符串来处理路径中的反斜杠  
#os.chdir(directory)
if __name__ == "__main__":
    menu = generate_menu(directory)  
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book\_sidebar.md' 
    with open(location, 'w',encoding='utf-8') as f:  
        f.write('\n'.join(['- [{}]({})'.format(title, url) for title, url in menu]))
       