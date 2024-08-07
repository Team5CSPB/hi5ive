import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

from api import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

