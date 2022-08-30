"""
https://huggingface.co/
"""

import numpy as np
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoConfig,
)


class TransformersModelBase:
    def __init__(self):
        if not hasattr(self, "full_model_name"):
            raise RuntimeError("Use subclasses instead")

        self.tokenizer = AutoTokenizer.from_pretrained(self.full_model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.full_model_name
        )
        self.config = AutoConfig.from_pretrained(self.full_model_name)

    def labels(self):
        return list(self.config.id2label.values())

    def predict(self, message):
        inputs = self.tokenizer(message, return_tensors="pt")
        logits = self.model(**inputs).logits.detach().numpy()
        e = np.exp(logits)
        outputs = e / e.sum()  # softmax
        assert outputs.size == len(self.labels())
        return dict(
            (label, outputs.item(i))
            for (i, label) in self.config.id2label.items()
        )


class BertBaseMultilingualUncasedSentiment(TransformersModelBase):
    full_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"


class DehatebertMonoFrenchModel(TransformersModelBase):
    full_model_name = "Hate-speech-CNERG/dehatebert-mono-french"


class TwitterXlmRobertaBaseSentiment(TransformersModelBase):
    full_model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
