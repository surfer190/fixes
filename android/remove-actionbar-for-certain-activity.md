# How to Remove the ACtionbar for a Certain Activity

1. Add to activity node:

```
android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
```

Full example:

```
<application
    android:allowBackup="true"
    android:icon="@drawable/lojacidadao"
    android:label="@string/app_name"
     android:theme="@style/AppTheme">
    <activity
        android:name="com.example.basicmaponline.Intro"
        android:screenOrientation="portrait"
        android:label="@string/app_name"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />

            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
```

Source: [Remove actionbar for certain activity](http://stackoverflow.com/questions/16823049/splash-screen-application-and-hide-action-bar)
