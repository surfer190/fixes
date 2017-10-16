# Types of Methods

## Static Method

In other programming languages like `php` you can create a **static** method

    class MyClass {
        public static function times2($input) {
            return $input * 2;
        }
    }

    echo MyClass::times2(40);

So static methods can be called without creating an instance / object first.

In python it is similar but it uses the `@staticmethod` decorator. 
Also they do not take a `self` or `cls` argument.

        class MyClass:
            @staticmethod
            def staticmethod():
                """
                Static methods don't have access to `cls` or `self`.
                They work like regular functions but belong to
                the class's namespace.
                """
                return 'static method called'
            def method(self):
                """
                Instance methods need a class instance and
                can access the instance through `self`.
                """
                return 'instance method called', self

## Class Methods

Class methods are similar to instance methods, but they differ in that an instance need not be created.
Ie. they can be called without an instance. They do require the `cls` as an argument which is not the instance but the actual class or blueprint for creating objects.

    class MyClass:
        @classmethod
        def classmethod(cls):
            """
            Class methods don't need a class instance.
            They can't access the instance (self) but
            they have access to the class itself via `cls`.
            """
            return 'class method called', cls

## The standard instance method

        class MyClass:
            def method(self):
                """
                Instance methods need a class instance and
                can access the instance through `self`.
                """
                return 'instance method called', self

## Calling the methods

        # All methods types can be
        # called on a class instance:
        >>> obj = MyClass()
        >>> obj.method()
        ('instance method called', <MyClass instance at 0x1019381b8>)
        >>> obj.classmethod()
        ('class method called', <class MyClass at 0x101a2f4c8>)
        >>> obj.staticmethod()
        'static method called'

        # Calling instance methods fails
        # if we only have the class object:
        >>> MyClass.classmethod()
        ('class method called', <class MyClass at 0x101a2f4c8>)
        >>> MyClass.staticmethod()
        'static method called'
        >>> MyClass.method()
        TypeError: 
            "unbound method method() must be called with MyClass "
            "instance as first argument (got nothing instead)"