#!/usr/bin/python
# -*- coding: utf8 -*-

# Jumping Bunny
#   Avoid obstacles jumping over them

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 18/Mar/2013

import random
import pygame

from Game import Game

class Menu(Game):

    def start(self):
        self.score=0
        self.min_speed=int(self.CONF["GAME"]["min_speed"])
        self.max_speed=int(self.CONF["GAME"]["max_speed"])
        self.bunny_jump_height=int(self.CONF["GAME"]["bunny_jump_height"])
        return

    def loop(self):

        wheel_incoming=False
        bunny="walking"
        bunny_x=20
        bunny_walking_y=self.DISPLAY.height-self.IMAGES["bunny"].get_height()
        bunny_y=bunny_walking_y

        while True:

            self.fill()
     
            if not wheel_incoming: # No obstacles? Launch one!
                if random.randint(0, 20) == 0:
                    wheel_incoming=True
                    wheel_speed=random.randint(self.min_speed, self.max_speed)
                    wheel_frame=0
                    wheel_x=self.DISPLAY.width
                    wheel_y=self.DISPLAY.height-self.IMAGES["wheel1"].get_height()
            else: 
                wheel_x-= wheel_speed
                wheel_frame+=1
                if wheel_frame==3:
                    wheel_frame=0
                self.DISPLAY.print_image(self.IMAGES["wheel"+str(wheel_frame)],wheel_x,wheel_y)
                if wheel_x < -100:
                    wheel_incoming=False
                    self.score+=1

            formated_score="%03i" % self.score
            self.DISPLAY.print_textbox(formated_score,self.FONTS["7SDD80"],self.COLORS["score"],self.COLORS["scoreboard"],y=10)

            if bunny == "jumping": # The bunny is jumping
                bunny_y += bunny_movement 
                if bunny_y < self.bunny_jump_height:
                    bunny_movement=2
                if bunny_y >= bunny_walking_y:
                    bunny="walking"
                    bunny_y=bunny_walking_y


            bunny_rect=pygame.Rect((bunny_x,bunny_y,180,250)) #Bunny hit check

            if wheel_incoming and bunny_rect.colliderect((wheel_x,wheel_y,100,100)): 
                self.SOUNDS['bump'].play()
                self.DISPLAY.print_image(self.IMAGES["bunny-hitted"],bunny_x,bunny_y)
                x=(bunny_x+wheel_x+80)/2
                y=(bunny_y+wheel_y+80)/2
                self.DISPLAY.print_image(self.IMAGES["explosion"],x,y)
                self.DISPLAY.show()
                self.wait(5000)
                self.score=0
                bunny="walking"
                bunny_y=bunny_walking_y
                wheel_incoming=False
                continue
            else:
                if bunny=="walking": 
                    self.DISPLAY.print_image(self.IMAGES["bunny"],bunny_x,bunny_y)
                else:
                    self.DISPLAY.print_image(self.IMAGES["bunny-jumping"],bunny_x,bunny_y)

            self.DISPLAY.show()

            input_type=self.CONTROLLER.check_user_action()

            if input_type == "K": #Keyboard
                if self.CONTROLLER.key_name == "escape": #quit game
                    break 
                elif self.CONTROLLER.key_name == "space" and bunny=="walking":
                    bunny_movement=-2
                    bunny="jumping"
                    self.SOUNDS['spring'].play()

       
                  
            self.wait(5)



# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

