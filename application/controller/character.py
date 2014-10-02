# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-controller -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. controller:: Character
    :platform: Linux
    :synopsis: None

.. controllerauthor:: sorcha <sorcha@localhost>
"""

from mamba.web.response import Ok
from mamba.application import route
from mamba.application import controller
from application.model.character import Character


class Character(controller.Controller):
    """
    None
    """

    name = 'Character'
    __route__ = 'character'

    def __init__(self):
        """
        Put your initialization code here
        """
        super(Character, self).__init__()

    @route('/')
    def root(self, request, **kwargs):
        return Ok('I am the Character, hello world!')

    @route('/create', method='POST')
    def create(self, request, **kwargs):
        str_kwargs = str(kwargs)
        return Ok(
            'Create a character with {} you say'.format(
                str_kwargs
            )
        )
