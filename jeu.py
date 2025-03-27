import pyxel , random

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60
tir_liste =[]



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

def tirs_creation( x , y,tir_liste ) : 
  if pyxel.btnr(pyxel.KEY_SPACE):
    tir_liste.append([x+1,y-4])
  return tir_liste

def tir_deplacement (tir_liste) :
  for tir in tir_liste :
    tir[1] -=1
    if tir [1] <- 8:
      tir_liste.remove(tir) 
  return(tir_liste)

def ennemi_creation (x,y,ennemi_liste):
  if (pyxel.frame_count % 30 == 0):
    ennemi_liste.append([random(4,124),0])
  return (ennemi_liste)

def ennemi_mouvement (ennemi_liste) :
  for position in ennemi_liste:
    position[1] +=1
    if position[1] >-1 :
      ennemi_liste.remove(position)
  return (ennemi_liste)

  



def update () :
  global e_x ,e_y ,tir_liste
  e_x,e_y=e_deplacement(e_x,e_y)
  tir_liste=tirs_creation(e_x,e_y,tir_liste)
  tir_liste=tir_deplacement(tir_liste)
  ennemi_liste=ennemi_creation(ennemi_liste)
  ennemi_liste=ennemi_mouvement(ennemi_liste)
  


def draw ():
  pyxel.cls(0)
  pyxel.rect(e_x,e_y,4,4,4)
  
  for tir in tir_liste:
    pyxel.rect(tir[0],tir[1],1,4,11)

 




pyxel.run(update,draw)

# Pour run le truc que tu voulais c'est la commande : pyxel edit sprites.pyxres