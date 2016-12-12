from picamera import PiCamera

cam =  PiCamera()


def capture_img(capture_resolution = (640, 480), square_size = 128:
        # Create the in-memory stream
    stream = io.BytesIO()

    cam.resolution = capture_resolution
    cam.capture(stream, format='jpeg')
    cam.close()

    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    img = Image.open(stream)
    img = image_utils.square(img)
    img = image_utils.scale(img, square_size)
    return img