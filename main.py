import charset_normalizer


if __name__ == '__main__':
    with open('file.xml', 'rb') as f:
        content = f.read()

    encoding = charset_normalizer.from_bytes(content).best().encoding
    print('encoding: ', encoding)
