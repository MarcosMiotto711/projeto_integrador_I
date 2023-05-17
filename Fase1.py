while True:
    mp10 = input('Digite o valor da quantidade de partículas inalaveis (MP10) no ar: ')
    mp10 = mp10.replace(',', '.')
    if mp10.replace('.', '').isdecimal() is False or mp10.count('.') > 1:
        print('Este número não é válido!')
    else:
        mp10 = float(mp10)
        break
while True:
    mp25 = input('Digite o valor da quantidade de partículas inalaveis finas (MP2,5) no ar: ')
    mp25 = mp25.replace(',', '.')
    if mp25.replace('.', '').isdecimal() is False or mp25.count('.') > 1:
        print('Este número não é válido!')
    else:
        mp25 = float(mp25)
        break
while True:
    o3 = input('Digite o valor da quantidade de ozônio (O2) no ar: ')
    o3 = o3.replace(',', '.')
    if o3.replace('.', '').isdecimal() is False or o3.count('.') > 1:
        print('Este número não é válido!')
    else:
        o3 = float(o3)
        break
while True:
    co = input('Digite o valor da quantidade de monóxido de carbono (CO) no ar: ')
    co = co.replace(',', '.')
    if co.replace('.', '').isdecimal() is False or co.count('.') > 1:
        print('Este número não é válido!')
    else:
        co = float(co)
        break
while True:
    no2 = input('Digite o valor da quantidade de dióxido de nitrogênio (NO2) no ar: ')
    no2 = no2.replace(',', '.')
    if no2.replace('.', '').isdecimal() is False or no2.count('.') > 1:
        print('Este número não é válido!')
    else:
        no2 = float(no2)
        break
while True:
    so2 = input('Digite o valor da quantidade de dióxido de enxofre (SO2) no ar: ')
    so2 = so2.replace(',', '.')
    if so2.replace('.', '').isdecimal() is False or so2.count('.') > 1:
        print('Este número não é válido!')
    else:
        so2 = float(so2)
        break
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
