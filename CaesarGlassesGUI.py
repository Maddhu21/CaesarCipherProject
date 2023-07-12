import tkinter as tk

def encrypt():          #encryption function
    text = plain_text.get()
    shift = int(shift_value.get())

    encrypted_text = ""
    idx = 0
    for char in text:
        if(idx % 2 == 0): #even index shift right
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        else: # odd index shift left
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    encrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        idx+=1

    #Second encryption
    cipher_text =""
    for char in encrypted_text:
        #normal shift
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            cipher_text += encrypted_char
        else:
            cipher_text += char


    output_text.delete(0, tk.END)
    output_text.insert(tk.END, cipher_text)

def decrypt():              #decryption function
    text = plain_text.get()
    shift = int(shift_value.get())

    #backwards, so normal shift first
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    #shift based on index
    plaintext = ""
    idx = 0
    for char in decrypted_text:
        if(idx % 2 == 0):
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
                plaintext += decrypted_char
            else:
                plaintext += char
        else:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    decrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
                plaintext += decrypted_char
            else:
                plaintext += char
        idx+=1

    output_text.delete(0, tk.END)
    output_text.insert(tk.END, plaintext)

# Tkinter fx
window = tk.Tk()
window.title("Caesar Glasses")
window.geometry("400x200")
center_frame = tk.Frame(window)
center_frame.pack(expand=True)

# Plain text input box
plain_text_label = tk.Label(center_frame, text="Plain Text:")
plain_text_label.grid(row=0, column=0, sticky="W", padx=10, pady=5)
plain_text = tk.Entry(center_frame)
plain_text.grid(row=0, column=1, padx=10, pady=5)
# Shift value box
shift_value_label = tk.Label(center_frame, text="Shift Value:")
shift_value_label.grid(row=1, column=0, sticky="W", padx=10, pady=5)
shift_value = tk.Entry(center_frame)
shift_value.grid(row=1, column=1, padx=10, pady=5)
#Output box
output_label = tk.Label(center_frame, text="Output:")
output_label.grid(row=2, column=0, sticky="W", padx=10, pady=5)
output_text = tk.Entry(center_frame)
output_text.grid(row=2, column=1, padx=10, pady=5)

# Button to call encrypt and decrypt fx
encrypt_button = tk.Button(center_frame, text="Encrypt", command=encrypt)
encrypt_button.grid(row=3, column=0, padx=10, pady=5)
decrypt_button = tk.Button(center_frame, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=1, padx=10, pady=5)
window.mainloop()