import pyxel , random

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60
tir_liste =[]
ennemi_liste=[]
vie=3
point=0



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
  
def ennemi_creation (ennemi_liste):
  if (pyxel.frame_count % 50 == 0):
    ennemi_liste.append([random.randint(0,120),0])
  return (ennemi_liste)

def ennemi_mouvement (ennemi_liste) :
  for position in ennemi_liste:
    position[1] +=1
    if position[1] >128:
      ennemi_liste.remove(position)
  return (ennemi_liste)

def suppresion_ennemi ():
    for position in ennemi_liste:
      for tir in tir_liste :
        if position [0] <= tir[0]+1  and tir[1]+8 >= position[1] and position[1]+8 >= tir[1]+8 :
          tir_liste.remove(tir)
          ennemi_liste.remove(position)
          point+=1
    return(ennemi_liste,tir_liste)

def vaisseau_suppresion (vie):
  for position in ennemi_liste :
    if position[0] <= e_x+4 and position[1] <= e_y+4 and position[0]+4 >= e_x and position[1]+4 >= e_y:
      ennemi_liste.remove(position)
      vie-=1
  return (vie)



def update () :
  global e_x ,e_y ,tir_liste,ennemi_liste,vie
  e_x,e_y=e_deplacement(e_x,e_y)
  tir_liste=tirs_creation(e_x,e_y,tir_liste)
  tir_liste=tir_deplacement(tir_liste)
  ennemi_liste=ennemi_creation(ennemi_liste)
  ennemi_liste=ennemi_mouvement(ennemi_liste)
  suppresion_ennemi()
  vie=vaisseau_suppresion(vie)
  


def draw ():
  pyxel.cls(0)
  if vie >0 :
    pyxel.rect(e_x,e_y,4,4,4)
    for tir in tir_liste:
      pyxel.rect(tir[0],tir[1],1,4,11)

    for position in ennemi_liste :
      pyxel.rect(position[0],position[1],4,4,12)
    
    pyxel.text(10,10,"Vie"+str(vie),10)
    
    pyxel.text(10,10,str(point),10)
  else:
    pyxel.text(10,50,"Perdu retourne au lobby",8)


 




pyxel.run(update,draw)

# Pour run le truc que tu voulais c'est la commande : pyxel edit sprites.pyxres