import random
import markovify
from sylco import sylco

with open('/Users/divyasingh/Desktop/pywords-master/words/reversed_lyrics.txt') as f:
    text = f.read()

reversed_lyrics = markovify.NewlineText(text)

for i in range(10976):
    print(reversed_lyrics.make_short_sentence(70))
# Specify then remove punctuation
# punctuations = set([',','.','"','?','!'])

# def clean(sentence):
#     if sentence[-1] in punctuations:
#         return sentence[:-1]
#     return sentence

# def make_verse(verse_model):
#     verse = ''
#     stem = None

#     # Markovify for each line
#     for i in range():
#         while True:

#             line = verse_model.make_sentence()

#             if line is not None:

#                 syl_count = sylco(line)
#                 if syl_count > 16 or syl_count < 6:
#                     continue

#                 if i == 0:
#                     stem = clean(line.rsplit(None, 1)[-1])

#                 verse += (line + '\n')
#                 break

#     return verse

# def make_song(verse_model):

#     song = make_verse(verse_model)

#     return song

# print (make_song(reversed_lyrics))