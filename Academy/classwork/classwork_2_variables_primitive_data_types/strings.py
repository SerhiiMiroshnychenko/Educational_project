"""Strings"""

print('foo' * -8)
print(len('foo' * -8))
print('foo' * 0)
print(chr(38))
print(ord("#"))
s = 'foobar'
print(s[5:0:-2])
s = '12345' * 5
print(s[::-5])
print('FOO Bar 123 baz qUX'.swapcase())
# s.count(<sub>[, <start>[, <end>]]) Підраховує випадки входження підрядка в цільовий рядок
print('foo goo moo'.count('oo'))
print('foo goo moo'.count('oo', 0, 8))
# s.endswith(<suffix>[, <start>[, <end>]]) Визначає, чи закінчується цільовий рядок даним підрядком
print('foobar'.endswith('bar'))
print('foobar'.endswith('baz'))
print('foobar'.endswith('oob', 0, 4))
print('foobar'.endswith('oob', 2, 4))
# s.find(<sub>[, <start>[, <end>]]) Шукає заданий підрядок у цільовому рядку
print('foo bar foo baz foo qux'.find('foo'))
print('foo bar foo baz foo qux'.find('grault'))
print('foo bar foo baz foo qux'.find('foo', 4))
print('foo bar foo baz foo qux'.find('foo', 4, 7))
# s.index(<sub>[, <start>[, <end>]]) Шукає заданий підрядок у цільовому рядку
# s.rfind(<sub>[, <start>[, <end>]]) Шукає в цільовому рядку заданий підрядок, починаючи з кінця
print('foo bar foo baz foo qux'.rfind('foo'))
print('foo bar foo baz foo qux'.rfind('grault'))
print('foo bar foo baz foo qux'.rfind('foo', 0, 14))
print('foo bar foo baz foo qux'.rfind('foo', 10, 14))
# s.rindex(<sub>[, <start>[, <end>]]) Шукає в цільовому рядку заданий підрядок, починаючи з кінця
# s.startswith(<prefix>[, <start>[, <end>]]) Визначає, чи цільовий рядок починається з заданого підрядка
print('foobar'.startswith('foo'), 'foobar'.startswith('bar'), 'foobar'.startswith('bar', 3), 'foobar'.startswith('bar', 3, 2))
# s.isalnum() Визначає, чи цільовий рядок складається з буквено-цифрових символів
# s.isalpha() Визначає, чи складається цільовий рядок із символів алфавіту
# s.isdigit() Визначає, чи цільовий рядок складається з цифр
# s.isidentifier() Визначає, чи є цільовий рядок дійсним ідентифікатором Python
print('foo32'.isidentifier(), '32foo'.isidentifier(), 'foo$32'.isidentifier())

from keyword import iskeyword
print(iskeyword('and'))
# s.islower() Визначає, чи символи цільового рядка є малими літерами
# s.isprintable() Визначає, чи цільовий рядок складається повністю з друкованих символів
print('a\tb'.isprintable(), 'a b'.isprintable(),''.isprintable(), 'a\nb'.isprintable()) # це єдиний .isxxxx()метод, який повертає, Trueякщо sце порожній рядок. Усі інші повертаються Falseдля порожнього рядка.
# s.isspace() Визначає, чи цільовий рядок складається з пробілів
print(' \t \n '.isspace(), '   a   '.isspace(),  '\f\u2005\r'.isspace())
# \f\u2005\r --> Однак є кілька інших символів ASCII, які кваліфікуються як пробіли
# s.istitle() Визначає, чи цільовий рядок має регістр заголовка
print('This Is A Title'.istitle(), 'This is a title'.istitle(), 'Give Me The #$#@ Ball!'.istitle())
# s.isupper() Визначає, чи є символи алфавіту цільового рядка великими
print('ABC'.isupper(), 'ABC1$D'.isupper(), 'Abc1$D'.isupper())
# s.center(<width>[, <fill>]) Центрує рядок у полі
print('foo'.center(10), 'bar'.center(10, '-'), 'foo'.center(2))
# s.expandtabs(tabsize=8) Розгортає вкладки в рядку
print('a\tb\tc'.expandtabs(), 'aaa\tbbb\tc'.expandtabs(), 'a\tb\tc'.expandtabs(4), 'aaa\tbbb\tc'.expandtabs(tabsize=4))
# s.ljust(<width>[, <fill>]) Вирівнює рядок у полі за лівим краєм
print('foo'.ljust(10)< 'foo'.ljust(10, '-'), 'foo'.ljust(2))
# s.lstrip([<chars>]) Вирізає початкові символи з рядка
print('   foo bar baz   '.lstrip())
print('\t\nfoo\t\nbar\t\nbaz'.lstrip(), 'http://www.realpython.com'.lstrip('/:pth'))
# s.replace(<old>, <new>[, <count>]) Замінює входження підрядка в рядок
print('foo bar foo baz foo qux'.replace('foo', 'grault'), 'foo bar foo baz foo qux'.replace('foo', 'grault', 2))
# s.rjust(<width>[, <fill>]) Вирівнює рядок у полі за правим краєм
print('foo'.rjust(10), 'foo'.rjust(10, '-'), 'foo'.rjust(2))
# s.rstrip([<chars>]) Вирізає кінцеві символи з рядка

# Далі тут: https://realpython.com/python-strings/
