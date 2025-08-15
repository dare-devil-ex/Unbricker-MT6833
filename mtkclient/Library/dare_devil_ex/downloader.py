# Authour: dare_devil_ex

try:
    from wget import download as wkaie
    from os import system as s
except:
    s("pip intall wget")

s("cls")
banner = "𝓓𝓞𝓦𝓝𝓛𝓞𝓐𝓓𝓔𝓡"
evergreenBanner = "ᴇᴠᴇʀɢʀᴇᴇɴ ɢʟᴏʙᴀʟ ʀᴏᴍ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.."
evergoBanner = "ᴇᴠᴇʀɢᴏ ɢʟᴏʙᴀʟ ʀᴏᴍ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.."

class downloader:
    def wkaiedl(hw):
        print("=======================================")
        print(banner, "⬇️")
        print("=======================================")
        if hw == 1:
            print(evergoBanner)
            godownload = "https://cdnorg.d.miui.com/OS1.0.1.0.TGBINXM/evergo_in_global_images_OS1.0.1.0.TGBINXM_20240307.0000.00_13.0_in_bab47e0b8a.tgz"
            wkaie(godownload)
        if hw == 2:
            print(evergreenBanner)
            greendownload = "https://cdnorg.d.miui.com/OS1.0.1.0.TGBMIXM/evergreen_global_images_OS1.0.1.0.TGBMIXM_20240226.0000.00_13.0_global_e1e9e4ff66.tgz"
            wkaie(greendownload)