---
author: ''
category: Clojure
date: '2021-06-24'
summary: ''
title: Getting Started Clojure
---
## Getting Started Clojure

I am journaling my intro to clojure.
I have heard it is good and it comes recommended by some good people - so I am trying it.

First thing I did was search for `clojure` online and I found the [getting started page](https://clojure.org/guides/getting_started)

### Java and JDK

First step is ensuring I have java and a JDK...

I ran:

    $ java -showversion
    java version "1.8.0_74"
    Java(TM) SE Runtime Environment (build 1.8.0_74-b02)
    Java HotSpot(TM) 64-Bit Server VM (build 25.74-b02, mixed mode)

and I needed `JAVA_HOME` to be set, but it was not:

    printenv | grep JAVA_HOME

but you can do:

    $ which java
    /usr/bin/java

or use java to find java:

    $ java -XshowSettings:properties -version 2>&1 > /dev/null | grep 'java.home' 
    java.home = /Library/Java/JavaVirtualMachines/jdk1.8.0_74.jdk/Contents/Home/jre

Now set it in `~/.bashrc`:

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_74.jdk/Contents/Home/jre
    export PATH=$JAVA_HOME/bin:$PATH

### Installing Clojure

Now you can install with my least favourite way of installing things...homebrew:

    brew install clojure/tools/clojure

### Editors and Build Tools

Check the [editors and tools page](https://clojure.org/community/tools)

I decided to use Visual studio code and I will install calva if I need it.

Then for depency management I will use [`clj` and `deps.edn`](https://clojure.org/guides/deps_and_cli) simply because it was the first on the list.

### Clojure CLI

You use the clojure CLI for:

* Running an interactive REPL (Read-Eval-Print Loop)
* Running Clojure programs
* Evaluating Clojure expressions

You will want to use clojure or java library - called `deps` for dependencies

To use a library you need to:

1. specify name and version of the library you want to use
2. Getting it (once) from the git or maven repositories to your local machine
3. Making it available on the JVM classpath so Clojure can find it while your REPL or program is running

Clojure tools specify a syntax and file for this: `deps.edn`

### Starting a REPL (Read Eval Print Loop)

Type `clj`:

    $ clj
    Clojure 1.10.3
    user=> 

Now get the sum of 5 and 2:

    user=> (+ 5 2)
    7

Exit the `repl` with `Ctrl-D`.

To use a dependency like `clojure.java-time` you must declare it in a `deps.edn` file:

    {:deps
     {clojure.java-time/clojure.java-time {:mvn/version "0.3.2"}}}

Restart the `repl` and the library will download:

    $ clj
    Downloading: clojure/java-time/clojure.java-time/0.3.2/clojure.java-time-0.3.2.pom from clojars
    Downloading: clj-tuple/clj-tuple/0.2.2/clj-tuple-0.2.2.pom from clojars
    Downloading: clojure/java-time/clojure.java-time/0.3.2/clojure.java-time-0.3.2.jar from clojars
    Downloading: clj-tuple/clj-tuple/0.2.2/clj-tuple-0.2.2.jar from clojars
    Clojure 1.10.3
    user=> (require '[java-time :as t])
    nil
    user=> (str (t/instant))
    "2021-06-20T11:13:21.824Z"

### Writing a Program

BY default `clojure` looks for source code in the `src` directory.

Create `hello.clj`:

    (ns hello
    (:require [java-time :as t]))

    (defn time-str
    "Returns a string representation of a datetime in the local time zone."
    [instant]
    (t/format
        (t/with-zone (t/formatter "hh:mm a") (t/zone-id))
        instant))

    (defn run [opts]
    (println "Hello world, the time is" (time-str (t/instant))))

the program has an entry function called `run` executed with:

    $ clj -X hello/run
    Hello world, the time is 01:23 PM







## Sources

* [Find Java Home](https://www.baeldung.com/find-java-home)
* [Setting java home](https://docs.oracle.com/cd/E19182-01/821-0917/inst_jdk_javahome_t/index.html)