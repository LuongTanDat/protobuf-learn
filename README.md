# [Protocol Buffers In C++](https://medium.com/geekculture/protocol-buffers-in-c-d60865ae7782)

## Install PROTOC compiler

- Mac: `brew install protobuf`

- Ubuntu : `sudo apt install protobuf-compiler`

- Windows: [link](https://www.geeksforgeeks.org/how-to-install-protocol-buffers-on-windows/)

> Check if it works

```bash
$ protoc --version
libprotoc 3.17.1
```

## Defining Protocol Format (message)

- The definitions in a `.proto` the file is simple: you add a message for each data structure you want to serialize, then specify a name and a type for each field in the message.

```
// person.proto
syntax = "proto3";

package PERSON;

message Person
{
    string name = 1;
    int32 id = 2;
    string name = 3;
}
```

- The `.proto` the file starts with a package declaration(here `PERSON`), which helps to prevent naming conflicts between different projects. In C++, your generated classes will be placed in a namespace(`PERSON`) matching the package name.

- Next, we have our message definitions. A message is just an aggregate containing a set of typed fields. Many standard simple data types are available as field types, including `bool`, `int32`, `float`, `double`, and `string`.

- Each field must be annotated with one of the following modifiers:

    - `optional` : The field may or may not be set. If an optional field value isn’t set, a default value is used(`zero` for numeric types, the `empty` string for strings, `false` for bools).
    - `repeated` : Think of repeated fields as dynamically sized arrays(or `std::vector`)

- For protobuff the important element is **tag** (in `person.proto` `name=1`, `id=2`, `email=3`, these numbers are the **tags**), the smallest tag is `1` & largest is `2^29-1`, we cannot use `19000–19999` because these are reserved by Google.

## Compile `.proto` file

```bash
protoc -I=./protoc --cpp_out=./protoc message.proto
# if you are in the SRC_DIR or working directory, you can execute with fallowing cmd.
# protoc -I=./ --cpp_out=./ message.proto
# This generates the following files in your specified destination directory:
# 1. message.pb.cc
# 2. message.pb.h
```

## C++ code

- Let's see some [C++ code](main.cpp)

- Compile

```bash
g++ -std=c++2a -I /usr/local/include -I ./protoc -L /usr/lib/x86_64-linux-gnu/ main.cpp ./protoc/message.pb.cc -lprotobuf -pthread -o app
./app
```
