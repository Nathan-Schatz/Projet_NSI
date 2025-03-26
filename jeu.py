import pyxel

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60
t_y=23

def e_deplacement(x,y):
  if pyxel.btn(pyxel.KEY_RIGHT):
    if (x<120):
      x=x+1
  if pyxel.btn(pyxel.KEY_LEFT):
    if (x>0):
      x=x-1
  if pyxel.btn(pyxel.KEY_DOWN):
    if (y<120):
      y=y+1
  if pyxel.btn(pyxel.KEY_UP):
    if (y>0):
      y=y-1
  return x,y

def tirs_creation(yy) : 
  if pyxel.btn(pyxel.KEY_SPACE):
""
    

def update () :
  global e_x ,e_y ,m_x,m_y 
  e_x,e_y=e_deplacement(e_x,e_y)
  t_y=tirs_creation(t_y)
def draw ():
  pyxel.cls(0)
  pyxel.rect(e_x,e_y,4,4,4)
  
  
  pyxel.rect(e_x,t_y,1,4,4)




pyxel.run(update,draw)

