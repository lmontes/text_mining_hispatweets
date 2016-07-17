#!/usr/bin/env python

import json
from util import readlines

def obtain_labels(l):
    parts = l.split(":::")
    if len(parts) != 3:
        return None
    return (int(parts[0]), parts[1], parts[2])


def process_raw_data(data_dir, in_file, out_file):
    lines = readlines(data_dir + "/" + in_file)
    lines2 = list(map(obtain_labels, lines))

    country = {}
    gender = {}

    for l in lines2:
        country[l[0]] = l[1]
        gender[l[0]] = l[2]

    f = open(data_dir + "/" + out_file, "w")

    for person in gender.keys():
        filename = data_dir + "/" + country[person] + "/" + str(person) + ".json"
        tweets = readlines(filename)

        all_text = ""

        for t in tweets:
            tweetJson = json.loads(t)
            
            text = tweetJson["text"]
            text = text.replace("\n", " ")
            text = text.replace("\\n", " ")
            text = text.replace("\r", " ")
            text = text.replace("\\r", " ")
            
            all_text +=  " " + text
            
        f.write(gender[person] + " " + country[person] + " " + all_text + "\n")
            
    f.close()


process_raw_data("data", "training.txt", "train_tweets")
process_raw_data("data", "test.txt", "test_tweets")
