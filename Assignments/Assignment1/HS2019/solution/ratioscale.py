#!/usr/bin/env python3



#Previously, when we run the script in the terminal we had to provide 4 arguments: python3 path/ratioscale.py path/image.jpg newWidth newHeight
#Now the script is altered that we just can enter the width and not the height anymore, since we want that the image is scaled and that it has the same aspect ratio
#So now with the new script we just need to pass 3 arguments in the terminal: python3 path/ratioscale.py path/image.jpg newWidthOfImage

import stddraw
import sys
from picture import Picture


fileName = sys.argv[1]
w = int(sys.argv[2])

source = Picture(fileName)

#We need to calculate the scale factor (ratio between the old width and the new width to get the new height)
#So we divide the new width with the original width which we read from "source" (source is the original picture) which has an attribute .width()
scalefactor = w / source.width()

#Then we can calculate the new height (previous height times scalefactor).. it is important that we convert the height into an integer since we cannot have e.g. 0.5 Pixel and we could not run the for loop to redraw the picture with a floating point.
h = int(source.height() * scalefactor)

# The target is created with the new dimensions.
target = Picture(w, h)

for tCol in range(w):
    for tRow in range(h):
        sCol = tCol * source.width() // w
        sRow = tRow * source.height() // h
        target.set(tCol, tRow, source.get(sCol, sRow))

stddraw.setCanvasSize(w, h)
stddraw.picture(target)
# Picture gets presented.
stddraw.show()
