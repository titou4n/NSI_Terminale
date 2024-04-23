from pyfirmata import Arduino, util
import time

carte = Arduino('COM4') # numéro du port d’entrée
acquisition = util.Iterator(carte)
acquisition.start()
sortie = carte.get_pin('d:11:o') # numéro de la broche
for i in range(10):
    time.sleep(1.0)
    sortie.write(True)
    time.sleep(2.0)
    sortie.write(False)
carte.exit()