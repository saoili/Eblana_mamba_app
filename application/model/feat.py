# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Feat
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *
from storm.locals import Int, Reference

from mamba.application import model
from application.model.species import Species


class Feat(model.Model):
    """
    None
    """

    __storm_table__ = 'feat'
    
    id = Int(primary=True, unsigned=True)
    name = Unicode(size=50)
    description = Unicode(size=200)
    level_req = Int(unsigned=True)
    feat_req_id = Int(unsigned=True)
    species_req_id = Int(unsigned=True)
    class_req = Unicode(size=25)
    crafting = Bool(default=False)
    level_1_only = Bool(default=False)
    secret = Bool(default=False)
    species_req = Reference(species_req_id, Species.id)

