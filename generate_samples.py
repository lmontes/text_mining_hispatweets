#!/usr/env python

from nltk.tokenize import TweetTokenizer
from util import *
from features import *
import time
import re


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
        
            words = tokenizer.tokenize(tweet)
            
            total_words = 0
            total_emojis = 0
            total_hashtags = 0
            total_mentions = 0
            total_laughs = 0
            total_urls = 0
            total_numbers = 0
            total_emails = 0
            total_flooding = 0

            for wi in words:
                total_words += 1
                
                if is_emoji(wi):
                    total_emojis += 1                    
                  
                w = stripaccents(wi)

                # Si era algun tipo de simbolo que se ha eliminado no continua
                if w == "":
                    continue

                if w in bow_index:
                    bow_line[bow_index[w]] = bow_line[bow_index[w]] + 1
                    
                if is_hashtag(w):
                    total_hashtags += 1     
                if is_mention(w):
                    total_mentions += 1
                if is_laugh(w):
                    total_laughs += 1
                if is_url(w):
                    total_urls += 1
                if is_number(w):
                    total_numbers += 1
                if is_email(w):
                    total_emails += 1
                if has_character_flooding(w):
                    total_flooding += 1
                
            line = parts[classposition]
            
            # Start the line with the class name
            total = sum(bow_line)
            
            if total == 0:
                total = 1
                
            if total_words == 0:
                total_words = 1
            
            for k in bow_line:
                line += " " + str(float(k) / total)
               
            line += " " + str(float(total_emojis) / total_words)
            line += " " + str(float(total_hashtags) / total_words) 
            line += " " + str(float(total_mentions) / total_words)
            line += " " + str(float(total_laughs) / total_words)
            line += " " + str(float(total_urls) / total_words)
            line += " " + str(float(total_numbers) / total_words)
            line += " " + str(float(total_emails) / total_words)
            line += " " + str(float(total_flooding) / total_words)

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

