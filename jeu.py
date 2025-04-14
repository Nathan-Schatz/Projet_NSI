import pyxel , random

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60
tir_liste =[]
ennemi_liste=[]
explosion_liste=[]
vie=3
point=0
vitesse=50
menu=0

pyxel.load("Ressources/vaisseau.pyxres")

def debut (menu):
  if pyxel.btn(pyxel.KEY_TAB):
    menu+=1
  return(menu)

def retourne_debut (menu,vie):
  if pyxel.btn(pyxel.KEY_RETURN):
    menu=0
    vie=3
  return(menu,vie)
               

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
    tir_liste.append([x+5,y-4])
  return tir_liste

def tir_deplacement (tir_liste) :
  for tir in tir_liste :
    tir[1] -=1
    if tir [1] <- 8:
      tir_liste.remove(tir) 
  return(tir_liste)
  
def ennemi_creation (ennemi_liste):
  if (pyxel.frame_count % vitesse == 0):
    ennemi_liste.append([random.randint(4,120),0])
  return (ennemi_liste)

def ennemi_mouvement (ennemi_liste) :
  for position in ennemi_liste:
    position[1] +=1
    if position[1] >128:
      ennemi_liste.remove(position)
  return (ennemi_liste)


def suppresion_ennemi (point):
    for position in ennemi_liste:
      for tir in tir_liste :
        if position [0] <= tir[0]+4  and position[1] <= tir[1] and position[0]+4>= tir[0] and position[1]+4 >= tir[1]:
          tir_liste.remove(tir)
          ennemi_liste.remove(position)
          creation_annimation(position[0],position[1])
          point+=1
    return(point)

def vaisseau_suppresion (vie):
  for position in ennemi_liste :
    if position[0]-4 <= e_x+4 and position[1] <= e_y+4 and position[0]+4 >= e_x-4 and position[1]+4 >= e_y:
      ennemi_liste.remove(position)
      creation_annimation(e_x,e_y)
      vie-=1
  return (vie)

def depassement (vie):
  for position in ennemi_liste :
    if position[1]>=128 :
      ennemi_liste.remove(position)
      vie-=1
  return(vie)

def creation_annimation (x,y):
  explosion_liste.append([x,y,0])

def annimation ():
  for explosion in explosion_liste :
    explosion[2]+=2
    if explosion[2]==12:
      explosion_liste.remove(explosion)

def point_0(point):
  point=0
  return(point)


  
  

def update () :
  global e_x ,e_y ,tir_liste,ennemi_liste,vie,point,menu,explosion_liste
  if menu==0 :
    menu=debut(menu)
   
  else :
    if vie>0:
      e_x,e_y=e_deplacement(e_x,e_y)
      tir_liste=tirs_creation(e_x,e_y,tir_liste)
      tir_liste=tir_deplacement(tir_liste)
      ennemi_liste=ennemi_creation(ennemi_liste)
      ennemi_liste=ennemi_mouvement(ennemi_liste)
      point=suppresion_ennemi(point)
      vie=vaisseau_suppresion(vie)
      vie=depassement(vie)
      annimation()
      creation_annimation()
    else :
      menu,vie=retourne_debut(menu,vie)
      point=point_0(point)
      

    


def draw ():
  pyxel.cls(0)
  if menu==0:
    pyxel.text(5,20,"Pour jouer appuie sur TAB",10)
    pyxel.text(5,30,"Sinon appuei sur Echap",10)
  
  
  else:
    if vie>0:
      pyxel.blt(e_x,e_y,0,16,1,15,15)
      for tir in tir_liste:
        pyxel.blt(tir[0],tir[1],1,20,6,6,6)

      for position in ennemi_liste :
        pyxel.blt(position[0],position[1],2,20,7,7, 7)
      
      pyxel.text(10,10,"Vie"+str(vie),10)
      
      pyxel.text(10,15 ,"point"+str(point),10)
      for explosion in explosion_liste:
        pyxel.circ(explosion[0],explosion[1],2*(explosion[2]//4), 8+explosion[2]%3)
    else :
        pyxel.text(40,50,"Retourne au lobby ",10)
        pyxel.text(40,60,"retourner lobby entre ",10)


 




pyxel.run(update,draw)

# Pour run le truc que tu voulais c'est la commande : pyxel edit sprites.pyxres 
#ca c'est pour mac
#pour windows
#python -m pyxel edit Ressources/vaisseau.pyxres