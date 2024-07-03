import PySimpleGUI as sg
import os


def deletar():
    sg.theme('Green')

    layout = [
        [sg.Text('Digite o CPF a ser deletado:')],
        [sg.Input(key='cpf')],
        [sg.Button('Deletar')]
    ]

    window = sg.Window('Deletar', layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Deletar':

            Cpf = values['cpf']
            CpfTexto = f"{Cpf}.txt"

            try:
                os.remove(CpfTexto)
                sg.popup('Cpf CANCELADO , com sucesso!!!!!!! ')
            except FileNotFoundError:
                sg.popup('CPF não foi cancelado')


def atualizar():
    sg.theme('Green')

    layout = [

        [sg.Text('Digite o Cpf a ser atualizado')],
        [sg.Input(key='Cpf')],
        [sg.Button('Atualizar')]

    ]

    window = sg.Window('Atualizar', layout=layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:

            break

        elif event == 'Atualizar':

            Cpf = f"{values['Cpf']}.txt"

            try:

                os.remove(Cpf)
                Registro()
                sg.popup('CPF  foi atualiazodo!!')

            except:

                sg.popup('CPF não foi achado!!')



def consulta():
    sg.theme('Green')

    layout = [
        [sg.Text('Cpf')],
        [sg.Input(key='Cpf')],
        [sg.Button('Consultar')]
    ]

    window = sg.Window('Consultar', layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == 'Consultar':
            Cpf = values['Cpf']
            CpfTexto = f"{Cpf}.txt"

            try:
                with open(CpfTexto, "r") as file:
                    ArquivoTexto = file.read()
                    sg.popup(ArquivoTexto)
            except:
                sg.popup('CPF não encontrado!')


def Registro():
    sg.theme('Green')

    layout = [

        [sg.Text('Cpf')],
        [sg.Input(key='Cpf')],
        [sg.Text('Nome')],
        [sg.Input(key='Nome')],
        [sg.Text('Sobrenome')],
        [sg.Input(key='Sobrenome')],
        [sg.Text('Idade')],
        [sg.Input(key='Idade')],
        [sg.Button('Registrar')]
    ]

    window = sg.Window('registrar', layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Registrar':

            arquivo = f"{values['Cpf']}.txt"

            with open(arquivo, "w") as file:
                file.write(f"CPF: {values['Cpf']}\n")
                file.write(f"Nome: {values['Nome']}\n")
                file.write(f"Sobrenome: {values['Sobrenome']}\n")
                file.write(f"Idade: {values['Idade']}\n")


def menu():
    sg.theme('Green')

    layout = [

        [sg.Button('Registrar nomes')],
        [sg.Button('Consultar nomes')],
        [sg.Button('Atualizar nomes')],
        [sg.Button('Excluir nomes')],
        [sg.Button('Sair')]
    ]

    window = sg.Window('Menu', layout=layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Registrar nomes':
            Registro()

        elif event == 'Consultar nomes':
            consulta()

        elif event == 'Atualizar nomes':
            atualizar()

        elif event == 'Excluir nomes':
            deletar()

        elif event == 'Sair':
            break


def JanelaLogin():
    sg.theme('Green')

    layout = [
        [sg.Image(filename='pulmao.png')],
        [sg.Text('Usuario')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Entrar')],
        [sg.Text('', key='mensagem')],
        [sg.Button('Sair')]

    ]

    window = sg.Window('Menu', layout)

    while True:
        Event, values = window.read()
        if Event == sg.WIN_CLOSED:
            break
        elif Event == 'Entrar':
            SenhaCorreta = '123456'
            UsuarioCorreto = '123456'
            Usuario = values['usuario']
            Senha = values['senha']

            if Senha == SenhaCorreta and Usuario == UsuarioCorreto:
                window['mensagem'].update('Login feito com sucesso!')
                window.close()
                menu()
            else:
                window['mensagem'].update('Usuario incorreto!')

        elif Event == 'Sair':
            break


JanelaLogin()
