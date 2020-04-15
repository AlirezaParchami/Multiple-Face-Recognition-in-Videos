import cv2
import pickle
import face_recognition
import PIL
import PIL.ImageFont
import PIL.ImageDraw
import numpy as np
import time
font = PIL.ImageFont.truetype("Acme____.ttf", 20)

with open('encoded_people.pickle', 'rb') as filename:
    people = pickle.load(filename)
print("Data loaded successfully")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    start_time = time.time()
    scaleFactor = 4
    small_frame = cv2.resize(frame, (0, 0), fx=1/scaleFactor, fy=1/scaleFactor)
    rgb_small_frame = small_frame[:,:,::-1]
    # Find all the faces and face encodings in the current frame of video
    img_loc = face_recognition.face_locations(rgb_small_frame,model="hog")
    img_enc = face_recognition.face_encodings(rgb_small_frame, known_face_locations=img_loc)

    face_img = PIL.Image.fromarray(frame)

    for i in range(0, len(img_enc)):
        for k, v in people.items():
            result = face_recognition.compare_faces(v, img_enc[i], tolerance=0.5)
            if True in result:
                top, right, bottom, left = np.multiply(img_loc[i], scaleFactor)
                draw = PIL.ImageDraw.Draw(face_img)
                draw.rectangle([left, top, right, bottom], outline="red", width=2)
                draw.text((left, bottom), k, font=font)

    # Display the resulting frame
    open_cv_image = np.array(face_img)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, :].copy()
    cv2.imshow('frame',open_cv_image)
    print("--- %s seconds ---" % (time.time() - start_time))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()