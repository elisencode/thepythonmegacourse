# What are these?

This repository contains all the source code of The Python Mega Course, a comprehensive Python course authored by Ardit Sulce. 

If you're not a member of the course, you can become one for just a one-time payment of $15 using the discount link below: [https://www.udemy.com/the-python-mega-course/?couponCode=GITREADSECTION](https://www.udemy.com/the-python-mega-course/?couponCode=GITREADSECTION)

If you're not a member you can still use these Jupyter notebooks, but you won't be able to see the video lectures and you won't be able to ask questions to the instructor inside the course.

### How to use these notebooks?

There's one notebook for each section of the coures. Simply click the notebook you want, locate the lecture, and copy the code. Or if you know how to use Jupyter notebooks, then use the green download button further above to download all the notebooks and open them in your browser.

Clicking a lecture opens the corresponding video lecture on Udemy:
![Lectures are clickable](data/lecture_link_demo.gif)

### What are the prerequisites to use these?

To be able to run the Python code shown in these notebooks you should have Python 3 installed in your computer. If the code uses a third party library that is mentioned in the notebooks.

### Author
Ardit Sulce



---

My python codes here

---



[[error: ‘’ does not have a commit checked out fatal:](https://stackoverflow.com/questions/56873278/how-to-fix-error-filename-does-not-have-a-commit-checked-out-fatal-adding) Github commit error.](https://medium.com/@cryptobeastchain/error-filename-does-not-have-a-commit-checked-out-fatal-github-commit-error-07f28ca215b7)

1. Nested Git Repositories

   `cd subfolder view hidden files rm -rf .git`

2. '.git'

   `rm -rf ./.git`

3. Check for existing Git Repositories:

   `find . -name ".git" -type d -exec rm -rf {} \; git add .`

4. '.gitignore' file in '.idea' directory

   `cd .idea rm .gitignore`

5. Be careful: Multiple '.git' Directories inside Project Repo

---

[How to Remove .idea Directory from .git](https://otakoyi.software/blog/how-to-remove-idea-directory-from-git)

```
If you have accidentally added the .idea directory to .git repository, and you don’t want it to be there, then there is an easy way to remove it. You just have to use the command line and do the following:

# Create file .gitignore
touch .gitignore

# Add .idea to .gitignore
echo '.idea' >> .gitignore

# Remove directory from staging
git rm -r --cached .idea

# Add file to git
git add .gitignore

# Commit changes
git commit -m "Removed .idea from git"

# Push changes
git push
```

