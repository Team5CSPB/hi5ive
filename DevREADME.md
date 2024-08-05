## Helpful Notes to Share

### Start up the Flask Server in the venv
* `cd hi5ive`
* NEED to be in the same folder as pyproject.toml
* `source venv/bin/activate`
* `pip install -r requirements.txt` install dependencies 
* `export FLASK_APP=app.py` (Tells Flask how to import the application)
* `flask run`

if export doesn't work:
* `flask --app app run`

### Start up React app
* `cd hi5ive`
* `npm install`
* `npm run start`