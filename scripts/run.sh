parcel build src/client/index.js --no-minify --out-dir src/server/static/
FLASK_APP=src/server/server.py flask run
