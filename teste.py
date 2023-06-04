import tkinter

classificar_window = tkinter.Tk()
classificar_window.title("Classificar amostra")
classificar_window.resizable(height=False, width=False)
classificar_window.iconbitmap('icone.ico')
classificar_window.geometry(f'500x230+500+200')
resultado = 'pessima'
if resultado == 'boa':
    tkinter.Label(classificar_window, text='A qualidade do ar é boa!', font='Arial 20 bold',
                  background='#57b563').place(x=87, y=90)
    classificar_window.configure(background='#57b563')
if resultado == 'moderada':
    tkinter.Label(classificar_window, text='A qualidade do ar é moderada!', font='Arial 20 bold',
                  background='#f0ed46').place(x=45, y=35)
    tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, pessoas de
grupos sensíveis (crianças, idosos e pessoas com
doenças respiratórias e cardíacas) podem apresentar
sintomas como tosse seca e cansaço. A população, 
em geral, não é afetada.''', font='Arial 14 ', background='#f0ed46').place(x=15, y=70)
    classificar_window.configure(background='#f0ed46')
if resultado == 'ruim':
    tkinter.Label(classificar_window, text='A qualidade do ar é ruim!', font='Arial 20 bold',
                  background='#ee8c36').place(x=80, y=25)
    tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, toda a população
pode apresentar sintomas como tosse seca, cansaço, 
ardor nos olhos, nariz e garganta. Pessoas de grupos
sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas) podem apresentar efeitos
mais sérios na saúde.''', font='Arial 14', background='#ee8c36').place(x=15, y=60)
    classificar_window.configure(background='#ee8c36')
if resultado == 'muito ruim':
    tkinter.Label(classificar_window, text='A qualidade do ar é muito ruim!', font='Arial 20 bold',
                  background='#d63636').place(x=38, y=15)
    tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, toda a população
pode apresentar agravamento dos sintomas como tosse
seca, cansaço, ardor nos olhos, nariz e garganta e
ainda falta de ar e respiração ofegante. Pode ocasionar
também em efeitos ainda mais graves à saúde de grupos
sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas)
''', font='Arial 14', background='#d63636').place(x=5, y=50)
    classificar_window.configure(background='#d63636')
if resultado == 'pessima':
    tkinter.Label(classificar_window, text='A qualidade do ar é péssima!', font='Arial 20 bold',
                  background='#fd1616').place(x=56, y=35)
    tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, toda a população
pode apresentar sérios riscos de manifestações de
doenças respiratórias e cardiovasculares. Como
consequência, ocorre o aumento de mortes prematuras
em pessoas de grupos sensíveis.''', font='Arial 14', background='#fd1616').place(x=10, y=70)
    classificar_window.configure(background='#fd1616')

classificar_window.mainloop()
