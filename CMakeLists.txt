cmake_minimum_required(VERSION 3.10.2)

project(app LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}" ${CMAKE_MODULE_PATH})
# set(CMAKE_CXX_STANDARD_REQUIRED ON)

# # Flags
# set(GCC_CXX_FLAGS "${GCC_CXX_FLAGS} -lboost_system -lboost_thread")
set(CMAKE_THREAD_LIBS_INIT "-lpthread")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")
set(CMAKE_HAVE_THREADS_LIBRARY 1)
set(CMAKE_USE_WIN32_THREADS_INIT 0)
set(CMAKE_USE_PTHREADS_INIT 1)
set(THREADS_PREFER_PTHREAD_FLAG ON)

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
target_link_libraries(${PROJECT_NAME} ${LIB} ${PROTOBUF_LIBRARY})
