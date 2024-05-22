cmake_minimum_required(VERSION 3.15)
project(main)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../ <PROJECT_NAME>)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

add_executable(main main.c)
target_link_libraries(main PUBLIC <PROJECT_NAME>)

