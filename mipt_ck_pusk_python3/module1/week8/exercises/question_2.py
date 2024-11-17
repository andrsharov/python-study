class ParseError(Exception):
    """ Error while parsing file """
    def __init__(self, *args, line_no = None, text = None):
        super().__init__(*args)
        self.line_no = line_no
        self.text = text

    def __str__(self):
        if self.line_no is None and self.text is None:
            return f'standard message'
        elif self.line_no is not None and self.text is None:
            return f'cannot parse text on line {self.line_no}'
        elif self.line_no is None and self.text is not None:
            return f'cannot parse text: \'{self.text}\''
        elif self.line_no is not None and self.text is not None:
            return f'cannot parse text on line {self.line_no}: \'{self.text}\''

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
if issubclass(ParseError, Exception):
    print('OK')
else:
    print('FAIL')

if ParseError.__doc__.strip() == "Error while parsing file":
    print('OK')
else:
    print('FAIL')

try:
    raise ParseError('standard message')
except Exception as e:
    print(str(e))

try:
    raise ParseError('standard message', line_no=10)
except Exception as e:
    print(str(e))

try:
    raise ParseError(line_no=12)
except Exception as e:
    print(str(e))

try:
    raise ParseError('standard message', text='bkjhsdkjfh')
except Exception as e:
    print(str(e))

try:
    raise ParseError(text='bkjhsdkjfh', line_no=100)
except Exception as e:
    print(str(e))

try:
    raise ParseError('standard message', line_no=10)
except Exception as e:
    print(str(e))

try:
    raise ParseError(line_no=12)
except Exception as e:
    print(str(e))

try:
    raise ParseError('standard message', text='bkjhsdkjfh')
except Exception as e:
    print(str(e))

try:
    raise ParseError(text='bkjhsdkjfh', line_no=100)
except Exception as e:
    print(str(e))