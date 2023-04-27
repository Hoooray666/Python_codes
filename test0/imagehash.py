import imagehash
from PIL import Image
path1 = 'E:\\Python_codes\\test0\\images\\test0.bmp'
path2 = 'E:\\Python_codes\\test0\images\\football.jpg'

hash1 = imagehash.average_hash(Image.open(path1))
print(hash1)
