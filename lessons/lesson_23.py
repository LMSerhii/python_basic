t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y',
     'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
     'f', 'h', 'c', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Программирование на Python - лучший курс'
slug = ''

for s in title.lower():
     if 'а' <= s <= 'я':
          slug += t[ord(s) - start_index]
     elif s == '':
          slug += 'yo'
     elif s in ' !?;:.,':
          slug += '-'
     else:
          slug += s

while slug.count("--"):
     slug = slug.replace("--", "")


print(slug)

