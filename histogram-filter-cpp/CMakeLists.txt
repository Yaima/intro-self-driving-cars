cmake_minimum_required(VERSION 3.9)
project(udacity_cpp_histogram_filter_project)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_executable(udacity_cpp_histogram_filter_project
        tests.cpp)
