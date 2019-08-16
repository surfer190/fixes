# Find Java Home on Mac

How to Find Java home on mac

If `JAVA_HOME` is not set:

    echo $JAVA_HOME

then run:

    $(dirname $(readlink $(which javac)))/java_home

or do:

    java -XshowSettings:properties -version

and find `java.home`

then set that in `~/.bashrc` or profile with:

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/openjdk-12.0.1.jdk/Contents/Home

## Source

* [Baeldung: Find Java Home](https://www.baeldung.com/find-java-home)
