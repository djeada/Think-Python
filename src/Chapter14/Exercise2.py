"""
Exercise 2
Write a function called sed that takes as arguments a pattern string, a
replacement string, and two filenames; it should read the first file and
write the contents into the second file (creating it if necessary). If the
pattern string appears anywhere in the file, it should be replaced with the
replacement string.

If an error occurs while opening, reading, writing or closing files, your
program should catch the exception, print an error message, and exit.
"""

import os


def sed(pattern, replace, source, dest):
    try:
        fin = open(source, "r")
        fout = open(dest, "w")

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print("error")


pattern = "test"
replace = "halo"
source = "test.txt"
dest = "replaced.txt"
sed(pattern, replace, source, dest)
