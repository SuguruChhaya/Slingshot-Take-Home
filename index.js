let trie = {};

var inquirer = require('inquirer');
var cli = require('./lib/cli')


function add(word){
    let curr = trie;
    for (let i=0;i<word.length;i++){
        if (word[i] in curr){
            curr = curr[word[i]];
        }
        else{
            curr[word[i]] = {};
            curr = curr[word[i]];
        }
    }
}

function remove(word){
    
}

while (true){
    inquirer.prompt([
        {type:"input",
        name: "command",
        message:"command: "
    }
    ])

    .then((answers)=>{
        let arr = answers.command.split(" ");
        if (arr[0]=="add"){
            add(arr[1]);
        }
        else if (arr[0]=="delete"){
            remove(arr[1]);
        }
    })
}
