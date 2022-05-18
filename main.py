import re

document_text = open('input.txt')
frequency = {}
string = document_text.read().lower()
string1 = string


string = string .replace('and', ' ')
string = string .replace('as', ' ')
string = string .replace('in', ' ')
string = string .replace('if', ' ')
string = string .replace('or', ' ')
string = string .replace('but', ' ')
string = string .replace('how', ' ')
string = string .replace('so', ' ')

match_pattern = re.findall(r'\b[a-z]{3,15}\b', string )

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])






search = "fff"
s1 = str('')
s2 = 'Stop'

while search != s1 or search != s2:

    search = str(input('Введите что искать: \n'))
    count = 0
    if search == s2 or search == s1:
        break
    else:
        for i in range(len(string1)):
            if string1[i: i + len(search)] == search:
                count += 1

    print(count)

document_text.close()
