import pickle


def preprocessLyric(lyric):
    return lyric


def predoctGivenLyric(lyric):
    preprocessed_lyric = preprocessLyric(lyric)
    loaded_model = pickle.load(open("lyric_classifier.sav", "rb"))

    result = loaded_model.predict(preprocessed_lyric)
    if result == 1:
        print("Davido") # do davido processing here
    else:
        print("Wizkid") # send Davido
