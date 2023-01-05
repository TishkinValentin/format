import sys

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)

x = 1.23456789
print('1: %e | %f | %g' % (x, x, x))
print('2: %-6.2f | %010.2f | %+06.1f' % (x, x, x))
print('3: %(motto)-6.2f | %(pork)010.2f | %(food)+06.1f' % dict(motto=x, pork=x, food=x))
print('4: %(motto)s, %(pork)s and %(food)s %(motto)s' % dict(motto='spam', pork='ham', food='eggs'))
print('5: My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})
print('6: %(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop'))

print('Function *************************')
print('7: {0}, {1} and {2}'.format('spam', 'ham', 'eggs'))
print('8: {motto}, {pork} and {food}'.format(motto='spam', pork='ham', food='eggs'))
print('9: {motto}, {0} and {food} {1}'.format('ham', 'blabla', motto='spam', food='eggs'))
print('10: {}, {} and {}'.format('spam', 'ham', 'eggs'))
print('11: My {1[kind]} runs {0.platform}'.format(sys, {'kind' : 'laptop'}))
print('12: My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

print('13: {0:10} = {1:10}'.format('spam', 123.4567))
print('14: {0:>10} = {1:<10}'.format('spam', 123.4567))
print('15: {0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('16: {0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('17: {0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('18: {0:X}, {1:o}, {2:b}'.format(255, 255, 255))
print('19: {0:.{1}f}'.format(1 / 3.0, 4))
print('{:,d} {:,d}'.format(9999999999, 8888888888))
print('{:,.2f}'.format(296999.2567))

data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data)) # **data - здесь является специальным синтаксисом, который распаковывает словарь ключей и значений в индивидуальные присваивания ключевых слов "имя=значение"
print('My %(kind)-8s runs %(platform)8s' % data)