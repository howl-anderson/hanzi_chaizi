# 汉字拆字

> 拆字是指將一文字，以筆畫、字形等基本組成單位分解成多個文字。
> 参数 char_type默认为0，取第一种拆分方式；char_type第二种，通常为偏旁部首拆分方式

汉字拆字让字型相似的字具有相似的拆解结果。

**这种特性可以被深度学习模型用来作为字的特征之一：字形的特征。**

## [使用](chaizi/README.md)
### 样例 1
```python
from hanzi_chaizi import HanziChaizi

hc = HanziChaizi()
result = hc.query('名')

print(result)
```

输出

```text
['夕', '口']
```

### 样例2:
```python
from hanzi_chaizi import HanziChaizi

hc = HanziChaizi()
result = hc.query('冰', char_type=1)

print(result)
```

输出

```text
['冫', '水']
```

## 安装方式
```bash
pip install git+https://github.com/ykf173/hanzi_chaizi.git@fix_bug_and_char_type
```


## 从原始数据生成
### 数据来源
数据来自于 [漢語拆字字典](https://github.com/kfcd/chaizi)

### 解析
```bash
pytohn ./parse.py
```

## 致谢
拆字数据来自于 [漢語拆字字典](https://github.com/kfcd/chaizi)

## 学术引用 / Citation

```
@misc{kong2018hanzichaizi,
  title={Hanzi Chaizi},
  author={Xiaoquan Kong},
  howpublished={https://github.com/howl-anderson/hanzi_chaizi},
  year={2018}
}
```

如果该软件包被书籍、研讨会和学术研究论文引用，或者在公司产品中使用，欢迎写邮件把这一个情况告诉我。我很高兴看到软件包能被使用，对大家有价值。

If the package is cited in books, seminars, and academic research papers, or used in company products, you are welcome (but not required) to email me about this. I'm glad to see the package being used and valuable to everyone.

