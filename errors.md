## 2018/12/21
* CUDA8.0 not work for python3.6 + Tensorflow 1.8.0
- Reason: tf1.8.0 not compilant to CUDA8.0.
- Downgrade to Tensorflow 1.4.0 by: `sudo pip3 install tensorflow-gpu==1.4.1 --ignore-installed`.

* Error of python3.6 to find a ros version:
- Reason: PYTHONPATH is set before by a ros path.
- Check PYTHONPATH and set: `export PYTHONPATH="/usr/local/lib/python3.6/dist-packages"`.

* TypeError: softmax() got an unexpected keyword argument 'axis'
- `pip3 install --upgrade keras==2.1.3` for Tensorflow version 1.4.0 .
