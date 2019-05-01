from django import template
from PIL import Image
import io
import urllib
import base64


register = template.Library()

def compute_height_and_width(image_sizes):

	width, height = image_sizes

	if width >= height and width <= 720:
		return width, height

	if height >= width and height <= 720:
		return width, height

	if width > height:
		remainder = width % 360
		without_remainder = width - remainder
		times = int(without_remainder / 360) - 1
	else:
		remainder = height % 360
		without_remainder = height - remainder
		times = int(without_remainder / 360) - 1

	if times > 5:
		times = times - 3

	width = int(width / times)
	height = int(height / times)
	return width, height



@register.filter
def get64(url):
	if url.startswith('http'):
		image_file = io.BytesIO(urllib.request.urlopen(url).read())

		with Image.open(image_file) as image:
			image_sizes = compute_height_and_width(image.size)
			image = image.resize(image_sizes, Image.ANTIALIAS)
			image_file = io.BytesIO()
			image.save(image_file, 'png', quality=90)

		base = base64.b64encode(image_file.getvalue())
		return 'data:image/jpg;base64,' + base.decode('utf-8')

	return url