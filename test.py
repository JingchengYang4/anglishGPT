import torch

print(torch.torch_version)

from title_maker_pro.word_generator import WordGenerator
word_generator = WordGenerator(
    device="mps",
    forward_model_path="models/non-exist/forward-dictionary-model-v1",
    inverse_model_path="models/non-exist/inverse-dictionary-model-v1",
    blacklist_path="models/non-exist/blacklist.pickle",
    quantize=False,
)


print(word_generator.generate_word_from_definition("᛫ toward or at the stern ᛬ to the rear of ᛫ toward the stern ᛫"))
