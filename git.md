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
- Force push to remote repository without merge
```
git push -f origin <branch_name>
```
- Change the remote repository URL
```
git remote -v
git remote set-url origin https://github.com/rockkingjy/OpenKAI.git
git remote -v
```
- Check the size and count of object in the repository
```
git count-objects -vH
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
- Remove existed submodule
```
rm .gitmodules
rm -rf .git/modules/caffe
git rm --cached caffe
```
Tell Git to download the contents of rock/:
```
git submodule update --init --recursive
```
Discard un-committed local changes:
```
git checkout .
```
- Merging an upstream repository into your fork:
```
 git pull https://github.com/yankailab/OpenKAI.git master
```
