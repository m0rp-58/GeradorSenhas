from colorama import Fore
import string
from random import choice

print(Fore.MAGENTA + "M0rp's Gerador de Senha - Welcome!\n")
print("""
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫\n""")

print("Esse script vai gerar diversas senhas..")
inp = input("Digite 1, para continuar : ")
if(inp == '1'):
    caracteres = 15
    valores = string.ascii_lowercase
    valores2 = string.ascii_uppercase
    password = ''
    password2 = ''
    for i in range(caracteres):
        password += choice(valores)
        password2 += choice(valores2)
        print("Senha recebida: " + password)
        print("Senha recebida: " + password2)

else:
    print("Era para você digitar 1...")


