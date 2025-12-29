# Hanzi Chaizi | 汉字拆字

[![PyPI version](https://img.shields.io/pypi/v/hanzi_chaizi)](https://pypi.org/project/hanzi_chaizi/)
[![Python](https://img.shields.io/pypi/pyversions/hanzi_chaizi)](https://pypi.org/project/hanzi_chaizi/)
[![CI](https://github.com/howl-anderson/hanzi_chaizi/actions/workflows/python-app.yml/badge.svg)](https://github.com/howl-anderson/hanzi_chaizi/actions/workflows/python-app.yml)
[![License](https://img.shields.io/github/license/howl-anderson/hanzi_chaizi)](https://github.com/howl-anderson/hanzi_chaizi/blob/master/LICENSE)

Chinese character decomposition library for NLP and deep learning applications.

Decompose Chinese characters into basic structural components. Characters with similar structures yield similar decomposition results, making this useful as a glyph feature for deep learning models.

汉字拆字：将汉字拆解为基础部件。字形相似的字会得到相似的拆解结果，可用于深度学习模型的字形特征提取。

## Features | 特性

- Covers 20,000+ Chinese characters | 覆盖 20,000+ 汉字
- Zero third-party dependencies | 零第三方依赖
- Python 3.10+ support | 支持 Python 3.10+

## Installation | 安装

```bash
pip install hanzi_chaizi
```

## Usage | 使用

```python
from hanzi_chaizi import HanziChaizi

hc = HanziChaizi()
result = hc.query('名')

print(result)
```

Output | 输出:

```text
['夕', '口']
```

## Notes | 说明

Some characters (e.g. 农, 表, 衣, 囊) contain `\uf7ee` in their decomposition results. This is a Unicode Private Use Area character representing the bottom part of 衣 (the downward strokes), which has no standard Unicode codepoint.

部分汉字（如 农、表、衣、囊）的拆解结果中包含 `\uf7ee`。这是一个 Unicode 私有区域字符，用于表示"衣"的下半部分（撇捺结构），该部件在标准 Unicode 中没有独立编码。

Some characters cannot be decomposed. See [non_decomposable.txt](non_decomposable.txt) for the list.

部分汉字无法被拆解，详见 [non_decomposable.txt](non_decomposable.txt)。

## Development | 开发

See [develop.md](develop.md) for development guide. | 参见 [develop.md](develop.md) 开发指南。

## Credits | 致谢

Data from [漢語拆字字典](https://github.com/kfcd/chaizi) (CC BY 3.0) | 数据来自 [漢語拆字字典](https://github.com/kfcd/chaizi) (CC BY 3.0)

## Citation | 引用

```
@misc{kong2018hanzichaizi,
  title={Hanzi Chaizi},
  author={Xiaoquan Kong},
  howpublished={https://github.com/howl-anderson/hanzi_chaizi},
  year={2018}
}
```

If the package is cited in books, seminars, and academic research papers, or used in company products, you are welcome (but not required) to email me about this. I'm glad to see the package being used and valuable to everyone.

如果本项目被书籍、学术论文引用，或被公司产品使用，欢迎（但不强求）告知我。很高兴看到这个项目对大家有价值。
