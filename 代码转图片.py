import matplotlib.pyplot as plt
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

# ��������
plt.rcParams['font.family'] = 'Times New Roman'

# ���÷��
plt.style.use('ggplot')

code = '''

'''

# �������벢����ͼƬ
formatter = ImageFormatter(font_name='Times New Roman', style='default')
highlighted_code = highlight(code, PythonLexer(), formatter)
highlighted_code.save('code.png')