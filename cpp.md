## write a log into a file
```cpp
const std::string logfile = "/home/nvidia/aprint.txt";
double duration = 0;
std::ofstream filestream(logfile.c_str());
filestream << "Duration: "<< duration <<std::endl;
```
