# WordSearch Generator

A simple word search puzzle generator in Python.  
Supports horizontal, vertical, and diagonal word placements.  
Returns a clean 2D array that you can further customize and display however you like.

---

## 🚀 Features

- Automatically fits all words into a square grid
- Supports custom languages (via `alphabets.py`)
- Places words in:
  - Horizontal ↔️
  - Vertical ↕️
  - Diagonal ↘️ directions
- Returns a ready-to-use 2D array (no output to file or console by default)

---

## 📆 Installation

Using pip:

```bash
pip install wordsearch-gen
```

Or using GitHub:

```bash
git clone https://github.com/saweekmusic/wordsearch.git
```

And import it locally:

```python
from wordsearch import WordSearch
```

---

## 🧪 Example

```python
from wordsearch import WordSearch
from alphabets import Alphabets

words = ["painter", "back", "board", "cactus", "reliance"]
ws = WordSearch(words, language=Alphabets.ENGLISH)

for row in ws.grid:
    print(" ".join(row))
```

Output: *(will vary due to randomness)*

```
P A I N T E R S E T
C R A N G E M A I P
...
```

---

## 🧠 Customization

Want to use different alphabets?  
Check out `alphabets.py` to define your own language set.  
You can pass it like so:

```python
ws = WordSearch(words, language=Alphabets.SPANISH)
```

---

## 📂 Project Structure

```
wordsearch/
├── src/                # Package directory
│   ├── alphabets.py
│   └── wordsearch.py
├── examples/     
│   └── usage.py        # An example of usage
├── README.md
├── .gitignore
├── LICENSE
```

---

## 🤓 Who is this for?

- Educators making worksheets
- Devs wanting to visualize word data
- Puzzle nerds (you know who you are)
- Anyone who likes mixing logic with words

---

## 📋 License

MIT — feel free to use, modify, and share.  
If you build something fun with it, let me know! 😄

