
## Add a line in /opt/movidius/NCSDK/install-ncsdk.sh function configure_caffe_options:

sed -i 's/version ${version}/version "${version}"/' cmake/Dependencies.cmake

## Movidius with raspberry pi3:

https://medium.com/@hsheil/movidius-neural-compute-stick-and-raspberry-3-quick-start-guide-a89ff5e1d7ca

And Run YOLO:

https://github.com/gudovskiy/yoloNCS


