from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesSpielers = mc.player.getPos()
x = positionDesSpielers.x
y = positionDesSpielers.y
z = positionDesSpielers.z
mc.postToChat("Koordinate x: " + str(x) + " Koordinate y: " + str(y) + " Koordinate z: " + str(z))
#Alternativ: positionDesSpielers = mc.player.getTilePos()
