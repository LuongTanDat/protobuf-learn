import sys
sys.path.append("protoc")

import address_book_pb2 as address_book_pb
import person_pb2 as person_pb
import person2_pb2 as person2_pb
import phone_type_pb2 as phone_type_pb
import leimao_addressbook_pb2 as leimao_addressbook_pb
from leimao_addressbook_pb2 import google_dot_protobuf_dot_timestamp__pb2 as timestamp
import time

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


def example5():
    address_book = leimao_addressbook_pb.AddressBook()
    
    person01 = address_book.people.add()
    person01.name = "ANoi"
    person01.id = 12
    person01.email = "anoi@emoi.com"
    phone_number = person01.phones.add()
    phone_number.number = "0961056125"
    phone_number.type = leimao_addressbook_pb.Person.MOBILE
    phone_number = person01.phones.add()
    phone_number.number = "0961056125"
    phone_number.type = leimao_addressbook_pb.Person.HOME
    person01.last_updated.CopyFrom(timestamp.Timestamp(seconds=int(time.time())))
    
    person02 = address_book.people.add()
    person02.name = "An Do"
    person02.id = 28
    person02.email = "ando@emoi.com"
    phone_number = person02.phones.add();
    phone_number.number = "0947397728"
    phone_number.type = leimao_addressbook_pb.Person.HOME
    phone_number = person02.phones.add();
    phone_number.number = "0947397728"
    phone_number.type = leimao_addressbook_pb.Person.WORK
    person02.last_updated.CopyFrom(timestamp.Timestamp(seconds=int(time.time())))

    print(address_book)

if __name__ == "__main__":
    # example1()
    # example2()
    # example3()
    # example4()
    example5()
