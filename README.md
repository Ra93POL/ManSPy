# ManSPy
Management System (universal and interactive)
Python 2.7.10
Автор: Константин Поляков. Начало написания: 27.04.2014 год.
Подробно об алгоритмах, планах, возможностях текущей реализации: http://just-idea.ru

Универсальная и интерактивная ситсема управления. Универсальность заключается в возможности подключения любых систем (умный дом, персональный компьютер, социальные сети, роботы, аэропоника и прочее). Интерактивность - в том, что программа сама будет задавать уточняющие вопросы, а также оповещать о происходящем (критическое поывшение температур или цен, проникновение в жилище, угон автомобиля, день рождения у подруги). Интерактивность пока не реализована.

Любая внешняя система подключается к моей программе путём написания модулей действий, предоставляющих соответсвующее API для управления. После чео в модуле прописывается переменная с ФАСИФОМ - Форматом Ассоциировния Слов И Функций. В ФАСИФе указывается естественный язык, пример-предложение, слова-аргументы, которые будут переданы в функцию напрямую или через конвертирование, а ткже указываются вышестоящие абстрактные группы для слов-аргументов. В функцию передаётся в обязательном порядке первый аргумент, являющийся словарём (ассоциативным массивом). В первом аргументе пока только содержить информация, пвызвана ли данная функция через глагол-антоним или нет, чтобы в одно функци реализовать два противополжных действия (например, включение или выключения света).

Программа может получать команды из различных модулей интерфейсов: локального текстового чата (TKinter), jabber'а, социальна сеть "ВКонтакте", в котором  что-то сломал, автоподатчика. Программа ответит в тот интерфейс, из которого примет сообщения. Автоподатчик служит для автоматичской подачи самых каверзных сообщений из файла с целью тестирования программы.

Язык взаимодействия с программой: Эсперанто. В будущем планируется добавление кечуа (из-за разнообразия морфем и строгости порядка слов в предложении), пирахан (чтобы оказать, что возможности программы зависят от возможностей языка, а в пирахан остутсвуют числительные, только мало или много), английский (намного сложней из-за исключений), русский (вообще жесть). Интерсны таже иероглифы и языки жестов (которые образные, а не имтаторы звуковых языков). Также интерсно использоввание интерфейса мозг-компьютер, нео в этой области у меня мало знаний, да и рано его использовать.

Программа работает пока с одним предложением, а не с текстом. Из союзов подерживается лишь "kaj" с ошибками. Прямой порядок слов (подлежащее, сказуемое, прямое дополнение, косвенные дополнения), хотя язык благодаря винительному падежу позволяет нарушать порядок. Программа пока реагирует на команды - глаголы с повелительным (императивным) наклонением, остальные глаголы игнорируются.

Файл с паролями для "Вконтакте" и jabber кладётся в директория, выше директории программы. Пример файла:
```
"""
# комментарий
jabber: login@server.com passwrd
vkcom: ApplicationID login password
"""
```

В программе много жуков и мух - берегите нервы или запасайтесь сачками или тапками для их ловли. Внимание: быдлокод и возможная ересь!