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
        self.title=conf["GAME"]["title"] #unused currently
        self.screenshot=pygame.image.load(os.path.join(base_path,"screenshot.png"))
        self.base_path=base_path


class Menu(Game):

    def start(self):
      self.DISPLAY.print_text("GAMES PIT",1,1,self.FONTS["FreeSans80"], self.COLORS['title'])

      self.menu_items=[]
      self.index=0

      games_dir_name=os.path.join(self.CONF["GAME"]["base_path"],"..")
      if os.path.isdir(games_dir_name):
          dir_list=os.listdir(games_dir_name)
          for game in dir_list:
              if game != "menu":
                  self.menu_items.append(MenuItem(game, os.path.join(games_dir_name,game))) 
 

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
                  self.DISPLAY.print_text(self.menu_items[index].title, x, y,self.FONTS['FreeSans20'],self.COLORS['title'])

# LOOP THRU ITEMS IN A PAGE
          while True:  
              index,l,c=self.i2coords(offset,selected_index)
              x=c*250+50-10
              y=l*190+40-7
              buffer=self.DISPLAY.print_image(self.IMAGES['selector'], x, y)
                                  
              self.DISPLAY.show()        

              user_input=self.CONTROLLER.wait_for_user_action()

              self.DISPLAY.print_image(buffer, x, y)

              controller_type=user_input[0] 

              if controller_type == "K": #Keyboard
                  key_name,key_modifiers=user_input[1:]
                  if key_name == 'right' and c < 2:
                    selected_index += 1
                  if key_name == 'left' and c > 0:
                    selected_index -= 1
                  if key_name == 'up':
                      if l == 0:
                          if offset > 0:
                              offset=offset - 9
                              selected_index += 6
                              break
                      else:
                          selected_index -= 3
                  if key_name == 'down':
                      if l == 2:
                          if offset < len(self.menu_items) - 9: 
                              offset=offset + 9
                              selected_index -= 6
                              break
                      else:
                          selected_index += 3
                  if key_name == 'return':
                      return self.menu_items[index].name


              if controller_type == "M": #Mouse
                  coords,button=user_input[1:]  
                  index=self.coords2index(offset, coords)
                  if index:
                      return self.menu_items[index].name

# Main
def main(CONF, DISPLAY, CONTROLLER):

    menu=Menu(CONF,DISPLAY,CONTROLLER)
    menu.start()
    game_to_launch=menu.loop()
    return game_to_launch

