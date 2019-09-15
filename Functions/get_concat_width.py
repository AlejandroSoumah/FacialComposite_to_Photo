def get_concat_h_cut(img1_lct, img2_lct , outpath , outname , ext ):

    # img1_lct --> It's the location of the first image
    # img1_lct --> It's the location of the second image
    # outpath -->It's the location where the created image will be saved
    # outname --> The name of the file
    # ext --> The extension of the file
    im1 = Image.open(img1_lct)
    im2 = Image.open(img2_lct)
    dst = Image.new('RGB', (im1.width + im2.width, min(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))

    dst.save(outpath+'/'+outname+ext)
