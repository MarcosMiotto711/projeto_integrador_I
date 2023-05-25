import tkinter
#   import oracledb


#   Função da adição de uma cidade
def adicionar():
    adicionar_window = tkinter.Toplevel()
    adicionar_window.title("Adicionar amostra")
    adicionar_window.iconbitmap('icone.ico')
    adicionar_window.geometry(f'400x250+{largwindow}+{altwindow}')
    mp10 = tkinter.Entry(adicionar_window)
    mp10.pack(pady=50)


#   Função da alteração de uma cidade
def alterar():
    alterar_window = tkinter.Toplevel()
    alterar_window.title("Alterar")
    alterar_window.iconbitmap('icone.ico')
    alterar_window.geometry(f'400x250+{largwindow}+{altwindow}')


#   Função de exclusão de uma cidade
def excluir():
    excluir_window = tkinter.Toplevel()
    excluir_window.title("Excluir")
    excluir_window.iconbitmap('icone.ico')
    excluir_window.geometry(f'400x250+{largwindow}+{altwindow}')


#   Função da classificação da qualidade do ar segundo as amostras dadas
def classificar():
    classificar_window = tkinter.Toplevel()
    classificar_window.title("Classificar")
    classificar_window.iconbitmap('icone.ico')
    classificar_window.geometry(f'400x250+{largwindow}+{altwindow}')


#   Estabelecendo conexão com o banco de dados
#   conexao = oracledb.connect(
#       user="bd240223135",
#       password="Ljfvl6",
#       dsn="172.16.12.14/xe")
#   cursor = conexao.cursor()

#   Configuração da janela
window = tkinter.Tk()
window.configure(background='white')
window.title("Menu")
largwindow = int(round((window.winfo_screenwidth() / 2) - 280))
altwindow = int(round((window.winfo_screenheight() / 2) - 120))
window.geometry(f"560x240+{largwindow}+{altwindow}")
window.iconbitmap('icone.ico')
window.resizable(width=False, height=False)
fonte = 'Arial 14'
labeladc = tkinter.Label(window, text='', bg='black')
labeladc.place(x=18, y=18, width=254, height=64)
adc = tkinter.Button(window, text='ADICIONAR AMOSTRA', font=fonte, command=adicionar, bd=0, bg='white')
adc.place(x=20, y=20)
labelalt = tkinter.Label(window, text='', bg='black')
labelalt.place(x=288, y=18, width=254, height=64)
alt = tkinter.Button(window, text='ALTERAR AMOSTRA', font=fonte, command=alterar, bd=0, bg='white')
alt.place(x=290, y=20, width=250, height=60)
labelexc = tkinter.Label(window, text='', bg='black')
labelexc.place(x=18, y=98, width=254, height=64)
exc = tkinter.Button(window, text='EXCLUIR AMOSTRA', font=fonte, command=excluir, bd=0, bg='white')
exc.place(x=20, y=100, width=250, height=60)
labelcla = tkinter.Label(window, text='', bg='black')
labelcla.place(x=288, y=98, width=254, height=64)
cla = tkinter.Button(window, text='CLASSIFICAR A\nQUALIDADE DO AR', font=fonte, command=classificar, bd=0, bg='white')
cla.place(x=290, y=100, width=250, height=60)
sair = tkinter.Button(window, text='SAIR', font=fonte, fg='white', command=exit, bd=0, bg='#bb0b0b')
sair.place(x=153, y=179, width=254, height=44)
window.mainloop()
