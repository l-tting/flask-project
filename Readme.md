*INTRODUCTION TO GITHUB*
*Git* -> A version control system that keeps track of changes you make to your project over time
*Github* -> a cloud hosting / storage platform that hosts / stores git repositories

*repository* -> folder in Github

Github allows you to do the following:
1.store your projects securely online
2.back up your code
3.Collaborate with other developers
4.share your work with employers / clients
5.contribute to open source projects 


git config --global user.name " Your Name"
git config --global user.email " your email address"

*Pushing new code to Github*
1.Initializing git to track my files
**git init**

2.Connect local folder to my github repository
**git remote add origin https://github.com/l-tting/flask-project.git"**

3.Add files from local folder to my github repo
**git add .**

4.Commit before final push
 -> commit: a saved snapshot of your project
**git commit -m "My first commit"**


5.**git push origin main** or 
  **git push origin master**

  **master / main** -> branches -> 


*U* -> untracked
*A* -> added
*M* -> modified
 


*Updating existing code / repos in Github*
1.**git add .**
2.**git commit -m"added a p-tag in index"**
3.**git push origin master**