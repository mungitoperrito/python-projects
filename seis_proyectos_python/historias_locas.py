# Mad Libs en espanol

def get_words(word_types):

    word_list = dict()
    word = ''

    for word in word_types:

        kind_of_word = word.split('_')
        next_word = input(f"Entra una {kind_of_word[0]}: ")
        word_list[word] = next_word

    return word_list

def print_mad_lib(word_list):
        print(f'Programar es tan {word_list['adjectivo_01']}. ', end='')
        print(f'Siempre me {word_list['verbo_01']} resolver ', end='')
        print(f'problemas. Aprende a {word_list['verbo_02']} ', end='')
        print(f'con {word_list['organizacion_01']} y alcanza ', end='')
        print(f'tus {word_list['sustantivo-plural_01']}.')


############
### MAIN ###
############

word_types = ['adjectivo_01', 'verbo_01', 'verbo_02', 'organizacion_01',
              'sustantivo-plural_01' ]

word_list = get_words(word_types)
print_mad_lib(word_list)