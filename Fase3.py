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
window.configure(background='#90E0EF')
window.title("Menu")
largwindow = int(round((window.winfo_screenwidth() / 2) - 280))
altwindow = int(round((window.winfo_screenheight() / 2) - 120))
window.geometry(f"280x300+{largwindow}+{altwindow}")
window.iconbitmap('icone.ico')
#   window.resizable(width=False, height=False)
fonte = 'Arial 14'
adc = tkinter.Button(window, text='Inserir amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=adicionar, bd=0)
adc.pack(pady=10, padx=20, anchor='nw')
alt = tkinter.Button(window, text='Alterar amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=alterar, bd=0)
alt.pack(pady=10, padx=20, anchor='nw')
exc = tkinter.Button(window, text='Excluir amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=excluir, bd=0)
exc.pack(pady=10, padx=20, anchor='nw')
cla = tkinter.Button(window, text='Classificar a\nqualidade do ar', font=fonte, fg='#CAF0F8', bg='#0096C7',
                     command=classificar, bd=0)
cla.pack(pady=10, padx=20, anchor='nw')
sair = tkinter.Button(window, text='Sair', font=fonte, fg='#CAF0F8', bg='#0096C7', command=exit, bd=0)
sair.pack(pady=10, padx=70, anchor='nw')
window.mainloop()
