from os import path
from typing import final
from cryptography.fernet import Fernet

@final
class Crypto_demo:
    def __init__(self, message : str) -> None:

        #Static Variables
        self.secret_key = Fernet.generate_key() #A generated key
        self.key_file = "secret.key" #Secret key's file name
        self.text_message = message #The Original Text Message
        self.generate_Key_file()

        #Declaring a Fernet object to use anytimes
        self.fobj = Fernet(self.secret_key)

        # Dynamic varaibles 
        self.loaded_key = self.load_key() #Loaded Key 
        self.encoded_message = self.text_message.encode() #Encoding the message (just in case)
        self.encrypted_message = self.encrypt_message()
        self.decrypted_message = self.decrypt_message()


    # Execute this function just once
    def generate_Key_file(self) -> None:
        if path.isfile(self.key_file):
            pass
        else:
            with open(self.key_file, "wb") as Kfile :
                Kfile.write(self.secret_key)


    def load_key(self) -> bytes:
        return open(self.key_file, "rb").read()

    def encrypt_message(self) -> bytes:
        #Encrypting the Text after encoding (encoding is mandatory)
        encrypted_message = self.fobj.encrypt(self.encoded_message)
        return encrypted_message

    def decrypt_message(self) -> str :
        #Decrypting the Text and decoding before returning 
        decrypted_message = self.fobj.decrypt(self.encrypted_message)
        return decrypted_message.decode()

    def run(self) -> None:
        # self.generate_Key_file()
        print(f"Original message : {self.text_message}\n")
        print(f"Encrypted message : {self.encrypted_message}\n")
        print(f"Decrypted message : {self.decrypted_message}\n")
        assert self.text_message == self.decrypted_message
    

# if __name__=="__main__":
#     message = input("Enter your message : ")
#     crypto = Crypto_demo(message)
#     crypto.run()
