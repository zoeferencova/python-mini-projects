from translate import Translator

translator = Translator(to_lang='ko')

try:
    with open('test.txt', mode='r', encoding='utf-8') as my_file:
        text = ''.join(my_file.readlines())
        translation = translator.translate(text)
        with open('test.txt', mode='w', encoding='utf-8') as my_file:
            my_file.write(translation)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
