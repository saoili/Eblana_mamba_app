# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Character
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *
from storm.locals import Int, Reference

from mamba.application import model
from application.model.player import Player
from application.model.species import Species

class Character(model.Model):
    """
    None
    """

    __storm_table__ = 'character'
    
    id = Int(primary=True, unsigned=True)
    player_id = Int(unsigned=True)
    name = Unicode(size=200)
    char_level = Int(unsigned=True)
    wizard = Int(unsigned=True)
    bard = Int(unsigned=True)
    cleric = Int(unsigned=True)
    fighter = Int(unsigned=True)
    rogue = Int(unsigned=True)
    body = Int(unsigned=True)
    mana = Int(unsigned=True)
    armour = Int(unsigned=True)
    XP = Int(unsigned=True)
    blended = Int(unsigned=True)
    earth = Int(unsigned=True)
    air = Int(unsigned=True)
    fire = Int(unsigned=True)
    water = Int(unsigned=True)
    species_id = Int(unsigned=True)
    comments = Unicode(size=500)
    player = Reference(player_id, Player.id)
    species = Reference(species_id, Species.id)

