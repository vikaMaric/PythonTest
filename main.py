words = ['hello', 'goodbye', 'now', 'now', 'today', 'hello']


unique_words = []

for word in words:

    if word not in unique_words:
        unique_words.append(word)

print('Unique words:')
for unique_word in unique_words:
    print(unique_word)