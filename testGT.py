
import Image
import sys
from struct import *
import array

image_name = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
 
y = array.array('B')
u = array.array('B')
v = array.array('B')


f_y = open(image_name, "rb")
f_uv = open(image_name, "rb")
f_uv.seek(width*height, 1)

f_out = 'output/out.yuv'
fd_out = open(f_out, "wb")

image_out = Image.new("RGB", (width, height+4))
pix = image_out.load()
######################################################Y Channel
print "width=", width, "height=", height
for i in range(0, height):
    for j in range(0, width):
	readstr = f_y.read(1);	
	y.append(ord(readstr));
	fd_out.write(readstr);

	if i==440:
		for k in range(0,4):
			y.append(ord(readstr));
			fd_out.write(readstr);
			#print"Y add", k
print "Y size=", len(y)
######################################################U Channel
for i in range(0, height/2):
    for j in range(0, width/2):
	readstr = f_y.read(1);
        u.append(ord(readstr));
	fd_out.write(readstr)

	if i==440/2:
		for k in range(0,2):
			u.append(ord(readstr));
			fd_out.write(readstr);
			#print"U add", k
print "U size=", len(u) 
######################################################V Channel
for i in range(0, height/2):
    for j in range(0, width/2):
	readstr = f_y.read(1);
	v.append(ord(readstr));
	fd_out.write(readstr)
	if i==440/2:
		for k in range(0,2):
			v.append(ord(readstr));
			fd_out.write(readstr);
			#print"V add", k
print "V size=", len(v)

######################################################Show Image
for i in range(0,height):
    for j in range(0, width):     
#	print "i=", i, "j=", j , (i*width), ((i*width) +j)
        #pix[j, i] = y[(i*width) +j], y[(i*width) +j], y[(i*width) +j]
        Y_val = y[(i*width)+j]
        U_val = u[((i/2)*(width/2))+(j/2)]
        V_val = v[((i/2)*(width/2))+(j/2)]
        B = 1.164 * (Y_val-16) + 2.018 * (U_val - 128)
        G = 1.164 * (Y_val-16) - 0.813 * (V_val - 128) - 0.391 * (U_val - 128)
        R = 1.164 * (Y_val-16) + 1.596*(V_val - 128)
        pix[j, i] = int(R), int(G), int(B)
 
######################################################
# B = 1.164(Y - 16) + 2.018(U - 128)
# G = 1.164(Y - 16) - 0.813(V - 128) - 0.391(U - 128)
# R = 1.164(Y - 16) + 1.596(V - 128)
######################################################
#fd_y_out.append(fd_uv_out);
image_out.save("output/out.bmp")
image_out.show()
