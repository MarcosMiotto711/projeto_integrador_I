import tkinter
import oracledb


def adicionar():
    wincad = tkinter.Toplevel()
    wincad.title('Cadastro')
    wincad.configure(background='white')
    wincad.iconbitmap('icone.ico')
    wincad.geometry("240x260+383+234")
    tkinter.Label(wincad, text='', background='black').place(x=18, y=18, width=204, height=44)
    botao1 = tkinter.Button(wincad, text='VOLTAR', font=fonte, command=wincad.destroy, bd=0, bg='white')
    botao1.place(x=20, y=20, width=200, height=40)
    wincad.mainloop()


def alterar():
    print('alteração')


def excluir():
    print('exclusão')


def classificar():
    print('classificação')


#   Estabelecendo conexão com o banco de dados
conexao = oracledb.connect(
    user="bd240223135",
    password="Ljfvl6",
    dsn="172.16.12.14/xe")
cursor = conexao.cursor()

#   Configuração da janela
window = tkinter.Tk()
window.configure(background='white')
window.title("Menu")
larg = int(round((window.winfo_screenwidth() / 2) - 280))
alt = int(round((window.winfo_screenheight() / 2) - 120))
window.geometry(f"560x240+{larg}+{alt}")
window.iconbitmap('icone.ico')
window.resizable(width=False, height=False)
#   Wighets
fonte = 'Bahnschrift 16'
tkinter.Label(window, text='', bg='black').place(x=18, y=18, width=254, height=64)
adc = tkinter.Button(window, text='ADICIONAR AMOSTRA', font=fonte, command=adicionar, bd=0, bg='white')
adc.place(x=20, y=20, width=250, height=60)
tkinter.Label(window, text='', bg='black').place(x=288, y=18, width=254, height=64)
alt = tkinter.Button(window, text='ALTERAR AMOSTRA', font=fonte, command=alterar, bd=0, bg='white')
alt.place(x=290, y=20, width=250, height=60)
tkinter.Label(window, text='', bg='black').place(x=18, y=98, width=254, height=64)
exc = tkinter.Button(window, text='EXCLUIR AMOSTRA', font=fonte, command=excluir, bd=0, bg='white')
exc.place(x=20, y=100, width=250, height=60)
tkinter.Label(window, text='', bg='black').place(x=288, y=98, width=254, height=64)
cla = tkinter.Button(window, text='CLASSIFICAR A\nQUALIDADE DO AR', font=fonte, command=classificar, bd=0, bg='white')
cla.place(x=290, y=100, width=250, height=60)
sair = tkinter.Button(window, text='SAIR', font=fonte, fg='white', command=exit, bd=0, bg='#bb0b0b')
sair.place(x=153, y=179, width=254, height=44)
window.mainloop()
