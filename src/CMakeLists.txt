include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

file(GLOB_RECURSE SOURCES "*.cpp")
if(APPLE)
    file(GLOB MkLIB "/usr/local/lib/libMkLIB.dylib")
elseif(UNIX)
    # file(GLOB MkLIB "/usr/local/lib/libMkLIB.so")
endif()

add_compile_options( -gdwarf -g) # -Wall -Wextra -Wpedantic -Werror

add_executable(${PROJECT_NAME} ${SOURCES})

if(APPLE)
    target_link_libraries(${PROJECT_NAME} ${MkLIB} ) 
elseif(UNIX)
    target_link_libraries(${PROJECT_NAME} MkLIB ) 
endif()