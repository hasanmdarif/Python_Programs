import pyqrcode, sys
from pathlib import Path

# python3 py_qrcode.py your_text output_name
# example
# python3 qr_code.py i love my mom family
# the output is family.png

try:
    if len(sys.argv) > 1:
        output_location = Path(__file__).parent.absolute()
        if len(sys.argv) > 3:
            text = ''
            for i in range(1, len(sys.argv) - 1):
                text += sys.argv[i] + ' '
            generate_code = pyqrcode.create(text)
            generate_code.png("{}.png".format(sys.argv[len(sys.argv) - 1]), scale=10)
            print('\noutput path : {}/{}.png'.format(output_location, sys.argv[len(sys.argv) - 1]))
        else:
            generate_code = pyqrcode.create(sys.argv[1])
            generate_code.png("{}.png".format(sys.argv[len(sys.argv) - 1]), scale=10)
            print('\noutput path : {}/{}.png'.format(output_location, sys.argv[len(sys.argv) - 1]))
    else:
        print('Run this program by following this rules\npython3 py_qrcode.py "your text" "output name"')
except:
    print('Run this program by following this rules\npython3 py_qrcode.py "your text" "output name"')