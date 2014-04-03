# Sample program to create a pillar
import mcpi.minecraft as minecraft
import mcpi.block as block
# Connect to the Minecraft server
world = minecraft.Minecraft.create()
# Get the player's current position and store the coordinates
[x,y,z] = world.player.getPos()
# Set some variables to customize your pillar
height = 3
material = block.BRICK_BLOCK
# Build the pillar. It will be "height" blocks high and located one step away from the player.
for level in range(0, height):
 world.setBlock( x+1, y+level, z+1, material )
 level = level + 1;

