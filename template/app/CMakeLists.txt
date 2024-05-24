cmake_minimum_required(VERSION 3.15)
project(<APP_NAME>)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../../ <PROJECT_NAME>)

add_executable(<APP_NAME> main.c)

target_include_directories(<APP_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../../include)

target_link_libraries(<APP_NAME> PUBLIC <PROJECT_NAME>)

