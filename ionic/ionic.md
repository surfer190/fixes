## Hybrid mobile applications with Ionic Framework

#### Introduction

Open source frontend SDK (Standard Development Kit - Tools to develop) to develop hybrid mobile applications with web technologies

It is a web app run within a **native web view component** which has access to the **native API**'s, it is then compiled into the native app. The ionic framework provides lookalike native components.

Ionic is built on top of **Apache Cordova**, an open source framework allowing developers to access native device functions eg. camera, accelerometer from JS.

#### Knowledge requirements

- HTML5
- CSS
- JS
- Angular

#### Setting up Environment

- (Install node js)[https://nodejs.org/en/download/]
- (Install git)[https://git-scm.com/]
- Install Cordova

  ```
  sudo npm install -g cordova
  cordova -v
  ```

- Install Ionic

  ```
  sudo npm install -g ionic
  ionic -v
  ```

- Install native mobile SDK's
  - for iOS you need [Xcode](https://developer.apple.com/xcode/)
    - Install Command line tools: `Xcode -> preferences -> Downloads -> Command Line Tools`
    - iOS Simulator: `sudo npm install -g ios-sim`
    - iOS Deploy: `sudo npm install -g ios-deploy`
    - Provision phone for development - sign up as apple developer (**$99 a month fee** Madness!!)
  - for android you need [Android SDK](http://developer.android.com/sdk/index.html) just need SDK android studio application is not required
    - Add the extracted folder `tools` and `platform-tools` to your bash path
    - Check by running `android` in terminal - should open the Android SDK Manager
    - Minimum requirements:
      - Android SDK Tools
      - Android SDK platform-tools
      - Android SDK build-tools
      - SDK Platform (Any android version preferably the latest stable)





#### Source

(Hybrid Mobile App Development with Ionic)[http://shop.oreilly.com/product/0636920046141.do]
