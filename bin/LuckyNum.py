##########################################
# Title: LuckyNum
# 
#                Created: 2018-09-24
#                 Author: Bistrovic Igor
# 
# Version: 2.0.1
# 
# About: izbor brojeva za eurojackpot
# 
# Update:
# 18-12-15: ispravljen bug sa mogucim ponavljanjem brojeva u istoj kombinaciji
# 18-12-15: program ispisuje izabrane kombinacije u jednom redu
# 18-12-15: logger upisuje izabrane kombinacije u jednom redu
#
##########################################

# datum, broj kola
# usporedba izabranih brojeva sa izvučenim kombinacijama


import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y-%m-%d %a %H:%M:%S', 
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='D:/dev/logs/log-demo_luckynum.txt'
                    )
#logging.info('info')
#logging.debug('radnje')
#logging.warning('upozorenja')


# [ POCETAK PROGRAMA ]
luckynum_start = input("Pokrenuti LuckyNum? ")
if luckynum_start=="ne":
    logging.info('Prekinuto pokretanje aplikacije')
else:
    logging.debug('LuckyNum started.')

luckynum_kolo = 999
##luckynum_kolo = input("Broj kola: ")
##logging.info('%s | ' %(luckynum_kolo))

# [ KOMBINACIJA BROJEVA (5) ]
DobKo = set()
DobKo_brojevi_Size = 5
DobKo_Size = 0

while DobKo_Size < DobKo_brojevi_Size:
    g = random.randint(1,50)
    if g not in DobKo:
        DobKo_Size += 1
        DobKo.add(g)
#logging.info('Izabrani brojevi: %s', DobKo)

# [ DOPUNSKI BROJEVI (2) ]
DopBr = set()
Dop_brojevi_Size = 2
DopBr_Size = 0

while DopBr_Size < Dop_brojevi_Size:
    d = random.randint(1,10)
    if d not in DopBr:
        DopBr_Size += 1
        DopBr.add(d)
#logging.info('Dopunski brojevi: %s', DopBr)

# [ PRIKAZ KOMBINACIJE ]
print (DobKo, '/', DopBr)
print ("Dobitna kombinacija ", luckynum_kolo, ". kola EuroJackpota ce biti: ", DobKo, "/", DopBr)
logging.info ('Dobitna kombinacija %s. kola EuroJackpota ce biti: %s/%s', luckynum_kolo, DobKo, DopBr)

# [ KRAJ PROGRAMA ]
input ("\nPress Enter to continue...")
logging.info('LuckyNum closed.')