import random
import string
import pyperclip

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Inizializza i caratteri disponibili
    chars = ''
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    # Genera la password casuale
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        # Chiedi all'utente la lunghezza della password desiderata
        length = int(input("Inserisci la lunghezza della password: "))

        # Genera la password
        password = generate_password(length)

        # Stampa la password generata
        print("Password generata:", password)

        # Chiedi all'utente se desidera copiare la password negli appunti
        copy_choice = input("Vuoi copiare la password negli appunti? (sì/no): ").lower()
        if copy_choice == 'sì' or copy_choice == 'si':
            # Copia la password negli appunti
            pyperclip.copy(password)
            print("La password è stata copiata negli appunti.")
        
        # Chiedi all'utente se desidera generare un'altra password
        choice = input("Vuoi generare un'altra password? (sì/no): ").lower()
        if choice != 'sì' and choice != 'si':
            break

if __name__ == "__main__":
    main()
