# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: CharacterSpell
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *
from storm.locals import Int, Reference

from mamba.application import model
from application.model.character import Character
from application.model.spell import Spell


class CharacterSpell(model.Model):
    """
    None
    """

    __storm_table__ = 'character_spell'
    
    id = Int(primary=True, unsigned=True)
    character_id = Int(unsigned=True)
    spell_id = Int(unsigned=True)
    character = Reference(character_id, Character.id)
    spell = Reference(spell_id, Spell.id)

