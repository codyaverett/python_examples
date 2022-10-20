## Several hacky things in here in attempts to create a file that can
## Easily be loaded into a c++ program as a pixel map for a friend

# # read in binary image file and
# with open("autumn.bin", "rb") as f:
#     # convert binery to a pixel map format
#     pixel_map = [int(x) for x in f.read().split(" ")]
#     # write pixel map to file
#     with open("autumn.txt", "w") as f:
#         f.write(str(pixel_map))
import struct
import sys

# load image with openc-python
import cv2
import pygame

import sys, fitz  # import the bindings

# fname = sys.argv[1]  # get filename from command line
pix = fitz.Pixmap("autumn.jpg")  # any supported input format
pix.save("autumn.ppm")  # any supported output format


print("Loading image...")

# load image
img = cv2.imread("autumn.jpg")

# convert image to pixel map named "gray"
# dir(cv2)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Create buffer for pixel map
# buffer = bytearray()

# # write pixel map to binary buffer
# for i in range(len(gray)):
#     buffer.extend(struct.pack("B", gray[i]))

# # write binary buffer to file
# with open("autumn.bin", "wb") as f:
#     f.write(buffer)

# rgb of each pixel


# print("Converting image to pixel map...")
# pixel_map = []
# for i in range(len(gray)):
#     for j in range(len(gray[i])):
#         pixel_map.append(gray[i][j])


# Create a pygame window
pygame.init()
screen = pygame.display.set_mode((len(pix[0]), len(pix)))
pygame.display.set_caption("Autumn")


# load pixel map binary file
with open("autumn5.bin", "rb") as f:
    # convert binery to a pixel map format
    pixel_map = [float(x) for x in f.read()]

# while window is open
while True:
    # check for events
    for event in pygame.event.get():
        # if window is closed
        if event.type == pygame.QUIT:
            # quit
            pygame.quit()
            sys.exit()

    # draw each pixel
    for i in range(len(pixel_map)):
        # get pixel color
        color = pixel_map[i]
        # draw pixel
        pygame.draw.rect(
            screen,
            (color, color, color),
            (i % len(gray[0]), int(i / len(gray[0])), 1, 1),
        )

    # update screen
    pygame.display.update()
