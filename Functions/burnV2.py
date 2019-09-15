def burnV2(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)
