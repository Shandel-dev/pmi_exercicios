print("Código que converte segundos em horas, minutos e segundos")

seg = int(input("Digite o tempo em segundos: "))

hora = seg // 3600
minuto = seg % 3600 // 60
segundos = seg % 3600 % 60

print("Horas:", hora)
print("Minutos:", minuto)
print("Segundos:", segundos)
print("\033[32m{}h:{}m:{}s".format(hora, minuto, segundos))
