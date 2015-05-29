* Application Class that extends from Aplication

```
public class App extends Application{

    private static Context mContext;

    @Override
    public void onCreate() {
        super.onCreate();
        mContext = getApplicationContext();
        FacebookSdk.sdkInitialize(mContext);
        //Other Initialisations
    }
}
```

Change Android name to Application node:

`android:name="App"`

```
<application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:name="App" >
```


Source: (androids application class)[http://www.intertech.com/Blog/androids-application-class/#ixzz3bQEKgI5N]
