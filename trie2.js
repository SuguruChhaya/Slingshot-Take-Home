

class Node{
    constructor(){
        this.parent = null;
        this.children = {};
        this.isEnd = false;
    }
}

class Trie{
    constructor(){
        this.root = new Node();
        this.allWords = [];
    }
    insert(word){
        let curr = this.root;
        for (let i=0;i<word.length;i++){
            let toInsert = word[i];
            if (!(toInsert in curr.children)){
                curr.children[toInsert] = new Node();
                curr.children[toInsert].parent = curr;
            }
            curr = curr.children[toInsert];
        }
        curr.isEnd = true;
    }

    endNode(word){
        let curr = this.root;
        for (let i=0;i<word.length;i++){
            let toFind = word[i];
            if (!(toFind in curr.children)){
                return null;
            }
            curr = curr.children[toFind];
        }
        if (curr.isEnd){
            return curr;
        }
        else{
            return null;
        }
    }
    contains(word){
        return this.endNode(word)!=null;
    }

    delete(word){
        let end = this.endNode(word);
        if (end!=null){
            let curr = end;
            //*Cannot just delete the first character. 
            for (let i=word.length-1;i>=0;i--){
                if (Object.keys(curr.children).length!=0){
                    break;
                }
                else{
                    delete curr.parent.children[word[i]];
                    curr = curr.parent;
                }
            }
        }
        else{
            console.log("Item doesn't exist")
        }
    }
    startsWithPrefix(word){
        let curr = this.root;
        for (let i=0;i<word.length;i++){
            let toFind = word[i];
            if (!(toFind in curr.children)){
                return false;
            }
            curr = curr.children[toFind];
        }
        return true;
    }
    dfs(curr, wordSoFar){
        if (curr.isEnd){
            this.arr.push(wordSoFar);
        }
        else{
            for (let key in curr.children){
                this.dfs(curr.children[key], wordSoFar+key);
            }
        }
    }
    display(){
        //*DFS and show elements with closest match. 
        this.arr = [];
        this.dfs(this.root, "");
        for (let i=0;i<this.arr.length;i++){
            console.log(this.arr[i]);
        }
    }

    suggest(word){
        if (this.startsWithPrefix(word)){
            let curr = this.root;
            for (let i=0;i<word.length;i++){
                curr = curr.children[word[i]];
            } 
            this.arr = [];
            this.dfs(curr, word);
            for (let i=0;i<this.arr.length;i++){
                console.log(this.arr[i]);
            }
        }
    }
}

/*
let a = new Trie();
a.insert("abc");
a.insert("ad");

a.suggest("a");
a.suggest("ab");
a.suggest("abc");
console.log("display");
a.display()
a.delete("a");
a.delete("abc")
a.display()
*/
