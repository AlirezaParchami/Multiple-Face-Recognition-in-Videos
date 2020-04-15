import PIL.Image
import PIL.ImageDraw
import face_recognition
import os
import pickle

## Requirements
dir = os.getcwd()
people = dict()

people_dir = dir + '/people/'
for person in os.listdir(people_dir):
    print(person)
    person_dir = people_dir + person + '/'
    person_faces = list() #list of detected faces for the person
    print("Number of photos:", len(os.listdir(person_dir)))
    for photo in os.listdir(person_dir):
        image = face_recognition.load_image_file(person_dir + photo)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0: #it would be possible that no faces are found in a photo
            person_faces.append(face_encodings[0])
    name = person
    if len(person_faces) == 0:
        print("No faces were found.")
    else:
        print("Detected Faces from ",person,": ",len(person_faces))
        people[name] = person_faces

# Pickling (serializing) a dictionary into a file
with open('encoded_people.pickle', 'wb') as filename:
    pickle.dump(people, filename)