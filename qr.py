import qrcode
import uuid
def makeQR(text):
	img = qrcode.make(text)
	n = str(uuid.uuid4())
	img.save(f'{n}.jpg')
makeQR("test")