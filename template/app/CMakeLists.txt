cmake_minimum_required(VERSION 3.15)
project(<APP_NAME>)

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../../ <PROJECT_NAME>)
file(GLOB_RECURSE SRC_FILES
"${CMAKE_CURRENT_SOURCE_DIR}/src/*.c"
)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  add_definitions(-DDEBUG)
  add_compile_options(-g) # 添加调试信息
  add_compile_options(-O0) # 禁用优化
endif()

add_executable(<APP_NAME> 
    main.c
    ${SRC_FILES}
    )

target_include_directories(<APP_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../../include)
target_include_directories(<APP_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

target_link_libraries(<APP_NAME> PUBLIC <PROJECT_NAME>)

