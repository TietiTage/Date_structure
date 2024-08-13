import matplotlib.pyplot as plt
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

# 设置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 设置风格
plt.style.use('ggplot')

code = '''

'''

# 高亮代码并生成图片
formatter = ImageFormatter(font_name='Times New Roman', style='default')
highlighted_code = highlight(code, PythonLexer(), formatter)
highlighted_code.save('code.png')