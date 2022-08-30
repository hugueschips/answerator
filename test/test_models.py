import answerator.models

import numpy as np

TEST_VALUES = {
    "dehatebert_mono_french": {
        "Je suis vraiment satisfait!": {
            "HATE": 0.21370329038267621,
        },
        "Il est aussi moche que son pathetique chien": {
            "HATE": 0.5859833630943964,
        },
    },
}


def test_model_outpus():
    for (model_name, message_and_outputs) in TEST_VALUES.items():
        model = answerator.models.load_model(model_name)
        for (message, expected_outputs) in message_and_outputs.items():
            outputs = model.predict(message)
            for (label, expected_output) in expected_outputs.items():
                assert np.isclose(outputs[label], expected_output)
