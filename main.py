import os
from dotenv.main import load_dotenv
import qrcode, pyimgur, pyperclip

def wifi_to_qrcode(name: str, security: str, password: str, hidden: bool) -> str:
    "Takes the information about a Wi-Fi network and returns a formatted string compatible with QR code"
    return f"WIFI:S:{name};T:{security};P:{password};H:{str(hidden).lower()};;"

if __name__ == "__main__":
    # Welcome message
    print("Welcome to Wi-Fi QR Maker (Version 1.0.0) : ")

    # Managing the inputs
    ssid = input("What's your network's SSID? (case sensitive) : ")
    passwd = input("What's the password to your network? (case sensitive) : ")
    
    is_hidden = False
    while True:
        try:
            visibility = input("Is your network hidden ? [y/N] : ").upper()
            if visibility not in ["","Y","N"]:
                raise ValueError
            if visibility == "Y":
                is_hidden = True
            break
        except ValueError:
            print("You should enter Y or N!")
            continue

    while True:
        try:
            security_type = input("What's your network's security type? [WEP/WPA]: ").upper()
            if security_type not in ["WEP","WPA"]:
                raise ValueError
            break
        except ValueError:
            print("Unsupported security type!\nThe supported security types are : WEP and WPA.")
            continue

    # Translating the data into a QR code
    image_name = f"{ssid}_QR.png"
    image_dir = f"QR/{image_name}"
    image = qrcode.make(wifi_to_qrcode(ssid, security_type, passwd, is_hidden))
    image.save(image_dir)
    
    # Uploading the QR code to imgur
    load_dotenv()
    auth = pyimgur.Imgur(os.environ["CLIENT_ID"])
    uploaded_image = auth.upload_image(image_dir, title=image_name)
    
    # Copying the imgur url to the clipboard
    pyperclip.copy(uploaded_image.link)
    print("The link to the QR code has been copied to your clipboard!")
