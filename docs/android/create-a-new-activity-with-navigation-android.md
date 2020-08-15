---
author: ''
category: Android
date: '2015-02-13'
summary: ''
title: Create A New Activity With Navigation Android
---
#How to create a New Android Activity with Up Navigation

1. Create a New Blank Activity

2. Create a Link to the New Activity

```
public void gotoNewActivity(View v){
	Intent intent = new Intent(this.NewActivity.class);
	startActivity(intent);
}
```

3. Add a click Listener to the button/menu item to run the `gotoNewActivity` or add the onCLick in the `xml` layout:

```
xml (activity_main.xml): 

android:onClick="gotoNewActivity"

Listener (MainActivity.java):

Button button= (Button) findViewById(R.id.buttonId);
button.setOnClickListener(new View.OnClickListener() {
	    @Override
		    public void onClick(View v) {
				        gotoNewActivity();
						    }
});
```

4. CreateUp Navigation

- Make the Activity a Child of Main:

**AndroidManifest.xml**:

```
<Activity ....
	<meta-data
		android:name="android.support.PARENT_ACTIVITY"
		android:value="com.example.myApp.MainActivity" />
```

- Add UpAction 

**NewActivity.java <OnCreate>:**

```
getActionBar().setDisplayHomeAsUpEnabled(true);
```

- Handle the Click

**NewActivity.java: OnOptionsItemSelected...:**

```
NavUtils.navigateUpFromSameTask(this);
return true;
```

**Note: Activity must extend from Activity and not ActionBarActivity***
[Source](http://developer.android.com/training/implementing-navigation/ancestral.html)


