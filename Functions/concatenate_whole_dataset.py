def Concatenate_whole_Dataset(F_Dataset,S_Dataset,N_images,outname,location):
    for i in range(0,N_images):
        filename1 = os.path.basename('ExtraData/Faces/256_'+str(i)+'.jpg')  # returns 'helpers_image.tif'
        filename2 = os.path.basename('ExtraData/Sketch/256_'+str(i)+'.jpg') # return 'helpers_image.qml'

        location1='ExtraData/Faces/256_'+str(i)+'.jpg'
        location2='ExtraData/Sketch/256_'+str(i)+'.jpg'
        # Thanks to Cyrbil for noticing a bug here
        name1 = filename1.rsplit('.', 1)[0]  # returns 'helpers_image'
        name2 = filename2.rsplit('.', 1)[0]  # return 'helpers_image'

        outname=outname+str(i)
        if name1 == name2:  # This is True for this exact case
            get_concat_h_cut(location1, location2,location,outname,".jpg")
