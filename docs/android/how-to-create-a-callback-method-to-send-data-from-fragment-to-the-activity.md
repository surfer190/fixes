---
author: ''
category: Android
date: '2015-05-29'
summary: ''
title: Creating a Callback to Send Data From Fragment to Activity
---
# How to Implement a Callback Method to Send Data from a Fragment to an Activity

1. In the Fragment Class (MyFragment.java):

	Declare an Interface with as many abstract methods as required

        public interface Callbacks {
            public void runAbstractMethod(MyData mydata);
        }

	**Remember only signiture is required for an interface**

2. In the Activity Class:

    Add Code to the class declaration to Implment the Interface in the Fragment class

        public class MainActivity extends Activity
            implements MyFragment.Callbacks {

    Implement the methods (Alt + Enter) creates.

        @Override
        public void runAbstractMethod(MyData mydata){
            //Get a reference to the bundle representing all of the MyData objects data
            //Uses a custom method of the MyData Class
            Bundle b = mydata.makeBundle();
            //or if your class implements serializable you can use
            b.putSerialiazble("myData", (java.io.Serializable) mydata);

            //Create an Intent to Launch the Activity
            Intent intent = new Intent(this, MyDataActivity.class);
            intent.putExtra("MY_KEY", b);
            //Want to See a Result so use
            startActivityForResult(intent, "100");
        }

3. Setup Communication from Fragment to Actviity

	In Fragment Class (**MyFragment.java**):

	#### Get a reference to the Activity Class

	```
	//Declare a variable as an Implementation of the Callbacks Interface
	private Callbacks activity;

	//Override the OnAttach method
	public void onAttach(Activity activity){
		super.onAttach(activity);
		this.activity = (Callbacks)activity;
	}
	```

	#### Run the Method:

	```
	//Use a Click Listener or Some event
	public void RuntheMethod(){
		//Setup the data
		MyData mydata = ....

		//Run the Method
		activity.onItemSelected(mydata);
	}
	```

	**Make sure the Activity is registered in the Manifest File**

4. Receive Bundle from MainActivity in New Activity and pass to fragment

	In **MyDataActivity.java**:

        MyFragment fragment = new MyFragment();
        //after instantiating the fragment class
        Bundle args = getIntent().getBundleExtra("MY_KEY");
        fragment.setArguments(args);

        //use fragement manager and send it

5. Receive Arguments - in Fragments `OnCreate`

	In **MyFragment.java**:

    public void OnCreate(Bundle savedInstanceState){
        super.onCreate(savedInstance);

        bundle b = getArguments();
        if (b != null){
            MyData mydata = new Flower(b);
        }   

## Sources

* [Lynda Building Adaptive Android Apps with Fragments](https://www.linkedin.com/learning/building-flexible-android-apps-with-the-fragments-api-with-java/understanding-fragments)
