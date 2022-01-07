import requests

apiString = "https://api.lyrics.ovh/v1/"

davidoSongList = ["FEM", "Jowo", "Something Fishy", "Heaven", "The Best", "Holy Ground", "Tanana", "So Crazy", "Ekuro",
            "All of You", "Dami Duro", "Risky", "Fall", "One Thing", "Assurance", "Check Am", "If", "Get to You",
            "Company", "Green Light Riddim", "Blow My Mind", "1 Milli", "I Got A Friend", "Fade", "La La",
            "Very Special", "Mary Jane", "Gbon Gbon", "Video", "Back When", "No Visa", "Down", "Aye",
            "Sade", "Overseas", "Bless Me", "Sunlight", "MeBe", "On My Way", "Disturbance"]

wizkidSongList = ["Sweet Love", "Come Closer", "Nobody", "Picture Perfect", "Sexy", "Reckless", "Ginger", "Mighty Wine",
                  "No Stress", "Essence", "Gyrate", "Grace", "Sweet One", "Mood", "Steady", "Anoti", "Ojuelegba",
                  "On Top Your Matter", "In My Bed", "Kind Love", "Show You The Money", "Daddy Yo", "Omalicha", "Bombay",
                  "One Question", "Joy", "Caro", "Mummy Mi", "Roma", "Celebrate", "Ki Lo Fe",
                  "Love My Baby", "Gidi Girl", "Scatter the Floor", "Pakurumo", "Say My Name", "What You Wanna Do?",
                  "Shout Out", "Soco", "Naughty Ride"]

# with open("davido_lyrics.txt", "w") as f:
#     for song in davidoSongList:
#         davidoResponse = requests.get(apiString+"Davido/"+song)
#         f.write(davidoResponse.text+"\n")

# with open("wizkid_lyrics.txt", "w") as f:
#     for song in wizkidSongList:
#         wizkidResponse = requests.get(apiString+"Wizkid/"+song)
#         f.write(wizkidResponse.text+"\n")
