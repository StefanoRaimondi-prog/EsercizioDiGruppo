# Sistema gestione prenotazioni sala concerti (senza classi)

utenti_registrati = {}
concerti_registrati = []  # lista di dizionari: {nome, posti_disponibili}
prenotazioni_effettuate = []  # lista di tuple: (utente, concerto)

MAX_CONCERTI = 3
POSTI_PER_CONCERTO = 10
PASSWORD_CONCERTO = "GHIBLI"

# ------------------------- Funzioni -------------------------
def registra_utente():
    nome = input("Inserisci nome utente: ")
    if nome in utenti_registrati:
        print("Utente già registrato.")
        return
    password = input("Inserisci password: ")
    utenti_registrati[nome] = password
    print("Registrazione completata.")

def login():
    nome = input("Nome utente: ")
    password = input("Password: ")
    if utenti_registrati.get(nome) == password:
        print("Login riuscito!")
        return nome
    else:
        print("Credenziali errate.")
        return None

def aggiungi_concerto():
    if len(concerti_registrati) >= MAX_CONCERTI:
        print("Limite massimo di concerti raggiunto.")
        return
    pwd = input("Inserisci password segreta per aggiungere concerti: ")
    if pwd != PASSWORD_CONCERTO:
        print("Password segreta errata!")
        return
    nome_concerto = input("Nome del concerto: ")
    concerti_registrati.append({"nome": nome_concerto, "posti": POSTI_PER_CONCERTO})
    print(f"Concerto '{nome_concerto}' aggiunto con successo.")

def prenota_concerto(utente):
    if not concerti_registrati:
        print("Nessun concerto disponibile.")
        return
    print("Concerti disponibili:")
    for idx, c in enumerate(concerti_registrati):
        print(f"{idx + 1}. {c['nome']} (Posti: {c['posti']})")
    scelta = int(input("Seleziona il numero del concerto da prenotare: ")) - 1
    if 0 <= scelta < len(concerti_registrati):
        concerto = concerti_registrati[scelta]
        if concerto['posti'] > 0:
            concerto['posti'] -= 1
            prenotazioni_effettuate.append((utente, concerto['nome']))
            print("Prenotazione effettuata!")
        else:
            print("Posti esauriti per questo concerto.")
    else:
        print("Scelta non valida.")

# ------------------------- Main Loop -------------------------
def main():
    while True:
        print("\n1. Registrati\n2. Login\n3. Esci")
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            registra_utente()
        elif scelta == "2":
            utente = login()
            if utente:
                while True:
                    print("\n1. Prenota Concerto\n2. Aggiungi Concerto\n3. Logout")
                    scelta2 = input("Seleziona un'opzione: ")
                    if scelta2 == "1":
                        prenota_concerto(utente)
                    elif scelta2 == "2":
                        aggiungi_concerto()
                    elif scelta2 == "3":
                        break
        elif scelta == "3":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
