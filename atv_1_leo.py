def valid_user_archive_path():
    while True:
        txt_file_path_user = input("Insira um caminho válido para a leitura de um arquivo de texto.\n")
        txt_file_path_user = txt_file_path_user.replace("/", "\\")

        try:
            open(txt_file_path_user, 'r')
            break
        except Exception:
            print("Foi inserido um caminho inválido, tente novamente.")
            continue
    return txt_file_path_user

def defines_generic_informations_from_file_user(txt_file_path_user):
    num_words_archive_user = 0
    first_line_syllable_cao_appear = 0
    biggest_words_archive_user = ""
    num_characters_biggest_word_archive_user = 0
    vowel_appears_most_archive_user_list = [0, 0, 0, 0, 0]
    vowel_appears_most_archive_user = 0
    
    with open(txt_file_path_user, 'r') as txt_archive_user:
        i = 0
        for line_archive_user in txt_archive_user.readlines():
            line_archive_user = line_archive_user.split()
            i += 1

            for word_archive_user in line_archive_user:
                if len(word_archive_user) > num_characters_biggest_word_archive_user:
                    biggest_words_archive_user = word_archive_user
                    num_characters_biggest_word_archive_user = len(word_archive_user)
                elif len(word_archive_user) == num_characters_biggest_word_archive_user:
                    biggest_words_archive_user += f", {word_archive_user}"

                if first_line_syllable_cao_appear == 0:
                    if ("cao" in word_archive_user) or ("ção" in word_archive_user):
                        first_line_syllable_cao_appear = i

                num_words_archive_user += 1

                for letter_archive_user in word_archive_user.lower():
                    if letter_archive_user == "a":
                        vowel_appears_most_archive_user_list[0] += 1
                    elif letter_archive_user == "e":
                        vowel_appears_most_archive_user_list[1] += 1
                    elif letter_archive_user == "i":
                        vowel_appears_most_archive_user_list[2] += 1
                    elif letter_archive_user == "o":
                        vowel_appears_most_archive_user_list[3] += 1
                    elif letter_archive_user == "u":
                        vowel_appears_most_archive_user_list[4] += 1

    return (vowel_appears_most_archive_user_list, num_words_archive_user, first_line_syllable_cao_appear, biggest_words_archive_user, num_characters_biggest_word_archive_user, vowel_appears_most_archive_user)

def print_informations_for_user(vowel_appears_most_archive_user_list, num_words_archive_user, first_line_syllable_cao_appear, biggest_words_archive_user, num_characters_biggest_word_archive_user, vowel_appears_most_archive_user):
    print(f'Quantidade de palavras existentes no arquivo: {num_words_archive_user}.')

    print(f'Palavra(s) com mais caracteres ({num_characters_biggest_word_archive_user}): {biggest_words_archive_user}.')

    for i, number in enumerate(vowel_appears_most_archive_user_list):
        if number > vowel_appears_most_archive_user:
            number = vowel_appears_most_archive_user
            vowel_index = i
    vowel_appears_most_archive_user = "aeiou"[vowel_index]
    print(f'Vogal que mais aparece: {vowel_appears_most_archive_user}, com {vowel_appears_most_archive_user_list[vowel_index]} aparições.')

    if first_line_syllable_cao_appear == 0:
        print('No arquivo, não foi encontrado a sílaba "cao" ou "ção".')
    else:
        print(f'No arquivo, a primeira sílaba cao/ção encontrada ocorreu na linha {first_line_syllable_cao_appear}.')

def main():
    txt_file_path_user = valid_user_archive_path()
    necessary_variables = defines_generic_informations_from_file_user(txt_file_path_user)
    print_informations_for_user(*necessary_variables)

if __name__ == "__main__":
    main()