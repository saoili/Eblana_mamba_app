# This file is part of eblana_app
# Copyright (c) ${year} - sorcha <sorcha@localhost>

"""
.. module:: eblana_app
    :platform: Unix, Windows
    :synopsis: First draft Eblana app

.. moduleauthor:: sorcha <sorcha@localhost>
"""

from twisted.web import server
from twisted.application import service

from mamba import Mamba
from mamba.web import Page


def MambaApplicationFactory(settings):
    # create the application multi service
    application = service.MultiService()
    application.setName(settings.name)

    # register settings and multiservice through Mamba Borg
    app = Mamba(settings)
    app.multi_services = application

    # create the root page
    root = Page(app)

    # create the site
    mamba_app_site = server.Site(root)

    return mamba_app_site, application
