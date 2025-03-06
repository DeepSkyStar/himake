cmake_minimum_required(VERSION 3.15)

if(DEFINED ESP_PLATFORM)
else()
    project(<PROJECT_NAME> C CXX ASM)
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_C_EXTENSIONS ON)

file(GLOB_RECURSE SRC_FILES
"${CMAKE_CURRENT_SOURCE_DIR}/src/*.c"
)

# ESP_PLATFORM
# Ref https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME

# build for different sys.
if(DEFINED ESP_PLATFORM)
    idf_component_register(SRCS
                    ${SRC_FILES}
                    INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/include
                    )
    add_definitions(-D_HI_FREERTOS=1)
    add_definitions(-D_HI_ESP32=1)
else()
    if(CMAKE_BUILD_TYPE STREQUAL "Debug")
        add_definitions(-DDEBUG)
        add_compile_options(-g) # 添加调试信息
        add_compile_options(-O0) # 禁用优化
    endif()

    add_compile_options(-Werror)

    if("${PLATFORM}" STREQUAL "stm32")
        add_definitions(-D_HI_FREERTOS=1)
        add_definitions(-D_HI_STM32=1)
    else()
        add_compile_options(-fPIC)
    endif()

    # For build once.
    # if (NOT TARGET xxx)
    # add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../xxx/ xxx)
    # endif()
    if("${PLATFORM}" STREQUAL "stm32")
        add_library(<PROJECT_NAME> STATIC ${SRC_FILES})
    else()
        add_library(<PROJECT_NAME> SHARED ${SRC_FILES})
    endif()

    # target_include_directories(<PROJECT_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../xxx/include)
    target_include_directories(<PROJECT_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

    # target_link_libraries(<PROJECT_NAME> PUBLIC xxx)
endif()



