import tkinter
from tkinter import ttk
import oracledb
import numpy as np


def letra_num(matriz):
    nova_matriz = []
    for i in matriz:
        a = ord(i[0]) - ord('A') + 1
        b = ord(i[1]) - ord('A') + 1
        if a == 26:
            a = 0
        if b == 26:
            b = 0
        nova_matriz.append([a, b])
    return nova_matriz


def num_letra(matriz):
    matriz = np.array(matriz).T
    nova_matriz = []
    for i in matriz:
        a = chr(i[0] + ord('A') - 1)
        b = chr(i[1] + ord('A') - 1)
        if a == '@':
            a = 'Z'
        if b == '@':
            b = 'Z'
        nova_matriz.append([a, b])
    return nova_matriz


#   CRIPTOGRAFIA:
def criptografia(nome):
    nome = nome.upper()
    blanck_ind = []
    x = 0
    for i in nome:
        if i == ' ':
            blanck_ind.append(x)
        x += 1
    nome = nome.replace(' ', '')
    if len(nome) % 2 != 0:
        nome = nome + nome[len(nome) - 1]
    matriz_nome = []
    a = np.array([[2, 1], [5, 3]])
    for i in range(len(nome)):
        if i % 2 == 0:
            pass
        else:
            matriz_nome.append([nome[i - 1], nome[i]])
    c = np.array(letra_num(matriz_nome)).T
    p = np.dot(a, c)
    matriz_cod = []
    for i in p:
        lista = []
        for j in i:
            if j >= 26:
                lista.append(j % 26)
            else:
                lista.append(j)
        matriz_cod.append(lista)
    cripto = num_letra(matriz_cod)
    mensagem = ''
    for i in cripto:
        mensagem = mensagem + i[0] + i[1]
    for i in blanck_ind:
        mensagem = mensagem[0:i] + ' ' + mensagem[i:]
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO CLASSIFICACAO (VALOR) VALUES ('{mensagem}')")
    conexao.commit()
    cursor.close()


def descriptografia():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM CLASSIFICACAO")
    resultados = cursor.fetchall()
    ids = []
    for i in resultados:
        ids.append(i[0])
    id = max(ids)
    nome = ''
    for i in resultados:
        if i[0] == id:
            nome = i[1]
    blanck_ind = []
    x = 0
    for i in nome:
        if i == ' ':
            blanck_ind.append(x)
        x += 1
    nome = nome.replace(' ', '')
    matriz_nome = []
    for i in range(len(nome)):
        if i % 2 == 0:
            pass
        else:
            matriz_nome.append([nome[i - 1], nome[i]])
    c = np.array(letra_num(matriz_nome)).T
    a = np.array([[3, -1], [-5, 2]])
    p = np.dot(a, c)
    matriz_cod = []
    for i in p:
        lista = []
        for j in i:
            if j < 0:
                valor = j * -1
                valor = (int(valor / 26) * 26) + 26
                valor = valor + j
                lista.append(valor)
            elif j > 26:
                valor = j % 26
                lista.append(valor)
            else:
                lista.append(j)
        matriz_cod.append(lista)
    cripto = num_letra(matriz_cod)
    mensagem = ''
    for i in cripto:
        mensagem = mensagem + i[0] + i[1]
    for i in blanck_ind:
        mensagem = mensagem[0:i] + ' ' + mensagem[i:]
    if mensagem[len(mensagem) - 1] == mensagem[len(mensagem) - 2]:
        mensagem = mensagem[0:len(mensagem) - 1]
    mensagem = mensagem.lower()
    cursor.close()
    return mensagem


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
    classificar_window.title("Classificar amostra")
    classificar_window.resizable(height=False, width=False)
    classificar_window.iconbitmap('icone.ico')
    classificar_window.geometry(f'500x270+{largwindow - 250}+{altwindow - 125}')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM AMOSTRAS")
    amostras = cursor.fetchall()
    if amostras == []:
        tkinter.Label(classificar_window, text='Nenhuma amostra cadastrada!', font='Arial 20 bold').place(x=50, y=90)
        tkinter.Label(classificar_window, text='', background='black').place(x=157, y=204, width=185, height=49)
        retornar = tkinter.Button(classificar_window, text='Voltar ao Menu', font=fonte, fg='black',
                                  bd=0, command=classificar_window.destroy)
        retornar.pack(side='bottom', pady=20)
        return
    mp10 = 0
    mp25 = 0
    o3 = 0
    co = 0
    no2 = 0
    so2 = 0
    for i in amostras:
        mp10 += i[1]
        mp25 += i[2]
        o3 += i[3]
        co += i[4]
        no2 += i[5]
        so2 += i[6]
    x = len(amostras)
    mp10 = mp10 / x
    mp25 = mp25 / x
    o3 = o3 / x
    co = co / x
    no2 = no2 / x
    so2 = so2 / x
    if mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800:
        classificacao = 'pessima'
    elif mp10 > 150 or mp25 > 75 or o3 > 160 or co > 13 or no2 > 320 or so2 > 365:
        classificacao = 'muito ruim'
    elif mp10 > 100 or mp25 > 50 or o3 > 130 or co > 11 or no2 > 240 or so2 > 40:
        classificacao = 'ruim'
    elif mp10 > 50 or mp25 > 25 or o3 > 100 or co > 9 or no2 > 200 or so2 > 20:
        classificacao = 'moderada'
    else:
        classificacao = 'boa'
    criptografia(classificacao)
    resultado = descriptografia()
    cursor.close()
    cor = ''
    if resultado == 'boa':
        cor = '#57b563'
        tkinter.Label(classificar_window, text='A qualidade do ar é boa!', font='Arial 20 bold',
                      background='#57b563').place(x=87, y=90)
        classificar_window.configure(background='#57b563')
    if resultado == 'moderada':
        cor = '#f0ed46'
        tkinter.Label(classificar_window, text='A qualidade do ar é moderada!', font='Arial 20 bold',
                      background='#f0ed46').place(x=45, y=35)
        tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, pessoas de
grupos sensíveis (crianças, idosos e pessoas com
doenças respiratórias e cardíacas) podem apresentar
sintomas como tosse seca e cansaço. A população, 
em geral, não é afetada.''', font='Arial 14 ', background='#f0ed46').place(x=15, y=70)
        classificar_window.configure(background='#f0ed46')
    if resultado == 'ruim':
        cor = '#ee8c36'
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
        cor = '#d63636'
        tkinter.Label(classificar_window, text='A qualidade do ar é muito ruim!', font='Arial 20 bold',
                      background='#d63636').place(x=38, y=10)
        tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, toda a população
pode apresentar agravamento dos sintomas como tosse
seca, cansaço, ardor nos olhos, nariz e garganta e
ainda falta de ar e respiração ofegante. Pode ocasionar
também em efeitos ainda mais graves à saúde de grupos
sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas)''', font='Arial 14', background='#d63636').place(x=5, y=43)
        classificar_window.configure(background='#d63636')
    if resultado == 'pessima':
        cor = '#fd1616'
        tkinter.Label(classificar_window, text='A qualidade do ar é péssima!', font='Arial 20 bold',
                      background='#fd1616').place(x=56, y=35)
        tkinter.Label(classificar_window, text='''Com a qualidade do ar neste estado, toda a população
pode apresentar sérios riscos de manifestações de
doenças respiratórias e cardiovasculares. Como
consequência, ocorre o aumento de mortes prematuras
em pessoas de grupos sensíveis.''', font='Arial 14', background='#fd1616').place(x=10, y=70)
        classificar_window.configure(background='#fd1616')
    tkinter.Label(classificar_window, text='', background='black').place(x=157, y=204, width=185, height=49)
    retornar = tkinter.Button(classificar_window, text='Voltar ao Menu', font=fonte, fg='black', bg=cor,
                              bd=0, command=classificar_window.destroy)
    retornar.pack(side='bottom', pady=20)


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
