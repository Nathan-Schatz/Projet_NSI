import pyxel , random

pyxel.init (128,128,"neon nexus",quit_key=pyxel.KEY_ESCAPE)

e_x=60
e_y=60
tir_liste =[]
ennemi_liste=[]
explosion_liste=[]
boost_explosion_liste=[]
boost_liste=[]
vie=3
point=0
vitesse=1
menu=0
compteur=0
temps=0
scores={}
partie_numero=1
score_ennregistre= False
temps=0

pyxel.load("Ressources/vaisseau.pyxres")

def debut (menu):
  if pyxel.btn(pyxel.KEY_RETURN):
    menu+=1
  return(menu)

def retourne_debut (menu,vie,temps):
  if pyxel.btn(pyxel.KEY_TAB):
    menu=0
    vie=3
    temps=0
  return(menu,vie,temps)

def enregistrer_score(scores, partie_numero, point, temps):
    scores[partie_numero] = {"score": point, "temps": temps}
    return scores

def e_deplacement(x,y):
  if pyxel.btn(pyxel.KEY_RIGHT):
    if (x<120):
      x=x+3
  if pyxel.btn(pyxel.KEY_LEFT):
    if (x>0):
      x=x-3
  if pyxel.btn(pyxel.KEY_DOWN):
    if (y<120):
      y=y+3
  if pyxel.btn(pyxel.KEY_UP):
    if (y>0):
      y=y-3
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
  if (pyxel.frame_count % 50 == 0):
    ennemi_liste.append([random.randint(4,120),0])
  return (ennemi_liste)

def ennemi_mouvement (ennemi_liste) :
  for position in ennemi_liste:
    position[1] +=vitesse
    if position[1] >128:
      ennemi_liste.remove(position)
  return (ennemi_liste)


def suppresion_ennemi (point,compteur):
    for position in ennemi_liste:
      for tir in tir_liste :
        if position [0] <= tir[0]+4  and position[1] <= tir[1] and position[0]+4>= tir[0] and position[1]+4 >= tir[1]:
          tir_liste.remove(tir)
          ennemi_liste.remove(position)
          creation_annimation(position[0],position[1])
          point+=1
          compteur+=1
    return(point,compteur)

def vaisseau_suppresion (vie):
  for position in ennemi_liste :
    if position[0]-4 <= e_x+4 and position[1] <= e_y+4 and position[0]+4 >= e_x-4 and position[1]+4 >= e_y:
      ennemi_liste.remove(position)
      creation_annimation(e_x,e_y)
      vie-=1
  return (vie)



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

def temp(temps):
  if (pyxel.frame_count % 30 == 0):
    temps+=1
  return(temps)
  



def difficulté (vitesse,compteur):
  if compteur ==10:
    vitesse+=0.2
    compteur=0
  return(vitesse,compteur)

def boost_création(boost_liste):
  if (pyxel.frame_count % random.randint(250,1000) == 0):
    boost_liste.append([random.randint(4,120),0])
  return(boost_liste)

def boost_mouvement (boost_liste) :
  for place in boost_liste:
    place[1] +=1
    if place[1] >128:
      boost_liste.remove(place)
  return (boost_liste)

def boost_supression (vie):
  for place in boost_liste :
    if place[0]-4 <= e_x+4 and place[1] <= e_y+4 and place[0]+4 >= e_x-4 and place[1]+4 >= e_y:
      boost_liste.remove(place)
      creation_annimation_boost(place[0],place[1])
      vie+=1
  return (vie)

def creation_annimation_boost (x,y):
  boost_explosion_liste.append([x,y,0])

def annimation_boost ():
  for explosion_boost in boost_explosion_liste :
    explosion_boost[2]+=2
    if explosion_boost[2]==12:
      boost_explosion_liste.remove(explosion_boost)

    




  
  

def update () :
  global e_x ,e_y ,tir_liste,ennemi_liste,vie,point,menu,explosion_liste,compteur,vitesse,temps,scores,partie_numero,score_ennregistre,boost_liste,boost_explosion_liste
  if menu==0 :
    menu=debut(menu)
    temps=0
    score_ennregistre=False
   
  else :
    if vie>0:
      e_x,e_y=e_deplacement(e_x,e_y)
      tir_liste=tirs_creation(e_x,e_y,tir_liste)
      tir_liste=tir_deplacement(tir_liste)
      ennemi_liste=ennemi_creation(ennemi_liste)
      ennemi_liste=ennemi_mouvement(ennemi_liste)
      point,compteur=suppresion_ennemi(point,compteur)
      vie=vaisseau_suppresion(vie)
      vie=boost_supression(vie)
      boost_liste=boost_mouvement(boost_liste)
      boost_liste=boost_création(boost_liste)
      annimation()
      annimation_boost()
      vitesse,compteur=difficulté(vitesse,compteur)
      temps=temp(temps)
    else :
      menu,vie,temps=retourne_debut(menu,vie,temps)
      point=point_0(point)
    if vie <= 0 and menu != 0 and not score_ennregistre:
      global partie_numero
      scores = enregistrer_score(scores, partie_numero, point, temps)
      partie_numero += 1
      score_ennregistre = True
      

    


def draw ():
  pyxel.cls(0)
  if menu==0:
    pyxel.text(46,10,"neon nexus",10)
    pyxel.text(47,10,"neon nexus",7)
    pyxel.text(5,20,"Pour jouer appuie sur Entree",10)
    pyxel.text(5,30,"Sinon appuie sur Echap",10)
  
  
  else:
    if vie>0:
      pyxel.blt(e_x,e_y,0,16,1,15,15)
      for tir in tir_liste:
        pyxel.blt(tir[0],tir[1],1,20,6,6,6)

      for position in ennemi_liste :
        pyxel.blt(position[0],position[1],2,20,7,7, 7)
      for place in boost_liste :
        pyxel.rect(place[0],place[1],4,4,10)
      
      pyxel.text(10,10,"Vie "+str(vie),10)

      pyxel.text(10,16 ,"point "+str(point),10)

      pyxel.text(10,3,"Temps"+str(temps) + "s", 10)

      for explosion in explosion_liste:
        pyxel.circ(explosion[0],explosion[1],2*(explosion[2]//4), 8+explosion[2]%3)
      for explosion_boost in boost_explosion_liste :
        pyxel.circ(explosion_boost[0],explosion_boost[1],2*(explosion_boost[2]//4), 11+explosion_boost[2]%2)
    else :
        pyxel.text(20,20,"Retourne au lobby",10)
        pyxel.text(20,30,"Retourner lobby Tab",10)
        pyxel.rect(8, 50, 115, 70, 1) 
        pyxel.text(15, 54, "Scores :", 7)
        y_offset = 63
        for partie, data in scores.items():
          pyxel.text(13, y_offset, f"Partie {partie}: Score {data['score']}, Temps {data['temps']}s", 7)
          y_offset += 10


 
#le temps ne se réinitialse pas, il faut encore que je le fasse



pyxel.run(update,draw)

# Pour run le truc que tu voulais c'est la commande : pyxel edit sprites.pyxres 
#ca c'est pour mac
#pour windows
#python -m pyxel edit Ressources/vaisseau.pyxres