
### Ievade
- Spēlētāja lietotājvārds
- Grūtības pakāpe, kurā vēlās spēlēt
- Uzbrukuma jauda

### Apstrāde
- Dzīvību skaits atkarībā no izvēlētās grūtības pakāpes
- Punktu rēķināšana
- Rezultāta rēķināšana atkarībā no izvēlētās grūtības pakāpes

### Izvade
- Iegūtie punkti 
- Iegūtais rezultāts


| Mainīgā vārds   | Datu tips   |  Ko glabā                                               |
|-----------------|-------------|---------------------------------------------------------|
| speletaja_vards |   str       | Spēlētāja ievadītais vārds                              |
| grutibas_pakape |   float     | Grūtības pakāpes koeficients                            |   
| uzbrukuma_jauda |   int       | Varoņa pamata uzbrukuma punkti                          |
| gala_uzbrukums  |   float     | Aprēķinātais uzbrukuma spēks, ņemot vērā grūtības pakāpi|  

FORMULA: gala_uzbrukums = uzbrukuma_jauda * grutibas_pakape
No input() nāk tie mainīgie, kuru vērtības ieraksta pats lietotājs, piemēram, speletaja_lietotajvards, grutibas_pakape, uzbrukuma_jauda.
Izrēķināti tiek dati, kas tiek aprēķināti no manis ievadītajiem skaitļiem, piemēram, gala_uzbrukums.

