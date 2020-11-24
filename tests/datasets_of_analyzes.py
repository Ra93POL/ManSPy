"""
    Содержит примеры предложений на естественном языке с указанием результата каждого этапа его обрабоотки.
    Поля длЯ каждого примера:
    - w_text - входной текст на естественном языке
    - r_text_construct - ответ программы в режиме конструкционного ответа
    - is_ready - если предложение полностью поддерживается программой, то равно True (оп умолчанию). Иначе - False
"""

dataset_verb_and_actants = {
    'dataset_description': 'глагол + его актанты',
    'examples': [
        {
            'w_text': 'montru dolaran kaj euxran kurzon de rusia banko',
            'r_text_construct': ['USD-Russia', 'EUR-Russia'],
        },
        {
            'w_text': 'sxaltu tablan lampon en dormcxambro',
            'r_text_construct': ['1'],
        },
        {
            'w_text': 'montru adreson de komputilo',
            'r_text_construct': ['192.168.0.1'],
        },
        {
            'w_text': 'montru adreson de androido',
            'r_text_construct': [],
        },
        {
            'w_text': 'dolaran kurzon montru',
            'r_text_construct': ['USD-Russia'],
        },
        {
            'w_text': 'montru de rusia banko euxran kurzon',
            'r_text_construct': ['EUR-Russia'],
        },
    ]
}

dataset_verb_and_repeated_actants = {
    'dataset_description': 'Повторяющиеся одинаковые аргументы',
    'examples': [
        {
            'w_text': 'montru dolaran kaj dolaran kurzon de rusia banko',
            'r_text_construct': ['USD-Russia', 'USD-Russia'],
        },
        {
            'w_text': 'montru dolaran kaj dolaran kurzon de rusia kaj rusia banko',
            'r_text_construct': [
                'USD-Russia',
                'USD-Russia',
                'USD-Russia',
                'USD-Russia'
            ],
        },
    ]
}

dataset_verb_and_homogeneous_actants = {
    'dataset_description': 'Повторяющиеся разные аргументы (сложатся друг с другом поочерёдно - декартово произведение)',
    'examples': [
        {
            'w_text': 'montru adreson de komputilo kaj androido',  # TODO: должен вывести инфу, что `androido` не распознан
            'r_text_construct': ['192.168.0.1'],
        },
        {
            'w_text': 'montru euxran kaj dolaran kurzon de ukrainia kaj rusia kaj belarusia banko',
            'r_text_construct': [
                'EUR-Russia',
                'EUR-Belarus',
                'EUR-Ukraine',
                'USD-Russia',
                'USD-Belarus',
                'USD-Ukraine',
            ],
        },
        {
            'w_text': 'montru euxran kaj dolaran kurzon de ukrainia kaj rusia banko',
            'r_text_construct': [
                'EUR-Russia',
                'EUR-Ukraine',
                'USD-Russia',
                'USD-Ukraine'
            ],
        },
        # TODO: сложатся соответственно (не реализовано пока)
        # ('montru euxran kaj dolaran kurzon de ukrainia kaj rusia banko соответсвенно', [
        #     'EUR-Russia',
        #     'EUR-Ukraine',
        #     'USD-Russia',
        #     'USD-Ukraine'
        # ]),
    ]
}

dataset_antonym_of_verb = {
    'dataset_description': 'Антонимия через приставку, которая антонимирует значение, либо через глагол-антоним',
    'examples': [
        {
            'w_text': 'malsxaltu tablan lampon en dormcxambro kaj fermo',
            'r_text_construct': ['0'],
        },
        {
            'w_text': 'malmontru dolaran kurzon de rusia banko de mia domo',
            'r_text_construct': [],
        },
    ]
}

dataset_verb_and_homogeneous_direct_supplement = {
    'dataset_description': 'Однородные прямые дополнения, по сути - две разных функции (два разных действия) в одном предложении',
    'examples': [
        {
            'w_text': 'montru adreson de komputilo kaj dolaran kurzon',
            'r_text_construct': ['192.168.0.1', 'USD-Russia'],
        },
        {
            'w_text': 'montru adreson de komputilo kaj dolaran kurzon de belarusia banko',
            'r_text_construct': ['192.168.0.1', 'USD-Belarus'],
        },
        {
            'w_text': 'montru dolaran kurzon kaj adreson de komputilo',
            'r_text_construct': ['USD-Russia', '192.168.0.1'],
        },
    ]
}

dataset_punctuation = {
    'dataset_description': 'Пунктуация',
    'examples': [
        {
            'w_text': 'montru euxran, dolaran kurzon de ukrainia banko',
            'r_text_construct': ['EUR-Ukraine', 'USD-Ukraine'],
        },
        {
            'w_text': 'montru euxran, dolaran kurzon de ukrainia banko .',
            'r_text_construct': ['EUR-Ukraine', 'USD-Ukraine'],
        },
        {
            'w_text': 'montru euxran, dolaran kurzon de ukrainia banko ...',
            'r_text_construct': ['EUR-Ukraine', 'USD-Ukraine'],
        },
    ]
}

dataset_numbers_and_simple_math = {
    'dataset_description': 'Числительные и простая арифметика',
    'examples': [
        {
            'w_text': 'adiciu dudekon trion',
            'r_text_construct': ['23'],
        },
        {
            'w_text': 'adiciu kvardekon kaj trion kaj milionon',
            'r_text_construct': ['40 + 3 + 1000000'],
        },
        {
            'w_text': 'maladiciu dolaran kurzon kaj trion',
            'r_text_construct': ['3'],  # TODO correct: ['USD-Russia + -3']
        },
        {
            'w_text': 'adiciu dolaran kurzon kaj 1000',
            'r_text_construct': ['USD-Russia'],  # TODO correct: ['USD-Russia + 1000]
        },
        {
            'w_text': 'multigu trion kaj kvaron',
            'r_text_construct': ['3 * 4'],
        },
    ]
}

dataset_synonyms_of_verb = {
    'dataset_description': 'Синонимы',
    'examples': [
        {
            'w_text': 'malmultigu dolaran kurzon kaj trion',
            'r_text_construct': ['3'],  # TODO correct: ['USD-Russia / 3']
        },
        {
            'w_text': 'malobligu dolaran kurzon kaj trion',
            'r_text_construct': ['3'],  # TODO correct: не помню перевод obligu
        },
    ]
}

dataset_undirect_order_of_words = {
    'dataset_description': 'Непрямой порядок слов',
    'examples': [
        {
            'w_text': 'trion adiciu',
            'r_text_construct': ['3'],
        },
    ]
}

datasets = (
    dataset_verb_and_actants,
    dataset_verb_and_repeated_actants,
    dataset_verb_and_homogeneous_actants,
    dataset_antonym_of_verb,
    dataset_verb_and_homogeneous_direct_supplement,
    dataset_punctuation,
    dataset_numbers_and_simple_math,
    dataset_synonyms_of_verb,
    dataset_undirect_order_of_words,
)


# TODO: рассортировать, добавить примеры условий

TEST_INPUT_DATA_ESPERANTO = [
    # Это предложение выдаёт курс доллара только по росбанку (украинский не замечает).
    # TODO: Как вариант решения: проверять каждоый однородный член у дополнений (кроме первого)
    #  (однородные члены должны совпадать по части речи)
    #('montru dolaran kurzon de rusia banko kaj ukraina banko', ['USD-Russia', 'USD-Ukrain']),
    # TODO: однородные слова-посредники (не реализовано пока)
    #('montru dolaran kurzon de ukrainia banko kaj de rusia banko', ['USD-Ukraine', 'USD-Russia']),


    # ('Montru dolaran kurzon. Montru euxran kurzon de belarusia banko', []),
    # TODO: пока не поддерживаются
    # ('montru dolaran kurzon, kiu estas dolara', []),
    # ('Se euxra cambio de belarusia banko estas sepduk kvar, do sxaltu tablan lampon en dormcxambro', []),
    # ('Do sxaltu tablan lampon en dormcxambro, se euxra cambio de belarusia banko estas sepduk kvar', []),

    # ('montru dolaran kurzon kaj trion kaj kvardek', []),
    ('montru dolaran kurzon kaj trion kaj kvardekon', ['USD-Russia', '3', '40']),

    ('montru dolaran kurzon de kvarcent sesdek mil tricent dek du', ['USD-Russia']),  # TODO correct: не знаю, как нужно
    # ('montru dolaran kurzon de dua banko', []),
    # ('montru dolaran kurzon de triiliono', []),
    # ('montru dolaran kurzon de 2 banko', []),
    # ('montru dolaran kurzon de du', []),
    # ('montru dolaran kurzon de okdek', []),
    # ('montru dolaran kurzon de dek du', []),
]

dataset2 = {
    'dataset_description': '',
    'examples': [
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
        {
            'w_text': '',
            'r_text_construct': [],
        },
    ]
}