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
from _mysql_exceptions import IntegrityError


class Player(model.Model):
    """
    None
    """

    __storm_table__ = 'player'
    __unique__ = ["mobile", "email", "old_id"]

    id = Int(primary=True, unsigned=True, auto_increment=True)
    name = Unicode(size=250)
    mobile = Unicode(size=20, unique=True)
    email = Unicode(size=50, allow_none=False, unique=True)
    emergency_name = Unicode(size=250)
    emergency_mobile = Unicode(size=20)
    old_id = Int(size=20, unique=True)

    def init(self):
        self.__unique__ = ["mobile", "email", "old_id"]

    @transact
    def create_from_dict(self, data):
        player = Player()
        fields = [
            "name", "mobile", "email",
            "emergency_name", "emergency_mobile", "old_id"
        ]

        for field in self.__unique__:
            results = Player.find(
                getattr(Player, field) == data[field],
                async=False
            )
            if results.count() != 0:
                return (
                    "cannot create player with {}".format(
                        field
                    ) +
                    ": {}".format(
                        data[field]
                    ) +
                    " because we already have one"
                )

        for field in fields:
            setattr(player, field, data[field])
        player.store().add(player)
        player.store().flush()

        
        #not doing it this way because 
        #that uses up the next auto assign
        #try:
        #    player.store().flush()
        #except IntegrityError as err:
        #    print "err is type {}".format(type(err))
        
        return "Created player number {}".format(
            player.dict()["id"]
        )
        
