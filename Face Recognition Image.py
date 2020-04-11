import pickle
import face_recognition
import PIL
import PIL.ImageFont
import PIL.ImageDraw
font = PIL.ImageFont.truetype("Acme____.ttf", 20)

with open('encoded_people.pickle', 'rb') as filename:
    people = pickle.load(filename)

print("Face Detection")
img = face_recognition.load_image_file("test1.jpg")
img_loc = face_recognition.face_locations(img, model="hog")
img_enc = face_recognition.face_encodings(img, known_face_locations=img_loc)

face_img = PIL.Image.fromarray(img)

print("Face Tagging")
for i in range(0,len(img_enc)):
    for k,v in people.items():
        result = face_recognition.compare_faces(v,img_enc[i],tolerance=0.5)
        print(len(result))
        print(type(result))
        if True in result:
            top,right,bottom,left = img_loc[i]
            draw = PIL.ImageDraw.Draw(face_img)
            draw.rectangle([left,top,right,bottom], outline="red", width=2)
            draw.text((left,bottom), k,font=font)
face_img.show()