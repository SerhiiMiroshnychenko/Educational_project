from string import Template

"""The greeting program."""

name = 'Serhii'
day = 'Friday'

# String Interpolation / f-Strings (Python 3.6+)
print(f"Good day, {name}! {day} is a perfect day to learn some Python.")

# “New Style” String Formatting (str.format)
print('Good day, {}! {} is a perfect day to learn some Python.'.format(name, day))
print('Good day, {1}! {0} is a perfect day to learn some Python.'.format(day, name))
print('Good day, {name}! {day} is a perfect day to learn some Python.'.format(day=day, name=name))

# “Old Style” String Formatting (% Operator)
print('Good day, %s! %s is a perfect day to learn some Python.' % (name, day))

# Template Strings (Standard Library)
t = Template('Good day, $name! $day is a perfect day to learn some Python.')
print(t.substitute(name=name, day=day))
