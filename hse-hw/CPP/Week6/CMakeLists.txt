cmake_minimum_required(VERSION 3.5)

project(week6_hw LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(week6_hw main.cpp)

install(TARGETS week6_hw
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
