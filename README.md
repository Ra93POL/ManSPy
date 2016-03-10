# ManSPy - Managing System, written in Python 2.7.11

Разрабатывается под ОС Windows 7, но возможен запуск на Linux.

- Этот файл - ознакомление с программой
- http://github.com/Ra93POL/ManSPy/wiki - описание алгоритмов
- http://just-idea.ru - "взгляд в будущее", общие идеи, планы.

# Описание программы ManSPy и её запуск

## Описание

ManSPy разрабатывается как программа, "понимающая" естественный язык (ЕЯ), то есть собирающая максимальную информацию о предложениях в процессе анализа. В планах - построение экспертной системы с функцией системы управления (ассистента), но на данный момент делается упор на вторую часть плана.

Программа выполнена в форме "бота", который пока умеет делать лингвистические анализы предложений на языке Эсперанто и выполнять функции на языке Python, если они (функции) ассоциированы с соответствующими словосочетанием и/или глаголом. На данный момент реализована возможность выполнения функций при использовании простых предложений с прямым порядком слов, если глагол указан в повелительном наклонении. Программа умеет распозновать синонимы и антонимы глагола (в связи с чем в функцию передаётся в первом аргументе соответствующее "уведомление", чтобы в одной функции реализовать сразу два противоположных действия ) и других слов, если о них есть информация в базе данных (БД). Сейчас же реализуются ассоциации математических функций с соответсвующими глаголами и словосочетаниями, возможность использования конструкций условий и циклов, добавление семантических отношений (антонимов, синонимов, гиперонимов).

Программа построена с использованием принципа модульности, благодаря чему некоторые модули можно использовать отдельно от программы, а именно: модуль хранения семантических отношений, модуль лингвистического анализа текста на языке Эсперанто (реализованы графематический, морфологический и постморфологический (или же предсинтаксический - как угодно ;) ), синтаксический анализы). А в модуле анализа доступен модуль с объектами единиц речи: объекты слова, предложения, текста, имеющие удобные функции для построения алгоритмов анализа.

## Запуск

В программе используются следующие сторонние модули Python, не входящие в стандартную библиотеку и которые, следовательно, необходимо устанавливать отдельно:
- lxml - для парсинга страниц при авторизации во "ВКонтакте" и для парсинга страниц с курсами валют от ЦБ. (для ОС Windows: http://www.lfd.uci.edu/~gohlke/pythonlibs/)  
- cssselect - может проситься модулем lxml (https://codeload.github.com/SimonSapin/cssselect/zip/master, https://github.com/SimonSapin/cssselect/)
- xmpp - реализация протокола для jabber (http://xmpppy.sourceforge.net/, http://sourceforge.net/projects/xmpppy/files/, https://raw.githubusercontent.com/freebsd/freebsd-ports/master/net-im/py-xmpppy/files/patch-xmpp-transports.py - информация об исправлении ошибки в модуле)
- https://pypi.python.org/pypi/eonums/0.9.0 - простенький конвертер числительных на Эсперанто в числа и наоборот.
- repper и идущие после него модули — файлы из личного репозитория. https://github.com/Ra93POL/repository_personal. можно покласть их в любую папку, отдельно от программы. Для доступности этих модулей необходимо запустить файл repper_install.py из личного репозитория - он скопирует файл repper.py в основной репозиторий Питона. Repper.py импортируется только для того, чтобы добавить путь к личному репозиторию в переменную sys.path.
- TKinter - может требоваться на Линуксе (aptitude install python-tk)

Для запуска программы служит файл runManSPy.py, размещёнеый в корне репозитория. В файле присутствуют словарь с настройками программы:
```
Settings = {
  'logic': True, # включение/выключение модуля выполнения функций
  'convert2IL': True, # включение/выключение конвертации анализов во внутренний язык
  'test': True, # включение/выключение тестовой версии программы 
  'storage_version': 2, # (1, 2) версия БД (слова, их отношения, ФАСИФы)
  'assoc_version': 3 # (2, 3) версия способа ассоциирования лингвистических и технических данных (ФАСИФа)
  }
```

А также словарь, позволяющий включать/отключать модули интерфейсов (МИ), через которые происходит взаимодействие пользователя с программой:
```
interfaces = {
  'autofeed':    1, # Автоподатчик, включён
  'TKinter':     1, # Примитивный чатб включён
  'jabber':      0, # Jabber,  выключен, но можно включить
  'vkcom':       0, # ВКонтакте, выключен из-за наличия ошибок
  'Commandline': 0  # Один из первых МИ, выключен так как не имеет смысла
  }
```

Есть ещё файл с настройками для авторизации в Jabber и ВКонтакте. Он расположен уровнем выше директории репозитория, имеет имя  IFM_passwords.txt и следующее содержимое:
```
service: jabber
login: ИмяПользователя@Сервер
pass: Пароль

service: vkcom
app_id: ИдентификаторПриложения
login: ТелефонИлиЭлАдрес
pass: Пароль
```

# Файлы, генерируемые программой

После запуска появится директория DATA_BASE (расположена уровнем выше директории проекта), в которой будут сгенерированы следующие файлы:
- analysis.txt - результаты анализа предложений (графематический, морфологический, постморфологический, синтаксический). Сюда же пишутся предложения на внутреннем языке (ВЯ), которые строятся на основе анализов и выполняются программой.
- comparing_fasif.txt - резуьтаты сравнения актанта (словосочетания) с словосочетанием в ФАСИФе.
- history.txt - история диалога отдельно для каждого модуля интерфейсов (МИ)

А также директория Esperanto, в которой лежит файл БД main_data.db.

В директории репозитория также генерируется файл comparing_fasif.txt, содержащий результат сопоставления анализов актантов (словосочетаний) с описанием ассоциаций (ФАСИФами, про которые будет рассказано ниже).

# Директории репозитория

Репозиторий расположен в директории ManSPy (но может быть и любое другое имя), в которой расположены ещё две дмректории:
- ManSPy - сама программа
- IFModules - модули интерфейсов (МИ), выполненные в виде отдельных маленьких программ. В них реализованы варианты взаимодействия с программой: примитивный чат на TKinter'е, автоподатчик (используется для автоматической поочередной подачи предложений), доступ из чатов Jabber'а. Там же реализован механизм параллельной работы всех запущенных МИ и программы ManSPy. Вы можете писать собственные МИ, например, для доступа к программе из социальных сетей, виртуальных миров, а с использованием распознавания речи можно написать МИ для доступа через сотовую связь, также есть возможный вариант применения интерфейсов мозг-компьютер.

В файле runManSPy.py происходит создание объекта программы и его передача в модули интерфейсов. Объект программы имеет следующие функции, используемые в МИ:
- write_text(IFName, w_text) - передаёт текст на естественном языке. В планах - возвращение идентификатора сообщения.
- read_text(IFName[, index=None]) - возвращает все ответы, если указан индекс ответа index, то будет возвращён только один ответ.
- getlen_text(IFName) - возвращает длину "непрочитанных" ответов.

Аргумент IFName - это имя МИ, то есть через каждый МИ осуществляется отдельный диалог с программой.

# ФАСИФ - формат ассоциирования слов и функций.

ФАСИФ - это формат, в котором удобно описывать ассоциации между функцией и глаголом и/или словосочетанием. В ассоциациях лингвистическую информацию можно писать сразу для нескольких языков, хотя пока доступен один - Эсперанто. Существует два вида ФАСИФа.

Первый вид - это ассоциация функции и глагола. В данном случае указывается функция и имя глагола, возможно, с синонимами. В функцию будут передаваться состояния словосочетаний, которые могут быть выведены в качестве ответов, но могут быт и другие варианты использования (зависит от указанной функции). О состоянии словосочетания - ниже. На данный момент доступен для использования глагол montru, выводящий состояния в МИ. Глаголы могут быть переопределены в ФАСИФе второго вида для каждого словосочетания отдельно.

Второй вид - это ассоциация функции и словосочетания, а также функции и глагола, связанного со словосочетанием. В нём подробно описываются аргументы функции, их соответствие словам в конкретном словосочетании. Слово, ассоциированное с аргументом функции, называется аргументным. Причём для аргументного слова указываются гиперонимы - абстрактные группы, в это аргументное слово может входить. Кроме этого, для аргументов, при необходимости, указывается таблица конвертации, в которой указываются возможные аргументные слова и то, на что они должны замениться перед передачей в функцию, если не указано, то в функцию передаётся корень слова.

Каждое словосочетание может иметь несколько глаголов, и для каждого - своя функция.

В данный момент реализованы ФАСИФы для получения курса валют, включения/выключения света - сейчас сделана эмуляция, получения IP-адреса компьютера.

# Как работает ManSPy

Над предложением, поступающем от пользователя, производятся лингвистические анализы. Затем, происходит выбор соответствующих ФАСИФов для актантов глагола (словосочетаний), после чего анализы на основе ФАСИФа конвертируются во внутренний язык. Предложение на внутреннем языке интерпретируется модулем выполнения функций (МВФ).

# Написание собственных МИ

# Подробно о ФАСИФе