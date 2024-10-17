from setuptools import setup

setup(
    name="hanzi_chaizi",
    version="0.2",
    packages=["hanzi_chaizi"],
    url="https://github.com/howl-anderson/hanzi_chaizi",
    license="",
    author="Xiaoquan Kong",
    author_email="u1mail2me@gmail.com",
    description="""
The hanzi_chaizi package provides tools for breaking down Chinese characters into basic structural units, such as strokes and components. This decomposition reveals structural similarities between characters with similar shapes. These features can be used in deep learning models to capture character-based attributes, particularly shape-related ones, for applications like natural language processing or character recognition.
    """.strip(),
    include_package_data=True,
)
