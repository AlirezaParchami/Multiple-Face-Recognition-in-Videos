import PIL.Image
import PIL.ImageDraw
import face_recognition
import PIL.ImageFont
import os
import pickle

## Requirements
font = PIL.ImageFont.truetype("arial.ttf", 15)
dir = os.getcwd()
people = dict()

people_dir = dir + '/people/'
for person in os.listdir(people_dir):
    person_dir = people_dir + person + '/'
    person_faces = list()
    for photo in os.listdir(person_dir):
        print(photo)
        image = face_recognition.load_image_file(person_dir + photo)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            person_faces.append(face_encodings[0])
    name = person
    if len(person_faces) == 0:
        print("No faces were found.")
    else:
        print(len(person_faces))
        people[name] = person_faces

# Pickling (serializing) a dictionary into a file
with open('encoded_people.pickle', 'wb') as filename:
    pickle.dump(people, filename)