# Multiple-Face-Recognition-in-Videos
Using Deep Learning for Multiple Face Recognition (Face Detection + Face Tagging)

# Requirements
You need to install `pillow`,`dlib` and `face-recognition` libraries. To install them on you windows, follow the codes bellow in cmd.
```bash
pip install pillow
pip install cmake
pip install dlib
pip install face-recognition
```
Make sure that you have Visual Studio 2015 (or newer) on your windows.

# How to use
After installation of requirements, make folders whose name is the name of people. Put as many photos as you want in the folders and copy all of them in the `People` folder.
 Run `Face Encoding.py` to encode images into `encoded_people.pickle` and then, you can run either `Face Recognition Image.py` or `Face Recognition Webcam.py` based on your work.
 Whenever you need to add a new person or add new images to an encoded person, it would be enough to run `Add new person to trained data.py`
![Multiple Face Detection](https://i.imgur.com/XyLMQOB.jpg)

# Features
##### Detect Multiple Faces in a photo
By using hog algorithm in face-recognition library, the function is able to detect as many faces as possible.
![Multiple Face Detection](https://i.imgur.com/WoUIa3X.jpg)

##### Learning Phase
You can enter the name of unknown faces detected in the photos
![Learning Phase](http://uupload.ir/files/ej1w_3121321.jpg)
##### Webcam and Video Face Detection

# Features To do
- calculate the similarity of faces between given radius r1 and r2.
 
# Useful Sources
https://medium.com/@fenjiro/face-id-deep-learning-for-face-recognition-324b50d916d1

https://towardsdatascience.com/face-recognition-for-beginners-a7a9bd5eb5c2

http://devfun-lab.com/1214

https://www.vippng.com/preview/hmxhxhi_face-recognition-system-works/

http://drrajivdesaimd.com/2018/12/03/facial-recognition-technology/

https://theaseanpost.com/article/using-facial-recognition-tech-combat-terrorism-0

https://www.facefirst.com/blog/face-detection-vs-face-recognition/

https://sureshmaidaragi.blogspot.com/2018/01/face-recognition-in-android-using.html

# Sample Image
![Sample image for Face Recognition](http://drrajivdesaimd.com/wp-content/uploads/2018/10/multiple-fr.jpg)
