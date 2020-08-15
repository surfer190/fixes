---
author: ''
category: Android
date: '2016-05-24'
summary: ''
title: Unable To Import Library Via Gradle
---
# Unable to import library via Gradle (Failed to resolve error)

Sometimes you will get a failed to resolve error

```
Failed to resolve: com.github.PhilJay:MPAndroidChart:v2.4.0
```

Steps I took:

Change `distributionUrl` in `gradle-wrapper.properties` to the latest gradle

Run gradle wrapper task from command line

```
cd ~/AndroidStudioProject/myproject/ myapp
./gradlew tasks
```

Profit!

#### Source:

[Unable to import library via Gradle](https://github.com/PhilJay/MPAndroidChart/issues/1426)
