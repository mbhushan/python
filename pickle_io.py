import pickle

shopfile = "shopfile.txt"

shoplist = ['mango', 'banana', 'carrot']

f = open(shopfile, 'wt')

pickle.dump(shoplist, f)
f.close()

del shoplist

f = open("shopfile.txt",'rt')

storedlist = pickle.load(f)

print storedlist
