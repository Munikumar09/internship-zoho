## Day 2: 27 OCTOBER 2022
<h1 align="center">GIT COMMANDS AND CONCEPTS</h1>  

## git stash  
Git has an area called the stash where we can temporarily store a snapshot of our changes without committing them to the repository. It's separate from the working directory, the staging area, or the repository.  
To stash the changes in the working directory:  
```
$ git stash
```
To show the entries in the stashed stack:  
```
$ git stash list
```
!['git stash']('/../images/git_stash1.png)  
To apply the last saved changes in the stash to the current working directory:  
```
$ git stash apply
```
To apply the specified changes in the stash to the current working directory
```
$ git stash apply <stash_number>
```
!['git stash_number']('/../images/git_stash2.png)
To apply the last saved changes in the stash to the current working and delete from the stash stack:
```
$ git stash pop
```
To clear the stash area:  
```
$ git stash clear
```
## git tag  
Tagging in git refers to creating specific points in history for your repository. This is usually done to mark release points.  
Creating light weight tag on current branch:  
```
$ git tag <tag_name>
```
Creating annotated tag on current branch:
```
$ git tag -a <tag_name> -m "tag message"
```
To display all the tags:  
```
$ git tag
```
!['git tag']('/../images/tag1.png)  
To push a single tag from local repository to remote repository:  
```
$ git push origin <tag_name>
```
!['git stash_number']('/../images/tag2.png)  
To push all tags from local repository to remote repository:  
```
$ git push origin --tags
```
To delete tag from local repository:  
``` 
$ git tag origin <tag_name>
```
To delete tag from remote repository:  
```
$ git push origin -d <tag_name>
```
!['git stash_number']('/../images/tag3.png)  
## git cherry-pick  
cherry picking in git means to choose a commit from one branch and apply it into another branch. To use cherry pick command we have to on branch where we have to apply the commit.  
```
$ git cherry-pick <commit-hash>
```
!['git cherry-pick]('/../images/cherry_pick.png)  
<h1 align="center">Git Concepts</h1>  

## Repository
Repository is a container that stores everything related to out project. Git is a Version Control System(VCS) or program that tracks changes made to files. After initialization of git it creates ".git" repository which tracks all the changes made on files in our project to build a history over time.