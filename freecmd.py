import os
import sys
H = ["help","create","delete","exit"] 
def delete_file():
    # Просим пользователя ввести название файла
    filename = input("enter name of file you wanna destroy: ")
    
    # Проверяем существование файла
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f" '{filename}': removed successfully.")
        except PermissionError:
            print(f"insufficent rights for deletion of '{filename}'.")
        except Exception as e:
            print(f"cannot delete {e}")
    else:
        print(f"cannot find '{filename}' .")
def quit_with_confirmation():
    confirm = input("Do you want to exit?: ").strip().lower()
    if confirm in ['да', 'y', 'yes']:
        sys.exit(0)
    else:
        print("returning...")
def create_text_file():
    # Просим пользователя ввести название файла
    filename = input("insert filename: ")
    
    # Добавляем расширение .txt, если его нет
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        # Создаём файл и сразу закрываем его (пустой файл)
        with open(filename, 'w', encoding='utf-8') as file:
            pass  # Просто создаём файл, ничего не записывая
        print(f"Created a file'{filename}'.")
    except Exception as e:
        print(f"error while making a file: {e}")
def commands():
    a = input("your command =>")
    if a == H[0]:
        print("Available commands :",H)
    elif a==H[1]:
        q = ["y","yes"]
        q2 = ["n","no"]
        e = input("You sure you want to create a file? :").strip().lower()
        if e in q:
            create_text_file()
        elif e in q2:
            return 
        else:
            print("Answer is not yes or no")
            return
    elif a==H[2]:
        delete_file()
    elif a==H[3]:
        quit_with_confirmation()



        
while True:
    commands()









