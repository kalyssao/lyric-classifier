import pickle
import string
import pandas as pd


def preprocessLyric(lyric):
    sans_punctuation = lyric.translate(str.maketrans("", "", string.punctuation))
    lower = sans_punctuation.lower()

    lyric_df = pd.DataFrame([lower], columns=["lyric"])

    with open("vectorizer", "rb") as f:
        vectorizer = pickle.load(f)

    vectorized = vectorizer.transform(lyric_df)
    return vectorized


def predictGivenLyric(lyric):
    preprocessed_lyric = preprocessLyric(lyric)
    loaded_model = pickle.load(open("svm_model", "rb"))

    result = loaded_model.predict(preprocessed_lyric)
    if result == 0:
        print("Davido") # do davido processing here
    else:
        print("Wizkid") # send Davido
