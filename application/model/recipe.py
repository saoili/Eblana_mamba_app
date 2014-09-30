# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Recipe
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *

from mamba.application import model


class Recipe(model.Model):
    """
    None
    """

    __storm_table__ = 'recipe'

    id = Int(primary=True, unsigned=True)
    item_type = Unicode(size=20)
    effect1 = Unicode(size=200)
    effect2 = Unicode(size=200)
    attune_time = Int(unsigned=True)
    any_crystal = Int(unsigned=True)
    void_crystal = Int(unsigned=True)
    blended_crystal = Int(unsigned=True)
    air_crystal = Int(unsigned=True)
    fire_crystal = Int(unsigned=True)
    earth_crystal = Int(unsigned=True)
    water_crystal = Int(unsigned=True)
    class_req = Unicode(size=25)
    secret = Bool(default=False)
    craft = Bool(default=False)
    level = Unicode(size=50) # ie Apprentice, Journyman etc.
