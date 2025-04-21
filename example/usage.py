from src.wordsearch import WordSearch
from src.alphabets import Alphabets

words = ['range', 'board', 'set']
ws = WordSearch(words, language=Alphabets.ENGLISH)

# Print nicely in terminal (or handle however you want)
for row in ws.grid:
    print(' '.join(row))
