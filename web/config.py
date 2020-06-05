"""Flask configuration file."""

import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """Flask configuration class."""

    SECRET_KEY = os.environ.get('SECRET_KEY')  # noqa: WPS115
