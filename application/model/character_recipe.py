# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: CharacterRecipe
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
from application.model.recipe import Recipe


class CharacterRecipe(model.Model):
    """
    None
    """

    __storm_table__ = 'character_recipe'
    
    id = Int(primary=True, unsigned=True)
    character_id = Int(unsigned=True)
    recipe_id = Int(unsigned=True)
    characer = Reference(character_id, Character.id)
    recipe = Reference(recipe_id, Recipe.id)

