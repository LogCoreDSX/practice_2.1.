from datetime import datetime
import os

log_filename = f'resource/calculator_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

#Функция проверки и ввода
def true_number(mode):
    while True:
        if mode == 1: # Ввод при ошибочном вводе числа A B
            print("Input number A")
            try:
                xnum1 = int(input("Number A = "))
            except ValueError:
                say("void")
                print(f"Error. ONLY number.")
                continue
            say("void")
            print("Input number B")
            try:
                xnum2 = int(input("Number B = "))
            except ValueError:
                say("void")
                print(f"Error. ONLY number.")
                continue
            true_num_list = [xnum1, xnum2]
            return true_num_list
        elif mode == 2: # Ввод при ошибочном выбора режима
            while True:
                try:
                    print(f"Error. ONLY number.")
                    say("void")
                    xselect = int(input("Mode : "))
                    return xselect
                except ValueError:
                    continue

        # Ввод и проверка новых чисел
        elif mode == 3:
            print("Input new number")
            say("void")
            try:
                xnum1 = int(input("Number A = "))
            except ValueError:
                say("void")
                print(f"Error. ONLY number.")
                continue
            say("void")
            print("Input number B")
            try:
                xnum2 = int(input("Number B = "))
            except ValueError:
                say("void")
                print(f"Error. ONLY number.")
                continue
            true_num_list = [xnum1, xnum2]
            return true_num_list


#Функция обновление чисел
def var_update():
    say("void")
    numbers = true_number(3)
    return numbers


#Функция сообщений
def say(selectsay):
    if selectsay == "void":
        print("  ")
    elif selectsay == "end":
        print("--< End program >--")
    elif selectsay == "start":
        print("--< Start program >--")
    elif selectsay == "select":
        print("Select mode :")
    elif selectsay == "notmod":
        print("Not found mode")
    elif selectsay == "hi":
        print("C+a+l+c+u+l+a+t+o+r")


#Функция времени
def time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


#Функция получение результата решения
def final_update(xkey, xvar, xfinal):
    old_items = list(xfinal.items())
    yfinal = {}
    yfinal[xkey] = xvar
    for i in range(min(4, len(old_items))):
        key, var = old_items[i]
        yfinal[key] = var
    return yfinal


#Функция логирование
def log_update(mode_log, final_num):
    global log_filename
    if mode_log == 1:
        with open(log_filename, 'w', encoding ='utf-8') as file1,\
            open ('resource/calculator.log', 'w', encoding ='utf-8') as file2:
            if file1.tell() and file2.tell() == 0:
                file1.write("---History log file----\n")
                file2.write("---History log file----\n")
            items = list(final_num.items())
            for i in range(min(4, len(items))):
                key, value = items[i]
                file1.write(f"{i+1} : {key} ---- {value}\n")
                file2.write(f"{i+1} : {key} ---- {value}\n")
    elif mode_log == 0:
        with open(log_filename, 'w', encoding='utf-8') as file1, \
            open ('resource/calculator.log', 'w', encoding ='utf-8') as file2:
            file1.write("--- History log file ----")
            file2.write("--- History log file ----")
            for i in range(4):
                file1.write(" ")
                file2.write(" ")


#Функция показа истории
def final_visible(finalest):
    say("void")
    print("--History--")
    say("void")
    items = list(finalest.items())
    for i in range(min(4, len(items))):
        key, value = items[i]
        print(f"{i+1} : {key} ---- {value}\n")


#Функция последний операции
def prime_final_visible(finalest):
    say("void")
    print("--Last operation--")
    say("void")
    items = list(finalest.items())
    for i in range(min(1, len(items))):
        key, value = items[i]
        print(f"{key} ---- {value}\n")


# Главная часть
power_true = True 
say("void")
while True:
    say("void") 
    say("hi")
    if power_true == True:
        xfinal = {}
    say("start") 
    try:
        number1, number2 = 1, 1
        say("void")
        print("Imput number A")
        number1 = int(input("Number A = "))
        say("void")
        print("Input number B")
        number2 = int(input("Number B = "))
    except(ValueError) as e:
        print("Error. ONLY number.")
        list_num = true_number(1)
        if list_num[0] != 0 and list_num[0] != 0:
            number1, number2 = list_num[0], list_num[1]
        else:
            number1 = number1
            number2 = number2
    while True:
        power_true = False
        say("void")
        print(f"Numbers: \n A = {number1} \n B = {number2} ")
        say("void")
        say("select")
        if xfinal == {"No":"History", " ":" ", " ":" ", " ":" ", " ": " "}:
            print("Attention! \n Each new run leaves its own log file \n Select '<6>--Open file History' \n If you want to see the past history")
        say("void")
        print("<0>-------------Sum(+)       <1>----Subtraction(-)")
        print("<2>---------Product(*)       <3>-----Difference(/)")
        print("<4>------Update Number       <5>---Visible History")
        print("<6>--Open file History       <7>-----Clear History")
        print("                   <8>---Exit"                     )
        say("void")
        try:
            select_mode = int(input("Mode : "))
        except(ValueError) as e:
            print("")
            select_mode = true_number(2)
        if select_mode == 0 : # Сложение
            result = number1 + number2
            finalnum = f"{number1} + {number2} = {result}"
            xtime = time()
            final = final_update(xtime, finalnum, xfinal)
            xfinal = final
            log_update(1, final)
            prime_final_visible(final)
        elif select_mode == 1 : #Вычитание
            result = number1 - number2
            finalnum = f"{number1} - {number2} = {result}"
            xtime = time()
            final = final_update(xtime, finalnum, xfinal)
            xfinal = final
            prime_final_visible(final)
            log_update(1, final)
        elif select_mode == 2: # Умножение
            result = number1 * number2
            finalnum = f"{number1} * {number2} = {result}"
            xtime = time()
            final = final_update(xtime, finalnum, xfinal)
            xfinal = final
            prime_final_visible(final)
            log_update(1, final)
        elif select_mode == 3: # Деление
            if number2 == 0:
                say("void")
                print("<<Attention !>>")
                print("If Number B == 0 \n Number B = 1")
                temp_num2 = number2
                number2 = 1
            else:
                temp_num2 = 0
            result = number1 / number2
            finalnum = f"{number1} / {number2} = {result}"
            xtime = time()
            final = final_update(xtime, finalnum, xfinal)
            xfinal = final
            prime_final_visible(final)
            log_update(1, final)
            number2 = temp_num2
        elif select_mode == 4: # Обновление чисел
            numberx = var_update()
            number1 = int(numberx[0])
            number2 = int(numberx[1])
            continue
        elif select_mode == 5: # Открыть файл
            if xfinal == None:
                xfinal = {"No" : "History"}
                final_visible(xfinal)
            else:
                final_visible(xfinal)
        elif select_mode == 6:
            try:
                if xfinal != {"No":"History", " ":" ", " ":" ", " ":" ", " ": " "}:
                    folder_log = os.path.dirname(os.path.abspath(__file__))
                    path_log = os.path.join(folder_log, log_filename)
                    os.startfile(path_log)
                else:
                    folder_log = os.path.dirname(os.path.abspath(__file__))
                    path_log = os.path.join(folder_log, 'resource/calculator.log')
                    os.startfile(path_log)
            except(FileNotFoundError) as e:
               print("Error. File NOT FOUND.\n Create file select mode : 0-4")
               continue
        elif select_mode == 7: # Очистить историю
            say("void")
            if xfinal == {"No":"History", " ":" ", " ":" ", " ":" ", " ": " "}:
                log_update(0, xfinal)
            else:
                log_update(0, final)
            print("History clear complite")
            say("void")
            xfinal = xfinal = {"No" : "History"}
            prime_final_visible(xfinal)
        elif select_mode == 8: # Выход
            say("void")
            say("end")
            exit()
        else:
            say("notmod")
            
            


            
    

    
