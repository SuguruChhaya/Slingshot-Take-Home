from classes import Trie, Node
import pickle
from pymongo import MongoClient


while True:
    cluster = MongoClient("mongodb+srv://suguruchhaya:Sc1148236@cluster0.4gsk2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["test"]
    collection = db["test"]
    inp = input("'help' for options\n").strip().split(" ")
    for entry in collection.find({"_id":"trie"}):
        trie = pickle.loads(entry["trie"])
    if (len(inp)==1):
        if (inp[0]=="display"):
            trie.display()
        elif (inp[0]=="exit"):
            break
    elif (len(inp)==2):
        if (inp[0]=="insert"):
            trie.insert(inp[1])
        elif (inp[0]=="delete"):
            trie.delete(inp[1])
        elif (inp[0]=="search"):
            trie.search(inp[1])
        elif (inp[0]=="suggest"):
            trie.suggest(inp[1])

    else:
        print("invalid")
        
    collection.update_one({"_id":"trie"}, {"$set": {"trie": pickle.dumps(trie)}})



        


