x = int(input("Digite o x: "))
y = int(input("Digite o y: "))

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Quadrante I")
elif x < 0 and y > 0:
    print("Quadrante II")
elif x < 0 and y < 0:
    print("Quadrante III")
else:
    print("Quadrante IV")