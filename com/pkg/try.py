try:
    pass
except (IOError ,ZeroDivisionError) as e:
    print(e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'    #n != 0应该是True,断言失败，assert语句本身就会抛出AssertionError
    return 10 / n