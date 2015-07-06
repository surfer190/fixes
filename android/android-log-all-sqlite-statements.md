## Log All SQLite statements in Android ADB

```
adb shell setprop log.tag.SQLiteLog V

adb shell setprop log.tag.SQLiteStatements V

adb shell stop

adb shell start
```
