# Android could not resolve error

If you are sure there are no spelling errors in your dependency and that the project is hosted at the correct repo then most likely the issue is `gradle`

Often you will get an error like `failed to resolve ...`

Which may make it `Unable to compile` on Android Studio 2 and sometimes Android studio 1.

Sometimes you might also get an error like `peer not authenticated`

## The solution

1. Change `distributionUrl` in `gradle-wrapper.properties` to the [latest gradle](https://services.gradle.org/distributions/)

2. Run gradle wrapper task from command line

```
cd ~/AndroidStudioProject/myproject/ myapp
./gradlew tasks
```

### Sources:

- [Unable to import android library via gradle](https://github.com/PhilJay/MPAndroidChart/issues/1426)
- [Jitpack.io failed to resolve github repo](http://stackoverflow.com/questions/33058358/jitpack-io-failed-to-resolve-github-repo)
