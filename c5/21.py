import pickle

data = '14this is a line'
with open('t.txt', 'wb') as f:
    pickle.dump(data, f)



