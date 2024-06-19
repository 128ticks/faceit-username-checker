import requests
import time

def check_username_availability(start, end):
    available_usernames = []
    for user_id in range(start, end + 1):
        url = f"https://www.faceit.com/es/players/{user_id}"
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"User ID {user_id} is available.")
            available_usernames.append(user_id)
        else:
            print(f"User ID {user_id} is taken.")
            
        # Esperar 1 segundo entre solicitudes para no sobrecargar el servidor
        time.sleep(1)
            
    return available_usernames

# Chequear del ID 100 al 1000 para demostrar el funcionamiento
start_id = 1000
end_id = 1000000
available_usernames = check_username_availability(start_id, end_id)

print("Available User IDs:", available_usernames)
