# longest_word
sentence = input()
words = sentence.split()
longest = max(words, key=len)
print(longest)