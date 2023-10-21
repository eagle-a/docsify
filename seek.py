import os



def generate_md_menu():
        f = open(location, 'w', encoding='utf-8')
        files = os.listdir(directory)
        for file in files:
            file_dir = directory+'/'+ file
            f.write('['+file+']'+'('+file_dir+')\n')
            print('['+file+']'+'('+file_dir+')\n')
            files_low_1 = os.listdir(file_dir)
            print(files_low_1)
            #files_low_1 = os.path.join(file)
            for file_low_1 in files_low_1:
                file_low_dir = file_dir+'\\' + file_low_1
                print(file_low_dir)
                file_low_2 = os.listdir(file_low_dir)
                for file_md in  file_low_2: 
                    if(file_md != '_sidebar.md'):
                        f.write(' - ['+file_md[:-3]+']'+'('+directory_md+'\\'+file_low_1+'\\'+file_md+')\n')
                        print('['+file_md[:-3]+']'+'('+directory_md+'\\123'+file_low_1+'\\'+file_md+')')
                
    
        return 0
location = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\_sidebar.md'

directory_md = r'C:\Users\21216\Desktop\math_and_Program\docsify\docsify\docs\book'
directory = directory_md
if __name__ == "__main__":
    #menu = generate_dir_menu(directory)
    generate_md_menu()
    #print('over')