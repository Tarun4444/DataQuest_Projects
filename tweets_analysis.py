import csv
import numpy as np
import pandas as pa

def get_candidate(row):
    candidates=[]
    text=row["text"].lower()

    if "clinton" in text or "hillary" in text:
        candidates.append("clinton")
    if "trumph" in text or "donald" in text:
        candidates.append("trumph")
    if "sanders" in text or "bernie" in text :
        candidates.append("sanders")

    return ",".join(candidates)

f=open("tweets.csv","r")
tweets = list(csv.reader(f))
#tweets = np.genfromtxt('tweets.csv',delimiter=',',skip_header=1)
tweets

