from datetime import datetime
import json
start = None
end = None
sessions = []

def is_running():
    return start is not None


def load_sessions():
    global sessions
    try:
        with open("sessions.json","r", encoding="utf-8") as f:
             sessions = json.load(f) 
    except FileNotFoundError:
        return
      

def start_time():
    global start
    if start is None:
        start = datetime.now()
        print("Старт:", start.strftime("%H:%M:%S"))
    else:
        print("уже занято")

     

def end_time():
        global start
        global end
        if start is None:
             print("Сессия не была начата")
             return
        end = datetime.now()
        print("Конец:", end)
        duration = end - start
        mins = int(duration.total_seconds() // 60)
        print(f"Конец: {end.strftime('%H:%M:%S')}")
        print(f"Длительность: {mins} мин")
        sessions.append({
        "start": start.strftime("%H:%M:%S"),
        "end": end.strftime("%H:%M:%S"),
        "duration": mins})
        
        save_sessions()
        end  = None
        start = None
        return sessions


def show_sessions():
    print("\n📋 История сессий:")
    print("-" * 40)
    for i, session in enumerate(sessions, 1):
        print(f"{i}. {session['start']} → {session['end']} | {session['duration']} мин")
    print("-" * 40)
    print(f"Всего сессий: {len(sessions)}")

    
def save_sessions():
    with open("sessions.json", "w") as f:
        json.dump(sessions, f)

def clear_all():
    global sessions
    sessions.clear()
    save_sessions()

def total_time():
    total = 0
    for ses in sessions:
        total = total + ses["duration"]
    print(f"Всего времени: {total} мин")




