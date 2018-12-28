
* CUDA8.0 not work for python3.6 + Tensorflow 1.8.0

**Reason**: tf1.8.0 not compilant to CUDA8.0.

**Solution**: Downgrade to Tensorflow 1.4.0 by: `sudo pip3 install tensorflow-gpu==1.4.1 --ignore-installed`.

* Error of python3.6 to find a ros version:

**Reason**: PYTHONPATH is set before by a ros path.

**Solution**: Check PYTHONPATH and set: `export PYTHONPATH="/usr/local/lib/python3.6/dist-packages"`.

* TypeError: softmax() got an unexpected keyword argument 'axis'

**Reason**: keras version or tf version not support.

**Solution**: `pip3 install --upgrade keras==2.1.3` for Tensorflow version 1.4.0 .

* ImportError: libcublas.so.8.0: cannot open shared object file: No such file or directory

**Reason**: could not find the correct path.

**Solution**: `gedit ~/.bashrc`, add to the last line: `export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-8.0/bin:$PATH`, save and run `source ~/.bashrc`.

* Cannot install matplotlib on Xavier Jetson

**Reason** freetype2 not well installed for aarch64

**Solution** Download from [freetype2](https://archlinuxarm.org/packages/aarch64/freetype2), copy 
```
sudo cp ft2build.h /usr/include/
sudo cp libfreetype.so* /usr/lib/
sudo chmod 777 /usr/lib/libfreetype.so*
```
and install matplotlib normally by pip.

