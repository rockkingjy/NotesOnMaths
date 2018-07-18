
## Install brightness controller
```
sudo add-apt-repository ppa:apandada1/brightness-controller
sudo apt-get update
sudo apt-get install brightness-controller
```
## Visual Studio Code #ifdef grey out problem and other settings:
File -> Preference -> Settings, add:
```
    "C_Cpp.dimInactiveRegions": false,
    "window.zoomLevel": 0,
    "editor.fontSize": 12,
    "editor.wordWrap": "wordWrapColumn",
    "editor.wordWrapColumn": 80,
    "window.newWindowDimensions": "inherit",
```

## Install terminator
```
sudo apt-get install terminator
```
## Set the bash color
```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

chsh -s /usr/bin/zsh
```
## Set the vim color
```
cd /Users/jinyan
```
//create a setting file of vim if it doesn't exit;
```
vim .vimrc 
```
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



