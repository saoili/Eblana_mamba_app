# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. model:: Player
    :plarform: Linux
    :synopsis: None

.. modelauthor:: sorcha <sorcha@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import *

from mamba.application import model


class Player(model.Model):
    """
    None
    """

    __storm_table__ = 'player'

    id = Int(primary=True, unsigned=True, auto_increment=True)
    name = Unicode(size=250)
    mobile = Unicode(size=20, unique=True)
    email = Unicode(size=50, allow_none=False, unique=True)
    emergency_name = Unicode(size=250)
    emergency_mobile = Unicode(size=20)
    old_id = Int(size=20)

