capital = float(input("Digite el valor de su capital: "))
duplicado = capital + capital
meses = 0
interes = 0

meses = 0

while capital < duplicado:
    interes = capital*0.5
    capital = capital + interes
    meses = meses + 1


print("el capital se duplica en: " + str(meses) + " MESES ")
