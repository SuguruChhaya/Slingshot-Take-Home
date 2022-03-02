from classes import Trie, Node
import pickle
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://suguruchhaya:Sc1148236@cluster0.4gsk2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

for entry in collection.find({"_id":"trie"}):
    trie = pickle.loads(entry["trie"])

trie.insert("abc")
print(trie.search("abc"))
trie.suggest("a")
trie.display()
trie.delete("abc")