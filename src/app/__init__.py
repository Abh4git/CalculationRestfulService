

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app


def create_app():
    app = Flask(__name__)
    #app.config.from_object(config_class)

    return app

