
from pyecharts import Bar,Line
from pyecharts.engine import create_default_environment

bar = Bar("bar的主标题","bar的副标题")
bar.use_theme('dark')
bar.add('衣服',['春装','夏装','秋装','冬装'],[122,232,420,322],is_more_utils=True)

line = Line("主标题",'副标题')
line.use_theme('dark')
line.add('鞋子',['春','夏','秋','东'],[121,124,433,344],is_more_utils=True)

env = create_default_environment('html')
env.render_chart_to_file(bar,path='bar.html')
env.render_chart_to_file(line,path='line.html')

