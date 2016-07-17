#!/usr/env python

from util import readlines


def write_bow(v, path):
  f = open(path, "w")
  for i in v:
    f.write(i[0] + "\n")
  f.close()


lines = readlines("data/vocabulary.csv")[1:]

splitted = list(map(lambda l : l.split(";"), lines))

ge_std = list(map(lambda s : (s[0], float(s[2])), splitted))
co_std = list(map(lambda s : (s[0], float(s[3])), splitted))

ge_std.sort(key = lambda x : x[1], reverse = True)
co_std.sort(key = lambda x : x[1], reverse = True)


write_bow(ge_std[0:1000], "data/bow_gender")
write_bow(co_std[0:1000], "data/bow_country")

