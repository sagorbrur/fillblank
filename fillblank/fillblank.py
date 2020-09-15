import nltk

import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

from transformers import pipeline


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("punkt not found. downloading...")
    nltk.download('punkt')

class FillBlank:
  def __init__(self):
    self.unmasker = pipeline('fill-mask', model='bert-base-uncased')

  def fill(self, text):
    text = text.replace('<blank>', '[MASK]')
    output_dict = {}
    output_text = ""
    output_tokens = []
    sentences = tokens = nltk.tokenize.sent_tokenize(text)
    for sen in sentences:
      if '[MASK]' in sen:
        res = unmasker(sen)
        tokens = res[0]['sequence'].split()
        tokens = tokens[1:-1]
        result = " ".join(tokens)
        result = result.replace(res[0]['token_str'], '<'+res[0]['token_str']+'>')
        output_text+=result+" "
        output_tokens.append(res[0]['token_str'])

      else:
        output_text+=sen+" "

    output_dict = {
        'text': output_text,
        'predict_words': output_tokens
    }

    return output_text, output_dict



# if __name__ == "__main__":
#     fillblank = FillBlank()
#     text = "what a <blank>! She <blank> to eat."
#     output, dic = fillblank.fill(text)
#     print(output)
#     print(dic['text'])
#     print(dic['predict_words'])  
