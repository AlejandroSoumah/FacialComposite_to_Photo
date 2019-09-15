def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)
