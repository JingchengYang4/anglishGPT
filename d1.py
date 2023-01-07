import title_maker_pro.dictionary_definition
import random
import pickle

dictionary_path = "/Users/jingchengyang/Documents/Body.data"
parsed = []
num_tried = 0
error_titles = []

with open(dictionary_path, "rb") as f:
    for entry in title_maker_pro.dictionary_definition.DictionaryDefinition.gen_from_apple_dictionary(f):
        num_tried += 1
        try:
            parsed.append(title_maker_pro.dictionary_definition.AppleDictParser.parse(entry.parsed_entry))
        except title_maker_pro.dictionary_definition.InvalidParseAssumptionError:
            error_titles.append(0)

print(f"Error rate: {len(error_titles) / num_tried}")