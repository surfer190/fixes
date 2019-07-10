# The Perils of Inheritance

## Inheritance

    class Vehicle:
        pass
    
    class Bicycle(Vehicle):
        pass

## Composition

    class Engine:
        pass

    class Car:
        def __init__(self):
            self.engine = Engine()

## Design Patterns: Gang of Four

Books: Design Patterns - Elements of Reusable object-oriented software

> Favour object composition over class inheritance (at the beginning)

Class inheritance - white-box reuse
Object composition - black-box reuse

### Inheritance Advantages

1. Easy way to reuse code
2. Allows changing the inherited implementation

### Inheritance Disadvantages

1. Relationship between a base class and derived class is statically fixed
2. Inheritance supports weak encapsulation and fragile structures
3. A derived class inherits everything, even things it doesn't need or want
4. Changes in the base class interface breaks all derived classes


## Source

* [The Perils of Inheritance](https://www.youtube.com/watch?v=YXiaWtc0cgE)

