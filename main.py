import re

from datetime import datetime

start_time = datetime.now()

words_amount = {}
with open('text_for_tests.txt', 'r', encoding='utf-8') as f:
    for word in re.sub('[\\\\n\\[\\]()_!?=+<>«»@0123456789#\-$.,;:\'\"]', '', str(f.readlines()).lower().strip()).split():
        if word not in words_amount:
            words_amount[f'{word}'] = 1
        else:
            words_amount[f'{word}'] = words_amount.get(f'{word}') + 1

f.close()

print(f'Количество уникальных слов в тексте: {len(words_amount)}')

sorted_dict = dict(sorted(words_amount.items(), key=lambda x: x[1]))

for key, value in reversed(sorted_dict.items()):
    print(f'{key}: {value}')

with open('words_amount.txt', 'w', encoding='utf-8') as file:
    file.write(f'Количество уникальных слов в тексте: {len(words_amount)} \n')
    for key, value in reversed(sorted_dict.items()):
        file.write(f'{key}: {value} \n')

print(f'Время выполнения программы: {datetime.now() - start_time}')

