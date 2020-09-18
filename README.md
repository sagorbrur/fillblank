# Fill Blank
In our early education day, while learning english one of the most important task was to fill the blanks. 

Two type of question was provided:

* Cloze test with clues
* Cloze test without clues

It was totally difficult for non native English learner to fill the blanks. And cloze test without cloze was the most trickier.

But now a days machine can fill the blanks smartly. Mask Language Modeling(MLM) based language model give machine such power. 

**FillBlank** is a [BERT](https://huggingface.co/bert-base-uncased) based package, can fill `cloze test without clues` type text. This package mostly build using [huggingface](https://huggingface.co/transformers) transformers.

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

