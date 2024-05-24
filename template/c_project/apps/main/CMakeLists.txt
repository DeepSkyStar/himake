cmake_minimum_required(VERSION 3.15)
project(main)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../../ <PROJECT_NAME>)

add_executable(main main.c)

target_include_directories(main PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../../include)

target_link_libraries(main PUBLIC <PROJECT_NAME>)

