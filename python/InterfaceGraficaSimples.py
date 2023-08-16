import PySimpleGUI as sg

#pysimplegui.tema("tema escolhido")
sg.theme("DarkAmber")

# Atribui um layout com textos, caixas de entrada e botões à uma variável
layout = [  [sg.Text("HELLO WORLD")],                           
            [sg.Text("digite seu nome:"), sg.InputText()],
            [sg.Button("ok"), sg.Button("cancel")]]

# Atribui uma função que cria uma janela à uma variável
# variável = funcão_do_pysimplegui("nome_da_janela", layout).
janela = sg.Window("hello world", layout)

# Enquanto for verdadeiro: (ou seja, vai acontecer...)
while True:
    # A variável event de classe "Values" recebe uma função que lê oque acontece na tela
    event, values = janela.read()
    # Se a janeta fecha ou usuário clicar em cancel, o programa irá parar
    if event == sg.WIN_CLOSED or event == "cancel":
        break
    # Exibe mensagem doque aconteceu
    print("seu nome é", values)

# Encerra a janela
janela.close()