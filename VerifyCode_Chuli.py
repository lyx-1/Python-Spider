from PIL import Image

if __name__ == '__main__':
    image = Image.open('captcha.jpg')
    # image.show()

    image = image.convert('L')
    image.show()
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    image.show()