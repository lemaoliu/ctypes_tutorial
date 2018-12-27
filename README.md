# How to calling c++ from python: a tutorial

The main files are foo.py foo.cpp and CMakeLists.txt

1. Compile .so file
```
cd build; cmake ..; make; cd ..
```

2. Run application
```
python foo.py
```
 
3. BOOST_PYTHON_MODULE
Another way from Boost in c++
