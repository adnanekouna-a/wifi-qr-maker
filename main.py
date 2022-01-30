import qrcode

def wifi_to_qrcode(ssid: str, security: str, password: str, is_hidden: bool) -> str:
    "Takes the information about a Wi-Fi network and returns a formatted string compatible with QR code"
    return f"WIFI:S:{ssid};T:{security};P:{password};H:{str(is_hidden).lower()};;"

if __name__ == "__main__":
    print("Welcome to Wi-Fi QR Maker (Version 1.0.0) : ")
    ssid = input("What's your network's SSID? (case sensitive) : ")
    passwd = input("What's the password to your network? (case sensitive) : ")
    
    is_hidden = False
    while True:
        try:
            visibility = input("Is your network hidden ? [y/N] : ").upper()
            if visibility not in ["","Y","N"]:
                raise ValueError
            elif visibility == "Y":
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

    img = qrcode.make(wifi_to_qrcode(ssid, security_type, passwd, is_hidden))
    img.save('temp.png')



