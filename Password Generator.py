
import random,string

def main():
    print("WELCOME TO PASSWORD GENERATOR!")
    print("*******************************")
    number = int(input("How long is the passowrd: "))
    stepone(number)

def stepone(num):
        
        uppercaseLeter = (random.choice(string.ascii_uppercase))
        lowercaseLetter =  (random.choice(string.ascii_lowercase))
        digit = (random.choice(string.digits))
        punctuationSign = (random.choice(string.punctuation))
        password = uppercaseLeter + lowercaseLetter + digit + punctuationSign
        print(password)
    
main()

