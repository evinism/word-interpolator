from flask import Flask, request, jsonify, abort, render_template, url_for
from interpolate import interpolateWords
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/query")
def query():
  word1 = request.args.get('w1')
  word2 = request.args.get('w2')
  if (not word1) or (not word2):
    abort(400)
  wordResponses = interpolateWords(word1, word2)
  return jsonify(wordResponses)
