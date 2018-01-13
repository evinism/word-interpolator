from . import modelWrapper

model = modelWrapper.ensure_model()

def wordInModel(word):
  global model
  return word in model.wv

# interface: [('word', position(0 - 1)), ... ]
def interpolateWords(word1, word2):
  global model
  return model.wv.most_similar_cosmul(positive=[word1, word2])
