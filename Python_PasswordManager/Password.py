
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input('Account Name:')
    pwd = input('Passwort:')
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
          

def delete_entries():
    try:
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()

        if not lines:
            print("Die Datei 'passwords.txt' ist leer.")
            return

        print("Folgende Einträge sind verfügbar:")
        for index, line in enumerate(lines):
            parts = line.strip().split("|")
            if len(parts) == 2:  # Prüfen, ob die Zeile zwei Teile (Name und Passwort) enthält
                name, pwd = parts
                print(f"{index + 1}. Account Name: {name}, Passwort: {pwd}")
        #Nummerierung
        entry_index = input("Gib die Nummer des Eintrags ein, den du löschen möchtest, oder drücke 'q' zum Abbrechen: ")

        if entry_index.lower() == 'q':
            return

        entry_index = int(entry_index) - 1

        if entry_index < 0 or entry_index >= len(lines):
            print("Ungültige Eingabe. Bitte eine gültige Nummer wählen.")
            return

        deleted_entry = lines.pop(entry_index) #Der ausgewählte Eintrag wird aus der Liste lines entfernt und in der Variablen deleted_entry gespeichert.

        with open('passwords.txt', 'w') as f:
            f.writelines(lines)

        print(f"Eintrag gelöscht: {deleted_entry.strip()}")

    except FileNotFoundError:
        print("Die Datei 'passwords.txt' existiert nicht.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {str(e)}")
#Diese except-Blöcke behandeln mögliche Fehler, die während des Versuchs auftreten könnten. FileNotFoundError wird behandelt, wenn die Datei 'passwords.txt' nicht gefunden wird, 
#und Exception für andere unerwartete Fehler.

while True:
    mode = input("Willst du ein Passwort hinzufügen, Löschen oder sehen welche Passwörter existieren(add, delete, view), drücke q zum abbrechen?").lower()

  
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "delete":
        delete_entries()
    else:
        print("Ungültiger Modus.")
        continue


   # f.write(name + "|" + pwd + "\n")
    # r': Lesen (Read) - Dies ist der Standardmodus. Du kannst die Datei lesen, aber nicht schreiben oder Inhalt hinzufügen.
    #'w': Schreiben (Write) - Dies öffnet die Datei zum Schreiben. Wenn die Datei bereits existiert, wird der vorherige Inhalt gelöscht. Wenn die Datei nicht existiert, wird sie erstellt.
    #'a': Anhängen (Append) - Dies öffnet die Datei zum Schreiben, aber anstatt den vorhandenen Inhalt zu löschen, wird neuer Inhalt am Ende der Datei hinzugefügt. Wenn die Datei nicht existiert, wird sie erstellt.
    # "\n" macht das bei der .txt datei eine neue Zeile erstellt wird
    





