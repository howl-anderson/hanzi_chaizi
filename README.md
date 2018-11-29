# 汉字拆字

> 拆字是指將一文字，以筆畫、字形等基本組成單位分解成多個文字。

汉字拆字让字型相似的字具有相似的拆解结果。

**这种特性可以被深度学习模型用来作为字的特征之一：字形的特征。**

## 使用
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



## 从原始数据生成
### 数据来源
数据来自于 [漢語拆字字典](https://github.com/kfcd/chaizi)

### 解析
```bash
pytohn ./parse.py
```

## 致谢
拆字数据来自于 [漢語拆字字典](https://github.com/kfcd/chaizi)


