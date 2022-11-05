from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

e = Entity(model='cube', collider='box', color=color.white, texture="white_cube")
e.scale = (50,1,50)
e.position = (0,-1,0)



player = FirstPersonController()
app.run()