# Mad Libs en espanol

def get_words(word_types):

    word_list = dict()
    word = ''

    for word in word_types:

        kind_of_word = word.split('_')
        next_word = input(f"Entra una {kind_of_word[0]}: ")
        word_list[word] = next_word

    return word_list

def print_mad_lib(word_list, skeleton_text):
    pass


############
### MAIN ###
############

skeleton_text = ' Programar es tan {word_list[adjectivo_01]}. \
                Siempre me {word_list[verbo_01]} resolver problemas. \
                Aprende a {word_list[verbo_02]} con {organizacion_01} \
                y alcanza tu {word_list[sustantivo_01]}.'

word_types = ['adjectivo_01', 'verbo_01', 'verbo_02', 'organizacion_01',
              'sustantivo_01' ]

word_list = get_words(word_types)
print_mad_lib(word_list, skeleton_text)