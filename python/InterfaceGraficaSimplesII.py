from msilib.schema import CheckBox
from pickle import TRUE
from tabnanny import check
import PySimpleGUI as sg

# Criando uma classe para que possa ser usada em outros programas
class TelaPython:
    def __init__(self):
        
        # Adicionando cor à interface
        sg.theme("DarkAmber")

        # Definindo layout, assim como no arquivo "InterfaceGraficaSimples.py", o layout será uma lista atribuida à uma variável
        layout = [
            # Nessa linha, estou criando uma label, para criar uma label deve-se usar o Text depois de sg para identificar o objeto
            # O sg.Input é usado para adicionar um valor a esse objeto, e esse valor será dado pelo usuário
            # O parametro "key", é uma chave de onde o objeto pode ser referenciado
            [sg.Text("Seu nome: ",size=(7)), sg.Input(size=(30),key="nome")],
            [sg.Text("Seu email: ",size=(7)), sg.Input(size=(30),key="email")],
            [sg.Text("suas opções são:")],
            # Adicionando mais um componente, desta vez um checkbox
            [sg.Checkbox("opção1",size=(6), key="opção 1"), sg.Checkbox("opção2",size=(6), key="opção 2"), sg.Checkbox("opção3",size=(6), key="opção 3")],
            # Esse é um objeto do tipo botão, entre aspas será o texto presente dentro dele
            [sg.Button("entrar")]
        ]
        
        # Criando a janela e inserindo o layout
        janela = sg.Window("Login").layout(layout)
        # Ao utulizar o botão, ele encerrará a aplicação e retornará os dados
        self.Button, self.values = janela.Read()

    # Criando uma função para exibir os dados, afim de uma organização melhor
    def Iniciar(self):

        # atribuindo valor à variáveis atravéz do dado "inputado" pelo usuário sendo referenciado pelo atributo chave (key="")
        nome = self.values["nome"]
        email = self.values["email"]
        opcao1 = self.values["opção 1"]
        opcao2 = self.values["opção 2"]
        opcao3 = self.values["opção 3"]

        # Imprimindo os valores inputados 
        print(f"nome: {nome}")
        print(f"email: {email}")
        # Imprimindo se os check box estão marcados usando "True/False"
        print(f"sua opção 1 é : {opcao1}")
        print(f"sua opção 2 é : {opcao2}")
        print(f"sua opção 3 é : {opcao3}")

tela = TelaPython()
tela.Iniciar()
