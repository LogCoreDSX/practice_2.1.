while True:
    students = {}
    voidstr = " "
    print("--Begin program--")
    print(voidstr)
    try:
        with open('result/student.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, note = line.split(':')
                notes_list = note.split(',')
                notes = []
                for g in notes_list:
                    notes.append(int(g))
                avg = sum(notes) / len(notes)
                students[name] = avg
    except FileNotFoundError as e:
        print(f"Error. File NOT FOUND. Error : {e}")
        print("--End prorgam--")
        exit()
    with open('result/result.txt', 'w', encoding='utf-8') as file2:
        for name, avg in students.items():
            if avg > 4.0:
                file2.write(f"{name}: {avg}\n")
    best_name = ""
    best_avg = 0
    for name, avg in students.items():
        if avg > best_avg:
            best_avg = avg
            best_name = name
    print(f"Студент с наивысшим баллом : {best_name}")
    print(f"Средний балл : {best_avg}")
    print("\nВсе студенты :")
    for name, avg in students.items():
        status = ">" if avg > 4.0 else "<"
        print(f"{name} : {avg} {status} 4.0")
    print(voidstr)
    print("--End prorgam--")
    exit()