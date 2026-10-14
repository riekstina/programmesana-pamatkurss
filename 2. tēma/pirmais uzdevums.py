a = "5"
b = 5
c = 5.5
print (type(a))
print (type(b))
print (type(c))

print(a + a)


vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
kopa = punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")

# kļūda radās rindā, kurā bija jāieraksta punkti
# jā, radās arī ValueError kļūda

# python daļskaitļos vajag punktu, nevis komatu, jo python atpazīst tikai punktu kā daļskaitļa atdalītāju, bet komatu nē.

vards2 = input("Ievadi varoņa vārdu: ")
punkti2 = int(input("Ievadi bāzes punktus: "))
reizinatajs2 = float(input("Ievadi reizinātāju: "))