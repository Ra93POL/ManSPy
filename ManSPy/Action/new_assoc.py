# -*- coding: utf-8 -*-

# ассоциирование глагола и функции
'''
montru $ToUser # функция Системы - все переданные ей состояния будут выводиться в МИ
'''

# ассоцииование функции и словосочетания

'''
Тоже самое, только функция ассоциируется со словосочетанием.
Здесь указана функция для получения текущего состояния.
В случае со светом мы должны дополнительно указать функцию для изменения состояния, а также глагол.
В итоге, глагол имеет несколько функций, которые вызываютя в зависимости от словосочетаний (валентности глагола в данном предложении).
Также есть глаголы, имеющие одну функцию для любых словосочетаний (montru).
Если функция общего глагола переопределена, то необходимо указать, в каких случаях вызывается конкретная функция для словосочетания, а не общая.'''

_list_FASIF = ['''
# Описание Функции
GetCourse
currency y ;  Esperanto
# пробелы в начале строки обязательны
  USD      ;  dolar
  RUB      ;  rubl
  EUR      ;  eŭr
  UAH      ;  grivn
country n ;  Esperanto
  Russia  ;  rusi
  Belarus ;  belarusi
  Ukraine ;  ukraini
#argument n - если не требуется замена значения аргумента

# Шаблоны ЯЕ-предложений
Esperanto
dolaran: monero # аргументное слова: абстрактные группы через запятую
rusia: lando
dolaran cambion de rusia banko

Russian
доллара, валюта
русскому, страна, национальность
курс доллара согласно русскому банку
''']
