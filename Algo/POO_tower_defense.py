import random
import time

class Monstre:
  def __init__(self, nbreDeVie):
    self.vie=nbreDeVie

  def donneEtat (self):
    return self.vie

  def perdVie (self, degat):
    self.vie=self.vie-degat

class Tower:
  def __init__(self, nbreDeVie):
    self.vie=nbreDeVie

  def donneEtat (self):
    return self.vie

  def perdVie (self, degat):
    self.vie=self.vie-degat
  
def game():
  tower = Tower(200)
  attack_speed = 1
  damage_tower = 10
  start = time.time()
  life_monster = 500
  monster = Monstre(life_monster)
  while tower.donneEtat()>0 and monster.donneEtat()>0 :
    time.sleep(attack_speed)
    monster.perdVie(damage_tower)
    print(f"La tour a tiré {damage_tower} dégat, il reste {monster.donneEtat()}points de vie au mostre")
    if time.time()-start> 10:
      tower.perdVie(200)
      if tower.donneEtat()<=0 and monster.donneEtat()>0:
        msg = f"monster est vainqueur, il lui reste encore {monster.donneEtat()} points alors que tower est mort"
        return msg
      else :
        msg = f"Les deux combattants sont morts en même temps"
        return msg
    if monster.donneEtat()<=0 and tower.donneEtat()>0:
      msg = f"tower a tué monster, il lui reste encore {tower.donneEtat()} points alors que monster est mort"
      print(msg)
      pass
    if tower.donneEtat()<=0 and monster.donneEtat()>0:
      msg = f"monster est vainqueur, il lui reste encore {monster.donneEtat()} points alors que tower est mort"
      return msg
      
    
print(game())


