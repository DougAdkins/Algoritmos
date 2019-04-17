#coding: utf8

N = int(input("Digite o tempo em segundos: "))

if N >= 3600:
    H = N/3600
    Resto = int(((N-H)%3600))
print (Resto)
print (H)

#elif N <= 60:
#    M = 
