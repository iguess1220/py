def trim(s):
    if not isinstance(s,str):
        raise TypeError("bad operand type")
    if s != '':
      if s[:1] == ' ':
        return trim(s[1:])
      elif s[-1] == ' ':
        return trim(s[:-2])
      else :
        return s
    else:
        return s
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')