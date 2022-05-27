import PySimpleGUI as sg

info_tab = [
    [sg.Text('Título:'), sg.Text('', key='-TITLE-')],
    [sg.Text('Duração:'), sg.Text('', key='-LENGTH-')],
    [sg.Text('Visualizações:'), sg.Text('', key='-VIEWS-')],
    [sg.Text('Autor:'), sg.Text('', key='-AUTHOR-')],
    [
        sg.Text('Descrição:'), 
        sg.Multiline('', key='-DESCRIPTION-', size=(40,20), no_scrollbar= True, disabled = True)
    ],
]

download_tab = [
    [sg.Frame('Melhor qualidade', [[sg.Button('Baixar', key = '-BEST-'), sg.Text('', key = '-BESTRES-'), sg.Text('', key = '-BESTSIZE-')]])],
    [sg.Frame('Pior qualidade', [[sg.Button('Baixar', key = '-WORST-'), sg.Text('', key = '-WORSTRES-'), sg.Text('', key = '-WORSTSIZE-')]])],
    [sg.Frame('Audio', [[sg.Button('Baixar', key = '-AUDIO-'), sg.Text('', key = '-AUDIOSIZE-')]])],
    [sg.VPush()]
]

layout = [[
    sg.TabGroup([[
        sg.Tab('info', info_tab),
        sg.Tab('download', download_tab)
    ]])
]]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()