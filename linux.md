# Find a process and kill it
```sh
ps aux | grep <NAME>
sudo kill <numberOfProcess>
```

# How to set the programme start at boot up

```sh
sudo cp ./ZED  /etc/init.d/ZED
sudo chmod +x /etc/init.d/ZED
sudo update-rc.d ZED defaults
```
ZED is the name of the script, refering [My ZED project](https://github.com/rockkingjy/ZedDataCollection)
