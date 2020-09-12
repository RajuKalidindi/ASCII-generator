from PIL import Image, ImageDraw

path = input('Enter the path\n')

chars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '=', 'M', 'W', '&', '8', '%', 'B', '@', '$']
select = len(chars) / 256
try:
    image = Image.open(path)
except IOError:
    print("The entered path is invalid. Please recheck!")
    exit()

space = 10
n_width = 100
width, height = image.size
ratio = height / width
n_height = int(ratio * n_width)
image = image.resize((n_width, n_height))
width, height = image.size
pixel = image.load()

color = Image.new('RGB', (space * width, space * height), color = (0, 0, 0))
c = ImageDraw.Draw(color)

for i in range(width):
    for j in range(height):
        r, g, b = pixel[i, j]
        m = int((r + g + b) / 3)
        pixel[i, j] = (m, m, m)
        c.text((i * space, j * space), chars[int(m * select)], fill = (r, g, b))

color.save('color.jpg')
color.show()
im = Image.open('color.jpg').convert('L')
im.save('bw.jpg')
im.show()

