from pynput import keyboard as kb
import pydobot

dobot = pydobot.Dobot(port="COM3")
global x1,y1,z1,r,j1,j2,j3,j4
x1,y1,z1,r,j1,j2,j3,j4 = dobot.pose()
def pulsa(tecla):
	global x1,y1,z1,r
	print('Se ha pulsado la tecla ' + str(tecla))
	if tecla == kb.KeyCode.from_char('a'):
		y1+=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('d'):
		y1-=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('w'):
		z1+=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('s'):
		z1-=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('z'):
		x1+=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('c'):
		x1-=2
		dobot.move_to(x=x1, y=y1, z=z1,r=0)
	if tecla == kb.KeyCode.from_char('p'):
		dobot.suck(enable=True)
	if tecla == kb.KeyCode.from_char('o'):
		dobot.suck(enable=False)
	if tecla == kb.KeyCode.from_char('q'):
		return False

def suelta(tecla):
	print('Se ha soltado la tecla ' + str(tecla))
	if tecla == kb.KeyCode.from_char('q'):
		return False

escuchador = kb.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
	pass

dobot.close()
