cmake_minimum_required(VERSION 3.10.2)

project("protoc" LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)

set(INC ${INC} ${CMAKE_CURRENT_SOURCE_DIR})
file(GLOB PROTO_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")
set(SRC ${SRC} ${PROTO_SRCS})

# Find package
find_package(Protobuf REQUIRED)
set(INC ${INC} ${PROTOBUF_INCLUDE_DIR})
set(LIB ${LIB} ${PROTOBUF_LIBRARIES})

# Message
message(STATUS "Source directories:  ${SRC}")
message(STATUS "Include directories: ${INC}")
message(STATUS "Library directories: ${LIB}")

# Target
add_library(${PROJECT_NAME} SHARED ${SRC})
target_include_directories(${PROJECT_NAME} PUBLIC ${INC})
target_link_libraries(${PROJECT_NAME} INTERFACE ${LIB})
target_compile_definitions(${PROJECT_NAME} PUBLIC MESSAGE_PROTOBUF_VERSION=1)


# Install
install(TARGETS ${PROJECT_NAME}
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include/${PROJECT_NAME})
