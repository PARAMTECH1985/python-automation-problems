# Python program to illustrate
# matching a regular expression
# with asterisk(*)
import re
batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())