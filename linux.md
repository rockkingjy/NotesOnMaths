## matlab starup folder setting
In `./R2017a/toolbox/local/startup.m`:
```
cd /media/elab/sdd/mycodes/tracker/ECO
run('/media/elab/sdd/matlabInstall/vlfeat-0.9.21/toolbox/vl_setup.m')
```
Then start Matlab in the terminal:
```
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu \
/media/elab/sdd/R2017a/bin/matlab
```

## Record Screen
```
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
sudo apt-get update
sudo apt-get install simplescreenrecorder
```
## Check whether install the package and the version exists
```
apt-cache policy <nameOfPackage>
```
and installed with:
```
apt-get install <nameOfPackage>=<Version>
```
## non-gui mode
```
ctrl+alt+F2
```
## Delete files bypassing trash
```
rm -Rfv
```
-R: Recursively; -f: forcibly; -v:bypassing trash;

## Bash rename files in a folder(remove Depth_ for files in folder depth/)
```
rename 's/Depth_//' depth/Depth_*.png
```

## Find a process and kill it
```sh
ps aux | grep <NAME>
sudo kill <numberOfProcess>
```

## How to set the programme start at boot up

```sh
sudo cp ./ZED  /etc/init.d/ZED
sudo chmod +x /etc/init.d/ZED
sudo update-rc.d ZED defaults
```
ZED is the name of the script, if you need to save the data in SD card etc., you need to mount it before running the programme. Refering [My ZED project](https://github.com/rockkingjy/ZedDataCollection)

## Mount and unmount NTFS
To check the disk mounted:
```sh
df
```
unmount:
```sh
umount /dev/mmcblk1p1
```
mount:
```sh
sudo mount -t ntfs /dev/mmcblk1p1 /media/nvidia/
```

## Check sd card
```
lsblk
sudo fdisk -l
```

## Check ubuntu ker log:
```sh
tail -n 100 /var/log/kern.log
dmesg
```
