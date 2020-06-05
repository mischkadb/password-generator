"""Entry point for WSGI.

Used by gunicorn in production.
"""

from web.app import app

if __name__ == '__main__':
    app.run()
