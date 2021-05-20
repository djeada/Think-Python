"""
Exercise 6
The urllib module provides methods for manipulating URLs and downloading information from the web. The following example downloads and prints a secret
message from thinkpython.com:

import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
    print line.strip()
"""

import urllib.request


with open("words.txt") as fd:
    word_list = fd.read().splitlines()


def clean_word(line):
    for x in line.split(" "):
        print(x)
        if x in word_list:
            return x


conn = urllib.request.urlopen("http://thinkpython.com/secret.html")

for line in conn:
    print(line.strip())


zipcode = "02492"
conn = urllib.request.urlopen("http://uszip.com/zip/" + zipcode)

line = conn.readline()
while line:
    if "population" in str(line):
        print(clean_word(str(line)))
    line = conn.readline()

conn.close()
