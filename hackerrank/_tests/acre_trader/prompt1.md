1. Pixelated Farmland Imagery
AcreTrader has recently acquired some low-resolution aerial farmland
imagery. The imagery is represented as a 2D array of pixels, where
each pixel is composed of a length-3 RGB code. Each pixel represents
a single parcel of farmland. Each parcel of farmland grows exactly only
1 type of crop: corn, soy, or wheat. We would like to figure out what
crops are being grown in each farm by analyzing the imagery. Each
pixel is represented as a string with the following format:

" ( {R}, {G}, {B}) "

where each value of R/G/B is number in the range 0-255. For
example, the following list is an example of a 3x3 image (displayed
below).

CE' (255, 222, 89)', ' (18, 123, 0)', ' (132, 187, 49) '] ,
[' (246, 213, 188) ', ' (5, 131, 0)', ' (11, 151, 7)'],
[' (17, 130, 0)', '(233, 221, 183)', ' (132, 187, 49) ']]

The reference color codes for the targeted crops are as follows:
corn: (251, 236, 94)
soy: (13, 138, 4)
wheat: (245, 222, 180)
Based on the pixel data supplied in the imagery, count the total
number of farms growing each type of crop. Count the crops based
on the following guidelines:
1. If a pixel's color code matches exactly to its reference color, count the
pixel towards the matching crop.
2. If a pixel's color code does not match exactly to its reference color,
count the pixel towards the crop that is the most similar to the
reference color by its euclidean distance to the reference color.
3. If a pixel's color code is equidistant to two or more reference colors,
add half a point (0.5) for each crop it is equidistant to.
4. An image will always contain at least one pixel.
5. An image is not guaranteed to have equal width and height.
Complete the function by returning the data in a list of counts in the
order of [corn, soy, wheat], like below:
[20.0, 14.5, 12.0]
Please return counts as a list of float types.

The reference color codes for the targeted crops are as follows:
corn: (251, 236, 94)
soy: (13, 138, 4)
wheat: (245, 222, 180)
Based on the pixel data supplied in the imagery, count the total
number of farms growing each type of crop. Count the crops based
on the following guidelines:
1. If a pixel's color code matches exactly to its reference color, count the
pixel towards the matching crop.
2. If a pixel's color code does not match exactly to its reference color,
count the pixel towards the crop that is the most similar to the
reference color by its euclidean distance to the reference color.
3. If a pixel's color code is equidistant to two or more reference colors,
add half a point (0.5) for each crop it is equidistant to.
4. An image will always contain at least one pixel.
5. An image is not guaranteed to have equal width and height.
Complete the function by returning the data in a list of counts in the
order of [corn, soy, wheat], like below:
[20.0, 14.5, 12.0]
Please return counts as a list of float types.