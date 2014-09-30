# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Lammie
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


class Lammie(model.Model):
    """
    None
    """

    __storm_table__ = 'lammie'
    
    id = Int(primary=True, unsigned=True)
    name = Unicode(size=200)
    description = Unicode(size=1000)
    attune_time = Int()
    expiry_event = Int()
    lammie_type = Unicode(size=50)
    used = Unicode(size=3)# yes / no / na
    barcode = Unicode(size=20)
    slot = Unicode(size=15)
    class_to_use = Unicode(size=15)
    character_id = Int(unsigned=True)
    character = Reference(character_id, Character.id)

