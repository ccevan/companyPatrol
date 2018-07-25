
from pyecharts import Bar

bar = Bar("收益表","服装收益表")
bar.use_theme('dark')

bar.add("服装",['夏装','秋装','春装','冬装'],['150','200','121','100'],is_more_utils=True)

bar.print_echarts_options()
bar.render(r'cloth.html')

