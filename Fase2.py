#   Conexão com o banco de dados:
import oracledb

conexao = oracledb.connect(
    user="bd240223135",
    password="Ljfvl6",
    dsn="172.16.12.14/xe")

#   Leitura das amostras guardadas na tabela "AMOSTRAS" no banco de dados:
cursor = conexao.cursor()
cursor.execute("SELECT * FROM AMOSTRAS")
amostras = cursor.fetchall()

#   Calcular a média dos parâmtetros armazenados:
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
print(f'''A média dos parâmetros já armazenados são:
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}\n''')

#   Classificar a qualidade do ar e listar os efeitos à saúde:
if mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800:
    print('A qualidade do ar é péssima!')
    print('''Com a qualidade do ar neste estado, toda a população pode apresentar sérios riscos de manifestações de
doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras
em pessoas de grupos sensíveis.''')
elif mp10 > 150 or mp25 > 75 or o3 > 160 or co > 13 or no2 > 320 or so2 > 365:
    print('A qualidade do ar é muito ruim!')
    print('''Com a qualidade do ar neste estado, toda a população pode apresentar agravamento dos sintomas como tosse
seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Pode ocasionar
também em efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas).''')
elif mp10 > 100 or mp25 > 50 or o3 > 130 or co > 11 or no2 > 240 or so2 > 40:
    print('A qualidade do ar é ruim!')
    print('''Com a qualidade do ar neste estado, toda a população pode apresentar sintomas como tosse seca, cansaço,
ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.''')
elif mp10 > 50 or mp25 > 25 or o3 > 100 or co > 9 or no2 > 200 or so2 > 20:
    print('A qualidade do ar é moderada!')
    print('''Com a qualidade do ar neste estado, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças
respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral,
não é afetada.''')
else:
    print('A qualidade do ar é boa!')
cursor.close()
