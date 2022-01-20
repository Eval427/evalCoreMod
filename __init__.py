import renpy
import renpy.ast as ast
import renpy.display.im as im
import renpy.parser as parser

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

#Adding side images for unique character expressions
varaSmallExpressions = ["smnormal", "smgrowl", "smnone", "smshocked", "smshocked_b", "smsad", "smnormal_ghost", "smsmile"]
adineIceCreamExpressions = ["annoyed_eval_icecream", "disappoint_eval_icecream", "frustrated_eval_icecream", "giggle_eval_icecream", "normal_eval_icecream", "sad_eval_icecream", "think_eval_icecream"]
remyShotExpressions = ["angry_eval_shot", "look_eval_shot", "normal_eval_shot", "sad_eval_shot", "shy_eval_shot", "smile_eval_shot"]
adineGoggleExpressions = ["annoyed", "disappoint", "frustrated", "giggle", "normal", "sad", "think"]
remyGoggleExpressions = ["look", "normal", "sad", "shy", "smile"]
varaGoggleExpressions = ["smnone", "smnormal", "smsmile"]
amelyGoggleExpressions = ["smnormal", "smsad"]
adineExtraExpressions = ["determined", "optimism", "none", "contemplate", "excited", "scared", "sigh", "laugh"]

def load_side_ims():
    def clip_vara_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (0, 150, 350, 400)), 250, 300), horizontal=True)

    def clip_adine_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (50, 0, 500, 600)), 250, 300), horizontal=True)
    
    def clip_remy_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (5, 30, 500, 600)), 250, 300), horizontal=True)

    def clip_amely_side_image(imagefile):
        return im.Scale(im.Crop(imagefile, (180, 114, 500, 500)), 250, 250)
    
    for expression in varaSmallExpressions:
        renpy.exports.image("side vara %s"%expression.replace("_", " "), clip_vara_side_image("cr/vara_%s.png"%expression))
    
    for expression in adineIceCreamExpressions:
        renpy.exports.image("side adine %s"%expression.replace("_", " "), clip_adine_side_image("cr/adine_%s.png"%expression))
    
    for expression in remyShotExpressions:
        renpy.exports.image("side remy %s"%expression.replace("_", " "), clip_remy_side_image("cr/remy_%s.png"%expression))
    
    for expression in remyGoggleExpressions:
        renpy.exports.image("side remy %s goggles"%expression, clip_remy_side_image("cr/remy_%s_goggles.png"%expression))
    
    for expression in varaGoggleExpressions:
        renpy.exports.image("side vara %s goggles"%expression, clip_vara_side_image("cr/vara_%s_goggles.png"%expression))
    
    for expression in amelyGoggleExpressions:
        renpy.exports.image("side amely %s goggles"%expression, clip_amely_side_image("cr/amely_%s_goggles.png"%expression))
        renpy.exports.image("side amely %s goggles flip"%expression, clip_amely_side_image("cr/amely_%s_goggles_flip.png"%expression))
    
    #For most of Adine's goggle expressions
    for expression in adineGoggleExpressions:
        if expression in ["giggle", "think"]:
            for letter in ["a", "b", "c", "d"]:
                if letter == "a":
                    renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
                else:
                    renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
        else:
            for letter in ["a", "b", "c", "d", "e"]:
                if letter == "a":
                    renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
                else:
                    renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
    
    #For Adine's sad shot expressions that had to be differently formatted
    for letter in ["a", "b", "c", "d", "e"]:
        if letter == "a":
            renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
        else:
            renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
    
    #For Adine's extra side image expressions
    for expression in adineExtraExpressions:
        for letter in ["a", "b", "c"]:
            if letter == "a":
                renpy.exports.image("side adine %s"%expression, clip_adine_side_image("cr/adine_%s.png"%expression))
            else:
                renpy.exports.image("side adine %s %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_%s.png"%(expression, letter)))

#For Adine's extra expressions
for expression in adineExtraExpressions:
    for letter in ["a", "b", "c"]:
        if letter == "a":
            renpy.exports.image("adine %s"%expression, "cr/adine_%s.png"%expression)
        else:
            renpy.exports.image("adine %s %s"%(expression, letter), "cr/adine_%s_%s.png"%(expression, letter))
    
    for letter in ["a", "b", "c"]:
        if letter == "a":
            renpy.exports.image("adine %s flip"%expression, im.Flip("cr/adine_%s.png"%expression, horizontal=True))
        else:
            renpy.exports.image("adine %s %s flip"%(expression, letter), im.Flip("cr/adine_%s_%s.png"%(expression, letter), horizontal=True))

@loadable_mod
class AWSWMod(Mod): 
    def mod_info(self):
        return ("Eval Core Mod", "1.0.0", "Eval")
    
    def mod_load(self):
        pass
    
    def mod_complete(self):
        if "Side Images" in modinfo.get_mods():
            load_side_ims()