
## Add a line in /opt/movidius/NCSDK/install-ncsdk.sh function configure_caffe_options:

sed -i 's/version ${version}/version "${version}"/' cmake/Dependencies.cmake

