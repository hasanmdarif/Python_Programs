# this program takes input as dictionary and converts that data into QRcode which is saved in current directory
import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = {}
while True:
    ans = input("want to add items?(y/n)")
    if ans == "y":
        new_key = input("name of key : ")
        new_value = input("value : ")
        data[new_key] = new_value
    else:
        break
final_data = ""
for key, value in data.items():
    final_data += str(key) + " : " + str(value) + "\n"
print(final_data)
name = input("Give name to image : ")
qr.add_data(final_data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("{}.png".format(name))
