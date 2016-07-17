#!/usr/env python

from nltk.tokenize import TweetTokenizer
from util import readlines, stripaccents
import time
import re


re_laugh = re.compile(".*j[aeiou]j.*")

def is_laugh(word):
    return re_laugh.match(word)

def generate_samples(samples, bow, outputfile, classposition):
    start_time = time.time()
    tokenizer = TweetTokenizer()
    bow_len = len(bow)

    i = 0
    bow_index = {}
    for w in bow:
        bow_index[w] = i
        i = i + 1

    f = open(outputfile, "w")

    for l in samples:
        parts = l.split(" ")

        bow_line = [0]*bow_len

        if len(parts) > 2:
            tweet = " ".join(parts[2:-1])
        
            words = tokenizer.tokenize(stripaccents(tweet))
            
            total_words = 0
            total_hashtags = 0
            total_mentions = 0
            total_laughs = 0
        
            for w in words:
                if w in bow_index:
                    bow_line[bow_index[w]] = bow_line[bow_index[w]] + 1
                    
                total_words += 1
                
                if w.startswith("#"):
                    total_hashtags += 1
                    
                if w.startswith("@"):
                    total_mentions += 1

                if is_laugh(w):
                    total_laughs += 1 
                
            line = parts[classposition]
            
            # Start the line with the class name
            total = sum(bow_line)
            
            if total == 0:
                total = 1
                
            if total_words == 0:
                total_words = 1
            
            for k in bow_line:
                line += " " + str(float(k) / total)
                
            line += " " + str(float(total_hashtags) / total_words) + " " + str(float(total_mentions) / total_words) + " " + str(float(total_laughs) / total_words)

            f.write(line + "\n")

    f.close()

    tokenize_time = time.time()
    print(tokenize_time - start_time)


# Read the files
start_time = time.time()
train_samples = readlines("data/train_tweets")
test_samples = readlines("data/test_tweets")
bow_gender = readlines("data/bow_gender")
bow_country = readlines("data/bow_country")
read_time = time.time()

print("Read time: " + str(read_time - start_time))


# Generate the samples
generate_samples(train_samples, bow_gender, "data/train_ge", 0)
generate_samples(test_samples, bow_gender, "data/test_ge", 0)
    
generate_samples(train_samples, bow_country, "data/train_co", 1)
generate_samples(test_samples, bow_country, "data/test_co", 1)

