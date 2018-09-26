
import Image
import sys
from struct import *
import array

image_name = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
print "width=", width, "height=", height

f_y = open(image_name, "rb")
outFileName = 'output/out1.yuv'
fd_out = open(outFileName, "wb")

######################################################Y Channel
for i in range(0, height):
	readstr = f_y.read(width);	
	fd_out.write(readstr);
	if i==0 or i==439 or i==440 or i==879 or i==880 or i==1319 or i==1320 or i==1759:
		for k in range(0,4):
			fd_out.write(readstr);
######################################################U Channel
for i in range(0, height/2):
	readstr = f_y.read(width/2);
	fd_out.write(readstr)
	if i==0 or i==439/2 or i==440/2 or i==879/2 or i==880/2 or i==1319/2 or i==1320/2 or i==1759/2:	#if i==440/2:
		for k in range(0,2):
			fd_out.write(readstr);
######################################################V Channel
for i in range(0, height/2):
	readstr = f_y.read(width/2);
	fd_out.write(readstr)
	if i==0 or i==439/2 or i==440/2 or i==879/2 or i==880/2 or i==1319/2 or i==1320/2 or i==1759/2:	#if i==440/2:
		for k in range(0,2):
			fd_out.write(readstr);
f_y.close()
fd_out.close()

######################################################Add Vertical Padding
fd0 = open('output/out1.yuv', "rb")
fd1 = open('output/out2.yuv', "wb")

new_height= 1792
new_width = 3520
######################################################Y Channel
for i in range(0, new_height):
    for j in range(0, new_width):
	readstr = fd0.read(1);	
	fd1.write(readstr);
	if j==0 or j==439 or j==440 or j==879 or j==880 or j==1319 or j==1320 or j==1759 or j==1760 or j==2199 \
or j==2200 or j==2639 or j==2640 or j==3079 or j==3080 or j==3519:
            for k in range(0,4):
		fd1.write(readstr);
######################################################U Channel
for i in range(0, new_height/2):
    for j in range(0, new_width/2):
        readstr = fd0.read(1);	
	fd1.write(readstr);
	if j==0 or j==439/2 or j==440/2 or j==879/2 or j==880/2 or j==1319/2 or j==1320/2 or j==1759/2 or j==1760/2 or j==2199/2 \
or j==2200/2 or j==2639/2 or j==2640/2 or j==3079/2 or j==3080/2 or j==3519/2:
		for k in range(0,2):
			fd1.write(readstr);
######################################################V Channel
for i in range(0, new_height/2):
    for j in range(0, new_width/2):
	readstr = fd0.read(1);	
	fd1.write(readstr);
	if j==0 or j==439/2 or j==440/2 or j==879/2 or j==880/2 or j==1319/2 or j==1320/2 or j==1759/2 or j==1760/2 or j==2199/2 \
or j==2200/2 or j==2639/2 or j==2640/2 or j==3079/2 or j==3080/2 or j==3519/2:
		for k in range(0,2):
			fd1.write(readstr);

