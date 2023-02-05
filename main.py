from pathlib import Path
import sys
import os

sys.path.insert(1, './Scripts')

from flask_app import app

port = os.environ.get("PORT", 5001)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)