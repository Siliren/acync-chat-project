from datetime import datetime

def format_message(username, message):
    curent_time = datetime.now().strftime('%H:%M')

    return f"[{curent_time}]{username} : {message}"

def system_message(message):
    return f"[SYSTEM] {message}"