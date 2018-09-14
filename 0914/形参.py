#  def num_sum(x,y): # ※形参，给真实数据占位
#     """两个参数求和"""
#     print(x+y)
# num_sum(1,2) # 实参，设置得真实数据 


a = 10

# def test(a):
#     """当形参和变量同名时，在函数内用的是形参,形参只在函数内有效"""
#     a = 5
#     print(a)

# test('a')


def print_line(chart,num):
    """打印单行"""
    print(chart * num)
def print_lines(chart,chart_count,line_count):
    i = 0
    while i < line_count:
            print_line(chart,chart_count)
            i += 1
print_lines('*',30,1)
print_lines('=',30,1)
print_lines('*',30,1)
print_lines('=',30,1)
print_lines('*',30,1)
print_lines('=',30,1)

