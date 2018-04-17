1. Create a bootable USB stick on macOS

Download ubuntu-16.04.1-desktop-amd64.iso 

Create the bootable USB according to the [[link](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos#6)].

Attention: ubuntu-16.04.3-desktop-amd64.iso always cause error!

2. Install Ubuntu16.04.1

Reinstall by reboot and F12, choose UEFI OPTIONS usb boot;

After login to Ubuntu, double click the icon on the desktop to reinstall ubuntu; Restart from the hard disk;

Attention: If choose from the LEGACY OPTIONS, it will cause the problem of unable to login to ubuntu and go to grub!

3.Install Nvidia GPU driver and CUDA 8.0

Follow the instructions: http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-installation

Connect to internet -> Download CUDA Toolkit 8.0 GA1 the cuda_8.0.61_375.26_linux.run -> Ctrl+Alt+F1 -> login -> 
```
sudo gedit /etc/modprobe.d/blacklist-nouveau.conf
```
Add: 
```
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off\nalias lbm-nouveau off
```
Then:
```
sudo update-initramfs -u
cd Downloads
sudo service lightdm stop 
chmod 777 cuda_8.0.61_375.26_linux.run
sudo ./cuda_8.0.61_375.26_linux.run --override --no-opengl-lib     
```
(OpenGL-lib will cause login loop!!!)
```
reboot
nvidia-smi
```

To change the cuda PATH permanently:http://docs.openkai.xyz/x86build.html or:
```
sudo gedit ~/.bashrc
```
Add:
```
export PATH=/usr/local/cuda-8.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH
```
```
source ~/.bashrc
nvcc —version
```
Don’t need to try to run examples of CUDA.

If cannot find -lglut -lGL:
```
sudo apt-get install freeglut3-dev
sudo apt-get install libgl-dev
```

Attention: Should be CUDA8.0, CUDA9.0 will cause some error later.

4. Install cuDNN7.0 on ubuntu: 

Follow the “CUDNN Installation Guide”, install with the deb file(more easier). 

Test with the examples; cuDNN version check:
```
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```


## Install brightness controller
```
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt-get update
sudo apt-get install brightness-controller
```

## Install terminator

sudo apt-get install terminator

## Set the bash color

sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

chsh -s /usr/bin/zsh

## Set the vim color
cd /Users/jinyan

//create a setting file of vim if it doesn't exit;

vim .vimrc 

//copy the file Tips/.vimrc to .vimrc


## Set the ssh to login to the remote server

### Server end:
$sudo apt-get install openssh-server

$sudo service ssh status

check the mode of the fold: ls -l .ssh 

if it is not like this:

-rw------- 1 zbj zbj 1675 Feb 14 14:29 id_rsa

-rw-r--r-- 1 zbj zbj  389 Feb 14 14:29 id_rsa.pub

then you should change the mode of the fold /.ssh:

chmod 700 ~/.ssh

Open this file: vim /etc/ssh/sshd_config

to check these lines are not be annotated:

RSAAuthentication yes

PubkeyAuthentication yes

AuthorizedKeysFile .ssh/authorized_keys

Then run:
sudo /etc/init.d/ssh restart


### Customer end:

ssh-keygen

it will generate the private and public keys:

/root/.ssh/id_rsa

/root/.ssh/id_rsa.pub -- public keys

copy it to the server end:

ssh-copy-id username@host(ipaddress)


### login remote server:

ssh username@host(ipaddress)

### packet_write_wait: Connection to **** port 22: Broken pipe

change：/etc/ssh/ssh_config for the customer ends:

ServerAliveInterval 120

TCPKeepAlive no

Then run:
sudo /etc/init.d/ssh restart

or restart the ssh in Mac

## Set Teamviewer boot up start
* Set fix password:
Set teamviewer -> Extras -> Options -> Security -> Personal password;
* Account assignment:
Set teamviewer -> Extras -> Options -> General;
* Add teamviewer as start up programme
Applications -> Startup Applications -> /usr/bin/teamviewer;
* Set ubuntu automatic login;
System Settings -> User Accounts -> Automatic Login;

## Use ssh + frp + 3rd part Server for ssh tunneling 
* Rent a 3rd part server;
* Install [frp](https://github.com/fatedier/frp) on both 3rd part server and local server;
* ssh to access from your computer.



