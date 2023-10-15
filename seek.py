import os


def generate_dir_menu(directory):
    menu = []
    dir_menu = []
    for root, dirs, files in os.walk(directory):
            for dir in dirs:
                file_path = os.path.join(root, dir)
                relative_path = os.path.relpath(file_path, directory) 
                dir_menu.append(''.join(dir))
                menu.append('- [' + ''.join(dir) + '](/book/' + relative_path + ')')
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
    return dir_menu

def generate_md_menu():

        files = os.listdir(directory)
        for file in files:
            file = directory+'/'+ file
           # print(file)
            files_low_1 = os.listdir(file)
          #  files_low_1 = os.path.join(file)
            for file_low_1 in files_low_1:
                file_low_1 = file+'/'+ file_low_1
                #print(file_low_1)
                location = r''.join(file_low_1)+'/_sidebar.md'
                f = open(location, 'w', encoding='utf-8')
                file_low_2 = os.listdir(file_low_1)
                for file_md in  file_low_2: 
                    if(file_md != '_sidebar.md'):
                        f.write('['+file_md[:-3]+']'+'('+file_low_1+'/'+file_md+')')
                        print(file_low_1+'/'+file_md)
                
    
        return 0

directory = r'./docsify/docs/book'

if __name__ == "__main__":
    menu = generate_dir_menu(directory)
    generate_md_menu()
    print('over')