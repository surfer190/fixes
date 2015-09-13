# Installing Android Studio and Setting up your Environment for Android Development

1. Install Java 
  * OpenJDK (Java Standard Edition consisting of the VM? Java Class Library and the Java Compiler `javac`)
  * OpenJRE (JVM - Java Virtual Machine and Java core classes and libraries)

  ```
  sudo apt-get install openjdk-7-jre openjdk-7-jdk
  ```

  Check that your java  version is `1.7.XXXX`

  ```
  javac -version
  ```

2. Download and Install Android Studio

  [Link to Download Android Studio](https://developer.android.com/sdk/index.html)

3. Untar the downloaded folder to your required location:

   ### If you downloaded just the SDK:

  `tar zxvf android-sdk_r24.3.4-linux.tgz -C ~/utils`

   ### If you downloaded the whole package:

  `unzip android-studio-ide-141.2135290-linux.zip -d ~/utils

4. Add Android Studio Bin to Path

  `vim ~/.bashrc`

  `#Add Android Studio to Path
   PATH=$PATH:/home/stephen/utils/android-studio/bin/
   export PATH`

5. Run Android Studio

  `bash ~/android-studio/bin/studio.sh`
