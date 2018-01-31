## How to Flash TX1/2
1. Put your system into "reset recovery mode" by holding down the REC (S3)
      button and press the RST (S1) button once, wait 2 seconds to release REC button, 
      the LED will flash once on the board.
2. To check whether it's in reset recovery mode, by the command on the host:
```
lsusb
```
And it will show "NVidia Corp." on the terminal.

3. Conect the USB Micro-A cable.
4. Run command(the flash.sh file could be find in: ./jetpack/64_TX1/Linux_for_Tegra_64_tx1):
```
sudo ./flash.sh jetson-tx1 mmcblk0p1
```
This will take several minutes.

or:

If you want to flash with the image already exist, 

first download the OpenKAI image:  https://drive.google.com/open?id=1x3YBFgBJL2xZZQC_vzUzO8s-m05hZZFJ, put it in ./jetpack/64_TX1/Linux_for_Tegra_64_tx1/bootloader/

And run the command:
```
cd bootloader/
sudo ./tegraflash.py --bl cboot.bin --applet nvtboot_recovery.bin --chip 0x21 --cmd "write APP TX1_Jetpack30_OpenKAI_vek_20171121.img"
```

## For cloning the image, referring: https://elinux.org/Jetson/TX1_Cloning

## Sample of tensorrt located in: /usr/src/tensorrt
Run:
```
./bin/giexec
```
for the parameters information. And test with mnist:
```
./bin/giexec --model=/usr/src/tensorrt/data/mnist/mnist.caffemodel --deploy=/usr/src/tensorrt/data/mnist/mnist.prototxt --output=prob --batch=12
```
Test with FP16:
```
./bin/giexec --model=/usr/src/tensorrt/data/mnist/mnist.caffemodel --deploy=/usr/src/tensorrt/data/mnist/mnist.prototxt --output=prob --batch=12 --half2=true
```
