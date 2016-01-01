# -*- coding: utf-8 -*-

import codecs, sys, copy
import to_formule, NLModules, mymath, Action

def check_args(finded_args, fasif, R):
  # Проверка на наличие в абстрактной группе
  hyperonyms = {}
  for argname, data in fasif['argdescr'].items():
    # пока только основные гиперонимы вытягиваем
    hyperonyms[argname] = [word['base'] for word in data['hyperonyms']]
  for finded_arg in finded_args:
    for argname, argvalue in finded_arg.items():
      isright = False
      for hyperonym in hyperonyms[argname]:
        print argvalue, 'is hyponym of', hyperonym, R.isWordInAbstractGroup(argvalue, hyperonym)
        if R.isWordInAbstractGroup(argvalue, hyperonym):
          isright = True
          break
      if not isright: del finded_arg[argname]

  # Проверка на отсутствие обязательных аргументных слов
  checked_args = []
  for finded_arg in finded_args:
    isright = True
    for argname, argdescr in fasif['argdescr'].items():
      if argname not in finded_arg and argdescr['isreq']: # если отсутствует обязательный аргумент
        isright = False
        break
    if isright: checked_args.append(finded_arg)

  # Конвертирование аргументных слов по таблице из фасифа
  for checked_arg in checked_args:
    for argname, value in checked_arg.items():
      if value not in fasif['argdescr'][argname]['argtable']: continue
      checked_arg[argname] = fasif['argdescr'][argname]['argtable'][value]

  return checked_args

def parseFunction(function_str):
  if function_str[0] == '$': return function_str[1:]
  module_name, func_name = function_str.split('/')
  module_obj = Action.getModule(module_name)
  return getattr(module_obj, func_name)

def Extraction2IL(R, settings, Action, predicates, arguments):
  #print '    predficates ::', predicates, '\n'
  #print '    arguments ::', arguments, '\n'

  fdb = to_formule.FasifDB(settings)
  pattern_IL = {
    'arg0': {'antonym': False}, # передаётся первым аргументом в каждую функцию
    'action': {
      'wcomb_function': None,
      'wcomb_verb_function': None,
      'common_verb_function': None,
      'mood': '',
      'circumstance': '',
      'type circumstance': ''
      },
    'argument': [],
    'subject': None
  }
  ILs = []
  predicate = predicates.values()[0]

  # Вынимаем Фасиф
  for _argument in arguments:
    argument = NLModules.ObjUnit.Sentence(_argument)
    compared_fasifs = fdb.getFASIF('WordCombination', argument)
    IL = copy.deepcopy(pattern_IL)
    for id_fasif, data in compared_fasifs.items():
      # Вынимаем фасиф словосочетания  # здевсь же отсеиваем неподходящие фасифы (через continue)
      finded_args, fasif = data
      for argname, args in finded_args.items(): finded_args[argname] = list(set(args))
      finded_args = mymath.dproduct(finded_args)
      finded_args = check_args(finded_args, fasif, R)
      compared_fasifs[id_fasif] = (finded_args, fasif)
      with codecs.open('comparing_fasif.txt', 'a', 'utf-8') as flog:
        flog.write('\n%s\n%s\n' % (str(finded_args), str(fasif['functions'])))

      # Определяем функцию (через фасиф словосочетания или глагола)
      function = None
      for destination, data in fasif['functions'].items():
        if predicate['base'] not in data['verbs']: continue # в фасифе должна сохранять синонимичная группа глаола
        function = data['function']
        break
      IL['argument'] = finded_args
      if function:
        IL['action']['wcomb_verb_function'] = parseFunction(function)
      else:
        function = fasif['functions']['getCondition']['function']
        IL['action']['wcomb_function'] = parseFunction(function)
        id_group =  R.R.get_groups_by_word('synonym', 0, predicate['base'], 'verb')[0]
        compared_fasifs = fdb.getFASIF('Verb', id_group)
        if not compared_fasifs: sys.stderr.write('Fasif for "%s" wasn\'t found!' % predicate['base'])
        IL['action']['common_verb_function'] = parseFunction(compared_fasifs.values()[0][0][0])

      with codecs.open('comparing_fasif.txt', 'a', 'utf-8') as flog:
        flog.write('\npraIL: %s\n' % str(IL))

    IL['action']['mood'] = predicate['mood']
    ILs.append(IL)
    #fwcomb = to_formule.to_formule(argument, False)
    #print x, fdb.get_hashWComb(fwcomb)
  print 
  return ILs, {'function': [], 'argument': [[] for i in range(len(ILs))]}