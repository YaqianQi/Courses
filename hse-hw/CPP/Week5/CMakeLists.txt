cmake_minimum_required(VERSION 3.5)

project(week5_hw LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(week5_hw main.cpp ringbuf.cpp ringbuf.hpp)

install(TARGETS week5_hw
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
