
vards = input("Vārds: ")
hp = int(input("Dzīvības punkti: "))
jauda = float(input("Uzbrukuma jauda: "))
bojajums = hp * jauda
print("Dalībnieks", vards, "iegūst", bojajums, "punktus!")
# ja HP vērtību ieraksta 0, tad gala rezultāts vienmēr sanāks 0, jo jebkuru skaitli reizinot ar 0 iegūst 0.
# ja HP vērtību ieraksta negatīvu, tad gala rezultāts sanāks negatīvs, jo jebkuru skaitli reizinot ar negatīvu skaitli iegūst negatīvu rezultātu. To reāli izrēķinot, rezultāts sanāk neloģisks.
# ja vienkārši palaiž ar tukšu ievadi, rezultāts sanāk kļūdains, jo met ārā tādas kļūdas kā ValueError, jo programmai nav dots neviens skaitlis ar ko veikt aprēķinu.
# ja palaiž ar jaudu abc, tad rezultāts sanāk kļūdains, jo programma nevar reizināt skaitli ar tekstu.
# bīstamākā ievade no šīm iepriekš minētajām ir negatīva HP vērtība, jo tad gala rezultātā sanāk skaitlis, bet tas ir galīgi neloģiski. Pārējās kļūdas nav tik bīstamās, jo vienkārši met ārā ValueError vai 0.
