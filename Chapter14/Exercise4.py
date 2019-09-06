'''
Exercise 4
In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names.
The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given
suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files have the same checksum,
they probably have the same contents. To double-check, you can use the Unix command diff.
'''

import os
import sys
import hashlib

def get_files(dirname, extension):
    all_files = []
    length = len(extension)
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if filename[-length:] == str(extension):
                all_files.append(os.path.join(root, filename))
    print(all_files)
    return all_files

def chunk_reader(fobj, chunk_size=1024):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def find_duplicates(file_list, hash=hashlib.sha1):
    hashes = {}
    for file in file_list:
        hashobj = hash()
        for chunk in chunk_reader(open(file, 'rb')):
            hashobj.update(chunk)
        file_id = (hashobj.digest(), os.path.getsize(file))
        duplicate = hashes.get(file_id, None)
        if duplicate:
            print("Duplicate found: %s and %s" % (file, duplicate))
        else:
            hashes[file_id] = file


find_duplicates(get_files(os.getcwd(),'.py'))
