# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:44:20 2017

@author: Liam Hart
"""

import classes
import time

enemy = classes.Tank()
player = classes.Tank()

def checkInvincibility(Target):
    if Target.invincibility > 0:
        Target.decrementInvincibility()
        return 0
    else:
        return 1

def checkIfDead(Target):
    if Target.isDead == True:
        return True
    else:
        return False

# recursive algorithm to handle invalid user decisions
def playerDecide(enemy, charge):
    # user input deciding the action take this turn
    userChoice = input('>> ')
    
    # will correspond to user's first skill
    if userChoice == '1':
        enemy.hp_current -= player.primarySkill(enemy) * checkInvincibility(enemy)
        print('Enemy HP: {}'.format(enemy.hp_current))
    # will correspond to user's second skill
    elif userChoice == '2':
        enemy.hp_current -= player.secondarySkill(enemy) * checkInvincibility(enemy)
        print('Enemy HP: {}'.format(enemy.hp_current))
    # will correspond to user's final skill
    elif userChoice == '3':
        if charge < int(100):
            print('Haven\'t built enough charge!')
            playerDecide(enemy, charge)
        else:
            enemy.hp_current -= player.finalSkill(enemy) * checkInvincibility(enemy)
            print('Enemy HP: {}'.format(enemy.hp_current))
    

def battle():
    print('An enemy appears.')
    time.sleep(2)
    print('It appears to be a {}.'.format(enemy.name))
    time.sleep(2)
    print('Description: {}'.format(enemy.description))
    time.sleep(2)
    print('Stats: HP {}, Attack {}, Defense {}, Dexterity {}'.format(enemy.hp, enemy.attack, enemy.defense, enemy.dexterity))
    
     
    # main loop for the game
    while enemy.hp_current > 0 and checkIfDead(player) == False:
        if player.hp_current <= 0:
            time.sleep(2)
            print('You died.')
            player.kill()
     
        elif player.hp_current > 0:
            time.sleep(2)
            print('What would you like to do?')
            print('1. ' + player.primarySkillName)
            print('2. ' + player.secondarySkillName)
            if player.charge >= int(100):
                print('3. ' + player.finalSkillName)
            else:
                print('3. ' + str(int(player.charge)) + '% / 100%')
     
            # what will the player do?
            playerDecide(enemy, player.charge)
        
            if enemy.hp_current > 0:
                player.hp_current -= enemy.primarySkill(player)
                print('Your HP: {}'.format(player.hp_current))
                
            elif enemy.hp_current <= 0:
                print('\nThe {} dies.'.format(enemy.name))

            elif enemy.hp_current <= 0:
                print('\nThe {} dies.'.format(enemy.name))
            
            
battle()
            
            
            