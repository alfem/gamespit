#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import pygame
import os
from configobj import ConfigObj

class Game:    
    '''
    This class makes coding easier, as you don't need to read any files to 
    use graphics or sounds. Drop them in your game directory and they will
    be automatically loaded into your game object.

    Just use Game.images["one_of_your_images_without_extension"] whenever you
    need to access one of your pygame images.

    Sounds work in a similar way (Game.sounds["one_name"]).

    Fonts are pre-rendered in many sizes, depending on your game config file.
    Use Game.fonts["one_name-one_size"] whenever you want to print text strings.
    '''
    def __init__(self, name, CONF, DISPLAY, CONTROLLER):
        self.name=name
        self.CONF=CONF
        self.DISPLAY=DISPLAY
        self.CONTROLLER=CONTROLLER
        self.IMAGES={}
        self.SOUNDS={} 
        self.FONTS={} 
        self.COLORS={}

        game_path=os.path.join(os.path.realpath(CONF["games_path"]), name)
        game_conf=os.path.join(game_path, "game.conf")
        CONF.merge(ConfigObj(game_conf))

        self.convert_colors(CONF["COLORS"])
#       Automagically load files into python objects (inspired on the "on rails" way)
        self.autoload_images(os.path.join(game_path,"images"))
        self.autoload_sounds(os.path.join(game_path,"sounds"))
        if "font_sizes" in CONF["GAME"]:
            self.autoload_fonts(os.path.join(game_path,"fonts"),CONF["GAME"]["font_sizes"])

#       Activate mouse pointer
        if CONF["GAME"]["mouse"] == "True":
            pygame.mouse.set_visible(1)
            if "pointer" in CONF["GAME"]:
              pointer_definition=CONF["GAME"]["pointer"].strip().splitlines()
              self.DISPLAY.set_pointer(pointer_definition)
        else:
            pygame.mouse.set_visible(0)

#       Clean the screen
        self.clean()
        self.show_help()
        self.clean()

# Convert named or numeric colors to pygame colors
    def convert_colors(self, colors):
        for name, value in colors.iteritems():
            if self.CONF.as_bool("debug"):
                print " Defined color", name, value
            self.COLORS[name]=self.DISPLAY.string_to_color(value)


# Load every image in images folder
    def autoload_images(self, dir_name):
        if self.CONF.as_bool("debug"):
            print " Searching for images in", dir_name
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name,extension=os.path.splitext(file)
                if extension.upper() in [".PNG",".JPG"]: 
                   if self.CONF.as_bool("debug"):
                       print "  found", name
                   self.IMAGES[name]=pygame.image.load(os.path.join(dir_name,file))
            return

# Load every sound in sounds folder
    def autoload_sounds(self, dir_name):
        if self.CONF.as_bool("debug"):
            print " Searching for sounds in", dir_name
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name,extension=os.path.splitext(file)
                if extension.upper() in [".WAV",".OGG",".MP3"]: 
                   name=os.path.splitext(file)[0]
                   if self.CONF.as_bool("debug"):
                       print "  found", name
                   self.SOUNDS[name]=pygame.mixer.Sound(os.path.join(dir_name,file))
            return

# Load every font in fonts folder 
    def autoload_fonts(self, dir_name, sizes):
        if self.CONF.as_bool("debug"):
            print " Searching for fonts in", dir_name
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name=os.path.splitext(file)[0]
                if self.CONF.as_bool("debug"):
                    print "  found", name
                for s in sizes:
                  if self.CONF.as_bool("debug"):
                      print "   generating", name+s
                  self.FONTS[name+s]=pygame.font.Font(os.path.join(dir_name,file),int(s))
        return


    def clean(self):
      self.DISPLAY.clean(self.COLORS["background"])
      return

    def fill(self,color=""):
      if color:
          self.DISPLAY.fill(color)
      else:
          self.DISPLAY.fill(self.COLORS["background"])
      return

    def wait(self,ms):
      pygame.time.wait(ms)
      return

    def show_help(self):
      if "help" in self.CONF["GAME"]:
          text=self.CONF['GAME']['help']
          self.DISPLAY.print_textbox(text)
          self.DISPLAY.show()
          if not self.CONF.as_bool("debug"):
              self.wait(int(self.CONF['help_speed'])*len(self.CONF["GAME"]["help"]))
  
