import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ss(participants):
    participants_copy = participants.copy()
    random.shuffle(participants_copy)
    pairs = dict(zip(participants, participants_copy))
    
    while any(pair == pairs[pair] for pair in pairs):
        random.shuffle(participants_copy)
        pairs = dict(zip(participants, participants_copy))
    
    return pairs

def collect_unique_participants():
    participants = set()
    num_participants = int(input("Entrer le nombre de participants: "))
    for i in range(num_participants):
        while True:
            name = input(f"Entrez le nom du participant n. {i + 1}: ").strip()
            if name in participants:
                print("Ce prénom a déjà été rentré.")
            elif any(char.isdigit() for char in name):
                print("Veuillez rentrer un prénom valide.")
            else:
                participants.add(name)
                break
    return list(participants)

def log_attempt(name, log_file="log.txt"):
    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            file.write("Prénom,Tentatives\n")
    
   #LOG de SAISIE
    logs = {}
    with open(log_file, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            log_name, count = line.strip().split(",")
            logs[log_name] = int(count)
    
    logs[name] = logs.get(name, 0) + 1

    with open(log_file, "w") as file:
        file.write("Prénom,Tentatives\n")
        for log_name, count in logs.items():
            file.write(f"{log_name},{count}\n")

participants = collect_unique_participants()
assignments = ss(participants)
used_names = set()

while True:
    clear_screen()
    participant_name = input("Rentre ton prénom pour savoir qui sera ton secret santa ... (or type 'exit' to quit): ")
    
    if participant_name.lower() == 'exit':
        break

    if participant_name in used_names:
        print("Ce prénom a déjà été utilisé. Vous ne pouvez plus le rentrer.")
    elif participant_name in assignments:
        print(f"Salut {participant_name}! Ton secret santa est {assignments[participant_name]}.")
        used_names.add(participant_name)
        log_attempt(participant_name)
    else:
        print("Prénom inexistant. Veuillez rentrer un prénom valide.")
    
    input("Appuyez sur entrée...")
    clear_screen()
