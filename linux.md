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

## Check ubuntu ker log:
```sh
tail -n 100 /var/log/kern.log
```
