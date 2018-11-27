from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = int(input("Geben Sie eine X-Koordinate an: "))
y = int(input("Geben Sie eine y-Koordinate an: "))
z = int(input("Geben Sie eine z-Koordinate an: "))

mc.setBlock(x, y-1, z, 16)
mc.player.setPos(x, y, z)
