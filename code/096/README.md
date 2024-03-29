Do you ever work with binary data? 🐍

I've only done it once, myself. I didn't even understand what I was doing with the struct.unpack command. I just made it return the values I was reading off an IoT device according to docs 😂

Today I saw this example about reading data within a shapefile. For the uninitiated, in GIS circles we still use this shapefiles standard which is an assortment of multiple files that describe a geography (shape). The shp file is a binary object that encodes a lot of information about the geometry. So if we can tap directly into that, we should be able to parse useful information. If we know what we're looking for! 🙌

In the example I saw, the bounding box, which are the coordinates that describe a box encompassing the shape defined, comes in the format (min_x, min_y, max_x, max_y). As it turns out, this is 36 bytes into the file and stored as the next 4 sequence of 8-byte floats. So let's ... unpack this 😆

The python struct library allows us to specify this little eldian format as "<d", an 8-byte float. Obvious, no? 

So we need to ensure we read 8 bytes from the file to give it the full float information. The struct.unpack function will return a tuple of values, even if it's only one value; in the first block, I read these coordinates separately. 

But can we do better? Let's explore!

In the second block, my format can specify that I'm reading a sequence of 4 8-byte floats, and after seeking to the offset, I pass in that appropriate 8*4 byte buffer. Bam! The whole bounding box is returned 💪

The struct library has a couple more methods though! Let's keep going 🫣

The unpack_from function will take a buffer and read from a given offset. So basically I can do the 2nd block all in one go, no separate seeking. However, I define my buffer as that 4*8 bytes plus the offset. Then unpack_from I tell it to ignore that offset amount. So, not really any better than our 2nd block. But good to know!

Lastly, I explore the iter_unpack. This is nice because it returns me an iterable object, probably as a generator, I would hope. In this case, I seek to my offset and create a buffer for the bounding box equal to 4*8 bytes. Then I create my iterable by specifying each item of this "list" will be an 8-byte float via "<d". For consistency, I use a tuple comprehension to pull out the value from the single-item tuple each value is returned as, like in the first block. 

So there you have it, a quick exploration into stepping through a binary file and unpacking some bytes in a meaningful way using a GIS shapefile. How else might we have explored this? Let me know in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://lnkd.in/gZdWHmjH
------

<img src="../../static/0096.png" />

