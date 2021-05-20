"""
Exercise 5
What is the longest English word, that remains a valid English word, as you
remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can't
rearrange any of the letters. Every time you drop a letter, you wind up with
another English word. If you do that, you're eventually going to wind up with
one letter and that too is going to be an English word-one that's found in
the dictionary. I want to know what's the longest word and how many letters
does it have?
I'm going to give you a little modest example: Sprite. Ok? You start off with
sprite, you take a letter off, one from the interior of the word, take the r
away, and we're left with the word spite, then we take the e off the end,
we're left with spit, we take the s off, we're left with pit, it, and I.
Write a program to find all words that can be reduced in this way, and then
find the longest one.
This exercise is a little more challenging than most, so here are some
suggestions:
1. You might want to write a function that takes a word and computes a list
of all the words that can be formed by removing one letter. These are the
"children" of the word.
2. Recursively, a word is reducible if any of its children are reducible. As
a base case, you can consider the empty string reducible.
3. The wordlist I provided, words.txt, doesn't contain single letter words.
So you might want to add "I", "a", and the empty string.
4. To improve the performance of your program, you might want to memoize
the words that are known to be reducible.
"""

with open("words.txt") as fd:
    word_list = fd.read().splitlines()

word_list.append("a")
word_list.append("I")

memo = dict()
memo[""] = [""]


def child_list(word, word_list):
    lista = []
    for c in word:
        if word.replace(c, "") in word_list:
            lista.append(word.replace(c, ""))
    return lista


def is_reducible(word, word_list):
    if word in memo:
        return memo[word]

    if len(word) == 1:
        memo[word] = True
        return True

    for child in child_list(word, word_list):
        if child not in word_list:
            memo[child] = False
            return False
        else:
            return is_reducible(child, word_list)


def find_longest(word_list):
    longest = ""
    for word in word_list:
        if is_reducible(word, word_list):
            if len(word) > len(longest):
                print(longest)
                longest = word
    return longest


print(is_reducible("temperances", word_list))

print(find_longest(word_list))
