Install GStreamer;


Run on the pc to show the video from the camera of TX2
```
/usr/bin/gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! autovideosink
```
Run on the pc to store the images:
```
/usr/bin/gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! jpegenc ! multifilesink location=image_%06d.jpg max-files=2
```
