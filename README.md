# Fill Blank
[![Colab Notebook](https://img.shields.io/badge/notebook-colab%20notebook-orange)](https://github.com/sagorbrur/fillblank/blob/master/notebook/fillblank.ipynb)

In our early education day, while learning English one of the most important tasks was to fill the blanks. 

Two types of question were provided:

* Cloze test with clues
* Cloze test without clues

It was totally difficult for non-native English learners to fill the blanks. And cloze test without cloze was the most tricky.

But nowadays the machine can fill the blanks smartly. Mask Language Modeling(MLM) based language model give machine such power. 

**FillBlank** is a [BERT](https://huggingface.co/bert-base-uncased) based package, can fill `cloze test without clues` type text. This package mostly builds using [huggingface](https://huggingface.co/transformers) transformers.

## Installation 

```
pip install fillblank
```

## Dependency
* pytorch 1.6+


## How to Fill The Blank

```py
from fillblank.fillblank import FillBlank
text = "what a <blank>! She <blank> to eat."
filltheblank = FillBlank()
output, output_dictionary = filltheblank.fill(text)
print(output)
print(output_dictionary['predict_words']) 
# what a <mess>! she <needed> to eat.
#['mess', 'needed']
```

