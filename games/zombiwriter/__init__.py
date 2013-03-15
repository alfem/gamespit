#!/usr/bin/python
# -*- coding: utf8 -*-

# Zombiwriter
#   Learn typewritting by killing zombies

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 15/Mar/2013

import random
import pygame

from Game import Game

class Menu(Game):

    def start(self):
        self.zombie_speed=int(self.CONF['GAME']['zombie_speed'])
        self.zombie_grow=int(self.CONF['GAME']['zombie_grow'])
        self.letters=self.CONF['GAME']['letters']
        return

    def loop(self):

        while self.CONTROLLER.key_name != "escape": #quit game:
 
            score=0
            zombies=[]

            while True:

                if random.randint(0, self.zombie_grow) == 0: #New Zombi
                    x=random.choice((0, self.DISPLAY.width- self.IMAGES["zombie-right"].get_width()))
                    y=random.randint(0, self.DISPLAY.height- self.IMAGES["zombie-right"].get_height())
                    letter=random.choice(self.letters)
                    zombies.append([x,y,letter])

                self.fill()

                happiness=1

                min_distance=500

                for z in zombies: 
                   if z[0] > self.DISPLAY.centerx:
                       if random.randint(0,self.zombie_speed*2) == 0:
                           z[0] -= self.zombie_speed
                       self.DISPLAY.print_image(self.IMAGES["zombie-left"],z[0],z[1])
                   else:
                       if random.randint(0,self.zombie_speed*2) == 0:
                           z[0] += self.zombie_speed
                       self.DISPLAY.print_image(self.IMAGES["zombie-right"],z[0],z[1])
                   self.DISPLAY.print_text(z[2],self.FONTS["OhTheHorror50"],self.COLORS["letters"],x=z[0]+20,y=z[1]+20)
                   distance=abs(self.DISPLAY.centerx - z[0] + self.IMAGES["zombie-right"].get_width() / 2)
                   if  distance < min_distance:
                       min_distance=distance

                if min_distance < 270:
                    happiness=2
                    if min_distance < 190:
                      happiness=3
                      if min_distance < 40:
                          happiness=4


                self.DISPLAY.print_image(self.IMAGES["face"+str(happiness)])

                input_type=self.CONTROLLER.check_user_action()

                if input_type == "K": #Keyboard
                    if self.CONTROLLER.key_name == "escape": #quit game
                      break 
                    elif len(self.CONTROLLER.key_name) == 1:
                      score-=1
                      for z in zombies:
                          if self.CONTROLLER.key_name == z[2].lower():
                             self.DISPLAY.print_image(self.IMAGES["explosion"],z[0],z[1])
                             zombies.remove(z)
                             score+=2
                             break

                formated_score="%03i" % score
                self.DISPLAY.print_textbox(formated_score,self.FONTS["7SDD50"],self.COLORS["score"],self.COLORS["scoreboard"],y=10)
     
                self.DISPLAY.show()
                 
                self.wait(10)

                if happiness == 4:
                    self.DISPLAY.print_textbox("Zombies eat you!",self.FONTS["OhTheHorror50"],self.COLORS["score"],self.COLORS["scoreboard"],y=self.DISPLAY.centery)
                    self.DISPLAY.show()
                    self.wait(4000)
                    break 
                if score < 0:            
                    self.DISPLAY.print_textbox("No points! You Loose",self.FONTS["OhTheHorror50"],self.COLORS["score"],self.COLORS["scoreboard"],y=self.DISPLAY.centery)
                    self.DISPLAY.show()
                    self.wait(4000)
                    break


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

