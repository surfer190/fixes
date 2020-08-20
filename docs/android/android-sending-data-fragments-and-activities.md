---
author: ''
category: Android
date: '2015-05-11'
summary: ''
title: Android Sending Data Fragments And Activities
---
# How to send and receive data between Fragments and Activities

### To Activities

#### Send

Use `Extras`

###### From Activity

```
Intent intent = new Intent(this, NewActivity.class);
intent.putStringExtra("EXTRA_ID", session_id);
startActivity(intent);
```
###### From Fragment
```
Intent intent = new Intent(getActivity(),
 NewActivity.class);
intent.putStringExtra("EXTRA_ID", session_id);
startActivity(intent);
```

#### Receive

```
Intent intent = getIntent();

String session_id = intent.getStringExtra("EXTRA_ID");
```

Source: [How do I pass data between activities in Android?](http://stackoverflow.com/questions/2091465/how-do-i-pass-data-between-activities-in-android)

[How to get extra data from intent in android?](http://stackoverflow.com/questions/4233873/how-to-get-extra-data-from-intent-in-android)

### Activity to Fragment

Use a `Bundle`

#### Send

```
Bundle bundle = new Bundle();
bundle.putString("BUNDLE_ID", sline);
NewFragment frag = new NewFragment();
frag.setArguments(bundle);
```

#### Receive

```
String sline = getArguments().getString("BUNDLE_ID"); ```
### Fragment to Fragment

Define an `Interface`

Source: [Communicating with Other Fragments](http://developer.android.com/training/basics/fragments/communicating.html)
