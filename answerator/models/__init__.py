from answerator.models import transformers_models

_MODEL_CLASS_BY_NAME = {
    "dehatebert_mono_french": transformers_models.DehatebertMonoFrenchModel,
    "bert_base_multilingual_uncased_sentiment": transformers_models.BertBaseMultilingualUncasedSentiment,
    "twitter_xml_roberta_base_sentiment": transformers_models.TwitterXlmRobertaBaseSentiment,
}

MODELS = list(_MODEL_CLASS_BY_NAME.keys())


def load_model(name):
    return _MODEL_CLASS_BY_NAME[name]()
