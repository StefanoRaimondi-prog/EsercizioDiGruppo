# Dizionario per memorizzare gli utenti registrati con nome utente e password
utenti_registrati = {}

# Lista per memorizzare i concerti registrati, ogni concerto è un dizionario con nome e posti disponibili
concerti_registrati = []  # lista di dizionari: {nome, posti_disponibili}

# Lista per memorizzare le prenotazioni effettuate, ogni prenotazione è una tupla (utente, concerto)
prenotazioni_effettuate = []  # lista di tuple: (utente, concerto)

# Costanti per il limite massimo di concerti e posti disponibili per concerto
MAX_CONCERTI = 3 
POSTI_PER_CONCERTO = 10

# Password segreta per aggiungere concerti
PASSWORD_CONCERTO = "GHIBLI"

# Funzione per registrare un nuovo utente
def registra_utente():
    nome = input("Inserisci nome utente: ")
    if nome in utenti_registrati:
        print("Utente già registrato.")  # Controlla se l'utente è già registrato
        return
    password = input("Inserisci password: ")
    utenti_registrati[nome] = password  # Salva l'utente con la password
    print("Registrazione completata.")

# Funzione per effettuare il login di un utente
def login():
    nome = input("Nome utente: ")
    password = input("Password: ")
    if utenti_registrati.get(nome) == password:  # Verifica le credenziali
        print("Login riuscito!")
        return nome
    else:
        print("Credenziali errate.")
        return None

# Funzione per aggiungere un nuovo concerto
def aggiungi_concerto():
    if len(concerti_registrati) >= MAX_CONCERTI:  # Controlla il limite massimo di concerti
        print("Limite massimo di concerti raggiunto.")
        return
    password2 = input("Inserisci password segreta per aggiungere concerti: ")
    if password2 != PASSWORD_CONCERTO:  # Verifica la password segreta
        print("Password segreta errata!")
        return
    nome_concerto = input("Nome del concerto: ")
    # Aggiunge il concerto con il numero di posti disponibili
    concerti_registrati.append({"nome": nome_concerto, "posti": POSTI_PER_CONCERTO})
    print(f"Concerto '{nome_concerto}' aggiunto con successo.")

# Funzione per prenotare un concerto
def prenota_concerto(utente):
    if not concerti_registrati:  # Controlla se ci sono concerti disponibili
        print("Nessun concerto disponibile.")
        return
    print("Concerti disponibili:")
    # Mostra l'elenco dei concerti disponibili
    for index, c in enumerate(concerti_registrati):
        print(f"{index + 1}. {c['nome']} (Posti: {c['posti']})")
    scelta = int(input("Seleziona il numero del concerto da prenotare: ")) - 1
    if 0 <= scelta < len(concerti_registrati):  # Controlla se la scelta è valida
        concerto = concerti_registrati[scelta]
        if concerto['posti'] > 0:  # Controlla se ci sono posti disponibili
            concerto['posti'] -= 1  # Riduce il numero di posti disponibili
            prenotazioni_effettuate.append((utente, concerto['nome']))  # Registra la prenotazione
            print("Prenotazione effettuata!")
        else:
            print("Posti esauriti per questo concerto.")
    else:
        print("Scelta non valida.")

# ------------------------- Main Loop -------------------------
# Funzione principale che gestisce il menu e il flusso del programma
def main():
    while True:
        print("\n1. Registrati\n2. Login\n3. Esci")
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            registra_utente()  # Opzione per registrare un nuovo utente
        elif scelta == "2":
            utente = login()  # Opzione per effettuare il login
            if utente:
                while True:
                    print("\n1. Prenota Concerto\n2. Aggiungi Concerto\n3. Logout")
                    scelta2 = input("Seleziona un'opzione: ")
                    if scelta2 == "1":
                        prenota_concerto(utente)  # Opzione per prenotare un concerto
                    elif scelta2 == "2":
                        aggiungi_concerto()  # Opzione per aggiungere un concerto
                    elif scelta2 == "3":
                        break  # Logout
        elif scelta == "3":
            print("Uscita dal programma.")  # Esce dal programma
            break
        else:
            print("Scelta non valida.")  # Gestisce scelte non valide

# Punto di ingresso del programma
if __name__ == "__main__":
    main()
