class Pokemon_card:
  def __init__(self, name, level, current_exp, attribute, max_health, health, knocked_out):
    self.name = name
    self.level = level
    self.current_exp = current_exp
    self.attribute = attribute
    self.max_health = max_health
    self.health = health
    self.knocked_out = knocked_out
  
  def dec_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knocked_out = True
      print('{name} has been knocked out.'.format(name = self.name))
    else:
      print('{name} has taken {amount1} damage, it now has {amount2} health.'.format(name = self.name, amount1 = amount, amount2 = self.health))
    
  def revive(self):
    if self.knocked_out == True:
      self.knocked_out = False
      self.health = self.max_health
      print("{name} has been revived! Full HP ({num} points) has been restored.".format(name = self.name, num = self.max_health))

  def gain_health(self, amount):
    if self.knocked_out == True:
      print("This Pokémon has been knocked out! Please use 'revive' instead.")
      return
    self.health += amount
    if self.health > self.max_health:
      self.health = self.max_health
      print("{name}'s HP has been fully restored.".format(name = self.name))
    else:
      print("Successfully gained {num1} HP! {name} now has {num2} HP.".format(num1 = amount, name = self.name, num2 = self.health))
    
# Attack function
  def attack(self, opponent):
    if self.health == 0:
      print("{name} is already being knocked out and can't attack anymore.".format(name = self.name))
      return
    if opponent.health == 0:
      print("{name} is already being knocked out and can't be attacked.".format(name = opponent.name))
      return
    damage = 0
    if self.type == "Water":
      if opponent.type == "Electric" or opponent.type == "Grass":
        damage = 2 * self.level
      elif opponent.type == "Water" or opponent.type == "Fire" or opponent.type == "Ice":
        damage = 0.5 * self.level
    elif self.type == "Fire":




    if opponent_health <= 0:
      opponent.health = 0
      opponent.is_knocked = True
      self.current_exp += 50
      print("The opponent's {name1} has been knocked out bu your {name2}. Your {name2} has gained 50 EXP. Congratulations!".format(name1 = opponent.name, name2 = self.name))
    if self.current_exp >= 100:
      self.level += 1
      self.current_exp -= 100
      print("Your {name} levels up! It is now level {num}.".format(name = self.name, num = self.level))