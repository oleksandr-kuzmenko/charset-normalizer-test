
`from_bytes` method usage:
```
$ python main.py
encoding:  mac_greek
```

CLI usage:
```
$ normalizer file.xml
{
    "path": "/Users/alx/ws/charset-normalizer-test/file.xml",
    "encoding": "cp1251",
    "encoding_aliases": [
        "1251",
        "windows_1251"
    ],
    "alternative_encodings": [],
    "language": "Russian",
    "alphabets": [
        "Basic Latin",
        "Control character",
        "Cyrillic",
        "Latin-1 Supplement",
        "Letterlike Symbols"
    ],
    "has_sig_or_bom": false,
    "chaos": 10.0,
    "coherence": 0.0,
    "unicode_path": null,
    "is_preferred": true
}
```