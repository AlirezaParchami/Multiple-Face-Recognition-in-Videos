import pickle

# Unpickling (de-serializing) a dictionary
with open('output.pickle', 'rb') as filename:
    dictionary = pickle.load(filename)

print(dictionary)

print(len(dictionary))