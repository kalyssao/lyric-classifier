import string


def removeBrackets(file):
    with open(file+'.txt') as infile, open(file+'_processed.txt', 'w+') as outfile:
        data = infile.read()
        print("just finished reading")
        data = data.replace("{\"lyrics\":\"", "")
        data = data.replace("Paroles de la chanson", '')
        data = data.strip('\r')
        outfile.write(data)


def removeCarriageReturn(file):
    with open(file+'.txt') as infile, open(file+'_cleaned.txt', "w+") as outfile:
        for line in infile:
            line = line.replace("\\n", ' ')
            line = line.replace("\\r", ' ')
            line = line.translate(str.maketrans("", "", string.punctuation))
            outfile.write(line)


# removeBrackets("davido_lyrics")
# removeBrackets("wizkid_lyrics")

# removeCarriageReturn("davido_lyrics_processed")
# removeCarriageReturn("wizkid_lyrics_processed")
