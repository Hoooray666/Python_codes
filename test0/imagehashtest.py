import imagehash
from PIL import Image
path1 = 'E:\\Python_codes\\test0\\images\\test0.bmp'
path2 = 'E:\\Python_codes\\test0\images\\football.jpg'

hash1 = imagehash.average_hash(Image.open(path1))
hash2 = imagehash.average_hash(Image.open(path2))
print(hash1-hash2)

hash1 = imagehash.phash(Image.open(path1))
hash2 = imagehash.phash(Image.open(path2))
print(hash1-hash2)

hash1 = imagehash.dhash(Image.open(path1))
hash2 = imagehash.dhash(Image.open(path2))
print(hash1-hash2)

hash1 = imagehash.whash(Image.open(path1))
hash2 = imagehash.whash(Image.open(path2))
print(hash1-hash2)
# print(hash2)


