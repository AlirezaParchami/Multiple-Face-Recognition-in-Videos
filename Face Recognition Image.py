import pickle
import face_recognition
import PIL
import PIL.Image
import PIL.ImageFont
from PIL import ImageOps
import PIL.ImageDraw
from tkinter import filedialog
from tkinter import *
import math

with open('encoded_people.pickle', 'rb') as filename:
    people = pickle.load(filename)

print("File Selection")
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(root.filename)
root.destroy()

print("Face Detection")
img = face_recognition.load_image_file(root.filename)
img_loc = face_recognition.face_locations(img, model="hog")
img_enc = face_recognition.face_encodings(img, known_face_locations=img_loc)
face_img = PIL.Image.fromarray(img)
face_img.copy().crop()
print("Face Tagging")
unknown_faces_location = []
unknown_faces_enconded = []
for i in range(0,len(img_enc)):
    best_match_count = 0
    best_match_name = "unknown"
    for k,v in people.items():
        result = face_recognition.compare_faces(v,img_enc[i],tolerance=0.5)
        count_true = result.count(True)
        if  count_true > best_match_count: # TO find the best person that matches with the face
            best_match_count = count_true
            best_match_name = k
    top,right,bottom,left = img_loc[i]
    draw = PIL.ImageDraw.Draw(face_img)
    draw.rectangle([left,top,right,bottom], outline="red", width=3)
    draw.text((left,bottom), best_match_name, font=PIL.ImageFont.truetype("Acme____.ttf", math.floor((right-left)/8)))
    if best_match_count == 0:
        unknown_faces_location.append(img_loc[i])
        unknown_faces_enconded.append(img_enc[i])
face_img.show()

if len(unknown_faces_enconded) > 0:
    print("There are ", len(unknown_faces_enconded), "unknown person(s) in the photo. Would you like to enter their information? (Y|N)")
    if input().lower()in ['y','yes']:
        print("Press Enter (empty name) if you do not know the person")
        for i in range(0,len(unknown_faces_location)):
            top, right, bottom, left = unknown_faces_location[i]
            roi =face_img.copy().crop([left,top,right,bottom])
            roi.show()
            name = input("Who is this person? ")
            if name in people:
                tmp = people[name]
                tmp.append(unknown_faces_enconded[i])
            elif name:
                print(name)
                people[name] = [unknown_faces_enconded[i]]
                #a = ImageOps.crop(face_img, unknown_faces_location[i])
                #a = PIL.Image.fromarray(a)
                #a.crop()
        with open('encoded_people.pickle', 'wb') as filename:
            pickle.dump(people, filename)
