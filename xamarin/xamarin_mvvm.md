# Xamarin MVVM

1. Create `Portable Class Library` don't create `Shared Project` as that doesn't allow dependency injection

## Folder Structure

MVVM
-> MVVM (Shared / Portable) [View Models]
-> MVVM.Droid
-> MVVM.IOS
-> MVVM.Windows (Just remove this now)
-> MVVM.Services (Create this folder and everything below)
---> Implemenation
---> Intefaces
---> Stubes

On each platform(Android, iOS, Shared) right click packagesRight click on Packages -> Add Package

JSON.net (Add only where you need -> Services)
MVVM Light Libraries Only (Add to MVVM, MVVM.Droid, MVVM.iOS)
