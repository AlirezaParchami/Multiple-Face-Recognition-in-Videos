import PIL.Image
import PIL.ImageDraw
import face_recognition
import PIL.ImageFont
font = PIL.ImageFont.truetype("arial.ttf", 15)

image = face_recognition.load_image_file("People/Bill Gates.jpg")
face_locations = face_recognition.face_locations(image)
face_img = PIL.Image.fromarray(image)
draw = PIL.ImageDraw.Draw(face_img)
for face in face_locations:
    draw.rectangle(face,outline="red",width=2)
    draw.text((face[0],face[1]), "Name",font=font)
face_img.show()