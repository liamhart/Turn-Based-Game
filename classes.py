# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:13:12 2017

@author: Liam Hart
"""

import sys
import os
import random
import time

#   All characters refer to this superclass. HP is health, attack is offensive capability, 
#   defense is defensive capability, dexterity gives a second chance to attack, chargeRate
#   determines how quickly the charge attack is built up, and charge keeps track of it.
class Hero():
    def __init__(self, name, description, hp, attack, defense, dexterity, 
                 primarySkillName, secondarySkillName, finalSkillName, 
                 chargeRate):
        self.name = name
        self.description = description
        self.hp = hp
        self.hp_current = hp
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.primarySkillName = primarySkillName
        self.secondarySkillName = secondarySkillName
        self.finalSkillName = finalSkillName
        self.chargeRate = chargeRate
        self.critMultiplier = 1.5
        self.charge = 0
        # count down number of hits user is invincible
        self.invincibility = 0;
        self.isDead = False;
    
    def setInvincibility(self, hits):
        self.invincibility = hits
        print(self.name + ' is now invincible! ' + str(self.invincibility) + ' shield charge(s) remaining!')
        
    def decrementInvincibility(self):
        if self.invincibility > 0:
            self.invincibility -= 1
            print(self.name + ' has ' + str(self.invincibility) + ' shield charge(s) remaining!')
            if self.invincibility == 0:
                print(self.name + ' is now vulnerable!')
        else:
            self.invincibility = 0
            
    def kill(self):
        self.isDead = True
        
    def buildCharge(self, damage):
        if self.charge <= 100:
            self.charge += damage / self.chargeRate
        return damage
        
# The Bruiser class, focuses on doing damage
class Bruiser(Hero):
    def __init__(self):
        super().__init__(name = 'Bruiser',
             description = 'A strong warrior relying on close combat to deal damage',
             hp = 400,
             attack = 120,
             defense = 50,
             dexterity = 30,
             primarySkillName = 'Lunge',
             secondarySkillName = 'Comet Punch',
             finalSkillName = 'Meteor',
             chargeRate = 2)
        
        
    # describe attacks
    def describe():
        # try something like [attack:description] for mapping desc storage
        
        
        return 0
    
    # standard attack, returns the amount of HP target has remaining
    def primarySkill(self, Target):
        # base power
        basepower = 60
        
        # odds of extra effects
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit!')
            return (((self.attack * basepower) * self.critMultiplier) / Target.defense)
        elif random.randrange(1,100) < 10:
            print('The attack missed.')
            return 0
        else:
            return self.buildCharge(((self.attack * basepower) / Target.defense))
        
    # secondary attack, returns amount of HP target has remaining
    def secondarySkill(self, Target):
        #base power
        basepower = 20
        hits = random.randrange(1,6)
        
        #odds of extra effects
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit!')
            print('Hit ' + str(hits) + ' time(s)!')
            return self.buildCharge((((self.attack * basepower * hits) * self.critMultiplier) / Target.defense))
        else:
            print('Hit ' + str(hits) + ' time(s)!')
            return self.buildCharge(((self.attack * basepower * hits) / Target.defense))
        
    # final attack, charges when damage is dealt, more powerful attack. Returns amount of HP the target has remaining
    def finalSkill(self, Target):
        # base power
        basepower = 300
        
        # odds for extra effects
        time.sleep(2)
        print('A special attack!')
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit! The attack is especially powerful.')
            time.sleep(2)
            return (((self.attack * basepower) * self.critMultiplier) / Target.defense)
        else:
            return ((self.attack * basepower) / Target.defense)
        
class Cleric(Hero):
    def __init__(self):
        super().__init__(name = 'Cleric',
             description = 'A powerful healer and friendly aquaintence',
             hp = 200,
             attack = 50,
             defense = 80,
             dexterity = 30,
             primarySkillName = 'Pound',
             secondarySkillName = 'Stabilize',
             finalSkillName = 'Recover',
             chargeRate = 5)
    
    # describe attacks
    def describe():
        # try something like [attack:description] for mapping desc storage
        
        
        return 0
    
    # standard attack, returns the amount of HP target has remaining
    def primarySkill(self, Target):
        # base power
        basepower = 40
        
        # odds of extra effects
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit!')
            return (((self.attack * basepower) * self.critMultiplier) / Target.defense)
        else:
            return self.buildCharge(((self.attack * basepower) / Target.defense))
        
    # secondary attack, returns amount of HP target has remaining
    def secondarySkill(self, Target):
        #base power (negative indicates healing)
        basepower = -120
        
        #odds of extra effects
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit!')
            return self.buildCharge(abs((basepower * self.critMultiplier)))
        else:
            return self.buildCharge(abs(basepower))
        
    # final attack, charges when damage is dealt, returns a target to their maximum HP
    def finalSkill(self, Target):
        # interaction
        time.sleep(2)
        print('A special attack!')
        time.sleep(2)
        print(Target.name + ' has been restored to full HP!')
        return Target.hp
    
# tank class, a lot of health, can defend others with sheild charges
class Tank(Hero):
    def __init__(self):
        super().__init__(name = 'Tank',
             description = 'A sturdy powerhouse and reliable defender',
             hp = 500,
             attack = 80,
             defense = 100,
             dexterity = 10,
             primarySkillName = 'Swing',
             secondarySkillName = 'Guard',
             finalSkillName = 'Wide Guard',
             chargeRate = 5)
    
    # describe attacks
    def describe():
        # try something like [attack:description] for mapping desc storage
        
        
        return 0
    
    # standard attack, returns the amount of HP target has remaining
    def primarySkill(self, Target):
        # base power
        basepower = 40
        
        # odds of extra effects
        time.sleep(2)
        if random.randrange(1,100) < 10:
            print('Critical Hit!')
            return self.buildCharge((((self.attack * basepower) * self.critMultiplier) / Target.defense))
        else:
            return self.buildCharge(((self.attack * basepower) / Target.defense))
        
    # secondary attack, returns amount of HP target has remaining (in this case their current HP at the start of the turn)
    def secondarySkill(self, Target):
        # guard a target from damage for one turn
        time.sleep(2)
        Target.setInvincibility(2)
        
        return 0
        
    # final attack, charges when damage is dealt, more powerful attack. Returns amount of HP the target has remaining
    def finalSkill(self, Target):
        # base power
        basepower = 300
        
        # odds for extra effects
        time.sleep(2)
        print('A special attack!')
        time.sleep(2)
