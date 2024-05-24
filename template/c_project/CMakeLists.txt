cmake_minimum_required(VERSION 3.15)

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
else()
    project(test_b)
    add_compile_definitions(PUBLIC
    $<$<PLATFORM_ID:Windows>:_HI_WIN=1>
    $<$<PLATFORM_ID:Linux>:_HI_LINUX=1>
    $<$<PLATFORM_ID:iOS>:_HI_IOS=1>
    $<$<PLATFORM_ID:Android>:_HI_ANDROID=1>
    $<$<PLATFORM_ID:Darwin>:_HI_MACOS=1>
    $<$<PLATFORM_ID:tvOS>:_HI_TVOS=1>
    $<$<PLATFORM_ID:watchOS>:_HI_WATCHOS=1>
    $<$<PLATFORM_ID:freertos>:_HI_FREERTOR=1>
    )
    # For sure build once.
    if (NOT BUILD_ONCE_<PROJECT_NAME>)
        # add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../xxx/ xxx)

        add_library(<PROJECT_NAME> STATIC ${SRC_FILES})

        # target_include_directories(<PROJECT_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../xxx/include)
        target_include_directories(<PROJECT_NAME> PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

        # target_link_libraries(<PROJECT_NAME> PRIVATE xxx)

    set(BUILD_ONCE_<PROJECT_NAME> ON CACHE BOOL "<PROJECT_NAME> has been built")
    endif()
endif()



