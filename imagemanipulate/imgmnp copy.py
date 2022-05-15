'''
amrita kj
may 2022
cp 12 - image manipulation write-up 

goal of the code:

to allow a user to manipulate images using the pillows library. 
by organizing numerous change options (ie. blur, rotate etc.) it should be user-friendly with clear instructions. 
the altered images should be saved into appropriate folders so the user can view them later.

point form plan:

pre-coding:
    -create folders for each type of edited image 
    -choose 10 jpeg images that the user will be able to choose between 
then:
    -organize image options and alter options into lists which can be easily called
    -create seperate functions for asking the user what they want to do. this way we can easily ask each on again
    -create seperate functions for each type of alteration. these functions will be nested in the previous y/n function
    -create a main function to organize all the other ones, and which will loop until the user quits
        -the user should be able to continue altering images until they select "quit"

'''
from PIL import Image, ImageFilter, ImageEnhance
import os, sys

flowers_list = ["flowers1", "flowers2", "flowers3", "flowers4", "flowers5", "flowers6", "flowers7", "flowers8", "flowers9", "flowers10"]
alter_list = ["rotate", "resize", "png", "black and white", "blur", "merge", "contrast", "show images"]
#some lists to organize the options in single lines 

def imageoptions():
    print('flowers + #1-10. ie: flowers1, flowers2, etc.') #incase we need to remind the user how to enter their choice

def alteroptions(x):
    for i in x:
        print ("-"+i)
    print("") #to display a list in an organized, bullet point fashion 

def askimage(): #ask user to choose an image 
    while True:
        global imgchoice, sit
        imgchoice = None
        print("saved images: ")
        alteroptions(flowers_list) #displays options 
        imgchoice = input("which image would u like to open? or (q) to quit: ").lower()
        if imgchoice == "q":
            sit = 1 #situations come into play later (to indicate what comes next)
            break     
        elif imgchoice in flowers_list:
            sit = 2
            userImage = Image.open(f"{imgchoice}.jpeg")
            userImage.show() #shows the user their image 
            break
        else:
            sit = 3
            break

def alteryn(): #asks user y/n to alters 
    while True:
        usryn = input("do you want to alter the image? (y/n): ").lower()
        if usryn == 'n':
            break #no alters- code moves on 
        elif usryn == 'y': 
            alteringimage()
            break #yes alters- continues to next function 
        else:
            print("invalid input ._.\n")
            continue
    
def alteringimage():
    while True:
        print("alter options: ")
        alteroptions(alter_list) #lists alter options from the organized list 
        usrchoice = input("which image alteration would u like to make?: ").lower()
        usrchoice.lower() #each option is assigned a number value within the list 
        if usrchoice in alter_list:
            if usrchoice == alter_list[0]: #ie. #0 in the list is = to rotate 
                rotate() #most functions are seperated, and called from another function
                break
            elif usrchoice == alter_list[1]:
                resize()
                break
            elif usrchoice == alter_list[2]:
                png()
                break
            elif usrchoice == alter_list[3]:
                bw()
                break
            elif usrchoice == alter_list[4]:
                blur()   
                break
            elif usrchoice == alter_list[5]: 
                while True: #choose an image to merge with 
                    imageoptions()
                    imgchoice2 = input("merge with which other image?: ").lower() 
                    if imgchoice2 in flowers_list:
                        mergelist = [f"{imgchoice}.jpeg",f"{imgchoice2}.jpeg"] #organizes the items to be merged using parameters 
                        break
                    else:
                        print("Invalid input\n")  
                merge(mergelist)
                break
            elif usrchoice == alter_list[6]:
                contrast()   
                break
            elif usrchoice == alter_list[7]:
                while True:
                    try: #ask user to identify the image they want to see
                        imageto_open = input('what is the images file name (ie. flowers1blur)?: ').lower()
                        images_edit = input('where was it saved? (ie. blur folder)?: ').lower()
                        newImage = Image.open(images_edit + '/' + imageto_open + '.jpeg')
                        newImage.show() #displays image 
                        break
                    except FileNotFoundError: #if unsuccessfully named, the code moves on 
                        print('oops! youve entered smt wrong ._.') 
                break 
                    

        else:
            print("invalid input\n")

def rotate(): #rotates the image based on how much the user idicated 
    while True:
        try:
            degrees = int(input("how many degrees would you like to rotate?: "))
            break
        except ValueError: #if the input is not a number, it repeats 
            print("invalid input ._.\n")
    pic = Image.open(f"{imgchoice}.jpeg")
    pic.rotate(degrees).save('rotate folder/'+imgchoice+'rotated.jpeg')
    print("saved in rotate folder\n") #in each function, the edited image is saved to its folder 

def resize():
    size200 = (200,200) #size option dimensions 
    size400 = (400,400)
    size600 = (600,600)
    while True:
        #asks the user for the size, then saves a thumbnail of the chosen size (either 200, 400 or 600)
        usrchoice = int(input("what size? (200, 400, 600): "))
        pic= Image.open(f"{imgchoice}.jpeg") 
        if usrchoice == 200:
            pic.thumbnail(size200)
            pic.save('size200/'+imgchoice+'200.jpeg')
            pic.save('all edited/'+imgchoice+'200.jpeg')
            print("saved to size200 \n") 
            break
        elif usrchoice == 400:
            pic.thumbnail(size400)
            pic.save('size400/'+imgchoice+'400.jpeg')
            print("saved to size400 \n")
            break
        elif usrchoice == 600:
            pic.thumbnail(size600)
            pic.save('size600/'+imgchoice+'600.jpeg')
            print("saved to size600\n")
            break
        else:
            print("Invalid input")

def png():
    pic = Image.open(f"{imgchoice}.jpeg")
    fn, fext = os.path.splitext(f"{imgchoice}.jpeg") #saves as a png file 
    pic.save('png folder/{}.png'.format(fn))
    print("saved in png folder\n")

def bw():
    pic = Image.open(f"{imgchoice}.jpeg")
    pic = pic.convert("L") #converts chosen image to black and white 
    pic.save('bw folder/'+imgchoice+'bw.jpeg')
    print("saved in bw folder\n")
  
def blur():
    while True:
        try:
            userBlur = float(input("how much would you like to blur (choose a number, 1-1000000000)?: "))
            break
        except ValueError: #if the blur amount is not a number, it will ask again 
            print("Invalid input\n")
    pic= Image.open(fr"{imgchoice}.jpeg")    
    im1 = pic.filter(ImageFilter.GaussianBlur(userBlur)) #blurs chosen image the given amount 
    im1.save('blur folder/'+imgchoice+'blur.jpeg')
    print("Saved in blur folder\n")

def merge(list): #merges 2 photos using the parameter created previously 
    images = [Image.open(x) for x in list]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths) #based on the width/height of each image, it proportionately positions the images 
    max_height = max(heights)
    pic1 = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for pic in images:
        pic1.paste(pic, (x_offset,0))
        x_offset += pic.size[0]
    pic1.save('merge folder/'+imgchoice+'merge.jpeg')
    print("saved in merge folder\n")
  

def contrast(): #increases the contrast of an image  
    pic= Image.open(f"{imgchoice}.jpeg")
    enh = ImageEnhance.Contrast(pic)
    enh.enhance(2.1).save('contrast folder/'+imgchoice+'contrast.jpeg')
    print("Saved in contrast folder\n")


def call(): #organizes the functions 
        while True:
            askimage()
            if sit == 1:
                print('u have quit') 
                return #ends code 
            elif sit == 2:
                break # situation 2 was the successful one, the code continues 
            else:
                print('invalid. try again.')
                continue #unsuccessful - will continue to ask to choose an image 
        alteryn() #continues to the alter section 

def imagemanipulation(): #the final code, which repeats until the user quits 
    call()
    while True:
        again = input('would u like to alter another (y/n)?:').lower()
        if again == 'y':
            call()
            continue 
        elif again == 'n':
            print('ok, bye!! :-]')
            return 
        else:
            print('invalid. try again._.')
            continue 

imagemanipulation() #the only function that needs to be called (!!)

