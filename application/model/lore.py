# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Lore
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *

from mamba.application import model


class Lore(model.Model):
    """
    None
    """

    __storm_table__ = 'lore'
    
    id = Int(primary=True, unsigned=True)
    name = Unicode(size=200)

