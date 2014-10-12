"""
pycd10api
============
Main WSGI application
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('index', '/')
    config.include("cornice")
    config.scan("pycd10api.views")
    return config.make_wsgi_app()
