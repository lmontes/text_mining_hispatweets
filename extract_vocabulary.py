#!/usr/env python

import statistics
from nltk.tokenize import TweetTokenizer
from util import readlines, stripaccents
import time

tokenizer = TweetTokenizer()


start_time = time.time()
lines = readlines("data/train_tweets")
read_time = time.time()

print(read_time - start_time)

count = {}

for l in lines:
    parts = l.split(" ")

    if len(parts) > 2:
        gender = parts[0]
        country = parts[1]
        tweet = " ".join(parts[2:-1])
    
        words = tokenizer.tokenize(stripaccents(tweet))
    
        for w in words:
            if w not in count:
                count[w] = dict()
            
            if gender in count[w]:
                count[w][gender] = count[w][gender] + 1
            else:
                count[w][gender] = 1
                    
            if country in count[w]:
                count[w][country] = count[w][country] + 1
            else:
                count[w][country] = 1

tokenize_time = time.time()
print(tokenize_time - read_time)


gender_keys = ["male", "female", "UNKNOWN"]
country_keys = ["argentina", "chile", "colombia", "espana", "mexico", "peru", "venezuela"]
keys = gender_keys + country_keys
n_keys = len(keys)

f = open("data/vocabulary.csv", "w")

f.write("word;total;ge_std;co_std;male;female;unknown;ar;cl;co;es;mx;pe;ve\n")

for w in count.keys():
    i = 0
    total = 0
    counts = [0]*n_keys

    for k in gender_keys:
        if k in count[w]:
            counts[i] = count[w][k]
            total += count[w][k]
        i = i + 1

    # Cuidado antes era 100
    if total < 500:
        continue

    for k in country_keys:
        if k in count[w]:
            counts[i] = count[w][k]
        i = i + 1

    gender_std = statistics.stdev(counts[0:3])
    country_std = statistics.stdev(counts[3:n_keys])

    line = w + ";" + str(total) + ";" + "{0:.3f}".format(gender_std) + ";" + "{0:.3f}".format(country_std)
    
    for k in counts:
        line += ";" + str(k)    
        
    f.write(line + "\n")

f.close()

generate_time = time.time()
print(generate_time - tokenize_time)
