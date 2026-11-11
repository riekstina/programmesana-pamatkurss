
print(17 / 5)
print(17 // 5)
print(17 % 5) 
print(2 ** 3) 


mantas = int(input("Cik mantu ir? "))
somas_ietilpiba = int(input("Cik mantu ietilpst somā? "))
pilnas = mantas // somas_ietilpiba
pari = mantas % somas_ietilpiba
# print("Pilnas somas: ", pilnas)
# print("Pārpalikums: ", pari)

print(f"Vajag {pilnas} somas un {pari} mantas paliks pāri.")
videji = mantas / somas_ietilpiba
# print(f"Vidēji {videji} somas") #aiz komata ir daudz ciparu, 15
print(f"Vidēji {videji:.1f} somas") # :.1f figūriekavas nodrošina to, ka pat dalot ar skaitļiem, kuru rezultātā aiz komata ir daudz ciparu, rezultāts tiek noapaļots līdz vienam ciparam aiz komata.

limenis = float(input("Varoņa līmenis: "))
speks = limenis ** 2
# print(f"Varoņa speks: {speks}")
print(f"Varoņa līmenis: {limenis}, varoņa spēks: {speks}")
