from matplotlib import pyplot
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
    while Char_Idx< len(Image_chars):
        for vert in Image_height_list:
            vert_pix_in_layer.append(Image_chars[Char_Idx: Char_Idx+Image_width_pixels])
            Char_Idx += Image_width_pixels
        ImageLayers.append(vert_pix_in_layer.copy())
        vert_pix_in_layer.clear()

# PartA: find 0s and 1s in

Layer_data = []
for Layer in ImageLayers:
    zeros=0
    ones=0
    twos = 0
    for image_row in Layer:
        zeros += image_row.count('0')
        ones += image_row.count('1')
        twos += image_row.count('2')
    Layer_data.append([zeros, ones, twos])

Layer_data.sort(key=lambda x: x[0])
Result = Layer_data[0][1] * Layer_data[0][2]
print('Answer Part1 = ', Result)

# part B 2

# create Imagelayer representation (deserialization)
def CompareImageLayers(TopLayer, ImageLayer)->list:
    newTopLayer = []
    for row_index in range(len(ImageLayer)):
        newTopLayer.append(compareRowStr(TopLayer[row_index],ImageLayer[row_index]))
    return newTopLayer

def compareRowStr(TopLayer_Row, ImageLayer_Row)-> str:
    mystr = ''
    for char_index in range(len(TopLayer_Row)):
        mystr += determine_visable_pixel_value(ImageLayer_Row[char_index], TopLayer_Row[char_index])
    return mystr

def determine_visable_pixel_value( NextLayerPixelValue: str, TopValue: str)-> str:
    if TopValue == '2':
       return NextLayerPixelValue
    elif TopValue =='1':
       return TopValue
    elif TopValue == '0':
        return TopValue

TopLayer = ImageLayers[0].copy()
for ImageLayer in range(1,len(ImageLayers)):
    TopLayer = CompareImageLayers(TopLayer, ImageLayers[ImageLayer])
for row in range(len(TopLayer)):
    TopLayer[row] = TopLayer[row].replace('0',' ')
    TopLayer[row] = TopLayer[row].replace('1', '#')
    print(TopLayer[row])
