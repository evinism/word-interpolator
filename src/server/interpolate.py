import random

# interface: [('word', position(0 - 1)), ... ]
def interpolateWords(word1, word2):
  return [
    (word1 + 'cat', random.random()),
    (word2 + 'dog', random.random()),
    (word1 + 'bloop', random.random())
  ]
