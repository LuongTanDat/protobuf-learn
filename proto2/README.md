# [Protocol Buffers In C++](https://medium.com/geekculture/protocol-buffers-in-c-d60865ae7782)

## Defining Protocol Format (message)

- The definitions in a `.proto` the file is simple: you add a message for each data structure you want to serialize, then specify a name and a type for each field in the message.

```
// person.proto
syntax = "proto2";

package PERSON;

message Person
{
    optional string name = 1;
    optional int32 id = 2;
    optional string name = 3;
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
protoc -I=./protoc --cpp_out=./protoc person.proto
find . -name "*.proto" -type f -exec protoc -I=./protoc --cpp_out=./protoc {} \;
# if you are in the SRC_DIR or working directory, you can execute with fallowing cmd.
# protoc -I=./ --cpp_out=./ message.proto
# This generates the following files in your specified destination directory:
# 1. message.pb.cc
# 2. message.pb.h
```

## C++ code example

- Let's see some [C++ code](main.cpp#L26)

- Compile

`g++`

```bash
g++ -std=c++2a -I /usr/local/include -I ./protoc -L /usr/lib/x86_64-linux-gnu/ main.cpp ./protoc/message.pb.cc -lprotobuf -pthread -o app
./app
```

`Cmake`

```bash
cmake ..
make
./app
```

# Protobuf

## `.proto` file & API’s

- Let's see some [C++ code](main.cpp#L26) and [`.proto` file](protoc/person.proto)

## Repeated Fields (Arrays or List)

- Repeated modifier allow us to create dynamic sized arrays or list,.

- Let's see some [C++ code](main.cpp#L62) and [`.proto` file](protoc/address_book.proto)

## ENUM (Enumeration)

- We can use Enums if we know all the values a field can take.

- Enum must start by tag `0`.

- The first value of enum is the default value (**tag 0**), even if we do not initialise the enum field default value(**tag 0**) will be initlised.

- Let's see some [C++ code](main.cpp#L113) and [`.proto` file](protoc/phone_type.proto)

## Packages

- In [person2.proto](protoc/person2.proto), we can import Date message from [date_pkg.proto](protoc/date_pkg.proto)

- But you have to notice that, you have to import consistent package name.

- Let's see some [C++ code](main.cpp#L131) and [`.proto` file](protoc/person2.proto)

## Compound Data Types

- There are two more compound data types which may be useful for complicated use cases. They are `OneOf` and `Any`. In this chapter, we will see how to use these two data types of Protobuf.

### OneOf

- We pass a few parameters to this `OneOf` data type and Protobuf ensures that only one of them is set. If we set one of them and try to set the other one, the first attribute gets reset.

<details>
    <summary>Protobuf Map example!</summary>

```c++
syntax = "proto3";
package theater;

message Theater
{
    string name = 1;
    string address = 2;
    
    repeated google.protobuf.Any peopleInside = 3;
    
    oneof availableEmployees
    {
        int32 count = 4;
        string errorLog = 5;
    }
}
```

```
name: "SilverScreen"
peopleInside {
    type_url: "type.googleapis.com/theater.Employee"
    value: "\n\004John"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Viewer"
    value: "\n\004Jane\020\036"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Employee"
    value: "\n\005Simon"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Viewer"
    value: "\n\006Janice\020\031"
}
```

</details>

### Any

- The next data type that can be of use for complicated uses cases is Any. We can pass any type/message/class to this data type and Protobuf would not complain.

<details>
    <summary>Protobuf Any example!</summary>

```c++
syntax = "proto3";
package theater;

import "google/protobuf/any.proto";

message Theater
{
    string name = 1;
    string address = 2;
    repeated google.protobuf.Any peopleInside = 3;
}

message Employee
{
    string name = 1;
    string address = 2;
}

message Viewer
{
    string name = 1;
    int32 age = 2;
    string sex = 3;
}
```

```
name: "SilverScreen"
peopleInside {
    type_url: "type.googleapis.com/theater.Employee"
    value: "\n\004John"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Viewer"
    value: "\n\004Jane\020\036"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Employee"
    value: "\n\005Simon"
}
peopleInside {
    type_url: "type.googleapis.com/theater.Viewer"
    value: "\n\006Janice\020\031"
}
```

</details>

## Map

- Map is one of the composite datatypes of Protobuf.

<details>
    <summary>Protobuf Map example!</summary>

```c++
syntax = "proto3";
package theater;

message Theater
{
    map<string, int32> movieTicketPrice = 9;
}
```

```
movieTicketPrice {
    key: "Avengers Endgame"
    value: 700
}
movieTicketPrice {
    key: "Captain America"
    value: 200
}
movieTicketPrice {
    key: "Wonder Woman 1984"
    value: 400
}
```
</details>

## Serialize

### output to String

<details>
    <summary>Protobuf Serialize example!</summary>

- Serialize

```c++
date::module::Person person = example4();
std::string data_string = person.SerializeAsString();
```

- Deserialize

```c++
date::module::Person person_from_string;
person_from_string.ParseFromString(data_string);
std::cout << "[ PARSE ][ FROM_STRING ]: " << person_from_string.DebugString() << std::endl;
```

</details>

### output to File

<details>
    <summary>Protobuf Serialize example!</summary>

- Serialize

```c++
date::module::Person person = example4();

// Write the new ::person back to disk.
std::fstream ofs_person("data.pb", std::ios::out | std::ios::trunc | std::ios::binary);
if (!person.SerializeToOstream(&ofs_person))
    std::cerr << "[ ERROR ] Failed to write ::person." << std::endl;
else
    std::cout << "[ OK ] Success to write ::person." << std::endl;

ofs_person.close();
```

- Deserialize

```c++
// Reads the entire ::person from a file and prints all the information inside.
// Read the existing ::person.
std::fstream ifs_person("data.pb", std::ios::in | std::ios::binary);
// std::ifstream ifs_person("data.pb");
date::module::Person person_stream;
if (!person_stream.ParseFromIstream(&ifs_person))
    std::cerr << "[ ERROR ] Failed to parse ::person." << std::endl;
else
    std::cout << "[ OK ] Success to parse ::person." << std::endl;

ifs_person.close();
std::cout << "[ PARSE ][ FROM_ISTREAM ]: " << person_stream.DebugString() << std::endl;
```

</details>

### Ouput to `char*`

<details>
    <summary>Protobuf Serialize example!</summary>

- Serialize

```c++
date::module::Person person = example4();

size_t size = person.ByteSizeLong();
void *buffer = malloc(size);
person.SerializeToArray(buffer, size);
```

```c++
std::ostringstream oss;
person.SerializeToOstream(&oss);
std::string text = oss.str();
const char *ctext = text.c_str();
```

- Deserialize

```c++
date::module::Person person_from_array;

person_from_array.ParseFromArray(buffer, size);
std::cout << "[ PARSE ][ FROM_ARRAY ]: " << person_from_array.DebugString() << std::endl;
```

```c++
std::string text2{ctext};
std::istringstream iss(text2);

date::module::Person person_stream;

if (!person_stream.ParseFromIstream(&iss))
    std::cerr << "[ ERROR ] Failed to parse ::person." << std::endl;
else
    std::cout << "[ OK ] Success to parse ::person." << std::endl;

std::cout << "[ PARSE ][ FROM_ISTREAM ]: " << person_stream.DebugString() << std::endl;
```

</details>
