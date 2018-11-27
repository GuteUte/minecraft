from random import randint
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
	positionDesAvatars = mc.player.getPos()
	x_KoordinateDesAvatars = positionDesAvatars.x
	y_KoordinateDesAvatars = positionDesAvatars.y
	z_KoordinateDesAvatars = positionDesAvatars.z
	zufallszahl = randint(0, 100)
	mc.setBlock(x_KoordinateDesAvatars, y_KoordinateDesAvatars, z_KoordinateDesAvatars, zufallszahl)
