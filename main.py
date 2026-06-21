from timer import start_time, end_time, show_sessions, load_sessions, is_running,clear_all,total_time
load_sessions()


while True:
    print("\n=== Трекер учёбы ===")
    if is_running():
        print("🟢 Таймер идёт...")  
        print("1. Стоп")
    else:
        print("⏸ Таймер остановлен")
        print("1. Старт")
    print("2. История")
    print("3. Выход")



    choice = input("Выбери: ") 

    
    if choice == "1":
        if is_running():
            end_time()
        else:
            start_time()
    elif choice == "2":
        print("1 показать  историю")
        print("2 удалить историю")
        print("3 всего времени")
        print("4 выход")
        sup = input("выбери: ")
        if sup == "1":
           show_sessions()
        elif sup == "2":
            clear_all()
        elif sup == "3":
            total_time()
        elif sup == "4":
            pass
    elif choice == "3":
        break
    else:
        print("бог знает что ты ввёл, попробуй ещё раз")