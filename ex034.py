while True:
    try:
        num1 = float(input("Primeiro número: "))
        op = str(input("Qual operação deseja realizar?\n+ adição\n- subtração\n* multiplicação\n/ divisão\n"))
        num2 = float(input("Segundo número: "))

        resul = 0

        if op == "+":
            resul = num1 + num2
        elif op == "-":
            resul = num1 - num2
        elif op == "*":
            resul = num1 * num2
        elif op == "/":
            resul = num1 / num2
        print(f"\033[33m{resul:.2f}")
        break
    except ValueError:
        print("Digite valores válidos!")
    except ZeroDivisionError:
        print("Erro! Não é possível fazer divisão por 0!")