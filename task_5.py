import json
import os
import random
from datetime import datetime


#Функция сообщений
def say(say_param):
    if say_param == "void":
        print(" ")
    elif say_param == "start":
        print(" ")
        print("<----Start program---->")
    elif say_param == "end":
        print(" ")
        print("<----End program---->")
    elif say_param =="er_num":
        print("<Error. ONLY Number !>")
    elif say_param == "notmod":
        print("<Not FOUND0 mode>")
    elif say_param == "notfile":
        print("<File NOT FOUND>")
    elif say_param == "cancel":
        print(" ")
        print("<Canceling>")
    elif say_param == "libnull":
        print("<There are no books in the library>")
    elif say_param == "booknull":
        print("<No book(s)>")


#Функция времени
def times():
    now = datetime.now()
    return now.strftime("%Y")


#Функция создание книги и добавление в my_books[]
def create_book(my_book, lib_main):
    real_year = int(times())
    for i in range(5):
            say("void")
            print(f"Processing create book. Phase {i + 1}")
            match i:
                case 0:
                    title = input("Input name book : ")
                case 1:
                    creator = input("Input name author : ")
                case 2:
                    while True:
                        try:
                            year = int(input("Input year of publication : "))
                            if year < 0 or year > real_year:
                                say("void")
                                print(f"Year of publication ONLY \n nature number \n OR \n input year > real year({real_year})")
                                continue
                            break
                        except ValueError:
                            say("void")
                            print(f"Error. ONLY number.")
                            continue
                case 3:
                    status = False
                case 4:
                    id_book = generate_id(my_book, lib_main)
    book = {"id_book" : id_book, "title" : title, "creator" : creator, "year" : year, "status" : status}
    title_book = book["title"]
    my_book.append(book)
    say("void")
    print("<Creating the book is completed>")
    print(f"Create book : {title_book} ")
    say("void")
    last_id = id_book
    return my_book, last_id


#Функция генерации ID
def generate_id(my_book, lib_main):
    while True:
        new_id = random.randint(1000, 9999)
        id_exists = False
        for book in my_book:
            if book["id_book"] == new_id:
                id_exists = True
                break
        if not id_exists:
            for book in lib_main:
                if book["id_book"] == new_id:
                    id_exists = True
                    break
        if not id_exists:
            return new_id


#Функция добавление книг в Lib_main[]
def add_book(my_book, lib, select_books):
    titles_book = []
    books_del = []
    for book in my_book:
        if book['title'] not in select_books:
            continue
        else:
            book['status'] = True
            titles_book.append(book['title'])
            lib.append(book)
            books_del.append(book)
    for book in books_del:
        my_book.remove(book)
    add_data_book = [lib, my_book]
    print("<Adding the book to the library is complete>")
    print("Adding book : ", *titles_book)
    say("void")
    return add_data_book


#Функция добавление книг в my_book[]
def read_book(my_book, lib, select_books):
    titles_book = []
    books_del = []
    for book in lib: 
        if book['title'] not in select_books: 
            continue
        else:
            book['status'] = False
            titles_book.append(book['title'])
            my_book.append(book)
            books_del.append(book)
    for book in books_del:
        lib.remove(book)
    add_data_book = [lib, my_book]
    print("<Adding the book to the My book is complete>")
    print("Adding book : ", *titles_book)
    say("void")
    return add_data_book


#Функция поиска
def search(lib):
    say("void")
    print("Select search mode : ")
    say("void")
    print("<0> - Title")
    print("<1> - Author")
    say("void")
    while True:
        try:
            select_search = int(input("Mode: "))
            if select_search not in [0, 1]:
                print("Mode must be 0 or 1")
                continue
            break
        except ValueError:
            say("void")
            say("er_num")
            continue
    if select_search == 0: # Поиск по названию
        say("void")
        search_term = input("Input book title: ").lower().strip()
        found_books = []
        for book in lib:
            if search_term in book["title"].lower():
                found_books.append(book)
    elif select_search == 1:  # Поиск по автору
        say("void")
        search_term = input("Input author: ").lower().strip()
        found_books = []
        for book in lib:
            if search_term in book["creator"].lower():
                found_books.append(book)
    say("void")
    if found_books:
        print(f"Found {len(found_books)} book(s):")
    say("void")
    for book in found_books:
        status = "Available" if book["status"] else "Borrowed"
        print(f"ID {book['id_book']:<4} | {book['title']:<50}{book['creator']:<20}{book['year']:<5} year >{status}<")
    return found_books


#Функция удаление одной книги по ID
def delete_book(lib):
    while True:
        say("void")
        print("Input ID book for delete :")
        say("void")
        try:
            del_id = int(input("ID : "))
            found = False
            for i, book in enumerate(lib):
                if book["id_book"] == del_id:
                    deleted = lib.pop(i)
                    print(f"Book '{deleted['title']}' deleted")
                    found = True
                    break
            if not found:
                print(f"Book with ID {del_id} not found")
                continue
            break
        except ValueError:
            say("void")
            say("er_num")
            continue


#Функция просмотра книг Lib_main[]
def visible_lib(lib):
    print("--- Library ---")
    say("void")
    for i in lib:
        status = "Available" if i["status"] else "Borrowed"
        print(f"ID {i['id_book']:<4} | {i['title']:<50}{i['creator']:<20}{i['year']:<5} year >{status}<")
    say("void")


#Функция просмотра книг my_book[]
def visible_my_book(my_book):
    print("-- My Books --")
    say("void")
    for i in my_book:
        status = "Available" if i["status"] else "Borrowed"
        print(f"ID {i['id_book']:<4} | {i['title']:<50}{i['creator']:<20}{i['year']:<5} year >{status}<")


#Функция создание доступных книг из my_book[]
def create_available_books_file(my_book):
    try:
        with open('resource/available_books.txt', 'w', encoding='utf-8') as file:
            if my_book:
                file.write("=== BOOKS AVAILABLE TO ADD TO LIBRARY ===\n")
                file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                file.write("=" * 50 + "\n\n")
                for i, book in enumerate(my_book, 1):
                    file.write(f"#{i}\n")
                    file.write(f"ID: {book['id_book']}\n")
                    file.write(f"Title: {book['title']}\n")
                    file.write(f"Author: {book['creator']}\n")
                    file.write(f"Year: {book['year']}\n")
                    file.write(f"Status: {'Available' if not book['status'] else 'Borrowed'}\n")
                    file.write("-" * 40 + "\n")
                file.write(f"\nTotal books available to add: {len(my_book)}")
                print(f"<File 'available_books.txt' created with {len(my_book)} books>")
            else:
                file.write("No books available to add to library.\n")
                file.write(f"Check date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                file.write("Create books first using Mode 0!")
                print("<No books in my_book. File created with empty list>")
        print("\n" + "=" * 50)
        print("FILE CONTENTS:")
        print("=" * 50)
        with open('resource/available_books.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError as e:
        say("notfile")
        print(e)
        exit()


#Функция выбора нескольких книг
def select_book(lib, my_book, sel):
    print("Input book TITLES to Space")
    print("# Война и мир 1984 === add books with titles: 'Война и мир', '1984'")
    print("\nNames books:")
    if sel == "lib":
        sa =  my_book
    elif sel == "books":
        sa = lib
    for book in sa: 
        print(f"  - {book['title']}")
    say("void")
    selectmode3 = input("Titles : ")
    return selectmode3.split()


#Главная часть
say("start") 
say("void")
print("--- Library ---")
last_id = 0
lib_main = []
my_book = []
while True:
    say("void")
    print("Select Mode :")
    say("void")
    print("<0> Create Book -------------------------- <1> Visible My Books")
    print("<2> Add Books -----------------------------<3> Visible Library")
    print("<4> Search books in Library -------------- <5> Deleted books to Library")
    print("<6> Create-Open file 'available_books.txt' <7> Edit JSON file")
    print("<8> Reset program ------------------------ <9> Exit program")
    say("void")
    try:
        select_mode = int(input("Mode : "))
        say("void")
    except ValueError:
        say("er_num")
        continue
    match select_mode:
        case 0:
            # data_book =
            my_book, last_id = create_book(my_book,lib_main)
        case 1:
            if my_book == []:
                print("<No book(s)>")
            else:
                visible_my_book(my_book)
        case 2:
            while True:
                print("--Add Book--")
                say("void")
                print("<0> My Book --- <1> Visible My Books")
                print("<2> Library --- <3> Visible Library ")
                print("          <4> Cancel                ")
                say("void")
                selectmode2 = input("Mode : ")
                say("void")
                if selectmode2 == "2":
                    if my_book != []:
                        sel = "lib"
                        selbooks = select_book(lib_main, my_book, sel)
                        ab = add_book(my_book, lib_main, selbooks)
                        lib_main, my_book = ab
                        break
                    else:
                        say("booknull")
                        break
                elif selectmode2  == "3":
                    if lib_main == []:
                        say("libnull")
                        break
                    else:
                        visible_lib(lib_main)
                        break
                elif selectmode2 == "0":
                    if lib_main != []:
                        sel = "books"
                        selbooks = select_book(lib_main, my_book, sel)
                        ad = read_book(my_book, lib_main, selbooks)
                        lib_main, my_book = ad
                        break
                    else:
                        say("libnull")
                        break
                elif selectmode2 == "1":
                    if my_book == []:
                        say("booknull")
                        break
                    else:
                        visible_my_book(my_book)
                        break
                elif selectmode2 == "4":
                    say("void")
                    print("<Canceling>")
                    break
                else:
                    say("notmod")
                    say("void")
                    continue
        case 3:
            if lib_main == []:
                say("libnull")
            else:
                visible_lib(lib_main)
        case 4:
            search(lib_main)
        case 5:
            if lib_main == []:
                say("libnull")
                continue
            else:
                visible_lib(lib_main)
                delete_book(lib_main)
        case 6:
            while True:
                say("void")
                print("<Available Books File>")
                say("void")
                print("<0> Create/Update available_books.txt")
                print("<1> Open and view available_books.txt")
                print("<2> Cancel")
                try:
                    say("void")
                    select_mode = int(input("Mode : "))
                    if select_mode == 1:
                        try:
                            folder_log = os.path.dirname(os.path.abspath(__file__))
                            path_log = os.path.join(folder_log, 'resource/available_books.txt')
                            os.startfile(path_log)
                            break
                        except(FileNotFoundError) as e:
                            say("notfile")
                            break
                    elif select_mode == 0:
                        create_available_books_file(my_book)
                        break
                    elif select_mode == 2:
                        say("cancel")
                        break
                    else:
                        say("notmod")
                        continue
                except ValueError:
                    say("void")
                    say("er_num")
                    continue
        case 7:
            print("<JSON File Manager>")
            say("void")
            print("<0> Save library to JSON")
            print("<1> Load library from JSON")
            print("<2> Cancel")
            say("void")
            while True:
                try:
                    json_select = int(input("Mode : "))
                    if json_select == 0:
                        if lib_main:
                            with open('resource/library.json', 'w', encoding='utf-8') as f:
                                json.dump(lib_main, f, ensure_ascii=False, indent=4)
                                say("void")
                                print("<Library saved to JSON file>")
                                say("void")
                                print(f"<Saved {len(lib_main)} books>")
                                break
                        else:
                            say("void")
                            print("<Library is empty>")
                            say("void")
                    elif json_select == 1:
                        try:
                            with open('resource/library.json', 'r', encoding='utf-8') as f:
                                lib_main = json.load(f)
                                if lib_main:
                                    last_id = max(book['id_book'] for book in lib_main)
                                    say("void")
                                    print("<Library loaded from JSON file>")
                                    print(f"<Loaded {len(lib_main)} books>")
                                    break
                        except FileNotFoundError:
                            say("void")
                            print("<JSON file NOT FOUND>")
                            say("void")
                    elif json_select == 2:
                        say("cancel")
                        break
                    else:
                        say("notmod")
                        continue
                except ValueError:
                    say("void")
                    say("er_num")
                    continue
        case 8:
            print("<Are you sure ?>")
            res = input("(Y/N) : ").upper()
            if res == "Y":
                my_book = []
                lib_main = []
                last_id = 0
                say("void")
                print("Resetting program...")
                say("void")
                say("start")
                say("void")
                print("--- Library ---")
                continue
            else:
                say("void")
                print("<Canceling reset>")
                continue
        case 9:
            say("end")
            exit()


