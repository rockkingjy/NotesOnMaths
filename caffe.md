## draw nets
```
./python/draw_net.py train_posenet.prototxt posenet.png
```

## Save log to a file:
```
python train.py 2>&1 | tee train.log
```

## parse log:
copy the train.log to /home/enroutelab/Amy/caffe/tools/extra
```
./parse_log.sh train.log
```

## plot log:
```
./plot_training_log.py.example 0  save.png train.log
```
