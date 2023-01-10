cmake_minimum_required(VERSION 3.22)
project(BakingDog)

set(CMAKE_CXX_STANDARD 14)

add_executable(BakingDog ada.cpp)

add_executable(main ada.cpp)
add_executable(add giftCollection.cpp)