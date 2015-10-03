# -*- coding: utf-8 -*-
""" Предоставляет API интеллекта, который используется модулями интерфейса.
    В качестве API:
      API = ISM.API(Settings) # Settings - словарь, задающий настройки.
      Answer = API.Asker(Question) # Asker - функция, принимающая вопрос
      и возвращающая ответ. Функция может возвращать информацию, которая
      не была запрошена, то есть необходимо постоянно вызывать эту функцию,
      передавая ей пустую строку (или вопрос), для получения такой информации.
    Примеры возможных интерфейсов: текстовый чат, распознаватель речи,
    мессенджеры, интерфейс мозг-компьютер, приёмник звонков и SMS и так далее.
"""
import os
db_path = os.path.abspath('DATA_BASE')
if not os.path.exists(db_path) or not os.path.isdir(db_path):
  os.mkdir(db_path)

import Logic, ImportAction, LangModules, API_ForDB, time, codecs, sys

class IMS_Exception(Exception): pass

def _save_history(text, Type, IFName):
  if text:
    Time = time.strftime('%c', time.gmtime(time.time()-time.altzone))
    text = "* %s  %s  %s: %s\n" % (Type, Time, IFName, text)
    API_ForDB.WriteToFile(text, 'history', 'a')

class API():
  # настройки задаются один раз. Но можно написать модуль для изменения
  # настроек через канал общения.
  settings = {'history': 1,
              'monitor': 1, # включает вывод на экран статистику работы ИСУ
              'logic': 1, # включает модуль логики
              'convert2IL': 1, # включает последний этап конвертации
                               # если при отключении включёна логика, то будет ошибка
              'language': 'Esperanto',
              'storage_version': 1, # 2 - это разрабатываемая версия
              'test': 1 # тестовый режим, включаемый в процессе отладки и разработки
              }
  # 'module_settings': {ИмяМодуля: СловарьНастроекМодуля_ИлиОбъектУправления}
  def ChangeSettings(self, NewSettings):
    # Проверяем правильность ключей
    keys = self.settings.keys()
    for user_key in NewSettings.keys():
      if user_key not in keys:
        raise IMS_Exception('error2: Wrong name of key in settings: %s' % str(user_key))
    # Обновляем настройки
    self.settings.update(NewSettings)
    self.settings['language'] = self.settings['language'].capitalize()
    # Сохраняем настройки для доступа из других частей ИСУ
    API_ForDB.WriteSettings(self.settings)
    
  def __init__(self, UserSettings={}):
    """ Инициализация ИСУ """
    # Меняем настройки по умолчанию на пользовательские
    self.ChangeSettings(UserSettings)
    print u"Загрузка модулей действий..."
    t1 = time.time()
    Import = ImportAction.ImportAction(self.settings)
    Import.importAll()
    t2 = time.time()
    print '  ', t2 - t1
    print u"Загрузка модуля естественного языка..."
    if self.settings['storage_version'] == 2: from LangModules import generate_code # генерирум модуль
    t1 = time.time()
    import Action
    self.LangClass = LangModules.LangClass(self.settings, Action)
    t2 = time.time()
    print '  ', t2 - t1
    print u"Инициализация модуля логики..."
    t1 = time.time()
    self.LogicShell = Logic.LogicShell(self.settings)
    t2 = time.time()
    print '  ', t2 - t1
    print u"Готово!"

  def print_errors(self, GrammarNazi, ErrorConvert):
    for analys, errors in GrammarNazi.items():
      if errors: sys.stderr.write(analys + ": ")
      for error in errors: sys.stderr.write("  " + error + "\n")
    for part, errors in ErrorConvert.items():
      if errors: sys.stderr.write(part + ": ")
      for error in errors: sys.stderr.write("  " + error + "\n")

  # Данная функция должна вызываться переодически, даже если ничего не вводится,
  # так как ИСУ может сама что-то сообщить, по своей инициативе.
  def write_text(self, IFName, w_text):
    if IFName not in self.LogicShell.list_answers: self.LogicShell.list_answers[IFName] = []
    if w_text:
      if self.settings['history']: _save_history(w_text, "W", IFName)
      ILs, GrammarNazi, ErrorConvert = self.LangClass.NL2IL(w_text)
      #print "GrammarNazi:", GrammarNazi
      self.print_errors(GrammarNazi, ErrorConvert)
      #print "ErrorConvert:", ErrorConvert, "\n"
      if not ErrorConvert['function']:
        index = 0
        for IL in ILs:
          if not ErrorConvert['argument'][index]: self.LogicShell.Shell(IL, IFName)
          index += 1

  def read_text(self, IFName, index=None):
    if IFName not in self.LogicShell.list_answers: self.LogicShell.list_answers[IFName] = []
    # Возвращает ответ или пустую строку, если ответа нет. None ответом не считается.
    r_text = u''
    if index == None:
      r = range(len(self.LogicShell.list_answers[IFName]))
      # montru dolaran euxran cambion de ukraina banko
      for i in r:
        _r_text = self.LogicShell.list_answers[IFName].pop(0)
        if _r_text: r_text += self.LangClass.IL2NL(_r_text) + ' '
    else:
      if len(self.LogicShell.list_answers[IFName]) > 0:
        _r_text = self.LangClass.IL2NL(self.LogicShell.list_answers[IFName].pop(index))
        if _r_text: r_text = _r_text
    if self.settings['history']: _save_history(r_text, "R", IFName)
    return r_text

  def getlen_text(self, IFName):
    if IFName not in self.LogicShell.list_answers: self.LogicShell.list_answers[IFName] = []
    return len(self.LogicShell.list_answers[IFName])
