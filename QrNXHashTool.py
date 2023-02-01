import hashlib
import pyfiglet
def hash_cracker(hash_value, hash_type, wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            word = line.strip()
            if hash_type == "md5":
                hash_obj = hashlib.md5(word.encode())
            elif hash_type == "sha1":
                hash_obj = hashlib.sha1(word.encode())
            elif hash_type == "sha3":
                hash_obj = hashlib.sha3_256(word.encode())
                hash_obj = hashlib.sha3_512(word.encode())
            elif hash_type == "blake2":
                hash_obj = hashlib.blake2b(your_passwd).hexdigest()
                hash_obj = hashlib.blake2s(your_passwd).hexdigest()
            if hash_obj.hexdigest() == hash_value:
                return word
    return None
banner = pyfiglet.figlet_format("QrNX\nHASH TOOL")
print(banner)
print("-------------------------------------------------------------------------")
wordlist = "Your Wordlist's Path"
option = int(input("Please Select An Operation,\n1-Encode\n2-Decode\nYour Answer: "))
while True:
    if option == 1:
        your_passwd = str(input("Please enter your string for hashing: ")).encode()
        algorithm = int(input("Please select the hashing type\n1-MD5\n2-SHA2\n3-SHA3\n4-BLAKE2\nYour Answer: "))
        if algorithm == 1:
            print("MD5:",hashlib.md5(your_passwd).hexdigest())
        elif algorithm == 2:
            print("SHA2-256bit:",hashlib.sha256(your_passwd).hexdigest())
            print("SHA2-512bit:",hashlib.sha512(your_passwd).hexdigest())
        elif algorithm == 3:
            print("SHA3-256bit:",hashlib.sha3_256(your_passwd).hexdigest())
            print("SHA3-256bit:",hashlib.sha3_512(your_passwd).hexdigest())
        elif algorithm == 4:
            print("BLAKE2:",hashlib.blake2b(your_passwd).hexdigest())
            print("BLAKE2:",hashlib.blake2s(your_passwd).hexdigest())
        cont = input("Do you want to continue? [y/n]")
        if cont == "n":
            break
    elif option == 2:
        your_passwd = str(input("Please enter your string for hashing: "))
        algorithm = int(input("Please select the hashing type\n1-MD5\n2-SHA2\n3-SHA3\n4-BLAKE2\nYour Answer: "))
        if algorithm == 1:
            plain_text = hash_cracker(your_passwd,"md5", wordlist)
            if plain_text:
                print("Decoded text:", plain_text)
            else:
                print("Hash value not found in wordlist")
        elif algorithm == 2:
            plain_text = hash_cracker(your_passwd,"sha1", wordlist)
            if plain_text:
                print("Decoded text:", plain_text)
            else:
                print("Hash value not found in wordlist")
        elif algorithm == 3:
            plain_text = hash_cracker(your_passwd,"sha3", wordlist)
            if plain_text:
                print("Decoded text:", plain_text)
            else:
                print("Hash value not found in wordlist")
        elif algorithm == 4:
            plain_text = hash_cracker(your_passwd,"blake2", wordlist)
            if plain_text:
                print("Decoded text:", plain_text)
            else:
                print("Hash value not found in wordlist")
        cont = input("Do you want to continue? [y/n]")
        if cont == "n":
            break
