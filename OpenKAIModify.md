## Add a class in OpenKAI

Take the example of add _GPS_my.h in src/Navigation/:

1. Put the _GPS_my.cpp and _GPS_my.h in the folder src/Navigation/.

2. Chage in _GPS_my.h to:
```
#ifndef SRC_NAVIGATION_GPS_MY_H_
#define SRC_NAVIGATION_GPS_MY_H_
```
3. Add in src/Config/Module.h:
```
#include "../Navigation/_GPS_my.h"
```
and add in src/Config/Module.cpp:
```
ADD_MODULE(_GPS_my);
```
4. Change in kiss/GPS_my.kiss:
```
{
	"name":"GPS_my",
	"class":"_GPS_my",
	"bInst":1,
	"bLog":1,
	"FPS":30,
	"Window":"GPSwin",
	"_Mavlink":"apMavlink",
	"mavDSfreq":30,
	"posDiffMax":0.5,
}
```
5. Run:
```
make clean
ccmake ../
make -4j
```
