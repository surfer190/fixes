---
author: ''
category: Android
date: '2015-09-13'
summary: ''
title: Android Improving Performance With Images In Memory
---
#Android Reduce Heap Space of Images

The Dalvik version of android garbage collector is non-compacting, as objects are freed other objects will not be shuffled around to optimize for free space.

A large problem for bitmaps, usually the largest continuous blocks allocated in your app.
Allocations for bitmaps can fail because there is not enough continuous free space for the bitmap which kicks off garbage collection to free up memory or call an  out of memory exception.

Compressed image formats need to be decompressed into a readable format, so once they are loaded they are not compressed.
Loaded by default with 32 bits per pixel. 8 bits per channel. Even if you are loading an image without alpha.
Android does not support 24 bit pixel formats.

Before rendering to the screen, the bitmap needs to be sent to the GPU as textures.
So images take up CPU memory and GPU memory.

Alternate pixel formats supported by android

```
ARGB_8888 : 32 bits per pixel
RGB_565 : 16 bits per pixel - No alpha channel
ARGB_4444 : 16 bits per pixel - Has alpha, cuts bits per pixel in half. Perfect for thumbnails with alpha.
ALPHA_8 : 8 bits per pixel
```
PNG, JPG, WEBP don't support the above as part of basic file structure.

So you have to set the `inPreferredCOnfig` flag:

```
mBitmapOptions = new BitmapFactory.Options();

mBitmapOptions.inPreferredConfig = Bitmap.Config.RGB_565;

BitmapFactory.decodeResource(getResources(), R.drawable.firstBitmap, mBitmapOptions);
```

Source: [Google Developers](https://www.youtube.com/watch?t=232&v=1WqcEHXRWpM)
