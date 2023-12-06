print("hi MAXI XI")
import time
import pydobot 

# Crea una instancia de la clase Dobot
dobot = pydobot.Dobot(port="COM3")

print(dobot.pose())  #DEVUELVE LA POSICIÓN ACTUAL DEL ROBOT
# Mueve el brazo a la posición (X, Y, Z ,R)  #R ES EL GIRO DEL TERMINAL
dobot.move_to(x=200, y=15, z=0,r=0)
time.sleep(2)
print(dobot.pose())
# Espera 2 segundos

# Cierra la conexión con el brazo
dobot.close()
