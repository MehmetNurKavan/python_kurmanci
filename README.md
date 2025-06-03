# Kurdish - python |  Python a Kurmancî

A lightweight and simple Python library for working with the Kurdish language (Latin script).  
It is designed to provide tools for building language-based applications, learning tools, or processing Kurdish text.  

## Project Structure

├── ``kurdish_python.py`` The main Kurdish language library (core of the project)\
├── ``test.py`` Test and demonstration of library functionality\
├── ``peyv_lîstik.py`` Sample vocabulary game using the library\
└── ``klpt.ipynb`` Kurdish Language Processing Toolkit

## Features

- Kurdish word support (Latin script)
- Utilities for processing and using Kurdish data
- Easy to integrate into any Python project
- Includes sample applications and test files

## Target Audience

- Python developers who prefer coding in Kurdish
- Students who are new to programming
- Educational institutions and teachers
- Developers aiming to improve code readability and consistency in native language contexts

---

## Example Usage

### 1. ``test.py`` Quick Tests

This file includes sample usage and basic tests to verify that the library functions as expected.

```bash
python test.py
```

### example

```python
nivîs("Hûn çawa ne, hevalno?")

nivîs(f"2.4 jorîn: {jorîn(2.4)}")

liste_min = lîste([5, 2, 8, 1, 9])
nivîs("Dirêjî: ", dirêjî(liste_min))

nivîs("Jimartin: ", jimartin([5, 2, 8]))

kopî = lîste_alîkar.kopîKirin(liste_min)
nivîs("Kopiya listê:", kopî)
nivîs("Paşxistin:", lîste_alîkar.paşxistin(kopî))
```

---

### 2. ``peyv_lîstik.py`` Sample Vocabulary Game

This is a simple word quiz game that demonstrates how the library can be used in a real application.  
Users are asked to guess the Turkish meanings of Kurdish words.

```bash
python peyv_lîstik.py
```

```bash
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
LÎSTIKA PEYVAN KURDÎ
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
1️⃣  Lîstikê Nû Dest Pê bike
2️⃣  Lîsteya Peyvan Nîşan bide
3️⃣  Derkeve

Hilbijardina xwe bike (1-3): 1
==================================================
🎮 LÎSTIKA PEYVAN - کەڵێنەی وشەکان 🎮
==================================================
Wateya peyvên kurdî bi tirkî bibêje!
Ji bo derketin 'der' binivîse.

📝 Pirs 1
Peyva 'çem' bi tirkî çi ye?
Bersiva te: nehir
✅ Rast e! +10 xal
💰 Xal: 10
📊 Rast: 1/1
------------------------------
Ji bo berdewamiyê Enter bike ('der' ji bo derketin):
📝 Pirs 2
Peyva 'zer' bi tirkî çi ye?
Bersiva te: sarı
✅ Rast e! +10 xal
💰 Xal: 20
📊 Rast: 2/2
------------------------------
Ji bo berdewamiyê Enter bike ('der' ji bo derketin):
📝 Pirs 3
Peyva 'mêze' bi tirkî çi ye?
Bersiva te: yemek
❌ Şaş e! Bersiva rast: masa
💰 Xal: 20
📊 Rast: 2/3
```

## Note on Kurdish NLP

Although this project is not primarily focused on NLP, it includes a sample word-guessing game in Kurdish ``peyv_listik.py`` to demonstrate how Kurdish content can be used in Python applications.

Additionally, Kurdish natural language processing (NLP) is an emerging and promising field. For more advanced Kurdish NLP tools and resources, check out the excellent [Kurdish Language Processing Toolkit (KLPT) ](https://github.com/sinaahmadi/klpt) developed by Sina Ahmadi. KLPT provides useful tools for morphological analysis, tokenization, POS tagging, and more.

```python
pip install klpt
```

## Language Scope

The library supports Kurdish written in Latin script.

### Contributing

Contributions are welcome — especially:
Kurdish language resources
Additional helper functions
Bug fixes or improvements

### Contact

For suggestions or collaboration, feel free to reach out.
