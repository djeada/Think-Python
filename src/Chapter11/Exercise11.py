"""
Exercise 11
This was sent in by a fellow named Dan O’Leary. He came upon a
common one-syllable, five-letter word recently that has the
following unique property. When you remove the first letter,
the remaining letters form a homophone of the original word,
that is a word that sounds exactly the same. Replace the first
letter, that is, put it back and remove the second letter and
the result is yet another homophone of the original word. And
the question is, what’s the word?

Now I’m going to give you an example that doesn’t work. Let’s
look at the five-letter word, ‘wrack.’ W-R-A-C-K, you know like
to ‘wrack with pain.’ If I remove the first letter, I am left
with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you
see the rack on that buck! It must have been a nine-pointer!’
It’s a perfect homophone. If you put the ‘w’ back, and remove
the ‘r,’ instead, you’re left with the word, ‘wack,’ which is
a real word, it’s just not a homophone of the other two words.

But there is, however, at least one word that Dan and we know
of, which will yield two homophones if you remove either of the
first two letters to make two, new four-letter words. The
question is, what’s the word?
"""


def read_dict():
    pronunciation = {}

    with open("c06d.txt") as fd:
        for line in fd:
            index = line.find(" ")
            word = line[:index]
            pron = line[index + 2 :]
            pronunciation[word] = pron

    return pronunciation


def are_homophones(d, a, b, c):
    try:
        return d[c] == d[b] == d[c]
    except KeyError:
        return False


def find_homophones(pron_dict):
    homophones = []

    for word in pron_dict:
        if are_homophones(pron_dict, word, word[1:], word[0] + word[2:]):
            homophones.append((word, word[1:], word[0] + word[2:]))
    return homophones


for x in find_homophones(read_dict()):
    print(x)

print(len(find_homophones(read_dict())))
