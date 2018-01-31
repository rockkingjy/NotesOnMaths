## TX1/2 cloning
https://elinux.org/Jetson/TX1_Cloning

OpenKAI image: https://drive.google.com/open?id=1x3YBFgBJL2xZZQC_vzUzO8s-m05hZZFJ

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
