# Git Commands

git add . => it is ussed to stag the file

git commit => it is used to commit the code to perticular git repo

git log => it states all the detail with the date and time also author,and what the commit messege

git log --oneline => it states only git messege

git log --oneline --graph --all => it showa the graphical representation of the git merge and commit

git show => it shows the how many changes at perticular commit and Hash

git diff => it shows the what differences are not staged yet to the git

git diff --staged => it states whats i have to commit

git checkout -b *** => it creates new branch and switch to it

git branch => it shows on which branch you are

git switch => it use to switch the branches internally in git

git switch -c => it creates a newbranch and also switch to it

git switch main => it switches to the main branch of the git hub

git merge experiment => it merge the second branch to main

git merge --abort => it cancel the merge process and restore the repository to previous state

git branch -d experiment => it uses to delete the branch

git push => it pushes the code to github

git remote -v => it states where the code is from fetch and push it is very useful


# Terminal Commands

cd => it is used to change the directory

cd .. => it goes back to previous directory

pwd => it shows the current working directory

ls (PowerShell) => it lists all files and folders

dir (Command Prompt) => it lists all files and folders


## Search

Get-ChildItem -Recurse -Filter *.py => it finds all python files

Get-ChildItem -Recurse -Filter *.py | Select-String "def " => it finds all function definitions

Get-ChildItem -Recurse -File | Select-String "print" | Measure-Object  => it counts how many lines contain print

(Get-ChildItem -Recurse -Filter *.py).Count => it counts total python files


## Files

dir > contents.txt => it stores the output into contents.txt

Get-Content contents.txt => it opens and shows the contents of the file

>       
=> it redirects output to a file

>>
=> it appends output to the existing file


# Merge Conflict Steps

1. git switch main

2. git merge feature

3. git status

4. Open the conflicted file

5. Remove

<<<<<<< HEAD
=======
>>>>>>> feature

6. Keep the correct code

7. git add .

8. git commit

9. git status

10. git log --oneline --graph --all

If you don't want to continue the merge:

git merge --abort