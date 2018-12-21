## To be able to use a module in a subfolder
Create a __init__.py empty file in the subfolder.

## After install python3.6:
To make python3 use the new installed python 3.6 instead of the default 3.5 release, run following 2 commands:
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
```
## Switch between the two python versions for python3 via command:
```
sudo update-alternatives --config python3
```
## Error of python3.6 to find a ros version:
Check PYTHONPATH and set:
```
export PYTHONPATH="/usr/local/lib/python3.6/dist-packages"
```
## Error of tensorflow GPU run on CUDA8.0:
To install the version that compatable to CUDA8.0:
```
sudo pip3 install tensorflow-gpu==1.4.1 --ignore-installed
```
