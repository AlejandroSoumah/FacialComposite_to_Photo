
def move_resize_images(path_old,path_new,ext,width,height,outname):

    # path old--> This is the old path of the folder you wish to move and resize
    # path new-->This is the new path of the folder you wish to place the resized images
    # ext --> This is the extension of the files
    # width --> The width you would like to resize your images to
    # height --> The height you would like to resize your images to
    # outname -->The name of the files you would like to resize and move

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path_old):
        for file in f:
            if '.jpg' or '.JPG' in file:
                files.append(os.path.join(r, file))

    # adjust width and height to your needs
    width = width
    height = height
    ext = ext

    for i in range(386,len(files)):
        im1 = Image.open(files[i])
        im2 = im1.resize((width, height), Image.NEAREST)
        im2.save(path_new+outname+str(387+i) + ext)
