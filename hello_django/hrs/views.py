from datetime import datetime
from random import randrange

from django.shortcuts import render

# Create your views here.
def home(request):
    fruits = ['苹果', '香蕉', '榴莲', '荔枝', '芒果', '草莓']
    start = 0
    end = randrange(len(fruits))
    fruits = fruits[start:end + 1]
    ctx = {
        'greeting': '你好世界',
        'current_time': datetime.now(),
        'num':len(fruits),
        'fruits': fruits
    }
    # 第二个参数是模板页面（路径在settings中配置）
    # 第三个参数是一个字典（替换模板中的占位符）
    return render(request, 'index.html', ctx)