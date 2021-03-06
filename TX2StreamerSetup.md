Install GStreamer on both the TX2 and pc;

Connect the camera to the TX2 and run:
```
gst-launch-1.0 v4l2src device="/dev/video0" ! x264enc tune=zerolatency ! video/x-h264, stream-format=byte-stream ! rtph264pay ! udpsink port=8081 host=192.168.100.63
```
or
```
gst-launch-1.0 v4l2src device="/dev/video0" ! "video/x-raw, width=640, height=480" ! x264enc tune=zerolatency ! video/x-h264, stream-format=byte-stream ! rtph264pay ! udpsink port=8081 host=192.168.100.63
```
Run on the pc to show the video from the camera of TX2
```
/usr/bin/gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! autovideosink
```
Run on the pc to store the images:
```
/usr/bin/gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! jpegenc ! multifilesink location=image_%06d.jpg max-files=2
```
Run on the pc to change the frame rate:
```
/usr/bin/gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videorate ! "video/x-raw, framerate=10/1" ! jpegenc ! multifilesink location=image_%06d.jpg max-files=10
```
