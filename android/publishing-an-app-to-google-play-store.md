#How to Publish and Android App to the App Store

1. In Android Studio select `Build->generate signed apk...`

2. This will create a file called `app-release-unaligned.apk` in `app/build/outputs/apk`

You will need to `zipalign`:

```
android-sdk/build-tools/22.0.1/zipalign -f -v 4 <app-release-unaligned.apk> <app-release.apk>
```

Review Permission: [Android Permissions List](http://developer.android.com/reference/android/Manifest.permission.html)
