---
author: ''
category: Android
date: '2015-05-15'
summary: ''
title: Check Your Key Hash Android
---
#How to Check your Key Hash for Facebook

Because generation of the Key hash using the commandline sometimes does not work or works only the first time.

```
keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore | openssl sha1 -binary | openssl base64

Password is: android

```

Use the following code, in an activity. It should output to `Logcat`

```
        PackageInfo info = null;
        try {
            info = getPackageManager().getPackageInfo(getPackageName(),  PackageManager.GET_SIGNATURES);
        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }

        for (Signature signature : info.signatures)
        {
            MessageDigest md = null;
            try {
                md = MessageDigest.getInstance("SHA");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
            md.update(signature.toByteArray());
            Log.d("KeyHash:", Base64.encodeToString(md.digest(), Base64.DEFAULT));
        }
```

Also if you get an error similar to this when Logging your session and state variables:

```
{Session state:CLOSED_LOGIN_FAILED, token:{AccessToken token:ACCESS_TOKEN_REMOVED permissions:[]}, appId:131***64547}
```

Make sure you have this code:

```
@Override
public void onActivityResult(int requestCode, int resultCode, Intent data) {

    super.onActivityResult(requestCode, resultCode, data);

    Session.getActiveSession().onActivityResult(this, requestCode, resultCode, data);

}
```

Source: http://stackoverflow.com/questions/23046136/facebook-login-fails-session-stateclosed-login-failed-tokenaccesstoken-tok/23047317#23047317
http://stackoverflow.com/questions/21851575/session-stateopening-tokenaccesstoken-tokenaccess-token-removed-permission
https://developers.facebook.com/docs/android/getting-started/
