#coding: utf8

P1 = int(input("Digite o primeiro peso:"))
P2 = int(input("Digite o segundo peso:"))
P3 = int(input("Digite o terceiro peso:"))

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))

R = ((N1*P1)+(N2*P2)+(N3*P3))/(P1+P2+P3)

print ("A média é: ", R)
