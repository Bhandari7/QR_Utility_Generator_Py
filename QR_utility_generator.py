import segno
from segno import helpers

#To get from qr code
#Utility-1, direct you to git profile
QR_code = segno.make_qr("https://github.com/Bhandari7")

#create a png file for QR of your utility
QR_code.save("QR_git.png")


#Utility-2, Wi-Fi configuration for your customers and guests
QR_code_wifi = segno.helpers.make_wifi(ssid="wifi_name", password="123abc", security='WPA')
QR_code_wifi.save("QR_wifi.png")
