import pickle
import os
import face_recognition
import numpy as np
dir = os.getcwd()

with open('encoded_people.pickle', 'rb') as filename:
    people = pickle.load(filename)

print("Put the photos of new person in a folder. Set the name of the folder as the person's name. Drop the folder to People Folder.")
newPersonName = input("Enter new person's name: ")

people_dir = dir + '/people/'
if not os.path.isdir(people_dir):
    print("There is no 'People' folder")
    exit(0)
if newPersonName not in os.listdir(people_dir):
    print("There is no folder with the given name in the 'People' folder")
    exit(0)

person_dir = people_dir + newPersonName + '/'
person_faces = list()
for photo in os.listdir(person_dir):
    image = face_recognition.load_image_file(person_dir + photo)
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        person_faces.append(face_encodings[0])

if len(person_faces) == 0:
    print("No faces were found.")
else:
    print(len(person_faces), "faces were founded from ", newPersonName, "in the folder.")
    if newPersonName in people:
        people[newPersonName] = people[newPersonName] + person_faces
    else:
        people[newPersonName] = person_faces

refToNewPerson = people[newPersonName]
unique_rows = np.unique(refToNewPerson , axis=0)
print(len(unique_rows),"new faces are founded.")
people[newPersonName] = [xi for xi in unique_rows]
print("There are now ",len(people[newPersonName]),"faces for ",newPersonName)

with open('encoded_people.pickle', 'wb') as filename:
    pickle.dump(people, filename)