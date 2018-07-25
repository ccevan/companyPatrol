
from pyecharts import Bar,Line
import random

# bar = Bar("主标题","副标题")
# month = ['{}月'.format(i) for i in range(1,13)]
# v1 = [random.randint(100,200) for i in range(1,13)]
# v2 = [random.randint(100,200) for i in range(1,13)]
# bar.use_theme("dark")
# bar.add('蒸发量',month,v1,mark_line=['average'],mark_point=['max','min'],is_convert=True)
# bar.add('降水量',month,v2,mark_line=['average'],mark_point=['max','min'],is_convert=True)

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1,is_label_show=True,is_datazoom_show=True,
        datazoom_type='both',datazoom_range=[50,100],yaxis_rotate=30,yaxis_min=5)
bar.render('html/months.html')

# xaxis_rotate=30 x轴坐标值旋转30度
# yaxis_rotate=30 y轴坐标值旋转30度
# yaxis_min=5 表示y轴最小值为5(数值轴有效)
# xaxis_min=5 表示x轴最小值为5(数值轴有效)