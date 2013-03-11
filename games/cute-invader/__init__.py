#!/usr/bin/python
# -*- coding: utf8 -*-

# Cute Invader
#   Hit the UFO before it lands

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 11/Mar/2013

import random
import pygame

from Game import Game

class Menu(Game):

    def start(self):
        self.ufo_score=0
        self.starship_score=0
        return

    def loop(self):

        ufo_x=random.randint(0, self.DISPLAY.width- self.IMAGES["ufo"].get_width())
        ufo_y=0
        ufo_movement=0

        starship_x=self.DISPLAY.centerx
        starship_y=self.DISPLAY.height-self.IMAGES["starship-normal"].get_height()
        starship_movement=0

        starship="normal"

        while True:

          if ufo_movement <= 0:
              ufo_direction=random.choice((-2,2))
              ufo_movement=random.randint(30,150)

          new_ufo_x=ufo_x + ufo_direction
          if new_ufo_x > 0 and new_ufo_x < self.DISPLAY.width - self.IMAGES["ufo"].get_width():
              ufo_x=new_ufo_x
          else:
              ufo_movement=0
          ufo_movement-=1



          self.fill()
 
          self.DISPLAY.print_image(self.IMAGES["ufo"],ufo_x,ufo_y)
          self.DISPLAY.print_image(self.IMAGES["starship-"+starship],starship_x,starship_y)

          if starship=="firing":
              self.DISPLAY.print_image(self.IMAGES["missile"],missile_x,missile_y)
              missile_y=missile_y-2
              if missile_y<=0:
                  starship="normal"


          self.DISPLAY.show()

          input_type=self.CONTROLLER.check_user_action()

          if  input_type == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                  break 
              elif self.CONTROLLER.key_name == "left":
                  starship_movement = -1
              elif self.CONTROLLER.key_name == "right":
                  starship_movement = 1
              elif self.CONTROLLER.key_name == "up":
                  starship_movement = 0
              elif self.CONTROLLER.key_name == "space" and starship=="normal":
                  starship_movement = 0
                  starship="firing"
                  missile_x=starship_x
                  missile_y=starship_y                  

          new_starship_x=starship_x + starship_movement
          if new_starship_x > 0 and new_starship_x < self.DISPLAY.width - self.IMAGES["starship-"+starship].get_width():
              starship_x=new_starship_x

# Missile hits UFO 
          if starship=="firing":
              missile_rect=pygame.Rect((missile_x+20,missile_y,32,32))
              if missile_rect.colliderect((ufo_x,ufo_y,140,70)):
                  self.DISPLAY.print_image(self.IMAGES["explosion"],missile_x,ufo_y)
                  self.DISPLAY.show()
                  self.starship_score+=1
                  self.show_score()
                  starship="normal"
                  ufo_x=random.randint(0, self.DISPLAY.width- self.IMAGES["ufo"].get_width())
                  ufo_y=0
              else:
                  ufo_y=ufo_y+.6
    
# UFO hits spaceship
          if ufo_y>self.DISPLAY.height-200:
                  self.DISPLAY.print_image(self.IMAGES["explosion"],starship_x,starship_y)
                  self.DISPLAY.show()
                  self.ufo_score+=1
                  self.show_score()
                  starship="normal"
                  ufo_x=random.randint(0, self.DISPLAY.width- self.IMAGES["ufo"].get_width())
                  ufo_y=0
              
          self.wait(1)


    def show_score(self):
        self.DISPLAY.print_textbox("UFO:"+str(self.ufo_score)+" - STARSHIP:"+str(self.starship_score))
        self.DISPLAY.show()
        self.wait(3000)

# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

