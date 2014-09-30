# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Spell
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *

from mamba.application import model


class Spell(model.Model):
    """
    None
    """

    __storm_table__ = 'spell'

    id = Int(primary=True, unsigned=True)
    description = Unicode(size=500)
    class_req = Unicode(size=25)
    level = Int(unsigned=True)
    spell_type = Unicode(size=50)
    instant = Bool(default=False)