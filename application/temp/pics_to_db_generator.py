from application.dll.db import images

for i in range(15):
    file = f'C:/Users/andre/OneDrive/Skrivbord/profile{i}.jpg'

    with open(file, 'rb') as f:
        contents = f.read()

    images.put(contents, filename=f'avatar{i+1}.jpg')
