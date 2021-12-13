import os, webbrowser
import PySimpleGUI as sg
from time import sleep

img = b'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'

def noises():
    try:
        os.system('escputil -n')
        sg.popup('Teste de ruídos',
                 'Sua impressora vai imprimir uma página com diversas informações... \n\nVerifique se todas as cores e linhas estão com qualidade de impressão satisfatória...')
    except:
        sg.popup_timed('Erro', 'Verifique se tens o escputil instalado em seu computador ou uma impressora compatível instalada...')
    
def simple_cleaning():
    try:
        os.system('escputil -c')
        sg.popup('Limpeza Simples',
                 'Processo de limpeza de cabeçote de impressão inicializado... \n\nAguarde até que a impressora fique silenciosa e as luzes parem de piscar...')
    except:
        sg.popup_timed('Erro', 'Verifique se tens o escputil instalado em seu computador ou uma impressora compatível instalada...')

def intense_cleaning():    
    try:        
        sg.popup_timed('Limpeza Intensa', 'Processo de limpeza de cabeçote de impressão intensa selecionado... \n\nAguarde até que a impressora fique silenciosa e as luzes parem de piscar...')
        os.system('escputil -c')
        sleep(120)
        os.system('escputil -c')
        sleep(120)
        os.system('escputil -c')
        sleep(120)
        os.system('escputil -c')
        sleep(120)
        os.system('escputil -c')
        
    except:
        sg.popup_timed('Atenção', 'Verifique se tens o escputil instalado em seu computador ou uma impressora compatível instalada...')
    
def manual():
    sg.popup('Manual',
                       '''O PrinterTools é uma ferramenta para teste e limpeza do cabeçote de impressão que utiliza o ESCPUTIL do sistema...

O ESCPUTIL deve estar instalado no sistema. Em sistemas Linux geralmente a instalação é possível com um simples:

    sudo apt-get install escputil
    
Para outros sistemas operacionais verifique se existem softwares oficiais para a mesma função...

Este software foi desenvolvido por Elizeu Barbosa Abreu...''')

sg.theme('Material1')

menu = [
    ['&Ferramentas', ['&Teste de Impressão', '&Limpeza Simples', '&Limpeza Pesada']],
    ['&Ajuda', ['&Manual', '---', '&Autor', ['&GitHub', '&Linkedin']]]
    ]

layout =[
    [sg.Menu(menu)],
    [sg.T(size=(1,1))],
    [sg.Stretch(),
     sg.Image(img),
     sg.T('Printer Tools', font=('Arial', 24)),
     sg.Stretch()],
    [sg.T(size=(1,1))],
    [sg.Button('Teste de Impressão', font=('Arial', 15), size=(30,4))],
    [sg.Button('Limpeza Simples', font=('Arial', 15), size=(30,4))],
    [sg.Button('Limpeza Pesada', font=('Arial', 15), size=(30,4))],
    [sg.T(size=(1,3))]
    ]

window = sg.Window('Printer Tools', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event in ('Teste de Impressão'):
        noises()
    elif event in ('Limpeza Simples'):
        simple_cleaning()
    elif event in ('Limpeza Pesada'):
        intense_cleaning()
    elif event in ('Manual'):
        manual()
    elif event in ('GitHub'):
        webbrowser.open_new('https://github.com/elizeubarbosaabreu')
    elif event in ('Linkedin'):
        webbrowser.open_new('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')
    
window.close()