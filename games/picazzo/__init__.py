#!/usr/bin/python
# -*- coding: utf8 -*-

# Picazzo
#   For little artists

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 12/Mar/2013


from Game import Game

class Menu(Game):

    def start(self):
        return

    def loop(self):

        color=1
        painting=False

        while True:

          if painting:
              self.DISPLAY.print_image(self.IMAGES["brush"+str(color)],self.CONTROLLER.mouse_position[0],self.CONTROLLER.mouse_position[1])
              self.DISPLAY.show()

          input_type=self.CONTROLLER.check_user_action()

          if input_type == "M": #Mouse
             if self.CONTROLLER.mouse_button == 1:
                 painting=not painting
             if self.CONTROLLER.mouse_button == 2:
                 self.clean()
             if self.CONTROLLER.mouse_button == 3:
                 color+=1
                 if color>4:
                    color=1
          elif input_type == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                  break 

          self.wait(5)

# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

