# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: CharacterBackground
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


class CharacterBackground(model.Model):
    """
    None
    """

    __storm_table__ = 'character_background'
    
    id = Int(primary=True, unsigned=True)
    character_id = Int(unsigned=True)
    description = Unicode(size=500)
    approved = Bool()
    character = Reference(character_id, Character.id)

