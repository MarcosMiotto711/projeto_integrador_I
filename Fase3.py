import tkinter
from tkinter import ttk
import oracledb


#   FUNÇÃO PARA ADIÇÃO DE UMA AMOSTRA
def adicionar(mp10, mp25, o3, co, no2, so2, msg, janela):
    cursor = conexao.cursor()
    mp10 = mp10.replace(' ', '')
    mp25 = mp25.replace(' ', '')
    o3 = o3.replace(' ', '')
    co = co.replace(' ', '')
    no2 = no2.replace(' ', '')
    so2 = so2.replace(' ', '')
    erro = 0
    errados = []
    if mp10.isdecimal() is False:
        errados.append('MP10')
        erro = 1
    if mp25.isdecimal() is False:
        errados.append('MP2.5')
        erro = 1
    if o3.isdecimal() is False:
        errados.append('O3')
        erro = 1
    if co.isdecimal() is False:
        errados.append('CO')
        erro = 1
    if no2.isdecimal() is False:
        errados.append('NO2')
        erro = 1
    if so2.isdecimal() is False:
        errados.append('SO2')
        erro = 1
    if erro == 1:
        mensagem = 'Os valores de '
        for i in range(len(errados)):
            mensagem = mensagem + errados[i] + ', '
        mensagem = mensagem[0:len(mensagem) - 2]
        mensagem = mensagem + ' são inválidos!'
        msg['text'] = mensagem
    if mp10 == '' and mp25 == '' and o3 == '' and co == '' and no2 == '' and so2 == '':
        msg['text'] = ''
    if erro == 0:
        cursor.execute(f"INSERT INTO AMOSTRAS(MP10, MP2_5, O3, CO, NO2, SO2) VALUES ({mp10}, {mp25}, {o3}, {co}, "
                       f"{no2}, {so2})")
        conexao.commit()
        janela.destroy()
    cursor.close()


#   FUNÇÃO PARA CRIAR UMA JANELA DE ADIÇÃO DE UMA AMOSTRA
def adicionar_win():
    #   CONFIGURAÇÃO DA JANELA DE ADIÇÃO DE UMA AMOSTRA
    adicionar_window = tkinter.Toplevel()
    adicionar_window.title("Adicionar amostra")
    adicionar_window.iconbitmap('icone.ico')
    adicionar_window.configure(bg='#90E0EF')
    adicionar_window.resizable(height=False, width=False)
    adicionar_window.geometry(f'570x200+{largwindow - 285}+{altwindow - 90}')
    #   Criar os widgets
    msg = tkinter.Label(adicionar_window, text='', font='Arial 15',
                        bg='#90E0EF')
    msg.place(x=0, y=96, width=570)
    mp10_label = tkinter.Label(adicionar_window, text='MP10', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    mp10_label.place(x=20, y=20)
    mp10_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    mp10_input.place(x=18, y=55)
    mp25_label = tkinter.Label(adicionar_window, text='MP2.5', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    mp25_label.place(x=107, y=20)
    mp25_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    mp25_input.place(x=110, y=55)
    o3_label = tkinter.Label(adicionar_window, text='O3', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    o3_label.place(x=219, y=20)
    o3_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    o3_input.place(x=202, y=55)
    co_label = tkinter.Label(adicionar_window, text='CO', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    co_label.place(x=307, y=20)
    co_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    co_input.place(x=294, y=55)
    no2_label = tkinter.Label(adicionar_window, text='NO2', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    no2_label.place(x=395, y=20)
    no2_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    no2_input.place(x=386, y=55)
    so2_label = tkinter.Label(adicionar_window, text='SO2', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    so2_label.place(x=485, y=20)
    so2_input = tkinter.Entry(adicionar_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6)
    so2_input.place(x=478, y=55)
    tkinter.Button(adicionar_window, text='Adicionar', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   command=lambda: adicionar(mp10_input.get(), mp25_input.get(), o3_input.get(), co_input.get(),
                                             no2_input.get(), so2_input.get(), msg,
                                             adicionar_window), bd=0).place(x=129, y=140)
    tkinter.Button(adicionar_window, text='Voltar ao Menu', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   bd=0, command=adicionar_window.destroy).place(x=265, y=140, height=43)


#   FUNÇÃO PARA EXECUTAR A EDIÇÃO DOS DADOS DE UMA AMOSTRA
def executar_alteracao(mp10, mp25, o3, co, no2, so2, msg, janela1, janela2, id_alterar):
    cursor = conexao.cursor()
    mp10 = mp10.replace(' ', '')
    mp25 = mp25.replace(' ', '')
    o3 = o3.replace(' ', '')
    co = co.replace(' ', '')
    no2 = no2.replace(' ', '')
    so2 = so2.replace(' ', '')
    erro = 0
    errados = []
    if mp10.isdecimal() is False:
        errados.append('MP10')
        erro = 1
    if mp25.isdecimal() is False:
        errados.append('MP2.5')
        erro = 1
    if o3.isdecimal() is False:
        errados.append('O3')
        erro = 1
    if co.isdecimal() is False:
        errados.append('CO')
        erro = 1
    if no2.isdecimal() is False:
        errados.append('NO2')
        erro = 1
    if so2.isdecimal() is False:
        errados.append('SO2')
        erro = 1
    if erro == 1:
        mensagem = 'Os valores de '
        for i in range(len(errados)):
            mensagem = mensagem + errados[i] + ', '
        mensagem = mensagem[0:len(mensagem) - 2]
        mensagem = mensagem + ' são inválidos!'
        msg['text'] = mensagem
    if mp10 == '' and mp25 == '' and o3 == '' and co == '' and no2 == '' and so2 == '':
        msg['text'] = ''
    if erro == 0:
        cursor.execute(f'''UPDATE AMOSTRAS 
SET MP10 = {mp10}, MP2_5 = {mp25}, O3 = {o3}, CO = {co}, NO2 = {no2}, SO2 = {so2}
WHERE ID ={id_alterar}''')
        conexao.commit()
        janela1.destroy()
        janela2.destroy()
    cursor.close()


#   FUNÇÃO PARA CRIAR UMA JANELA DE ALTERAÇÃO DA AMOSTRA SELECIONADA
def alterar(tree, janela):
    try:
        itemselecionado = tree.selection()[0]
    except:
        return
    valores_item = tree.item(itemselecionado, 'values')
    alterar_amostra_window = tkinter.Toplevel()
    alterar_amostra_window.title("Alterar valor da amostra")
    alterar_amostra_window.iconbitmap('icone.ico')
    alterar_amostra_window.configure(bg='#90E0EF')
    alterar_amostra_window.resizable(height=False, width=False)
    alterar_amostra_window.geometry(f'570x200+{largwindow - 285}+{altwindow - 90}')
    msg = tkinter.Label(alterar_amostra_window, text='', font='Arial 15',
                        bg='#90E0EF')
    msg.place(x=0, y=96, width=570)
    mp10_label = tkinter.Label(alterar_amostra_window, text='MP10', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    mp10_label.place(x=20, y=20)
    mp10_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                               textvariable=tkinter.StringVar(value=valores_item[1]))
    mp10_input.place(x=18, y=55)
    mp25_label = tkinter.Label(alterar_amostra_window, text='MP2.5', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    mp25_label.place(x=107, y=20)
    mp25_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                               textvariable=tkinter.StringVar(value=valores_item[2]))
    mp25_input.place(x=110, y=55)
    o3_label = tkinter.Label(alterar_amostra_window, text='O3', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    o3_label.place(x=219, y=20)
    o3_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                             textvariable=tkinter.StringVar(value=valores_item[3]))
    o3_input.place(x=202, y=55)
    co_label = tkinter.Label(alterar_amostra_window, text='CO', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    co_label.place(x=307, y=20)
    co_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                             textvariable=tkinter.StringVar(value=valores_item[4]))
    co_input.place(x=294, y=55)
    no2_label = tkinter.Label(alterar_amostra_window, text='NO2', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    no2_label.place(x=395, y=20)
    no2_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                              textvariable=tkinter.StringVar(value=valores_item[5]))
    no2_input.place(x=386, y=55)
    so2_label = tkinter.Label(alterar_amostra_window, text='SO2', font='Arial 18 bold', bg='#90E0EF', fg='#03045E')
    so2_label.place(x=485, y=20)
    so2_input = tkinter.Entry(alterar_amostra_window, font='Arial 16', bg='#CAF0F8', bd=0, justify='center', width=6,
                              textvariable=tkinter.StringVar(value=valores_item[6]))
    so2_input.place(x=478, y=55)
    tkinter.Button(alterar_amostra_window, text='Alterar', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   bd=0, command=lambda: executar_alteracao(mp10_input.get(), mp25_input.get(), o3_input.get(),
                                                            co_input.get(), no2_input.get(), so2_input.get(), msg,
                                                            alterar_amostra_window, janela,
                                                            int(valores_item[0]))).place(x=190, y=140)
    tkinter.Button(alterar_amostra_window, text='Voltar', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   bd=0, command=alterar_amostra_window.destroy).place(x=290, y=140, height=43)


#   FUNÇÃO PARA CRIAR UMA JANELA DE ALTERAÇÃO DE UMA AMOSTRA
def alterar_win():
    #   CONFIGURAÇÃO DA JANELA DE ALTERAÇÃO DE UMA AMOSTRA
    alterar_window = tkinter.Toplevel()
    alterar_window.title("Alterar amostra")
    alterar_window.iconbitmap('icone.ico')
    alterar_window.configure(bg='#90E0EF')
    alterar_window.resizable(height=False, width=False)
    alterar_window.geometry(f'510x300+{largwindow - 255}+{altwindow - 150}')
    fonte2 = ('Arial', 12)
    fonte_cabecalho = ('Arial', 14, 'bold')
    style = ttk.Style()
    style.configure("Treeview", font=fonte2)
    style.configure("Treeview.Heading", font=fonte_cabecalho)
    tv = ttk.Treeview(alterar_window, columns=('ID', 'MP10', 'MP2_5', 'O3', 'CO', 'NO2', 'SO2'), show='headings')
    tv.column('ID', minwidth=0, width=40, anchor='n')
    tv.column('MP10', minwidth=0, width=75, anchor='n')
    tv.column('MP2_5', minwidth=0, width=75, anchor='n')
    tv.column('O3', minwidth=0, width=75, anchor='n')
    tv.column('CO', minwidth=0, width=75, anchor='n')
    tv.column('NO2', minwidth=0, width=75, anchor='n')
    tv.column('SO2', minwidth=0, width=75, anchor='n')
    tv.heading('ID', text='ID')
    tv.heading('MP10', text='MP10')
    tv.heading('MP2_5', text='MP2.5')
    tv.heading('O3', text='O3')
    tv.heading('CO', text='CO')
    tv.heading('NO2', text='NO2')
    tv.heading('SO2', text='SO2')
    tv.pack(pady=10)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM AMOSTRAS')
    valores = cursor.fetchall()
    id_org = []
    for i in valores:
        id_org.append(i[0])
    id_org.sort()
    for i in id_org:
        for j in valores:
            if j[0] == i:
                tv.insert("", "end", text=i, values=j)
    cursor.close()
    tkinter.Button(alterar_window, text='Alterar amostra', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   command=lambda: alterar(tv, alterar_window), bd=0).place(x=65, y=246)
    tkinter.Button(alterar_window, text='Voltar ao Menu', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   bd=0, command=alterar_window.destroy).place(x=270, y=246, height=43)


def excluir(tree, janela):
    try:
        itemselecionado = tree.selection()[0]
    except:
        return
    valores_item = tree.item(itemselecionado, 'values')
    cursor = conexao.cursor()
    cursor.execute(f'''DELETE FROM AMOSTRAS
WHERE ID = {valores_item[0]}''')
    conexao.commit()
    cursor.close()
    janela.destroy()


#   Função de exclusão de uma cidade
def excluir_win():
    excluir_window = tkinter.Toplevel()
    excluir_window.title("Excluir amostra")
    excluir_window.resizable(height=False, width=False)
    excluir_window.iconbitmap('icone.ico')
    excluir_window.configure(bg='#90E0EF')
    excluir_window.geometry(f'510x300+{largwindow - 255}+{altwindow - 150}')
    fonte2 = ('Arial', 12)
    fonte_cabecalho = ('Arial', 14, 'bold')
    style = ttk.Style()
    style.configure("Treeview", font=fonte2)
    style.configure("Treeview.Heading", font=fonte_cabecalho)
    tv = ttk.Treeview(excluir_window, columns=('ID', 'MP10', 'MP2_5', 'O3', 'CO', 'NO2', 'SO2'), show='headings')
    tv.column('ID', minwidth=0, width=40, anchor='n')
    tv.column('MP10', minwidth=0, width=75, anchor='n')
    tv.column('MP2_5', minwidth=0, width=75, anchor='n')
    tv.column('O3', minwidth=0, width=75, anchor='n')
    tv.column('CO', minwidth=0, width=75, anchor='n')
    tv.column('NO2', minwidth=0, width=75, anchor='n')
    tv.column('SO2', minwidth=0, width=75, anchor='n')
    tv.heading('ID', text='ID')
    tv.heading('MP10', text='MP10')
    tv.heading('MP2_5', text='MP2.5')
    tv.heading('O3', text='O3')
    tv.heading('CO', text='CO')
    tv.heading('NO2', text='NO2')
    tv.heading('SO2', text='SO2')
    tv.pack(pady=10)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM AMOSTRAS')
    valores = cursor.fetchall()
    id_org = []
    for i in valores:
        id_org.append(i[0])
    id_org.sort()
    for i in id_org:
        for j in valores:
            if j[0] == i:
                tv.insert("", "end", text=i, values=j)
    cursor.close()
    tkinter.Button(excluir_window, text='Excluir amostra', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   command=lambda: excluir(tv, excluir_window), bd=0).place(x=65, y=246)
    tkinter.Button(excluir_window, text='Voltar ao Menu', font=fonte, fg='#CAF0F8', bg='#0096C7',
                   bd=0, command=excluir_window.destroy).place(x=270, y=246, height=43)


#   Função da classificação da qualidade do ar segundo as amostras dadas
def classificar_win():
    classificar_window = tkinter.Toplevel()
    classificar_window.title("Classificar ")
    classificar_window.iconbitmap('icone.ico')
    classificar_window.geometry(f'400x250+{largwindow - 200}+{altwindow - 125}')


#   ESTABELECENDO CONEXÃO COM O BANCO DE DADOS
conexao = oracledb.connect(
    user="bd240223135",
    password="Ljfvl6",
    dsn="172.16.12.14/xe")

#   CONFIGURAÇÃO DA JANELA DE MENU
window = tkinter.Tk()
window.configure(background='#90E0EF')
window.title("Menu")
largwindow = int(round(window.winfo_screenwidth() / 2))
altwindow = int(round(window.winfo_screenheight() / 2))
window.geometry(f"280x345+{largwindow - 140}+{altwindow - 175}")
window.iconbitmap('icone.ico')
window.resizable(width=False, height=False)
fonte = 'Arial 18'
#   Criar os widgets
adc = tkinter.Button(window, text='Inserir amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=adicionar_win,
                     bd=0)
adc.pack(pady=10)
alt = tkinter.Button(window, text='Alterar amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=alterar_win, bd=0)
alt.pack(pady=10)
exc = tkinter.Button(window, text='Excluir amostra', font=fonte, fg='#CAF0F8', bg='#0096C7', command=excluir_win, bd=0)
exc.pack(pady=10)
cla = tkinter.Button(window, text='Classificar a\nqualidade do ar', font=fonte, fg='#CAF0F8', bg='#0096C7',
                     command=classificar_win, bd=0)
cla.pack(pady=10)
sair = tkinter.Button(window, text='Sair', font=fonte, fg='#03045E', bg='#CAF0F8', command=exit, bd=0)
sair.pack(pady=10)
window.mainloop()
