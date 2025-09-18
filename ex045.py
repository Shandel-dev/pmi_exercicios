print("Informe uma data")
da = int(input("Dia: "))
ma = int(input("Mês: "))
aa = int(input("Ano: "))

mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [4, 6, 9, 11]

dataValida = True

if ma <= 12:
    if ma in mes31:
        if da > 31:
            msg = "Digite um dia válido!"
            dataValida = False
    elif ma in mes30:
        if da > 30:
            msg = "Digite um dia válido!"
            dataValida = False
    else:
        if (aa % 4 == 0 and aa % 100 != 0) or (aa % 400 == 0):
            if da > 29:
                msg = "Dia inválido!"
                dataValida = False
        else:
            if da > 28:
                msg = "Dia inválido!"
                dataValida = False
else:
    msg = "Digite um mês válido!"
    dataValida = False

if dataValida:
    print(f"{da:02d}/{ma:02d}/{aa}")
else:
    print(msg)