#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit menu

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import os
import pygame
from configobj import ConfigObj

from Game import Game


class MenuItem:
    def __init__(self, name, base_path):
        conf = ConfigObj(os.path.join(base_path,"game.conf"))
        self.name=name
        self.title=conf["GAME"]["title"]
        self.screenshot=pygame.image.load(os.path.join(base_path,"screenshot.png"))


class Menu(Game):

    def start(self):

      self.DISPLAY.print_text("GAMES PIT",self.FONTS["Famig___100"], self.COLORS['title'])
      self.DISPLAY.show()        
    
      self.menu_items=[]
      self.index=0

      games_dir_name=os.path.join(os.path.dirname(__file__),"..")

      if os.path.isdir(games_dir_name):
          dir_list=os.listdir(games_dir_name)
          for game in dir_list:
              if game != "menu":
                  self.menu_items.append(MenuItem(game, os.path.join(games_dir_name,game))) 

      self.wait(1000)
 

# Converts screen index to screen coordinates
    def i2coords(self, offset,i):
        index=offset+i
        l=i / 3
        c=i % 3
        return index,l,c

# Converts screen coordinates to index of menu items 
    def coords2index(self, offset, coords):
        for i in range(9):
            index,l,c=self.i2coords(offset,i)
            x=c*250+50
            y=l*190+40
            box=pygame.Rect(x,y,200,150)
            if box.collidepoint(coords): 
                return offset+i
        return False 


    def loop(self):

      offset=0
      selected_index=0

# LOOP THRU PAGES
      while True:
          self.fill()

          for i in range(9):
              index,l,c=self.i2coords(offset,i)
              if index < len(self.menu_items):
                  x=c*250+50
                  y=l*190+40
                  self.DISPLAY.print_image(self.menu_items[index].screenshot, x, y)
                  self.DISPLAY.print_text(self.menu_items[index].title, self.FONTS['FreeSans25'],self.COLORS['game'], x, y,)

# LOOP THRU ITEMS IN A PAGE
          while True:  
              index,l,c=self.i2coords(offset,selected_index)
              x=c*250+50-10
              y=l*190+40-7
              buffer=self.DISPLAY.print_image(self.IMAGES['selector'], x, y)
                                  
              self.DISPLAY.show()        

              input_type=self.CONTROLLER.wait_for_user_action()

              self.DISPLAY.print_image(buffer, x, y)

              if input_type == "K": #Keyboard
                  if self.CONTROLLER.key_name == 'right' and c < 2:
                    selected_index += 1
                  elif self.CONTROLLER.key_name == 'left' and c > 0:
                    selected_index -= 1
                  elif self.CONTROLLER.key_name == 'up':
                      if l == 0:
                          if offset > 0:
                              offset -= 9
                              selected_index += 6
                              break
                      else:
                          selected_index -= 3
                  elif self.CONTROLLER.key_name == 'down':
                      if l == 2:
                          if offset < len(self.menu_items) - 9: 
                              offset += 9
                              selected_index -= 6
                              break
                      else:
                          selected_index += 3
                  elif self.CONTROLLER.key_name == 'return':
                      return self.menu_items[index].name


              if input_type == "M": #Mouse

                  if self.CONTROLLER.mouse_button == 4 or (self.CONTROLLER.mouse_button == 1 and self.CONTROLLER.mouse_position[1] < 30): #Mouse Wheel UP
                      if offset > 0:
                          offset -= 9
                          selected_index = 0
                          break
                  elif self.CONTROLLER.mouse_button == 5 or (self.CONTROLLER.mouse_button == 1 and self.CONTROLLER.mouse_position[1] > self.DISPLAY.height - 30): #Mouse Wheel DOWN
                      if offset < len(self.menu_items) - 9: 
                          offset += 9
                          selected_index = 0
                          break
                  else:
                      index=self.coords2index(offset, self.CONTROLLER.mouse_position)
                      if index:
                          return self.menu_items[index].name

# Main
def main(name, CONF, DISPLAY, CONTROLLER):
    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    game_to_launch=menu.loop()
    return game_to_launch

