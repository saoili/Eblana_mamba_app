# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-controller -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. controller:: Player
    :platform: Linux
    :synopsis: None

.. controllerauthor:: sorcha <sorcha@localhost>
"""

from mamba.web.response import Ok, BadRequest
from mamba.application import route
from mamba.application import controller
from application.model.player import Player as PlayerModel


class Player(controller.Controller):
    """
    None
    """

    name = 'Player'
    __route__ = 'player'

    def __init__(self):
        """
        Put your initialization code here
        """
        super(Player, self).__init__()

    @route('/')
    def root(self, request, **kwargs):
        return Ok('I am the Player, hello world!')

    @route('/create', method='POST')
    def create(self, request, **kwargs):
        str_kwargs = str(kwargs)
        required = [
            "name", "mobile", "email",
            "emergency_name", "emergency_mobile", "old_id"
        ]
        unicodes = [
            "name", "mobile", "email",
            "emergency_name", "emergency_mobile"
        ]

        for requirement in required:
            if requirement not in kwargs:
                return BadRequest(
                    "Cannot create a player without {}".format(
                        requirement
                    )
                )

        for requirement in unicodes:
            kwargs[requirement] = unicode(
                kwargs[requirement]
            )
        kwargs["old_id"] = int(kwargs["old_id"])


        p = PlayerModel()
        print "p is {}".format(p)
        p.name = kwargs["name"]
        print "p.name is {}".format(p.name)

        x = p.create_from_dict(kwargs)
        print "x is {}".format(x)

        # want to replace the below with something 
        # that returns appropriate response codes
        # and messages 
        def temp_print(input):
            print input
            return input

        x.addCallback(temp_print)
        return Ok(
            'Create a PlayerModel with {} you say'.format(
                str_kwargs
            )
        )

