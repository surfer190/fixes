---
author: ''
category: Android
date: '2015-06-07'
summary: ''
title: Show Icons On Actionbar Not In Overflow Android
---
# Show Icons in Actionbar on Android, don't show in Overflow

1. You have to use the `AppCompat` Library ? Activity must extend `AppCompatActivity`:

    ```
    MainActivity extends AppCompatActivity
    ```

2. Make sure the theme is from `AppCompat` in **AndroidManifest.xml**:

    ```
    <activity
            android:name=".MainActivity"
            android:label="@string/app_name"
            android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        </activity>
    ```

3. Use `app:showAsAction` in **mwnu_mail.xml**:

    ```
    <menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <item android:id="@+id/action_settings"
        android:title="@string/action_settings"
        android:icon="@drawable/ic_settings_white_24dp"
        app:showAsAction="ifRoom"/>
    <item android:id="@+id/action_profile"
        android:title="@string/action_profile"
        android:icon="@drawable/ic_account_circle_white_24dp"
        app:showAsAction="ifRoom"/>
    </menu>
    ```
