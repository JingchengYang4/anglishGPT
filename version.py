import pickle

with (open("data/en_dictionary_parsed_randomized.pickle", "rb")) as openfile:
    data = pickle.load(openfile)
    print(data[0])

with open('data/blacklist.pickle', 'wb') as writefile:
    pickle.dump([], writefile, protocol=pickle.HIGHEST_PROTOCOL)