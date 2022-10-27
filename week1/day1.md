### Day 1: 26 OCTOBER 2022  	
<h1 align="center">GIT COMMANDS</h1>

**User git Configuration:**  
“git config” command is used to configure the user  
To configure user name: 
` $ git config --global user.name <user_name> `
To configure user email: 
$ git config –-global user.email “user email”$ 
![]('/../images/user_configuration.png)

git initialization:
git initialization means converting a current working directory into git repository.
“git init” commad is used to initailize git repository.
$git init

git status:
“git status” command is used to display the state of current working directory and staging area(index file).
It simply shows the difference between working tree and index file.
$ git status

git add:
to update the changes in the current working tree to the staging area or index file we have to use “git add” command.It also prepare the staged contents to next commit.
To add single file to the stanging area:
$ git add file1

To add more than one file:
$ git add file1 file2

To add all the files of specific type:
$ git add *.py

To add all the files in the current working directory:
$ git add .

