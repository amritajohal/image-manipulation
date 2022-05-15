from PIL import Image
import os 

'''
size300 = (300, 300)

while True:
    usrchoice = input('which image do u wanna modify (flowers1, flowers2 etc... -10)? ')
    usershow = Image.open(usrchoice + '.jpeg')
    usershow.show()
    confirm = input('is this correct? (y/n)')
    if confirm == 'y':
       break 

choice = input('how would u like to modify it (resize, black/white, blur, rotate)? ')

if choice == 'rotate':
    image1 = Image.open(usrchoice + '.jpeg')
    image1.rotate(90).save('rotate/' + usrchoice + '_rotate.jpeg')
    image2 = Image.open('rotate/' + usrchoice + '_rotate.jpeg')
    image2.show()
'''
'''
image1 = Image.open(r'sunflowerf/sunflower.jpeg')
image1.show()
'''
'''
x = 1
while x < 10:
    try: 
        image1 = Image.open(r'merge folder/flowers'+ str(x) +'Merge.jpeg')
        image1.show()
        x += 1
    except FileNotFoundError:
        break 
'''
'''
for filename in os.listdir("merge folder"):
   with open(os.path.join("merge folder", filename), 'r') as f:
       text = f.read()
       print(text)

'''
'''
imageto_open = input('which edited image would u like to see (ie. flowers1)?: ').lower
image_key = input('what was the chage made (ie. merge)?: ').lower
images_edit = input('where was it saved? (ie. blur folder)?: ').lower
print(r(images_edit + '/' + str(imageto_open) + str(image_key) + str('.jpeg')))
''''''
print('hi'+'hi')
x = 'hi'
y = 'hi 5'.upper()
print('hi'+ x + y)


'''

imageto_open = input('which edited image would u like to see (ie. flowers1blur)?: ').lower()
#image_key = input('what was the chage made (ie. merge)?: ').lower
images_edit = input('where was it saved? (ie. blur folder)?: ').lower()
print(images_edit + '/' + imageto_open + '.jpeg')













