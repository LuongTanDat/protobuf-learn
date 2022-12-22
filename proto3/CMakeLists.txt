cmake_minimum_required(VERSION 3.10.2)

project(app LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)


# add_subdirectory
add_subdirectory(protoc)
set(LIB ${LIB} protoc)

# Message
message(STATUS "Source directories:  ${SRC}")
message(STATUS "Include directories: ${INC}")
message(STATUS "Library directories: ${LIB}")

# Add sources
add_executable(${PROJECT_NAME} main.cpp)
target_sources(${PROJECT_NAME} PRIVATE ${SRC})
include_directories(${INC})
target_link_libraries(${PROJECT_NAME} ${LIB})
