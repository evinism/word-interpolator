import subprocess
from os.path import isfile
import nltk
from gensim.models import Word2Vec

from nltk.corpus import brown as corpus
corpus_name = "brown"

model_path = "data/" + corpus_name + ".model"


# woop woop
def ensure_model():
  global model_path
  global corpus

  if isfile(model_path):
    print("Loading model from path " + model_path)
    model = Word2Vec.load(model_path)
  else:
    print("no model found -- rebuilding...")
    nltk.download(corpus_name)

    print("generating model")
    model = Word2Vec(corpus.strings())

    print("saving model at " + model_path)
    subprocess.call("mkdir data")
    model.save(model_path)

  return model

ensure_model()
