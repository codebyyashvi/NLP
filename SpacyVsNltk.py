# import spacy 

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chaat of delhi")
# for sentence in doc.sents:
#     print(sentence)
# for sentence in doc.sents:
#     for word in sentence:
#         print(word)

import nltk 
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
print(sent_tokenize("Dr. Strange loves pav bhaji of mumbai. Hulk loves chaat of delhi"))

from nltk.tokenize import word_tokenize
print(word_tokenize("Dr. Strange loves pav bhaji of mumbai. Hulk loves chaat of delhi"))