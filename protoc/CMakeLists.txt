# cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
# project("protoc" LANGUAGES CXX)

# # Flags
# set(CMAKE_CXX_STANDARD 20)
# set(GCC_CXX_FLAGS "${GCC_CXX_FLAGS}")

# # Protobuf compile
# find_package(Protobuf REQUIRED)
# find_package(Threads)
# set(INC ${INC} ${PROTOBUF_INCLUDE_DIR})
# set(LIB ${LIB} ${PROTOBUF_LIBRARIES})
# file(GLOB PROTO_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.proto")
# # PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HDR ${PROTO_FILES})
# protobuf_generate(
#     PROTOS ${PROTO_FILES}
#     OUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}
#     OUT_VAR PROTO_SRCS
#     LANGUAGE cpp
#     USAGE_REQUIREMENT PRIVATE
#   )

# message(STATUS "PROTO_HDR:  ${PROTO_HDR}")
# message(STATUS "PROTO_SRC:  ${PROTO_SRC}")
# message(STATUS "PROTO_SRCS:  ${PROTO_SRCS}")
# message(STATUS "PROTO_FILES:  ${PROTO_FILES}")


# set(INC ${INC} ${PROTO_HDR})
# set(SRC ${SRC} ${PROTO_SRC})
# set(SRC ${SRC} ${PROTO_SRCS})


# # add_library(${PROJECT_NAME} STATIC ${PROTO_SRC} ${PROTO_HDR} ${PROTO_FILES})
# add_library(${PROJECT_NAME} SHARED ${SRC})
# target_include_directories(${PROJECT_NAME} PUBLIC ${INC})
# target_link_lset(INC ${INC} ${PROTOBUF_INCLUDE_DIR})
# set(LIB ${LIB} ${PROTOBUF_LIBRARIES})RY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
#         RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
#         PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include/${PROJECT_NAME})

cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project("protoc" LANGUAGES CXX)

# Flags
set(CMAKE_CXX_STANDARD 20)
set(GCC_CXX_FLAGS "${GCC_CXX_FLAGS}")

file(GLOB PROTO_HDRS "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
# set(INC ${INC} ${PROTO_HDRS})
set(INC ${INC} ${CMAKE_CURRENT_SOURCE_DIR})
file(GLOB PROTO_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")
set(SRC ${SRC} ${PROTO_SRCS})

# Find package
find_package(Protobuf REQUIRED)
set(INC ${INC} ${PROTOBUF_INCLUDE_DIR})
set(LIB ${LIB} ${PROTOBUF_LIBRARIES})
set(LIB ${LIB} -pthread -lprotobuf)

# Message
message(STATUS "Source directories:  ${SRC}")
message(STATUS "Include directories: ${INC}")
message(STATUS "Library directories: ${LIB}")

# Target
add_library(${PROJECT_NAME} SHARED ${SRC})
target_include_directories(${PROJECT_NAME} PUBLIC ${INC})
target_link_libraries(${PROJECT_NAME} PRIVATE ${LIB})
target_compile_definitions(${PROJECT_NAME} PUBLIC MESSAGE_PROTOBUF_VERSION=1)


# Install
install(TARGETS ${PROJECT_NAME}
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include/${PROJECT_NAME})
