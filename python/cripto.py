import getpass
import stdiomask

print("digite qualquer coisa")
senha = stdiomask.getpass(prompt = "senha: ", mask="*")
print (senha)
