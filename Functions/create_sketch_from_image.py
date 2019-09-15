def create_sketch_from_image(img_lct,sketch_lct,outname,ext,n_sketches):
    # img_lct --> It's the location of the images
    # sketch_lct --> It's the location of the generated sketch image
    # outname --> The name of the file
    # ext --> The extension of the file 256FaceNewData
    # n_sketches -->The number of sketches you will like to generate

    for i in range(0,n_sketches-1):
        img_rgb = cv2.imread(img_lct+'256_'+str(i)+'.jpg')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_gray_inv = 255 - img_gray
        img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
                                    sigmaX=100, sigmaY=100)


        img_blend = dodgeV2(img_gray, img_blur)
        sketch_pil = Image.fromarray(img_blend)
        sketch_pil.save(sketch_lct+'/'+outname+str(i)+ext)
