
Image_width_pixels = 25
Image_height_pixels = 6
ImageLayers = []
vert_pix_in_layer = []
Image_height_list = list(range(0, Image_height_pixels))
input_file = 'day8_input.txt'
with open(input_file, 'r') as file:
    Image_chars = file.read()

Char_Idx = 0
with open(input_file, 'r') as file:
    while Char_Idx< 1500:
        for vert in Image_height_list:
            vert_pix_in_layer.append(Image_chars[Char_Idx:Char_Idx+Image_width_pixels])
            Char_Idx+=Image_width_pixels
        ImageLayers.append(vert_pix_in_layer.copy())
        vert_pix_in_layer.clear()

Layer_data = []
for Layer in ImageLayers:
    zeros=0
    ones=0
    twos = 0
    for vert_layer in Layer:
        zeros += vert_layer.count('0')
        ones += vert_layer.count('1')
        twos += vert_layer.count('2')
    Layer_data.append([zeros, ones, twos])

Layer_data.sort(key=lambda x: x[0])
Result = Layer_data[0][1] * Layer_data[0][2]