# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-controller -*-
# Copyright (c) 2014 - sorcha <sorcha@localhost>

"""
.. controller:: Contact
    :platform: Linux
    :synopsis: Contact form for Eblana app

.. controllerauthor:: sorcha <sorcha@localhost>
"""

from mamba.core import templating
from mamba.web.response import Ok
from mamba.application import route
from mamba.application import controller


class Contact(controller.Controller):
    """
    Contact form for Eblana app
    """

    name = 'Contact'
    __route__ = 'contact'

    def __init__(self):
        """
        Put your initialization code here
        """
        super(Contact, self).__init__()
        self.template = templating.Template(controller=self)

    @route('/')
    def root(self, request, **kwargs):
        return Ok(self.template.render().encode('utf-8'))