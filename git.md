- Adding an existing project to GitHub using the command line

From the terminal, go to the directory of the existing project, do the following:
```sh
git init
git add .
git config --global user.name "rockkingjy"
git config --global user.email "rockking.jy@gmail.com"
git commit -m "First commit"
git remote add origin https://github.com/rockkingjy/selftrain.deeplearning.git
git remote -v
git push -u origin master
```
- Update Github after changes
```
git status
git add .
git commit -m "update"
git push -u origin master
```
- Pull from the GitHub
```
git pull origin master
```
- Clone the remote repository
```
git clone https://github.com/rockkingjy/OpenKAI_docs
```
- Change the remote repository URL
```
git remote -v
git remote set-url origin https://github.com/rockkingjy/OpenKAI.git
git remote -v
```
- Remove git repository
```
rm -rf .git
```
- Create a branch
```
git checkout -b mybranch
```
- Change to another branch
```
git checkout existingbranch
```
- Add submodule 'rock' as a submodule of the repository
```
 git submodule add git@github.com:rockking/caffe.git caffe
```
Tell Git to download the contents of rock/:
```
git submodule update --init --recursive
```
Discard un-committed local changes:
```
git checkout .
```
