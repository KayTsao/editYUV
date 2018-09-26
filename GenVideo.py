import Image
import sys
from struct import *
import array

f_in = sys.argv[1]
f_out = sys.argv[2] 
f_tmp = 'tmp.yuv'

dur = 10
frmRate = 30

width_in = 3520
height_in = 1760
width_out = 3584
height_out = 1792

tmp = array.array('B')

fd_tmp = open(f_tmp, 'wb+')	
with open(f_in, 'rb') as fd_in, open(f_out, 'wb') as fd_out:
    for i in range(dur*frmRate):
	print "Frame# ", i
	fd_tmp.seek(0,0)
######################################################Horizontal Padding
##Y Channel
	for j in range(0, height_in):
	    readstr = fd_in.read(width_in);	
	    fd_tmp.write(readstr);
	    if j==0 or j==439 or j==440 or j==879 or j==880 or j==1319 or j==1320 or j==1759:
		for k in range(0,4):
		    fd_tmp.write(readstr);
##U Channel
	for j in range(0, height_in/2):
	    readstr = fd_in.read(width_in/2);
	    fd_tmp.write(readstr)
	    if j==0 or j==439/2 or j==440/2 or j==879/2 or j==880/2 or j==1319/2 or j==1320/2 or j==1759/2:	#if i==440/2:
		for k in range(0,2):
	            fd_tmp.write(readstr);
##V Channel
        for j in range(0, height_in/2):
	    readstr = fd_in.read(width_in/2);
	    fd_tmp.write(readstr)
	    if j==0 or j==439/2 or j==440/2 or j==879/2 or j==880/2 or j==1319/2 or j==1320/2 or j==1759/2:	#if i==440/2:
		for k in range(0,2):
		    fd_tmp.write(readstr);
######################################################Vertical Padding
	fd_tmp.seek(0,0)
##Y Channel
	for j in range(0, height_out):
   	    for k in range(0, width_in):
		readstr = fd_tmp.read(1);	
		fd_out.write(readstr);
		if k==0 or k==439 or k==440 or k==879 or k==880 or k==1319 or k==1320 or k==1759 or k==1760 or k==2199 \
or k==2200 or k==2639 or k==2640 or k==3079 or k==3080 or k==3519:
            	    for l in range(0,4):
			fd_out.write(readstr);
##U Channel
	for j in range(0, height_out/2):
    	    for k in range(0, width_in/2):
        	readstr = fd_tmp.read(1);	
		fd_out.write(readstr);
		if k==0 or k==439/2 or k==440/2 or k==879/2 or k==880/2 or k==1319/2 or k==1320/2 or k==1759/2 or k==1760/2 or k==2199/2 \
or k==2200/2 or k==2639/2 or k==2640/2 or k==3079/2 or k==3080/2 or k==3519/2:
		    for l in range(0,2):
		    	fd_out.write(readstr);
##V Channel
	for j in range(0, height_out/2):
   	    for k in range(0, width_in/2):
		readstr = fd_tmp.read(1);	
		fd_out.write(readstr);
		if k==0 or k==439/2 or k==440/2 or k==879/2 or k==880/2 or k==1319/2 or k==1320/2 or k==1759/2 or k==1760/2 or k==2199/2 \
or k==2200/2 or k==2639/2 or k==2640/2 or k==3079/2 or k==3080/2 or k==3519/2:
		    for l in range(0,2):
			fd_out.write(readstr);
