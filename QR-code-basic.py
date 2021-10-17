# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
link = "https://github.com/SohamPhansalkar"
  
# Generate QR code
qr = pyqrcode.create(link)
  
# Create and save the svg file naming "myqr.svg"
qr.svg("QR-code.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
qr.png('QR-code.png', scale = 6)
