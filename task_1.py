#task1
while True :
    voidstr = " "
    list1 = []
    best_len = 0 ## Самая длинная строка
    best_len_str = ""
    print("--Begin program--")
    print(voidstr)
    try:
        str_count = int(input("Count string : "))
        if str_count <= 0:
            print("ONLY number > 0 \n Count string = 1")
            str_count = 1
        if str_count > 64 :
            print("ONLY range max 64 \n Count string = 64")
            str_count = 64
        print(voidstr)
        with open('resource/text1.txt', 'a', encoding = 'utf-8') as file1:
            for i in range(str_count):
                input1 = input(f"String {i + 1} : ")
                while True:
                    if len(input1) > 64 :
                        print("ONLY len max 64")
                        input1 = input(f"String {i + 1} : ")
                        continue
                    else:
                        break
                file1.write(input1 + "\n")
                list1.append(input1)
        with open('resource/text1.txt', 'r', encoding = 'utf-8') as file1:
            str_txt = file1.read()
            str_word = str_txt.split()
    except ValueError as e:
        print(f"Error. ONLY number. Error : {e}")
        str_count = 1
        str_word = ["ERROR"]
        print(">>Reset program<<")
        continue
    except FileNotFoundError  as e:
        print(f"Error. File NOT FOUND. Error : {e}")
        print("--End prorgam--")
        exit()
    for i in list1:
        if len(i) > best_len:
            best_len_str = i
            best_len = len(i)
    print(voidstr)
    print("Param txt file ")
    print(voidstr)
    print(f"Count string : {str_count}")
    print(f"Count word  : {len(str_word)}")
    print(f"Longest string : >> {best_len_str} << \n len(char + space): {best_len}")
    print(voidstr)
    print("--End prorgam--")
    exit()