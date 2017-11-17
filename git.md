# Adding an existing project to GitHub using the command line

From the terminal, go to the directory of the existing project, do the following:

git init

git add .

git commit -m "First commit"

git config --global user.name "rockkingjy"

git config --global user.email "rockking.jy@gmail.com"

git remote add origin https://github.com/rockkingjy/selftrain.deeplearning.git

git remote -v

git push -u origin master


# 
git pull origin master
