import sys
sys.path.append("protoc")

import address_book_pb2 as address_book_pb
import person_pb2 as person_pb
import person2_pb2 as person2_pb
import phone_type_pb2 as phone_type_pb


def example1():
    person01 = person_pb.Person()

    person01.name = "person01"
    person01.id = 1
    person01.email = "person01@xyz.com"

    print(person01)
    return person01


def example2():
    address_book = address_book_pb.AddressBook()

    person01 = address_book.people.add()
    person01.name = "person01"
    person01.id = 1
    person01.email = "person01@xyz.com"

    person02 = address_book.people.add()
    person02.name = "person02"
    person02.id = 2
    person02.email = "person02@xyz.com"

    person03 = address_book.people.add()
    person03.id = 100000
    person03.name = "Do Thu An"

    print(address_book)


def example3():
    person = phone_type_pb.Person()
    person.name = "asd"
    person.id = 99
    person.email = "asd@asd.com"
    person.phone_type = phone_type_pb.MOBILE

    print(person)


def example4():
    person01 = person2_pb.Person()
    date = person2_pb.date__pkg__pb2.Date()
    date.day = 28
    date.month = 6
    date.year = 2002
    person01.birthday.CopyFrom(date)
    person01.age = 20
    person01.id = 20010001

    print(person01)


if __name__ == "__main__":
    # example1()
    # example2()
    # example3()
    example4()
