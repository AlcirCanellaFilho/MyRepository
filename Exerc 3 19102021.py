'''3) Faça um programa que receba a idade, a altura e o peso de 30 pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.'''
cont=0
somaaltura=0
contaltura=0
sup50=0
contpeso=0
while cont < 10:
    idade=int(input("Digite a idade:"))
    if idade>50:
        sup50+=1        
    altura=float(input("Digite a altura:"))
    if idade>=10 and idade <=20:
        somaaltura+=altura
        contaltura+=1
    peso=float(input("Digite o peso:"))
    if peso < 40:
        contpeso+=1
    cont+=1
        
print("Quantidade de pessoas com mais de 50 anos:", sup50)
mediaaltura=somaaltura/contaltura
print("Média das alturas de pessoas entre 10 e 20 anos: %.2f"%mediaaltura)
porcentagem=float(contpeso/(cont/100))
print("Porcentagem de pessoas com peso inferior a 40 quilos: %.2f"%porcentagem,"%")




