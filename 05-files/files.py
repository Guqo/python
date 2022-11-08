def textfile_read(path, encoding='utf-8'):
    '''
    Načtení textového souboru

    :param path: cesta k souboru (string)
    :param encoding: ködování (string)
    :return: data v podobě řetězce (string)
    '''
    try:
        with open(path, encoding) as file:
            data = file.read()
        return data
    except FileNotFoundError as error:
        print(f"Soubor nebyl nalezen: {error},{type(error)}")
        data = False
    except Exception as error:
        print(f"Chyba načtení souboru: {error},{type(error)}")
        data = False
    finally:
        print("Tohle se provede vždy")
    return data

def textfile_write(path, text='', encoding='utf-8'):
    '''
    Načtení textového souboru

    :param path: cesta k souboru (string)
    :param text: textová data (string)
    :param encoding: ködování (string)
    :return: data v podobě řetězce (string)
    '''
    try:
        with open(path, mode="w", encoding=encoding) as file:
            file.write(text)
            result = True
    except FileNotFoundError as error:
        print(f"Soubor nebyl nalezen: {error},{type(error)}")
        result = False
    except Exception as error:
        print(f"Chyba zápisu souboru: {error},{type(error)}")
        result = False
    finally:
        # print("Tohle se provede vždy")
    return result