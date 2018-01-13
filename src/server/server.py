from flask import Flask, request, jsonify, abort, render_template, url_for
from . import words
app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
  return app.send_static_file('build/index.html')

@app.route("/exists")
def exists():
  word = request.args.get('word')
  if not word:
    abort(400)
  wordExists = words.wordInModel(word)
  return jsonify({"exists": wordExists})

@app.route("/query")
def query():
  word1 = request.args.get('w1')
  word2 = request.args.get('w2')
  if (not word1) or (not word2):
    abort(400)
  if (not words.wordInModel(word1)) or (not words.wordInModel(word2)):
    abort(404)
  wordResponses = words.interpolateWords(word1, word2)
  return jsonify(wordResponses)
