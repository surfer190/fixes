---
author: ''
category: Microservices
date: '2022-06-24'
summary: ''
title: Protocol Buffers
---

## Protocol Buffers

* language-neutral
* platform-neutral
* extensible mechanism for serializing structured data in a:
    - forward-compatible way
    - backward-compatible way

Like json but smaller, faster and generates native language bindings

Protocol buffers contain:

* definition language (called `.proto` files)
* code to interface with data from the proto compiler
* language specific runtime libraries
* serialisation format for data written to file or sent over network

### What Problems to Protocol Buffers Solve?

* serialisation format
* good for inter-service communications and archival storage on disk

> What is serialisation? Converting objects into different representations - usually for storage in a file or transmission over a network

Protocol buffer messages are described in `.proto` files:

    message Person {
      optional string name = 1;
      optional int32 id = 2;
      optional string email = 3;
    }

The `proto compiler` generates code for various languages at build time.

The data format might change and the data in protocol buffers may persist for a very long time - therefore it is crucial that they are backwards compatible.

Changes like adding and removing fields will not break existing services.

### Benefits of Protocol Buffers

* Compact data storage
* Fast parsing
* Available for many programming languages
* Optimised functionality through auto generated classes

The same message can be read by different programming languages (language agnostic)

Directly supported languages:

* C++
* C#
* Java
* Kotlin
* Objective-C
* PHP
* Python
* Ruby
* Go (through plugins)
* Dart (through plugins)

### Cross-project Support

> You can use protocol buffers across projects by defining message types in `.proto` files that reside outside of a specific project’s code base.

If you're defining message types or enums that you anticipate will be widely used outside of your immediate team, you can put them in their own file with no dependencies.

Commonly used definitions at google:

[`status.proto`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto):

    message Status {
        // The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].
        int32 code = 1;

        // A developer-facing error message, which should be in English. Any
        // user-facing error message should be localized and sent in the
        // [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.
        string message = 2;

        // A list of messages that carry the error details.  There is a common set of
        // message types for APIs to use.
        repeated google.protobuf.Any details = 3;
    }

[`timestamp.proto`](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/timestamp.proto):

    message Timestamp {
        // Represents seconds of UTC time since Unix epoch
        // 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to
        // 9999-12-31T23:59:59Z inclusive.
        int64 seconds = 1;

        // Non-negative fractions of a second at nanosecond resolution. Negative
        // second values with fractions must still have non-negative nanos values
        // that count forward in time. Must be from 0 to 999,999,999
        // inclusive.
        int32 nanos = 2;
    }

### Updating Proto Definitions Without Updating Code

 * old code will read new messages without issues, ignoring any newly added fields
 * To the old code, fields that were deleted will have their default value, and deleted repeated fields will be empty.
 * New code will also transparently read old messages. New fields will not be present in old messages; in these cases protocol buffers provide a reasonable default value.
 
### When to not use Protocol Buffers
 
* The message is big (larger than a few MB)
* Two messages cannot be compared in binary - representations will differ
* Not good for specific compression like JPEG or PNG
* Not good for large, multi-dimensional arrays of floating point numbers
* They don't inherently describe their data - you need access to the proto file
* Not a formal standard
 
### Who uses protocol buffers
 
* [gRPC](https://grpc.io/)

### How do Protocol Buffers Work?

1. Create a proto file
2. Generate code using the `protoc` compiler
3. Compile protocol buffer code with your project code
4. Use protocol buffer classes to serialise, share and deserialise data

### Protocol Buffers Definition Syntax

[Field rules](https://developers.google.com/protocol-buffers/docs/proto#specifying-rules):

* `optional` - can have 0 or 1 of this field
* `repeated` - can have repeated values any number of times
* `singular` - 
* `required` - (Discouraged as it breaks forward and backward compatability) well-formed message has exactly 1 field

Protocol buffers support the usual [primitive data types](https://developers.google.com/protocol-buffers/docs/proto#scalar):

* `double`
* `float`
* `int32`
* `int64`
* `uint32`
* `bool`
* `string`
* `bytes`

> scalar means a single value. As opposed to a vector, lists, arrays, maps and set of data / data points.

Can also be:

* `message` - nest parts of the definition
* `enum` - set of values to choose from
* `oneof` - at most one field set out of the optional
* `map` - key-value pairs

> After setting optionality and field type, you assign a field number. Field numbers cannot be repurposed or reused. If you delete a field, you should reserve its field number to prevent someone from accidentally reusing the number.

You can create datatypes by creating new `message`s:

    message Date {
        int32 year = 1;
        int32 month = 2;
        int32 day = 3;
    }

## Language Guide and Style Guide

* [Language Guide](https://developers.google.com/protocol-buffers/docs/proto)
* [Style Guide](https://developers.google.com/protocol-buffers/docs/style)

## Python Tutorial

I will now go through the [python tutorial on protocol buffers](https://developers.google.com/protocol-buffers/docs/pythontutorial)

**Warning: The tutorial is very old and based on python2 - I have updated it as best I can however there may be more recent and relevant sources elsewhere**

For more info check [python generated code guide](https://googleapis.dev/python/protobuf/latest/) and [python generated code](https://developers.google.com/protocol-buffers/docs/reference/python-generated)

### Install Protoc

[Protobuf releases](https://github.com/protocolbuffers/protobuf/releases/)

I got the universal osx version and installed it with:

    sudo install -m 0755 -o me -g admin ./bin/protoc /usr/local/bin/.

Check the version:

    $ protoc --version
    libprotoc 3.21.1

### The Problem

Address book of contacts: name, id, email address and phone number - the application reads and writes the contacts to a file.

Ways to serialise this structured data:

* Python pickling - default - does not deal with schema evolution well and is not compatible with other languages.
* Invent an ad-hoc way to encode the data
* serialise to xml - good for sharing between applications - but heavy weight in size and parsing xml is slower than simple fields in a class.
* Protocol buffers - define the message in a `.proto` - compiles a class for efficient serialisation and serialisation from binary. Future changed

### Write protocol buffer schema

`addressbook.proto`:

    syntax = "proto2";

    // namespace - prevent collisions
    package tutorial;

    // Person contains many PhoneNumber messages
    message Person {
    optional string name = 1;
    optional int32 id = 2;
    optional string email = 3;

    enum PhoneType {
        MOBILE = 0;
        HOME = 1;
        WORK = 2;
    }

    
    // =1, =2 is a unique tag for binary encoding
    message PhoneNumber {
        optional string number = 1;
        // setting our own default
        optional PhoneType type = 2 [default = HOME];
    }

    repeated PhoneNumber phones = 4;
    }

    // Address book contains many Person messages
    message AddressBook {
        // think of repeated as a list
        repeated Person people = 1;
    }

> `required` field:  serializing an uninitialized message will raise an exception. Parsing an uninitialized message will fail.

> There is no inheritance in protobufs

> Tag numbers 1-15 require one less byte to encode - repeated fields are good for these numbers

### Compiling Protocol Buffers

Generate classes for the protocol buffers with:

    protoc

or

    protoc -I=. --python_out=. ./addressbook.proto

> we specify we want the python generated classes with `--python_out`

Data access code is not generated directly like in `C++` and `java`.

> In Python, the compiler only outputs code to build descriptors for the generated classes, and a Python metaclass does the real work. __It seems like this is the reason that the generated class for me did not contain the empty classes - so my IDE didn't pick them up but I could still use them at runtime__

### Install the Python Protobuf Libary

Install [python protobuf package](https://pypi.org/project/protobuf/)

    pip install protobuf

### Creating a file

    from protocol_buffers import addressbook_pb2

    person = addressbook_pb2.Person()

    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"

    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME

> AttributeError: Protocol message Person has no "no_such_field" field.

    person.no_such_field = 1
    person.id = 'skdjfhkas'

Other functions:

* `IsInitialized()`: checks if all the required fields have been set.
* `__str__()`: returns a human-readable representation of the message, particularly useful for debugging. (Usually invoked as str(message) or print message.)
* `CopyFrom(other_msg)`: overwrites the message with the given message's values.
* `Clear()`: clears all the elements back to the empty state. 

Reading and writing to binary:


* `SerializeToString()`: serializes the message and returns it as a string. Note that the bytes are binary, not text; we only use the str type as a convenient container.
* `ParseFromString(data)`: parses a message from the given string. 

### Writing a Message

Earlier we created messages - but they were ephemeral and not written anywhere.
Now we will write them to an output stream.

This example reads the addressbook from a file, adds a new person and then writes it back to a file.

    #!/usr/bin/env python3
    from protocol_buffers import addressbook_pb2
    import sys

    # This function fills in a Person message based on user input.
    def PromptForAddress(person):
    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")

    email = input("Enter email address (blank for none): ")
    if email != "":
        person.email = email

    while True:
        number = input("Enter a phone number (or leave blank to finish): ")
        if number == "":
        break

        phone_number = person.phones.add()
        phone_number.number = number

        type = input("Is this a mobile, home, or work phone? ")
        if type == "mobile":
        phone_number.type = addressbook_pb2.Person.PhoneType.MOBILE
        elif type == "home":
        phone_number.type = addressbook_pb2.Person.PhoneType.HOME
        elif type == "work":
        phone_number.type = addressbook_pb2.Person.PhoneType.WORK
        else:
        print("Unknown phone type; leaving as default value.")

    # Main procedure:  Reads the entire address book from a file,
    #   adds one person based on user input, then writes it back out to the same
    #   file.
    if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    try:
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()
    except IOError:
    print(sys.argv[1] + ": Could not open file.  Creating a new one.")

    # Add an address.
    PromptForAddress(address_book.people.add())

    # Write the new address book back to disk.
    f = open(sys.argv[1], "wb")
    f.write(address_book.SerializeToString())
    f.close()

## Extending a Protocol Buffer

Updating a protocol buffer so that old buffers are forward compatible and new buffers are backward compatible.
Rules:

* you must not change the tag numbers of any existing fields.
* you must not add or delete any required fields.
* you may delete optional or repeated fields.
* you may add new optional or repeated fields but you must use fresh tag numbers (that is, tag numbers that were never used in this protocol buffer, not even by deleted fields).

Considerations:

* Old code will happily read new messages and simply ignore any new fields.
* To the old code, optional fields that were deleted will simply have their default value, and deleted repeated fields will be empty.
* New code will also transparently read old messages.
* New optional fields will not be present in old messages, so you will need to either check explicitly whether they're set with `has_`, or provide a reasonable default value in your `.proto` file with `[default = value]` after the tag number.
* If the default value is not specified for an optional element, a type-specific default value is used instead: for strings, the default value is the empty string. For booleans, the default value is false. For numeric types, the default value is zero.
* A new repeated field, your new code will not be able to tell whether it was left empty (by new code) or never set at all (by old code) since there is no `has_` flag for it. 

## Python API Reference

* [More Information in the Python Protocol buffers API](https://googleapis.dev/python/protobuf/latest/)

## Sources

* [Protocol Buffers Overview](https://developers.google.com/protocol-buffers/docs/overview)
* [What is a scalar data type](https://softwareengineering.stackexchange.com/questions/238033/what-does-it-mean-when-data-is-scalar)
