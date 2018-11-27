import time
from random import randint
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

zaehler = 0
while zaehler < 5:
	x_Koordinate = randint(-126, 126)
	y_Koordinate = randint(-62, 62)
	z_Koordinate = randint(-126, 126)
	neuePosition = mc.getBlock(x_Koordinate, y_Koordinate, z_Koordinate)
	if neuePosition == 0:
		mc.player.setPos(x_Koordinate, y_Koordinate, z_Koordinate)
		time.sleep(5)
		zaehler += 1
