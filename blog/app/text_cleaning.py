import string
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

punctuation = [i for i in string.punctuation if (i != '!') and (i != '?')]
stopword = pd.read_csv('blog/app/stopword_selected.csv', names=[0])[0].tolist()

def is_in_punct(text):
  """Mengecek apakah text memiliki tanda baca"""
  word = []
  for i in text:
    if i not in punctuation:
      word.append(i)

  return ''.join(word)

def replace_exclamation_question(text):
  """Menggantikan '!' dan '?' dengan placeholder sebagai tambahan fitur"""
  return text.replace('!', ' tanda seru').replace('?', ' tanda tanya')

def remove_not_punct(text):
  """Menghapus punctuation"""
  sentence = []
  for word in text.split():
    s = ''.join(filter(is_in_punct, word))
    sentence.append(s)
  
  return ' '.join(sentence)

def remove_stopword(text):
  sentence = []
  for word in text.split():
    if word not in stopword:
      sentence.append(word)
  
  return ' '.join(sentence)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stemming(text):
  word = []
  for i in text.split():
    if i.isupper():
        i = stemmer.stem(i).upper()
        word.append(i)
    else:
        i = stemmer.stem(i)
        word.append(i)

  return ' '.join(word)

def replace_num(text):
  """"Mengganti digit dengan placeholder"""
  word = []
  for i in text.split():
    if i.isdigit():
      continue
    else:
      word.append(i)
    
  return ' '.join(word)
