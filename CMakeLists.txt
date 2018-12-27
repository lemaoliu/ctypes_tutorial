
cmake_minimum_required(VERSION 2.8.9)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}")
set(CMAKE_MACOSX_RPATH 1)
project (foo)

## if foo.cpp incudes other cpp files, we have to 
## write all cpp files below.
set (SOURCE foo.cpp)
add_library(foo MODULE ${SOURCE})

