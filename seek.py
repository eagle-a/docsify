import os

def generate_menu(directory):
    menu = []
    dirs = os.listdir(directory)
    for dir in dirs:
        menu.append([dir])
        menu.append('- [{}]'.format(dir))
        for root, files in os.walk(dir):
            for file in files:

                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    # 使用 os.path.relpath 来正确地计算相对路径
                    relative_path = os.path.relpath(file_path, directory)
                    # 仅保存文件名和相对路径
                    menu.appendstr(
                        ''.join('- [{}]({})'.format(os.path.basename(file), relative_path)))
                   # menu.append([os.path.basename(file), relative_path])
    return menu


# 注意使用原始字符串来处理路径中的反斜杠
directory = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'

if __name__ == "__main__":
    menu = generate_menu(directory)
    location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book\_sidebar.md'
    f = open(location, 'w', encoding='utf-8')
    for url in menu:
        f.write(str(url))  # 添加 '\n' 是为了在每个url后面都有一个新的一行
        f.write('\n')
    f.close()  # 不要忘记关闭文件
