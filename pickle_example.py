import pickle
import os

arbitrary_data = {"hey" : [1, 2, 3], 10 : int}

print("Data to pickle:", arbitrary_data)

with open('example_out.pkl', 'wb') as fn:
    pickle.dump(arbitrary_data, fn)

with open('example_out.pkl', 'rb') as fn:
    loaded_data = pickle.load(fn)

print("Loaded pickle: ", loaded_data)

os.remove('example_out.pkl')
