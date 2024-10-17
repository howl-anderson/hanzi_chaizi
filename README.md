# Hanzi decomposition (Chinese character decomposition) | 汉字拆字

> 拆字是指將一文字，以筆畫、字形等基本組成單位分解成多個文字。
> The decomposition of characters refers to breaking down a single character into multiple characters based on its basic components, such as strokes and structural elements.

> 汉字拆字让字型相似的字具有相似的拆解结果。
> Hanzi decomposition yields similar decomposition results for characters with similar structures.

> 这种特性可以被深度学习模型用来作为字的特征之一：字形的特征。
> This feature can be used by deep learning models as one of the features of characters: the structural feature.

## Installation

```bash
pip install hanzi_chaizi
```

## Usage

```python
from hanzi_chaizi import HanziChaizi

hc = HanziChaizi()
result = hc.query('名')

print(result)
```

Output:

```text
['夕', '口']
```



## Development

### Data source

Data from this project: [漢語拆字字典](https://github.com/kfcd/chaizi)

### parsing and convert data format

```bash
pytohn dev_scripts/parse.py
```

## Credits

Data from this project: [漢語拆字字典](https://github.com/kfcd/chaizi)

## Citation

```
@misc{kong2018hanzichaizi,
  title={Hanzi Chaizi},
  author={Xiaoquan Kong},
  howpublished={https://github.com/howl-anderson/hanzi_chaizi},
  year={2018}
}
```

If the package is cited in books, seminars, and academic research papers, or used in company products, you are welcome (but not required) to email me about this. I'm glad to see the package being used and valuable to everyone.

