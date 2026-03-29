from src.preprocess import load_dataset
from src.trie import Trie
from src.autocomplete import rank_suggestions


df = load_dataset()

trie = Trie()

for word in df["word"].dropna():
    trie.insert(str(word))


prefix = input("Enter prefix: ")

node = trie.search_prefix(prefix)

results = []

if node:
    trie.collect_words(node, prefix, results)


suggestions = rank_suggestions(results, df)

print("\nSuggestions:")

for s in suggestions:
    print(s)