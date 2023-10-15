word_count = {}
text = input("Text: ")

words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

words = list(word_count.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_count[word]}")
"""
Output:
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""