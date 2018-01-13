python src/server/modelWrapper.py
parcel src/client/index.html --out-dir src/server/static/build/ &
FLASK_APP=src/server/server.py flask run
