# coding: utf-8

import colorsys

N = 5
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

print(RGB_tuples)

#print(colormap.rgb2hex(RGB_tuples[0][0], RGB_tuples[0][1], RGB_tuples[0][2]))


for (r,g,b) in RGB_tuples:
    print '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
#7f3f3f
#727f3f
#3f7f59
#3f597f
#723f7f
