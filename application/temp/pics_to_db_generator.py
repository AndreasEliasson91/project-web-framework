from application.dll.db import images

for i in range(5):
    file = f'C:/Users/andre/OneDrive/Skrivbord/father{i+1}.png'

    with open(file, 'rb') as f:
        contents = f.read()

    images.put(contents, filename=f'father{i+1}.png')
