import chardet
import cchardet
import charset_normalizer



if __name__ == '__main__':
    with open('file.xml', 'rb') as f:
        content = f.read()

    encoding = chardet.detect(content)['encoding']
    print('chardet: ', encoding)

    encoding = cchardet.detect(content)['encoding']
    print('cchardet: ', encoding)

    encoding = charset_normalizer.detect(content)['encoding']
    print('charset_normalizer: ', encoding)
