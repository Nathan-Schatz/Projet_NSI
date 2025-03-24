import pyxel

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60

def e_deplacement(x,y):
  if pyxel.btn(pyxel.KEY_Q):
    if (x<120):
      x=x+1
  if pyxel.btn(pyxel.KEY_LEFT):
    if (x>0):
      x=x-20
  if pyxel.btn(pyxel.KEY_DOWN):
    if (y<120):
      y=y+1
  if pyxel.btn(pyxel.KEY_UP):
    if (y>0):
      y=y-1
  return x,y
    

def update () :
 global e_x ,e_y


def draw ():
  pyxel.cls(0)
  pyxel.rect(e_x,e_y,4,4,4)

pyxel.run(update,draw)

