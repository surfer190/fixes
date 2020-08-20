---
author: ''
category: Android
date: '2016-03-26'
summary: ''
title: Publishing An App To Google Play Store
---
#How to Publish and Android App to the App Store

1. In Android Studio select `Build->generate signed apk...`

2. This will create a file called `app-release-unaligned.apk` in `app/build/outputs/apk`

You will need to `zipalign`:

```
android-sdk/build-tools/22.0.1/zipalign -f -v 4 <app-release-unaligned.apk> <app-release.apk>
```

## Make sure Version is updated

You need to update your `versionCode` and `versionName`

If you are using `gradle` you can set this in `app/build.gradle` instead of `AndroidManifest.xml`

```
defaultConfig {
        versionCode 6
        versionName "1.0.5"
    }
```

Review Permission: [Android Permissions List](http://developer.android.com/reference/android/Manifest.permission.html)
