import re

words_amount = {}
with open('text_for_tests.txt', 'r', encoding='utf-8') as f:
    for word in re.sub('[\\\\n\\[\\]!?@#$.,;:\'\"]', '', str(f.readlines()).lower().strip()).split():
        if word not in words_amount:
            words_amount[f'{word}'] = 1
        else:
            words_amount[f'{word}'] = words_amount.get(f'{word}') + 1

print(words_amount)

sorted_dict = dict(sorted(words_amount.items(), key=lambda x: x[1]))

for key, value in sorted_dict.items():
    print(f'{key}: {value}')

