print("""
    Vamos a dibujar
    un cuadrado""")
import time

import pydobot 

# Crea una instancia de la clase Dobot
dobot = pydobot.Dobot(port="COM3")
z1=-56.5
print(dobot.pose())
# Mueve el brazo a la posición (0, 0, 0)
dobot.move_to(x=213.6775665283203, y=16.8169002532959, z=z1,r=0)
dobot.set_eio(10,1)
print(dobot.pose())
dobot.move_to(x=213.6775665283203, y=36.8169002532959, z=z1,r=0)
print(dobot.pose())
dobot.move_to(x=293.6775665283203, y=36.8169002532959, z=z1,r=0)
print(dobot.pose())
dobot.move_to(x=293.6775665283203, y=16.8169002532959, z=z1,r=0)
print(dobot.pose())
dobot.move_to(x=213.6775665283203, y=16.8169002532959, z=z1,r=0)

print(dobot.pose())
time.sleep(2)
dobot.set_eio(10,0)
# Espera 2 segundos

# Cierra la conexión con el brazo
dobot.close()
