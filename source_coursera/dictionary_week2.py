# -*- coding: utf-8 -*-
#!DICTIONARY!#
################
#------------------#
empty_dict = {}
empty_dict = dict() #declaration of dictionary

collections_map = {
	'mutable': ['list', 'set', 'dict'],
	'immutable': ['tuple', 'frozenset']
}

print(collections_map['immutable']) #printing by 'immutable' key


#------------------#
#to be ready for fail in search
print(collections_map.get('irresistible', 'not found'))


#------------------#
print('mutable' in collections_map)


#------------------#
#adding key and value
beatles_map = {
	'Paul': 'Bass',
	'John': 'Guitar',
	'George': 'Guitar', 
}

print(beatles_map)

beatles_map['Ringo'] = 'Drums'

print(beatles_map)

 
#------------------#
#deleting
del beatles_map['John']

print(beatles_map)


#------------------#
#adding
beatles_map.update({ 
	'John': 'Guitar'
})

print(beatles_map)


#------------------#
print(beatles_map.pop('Ringo')) #output => Drums

print(beatles_map) #without Ringo


#------------------#
#if no key in dictionary - add it
unknown_dict = {}
#trying to get 'key' if cannot put default value
print(unknown_dict.setdefault('key', 'default'))

print(unknown_dict) #output => key - default


#------------------#
""" Для быстрого получения адреса памяти ключа используется функция 
хэширования от его содержимого. Подумайте, какие из знакомых вам 
типов данных могут быть ключами в словарях?
#	Целые числа
#	Кортежи
#	None
#	Строки
"""


#------------------#
#iteration in dictionary
print(collections_map)

for key in collections_map:
	print(key) #$> mutable immutable

for key, value in collections_map.items():
	print('{} = {}'.format(key, value)) #$> mutable = ['list', 'set', 'dict'] immut/

for value in collections_map.values():
	print(value) #$> ['list', 'set', 'dict'] ['']/


#------------------#
#OrderedDict - dict is ordered always
from collections import OrderedDict 

ordered = OrderedDict()

for number in range(10):
	ordered[number] = str(number)

for key in ordered:
	print(key) #$> 0 1 2 3 4 ../


#------------------#
#Example Task = find 3 most common words in Zen of python
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


zen_map = dict() #create dictionary

for word in zen.split():
	cleaned_word = word.strip('.,!-').lower() #cleans the word
	if cleaned_word not in zen_map:
		zen_map[cleaned_word] = 0
	
	zen_map[cleaned_word] += 1

print(zen_map)


#most common 3 words
import operator

zen_items = zen_map.items()
word_count_items = sorted(
	zen_items, key=operator.itemgetter(1), reverse=True
)

print(word_count_items[:3]) #$> [('is', 10), ('better', 8), ('than', 8)]


#most common 3 words v2
from collections import Counter

cleaned_list = []
for word in zen.split():
	cleaned_list.append(word.strip('.,!-').lower())

print(Counter(cleaned_list).most_common(3)) 
#$> [('is', 10), ('better', 8), ('than', 8)]
