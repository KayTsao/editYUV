f_in = 'Orig_1s.yuv'
f_out = '10_frames.yuv'

width_in = 3520
height_in = 1760
height_pad = 4

f_size_in = width_in*height_in*3/2
f_size_out = width_in*(height_in+height_pad)*3/2

with open(f_in, 'rb') as fd_in, open(f_out, 'wb') as fd_out:
    for i in range(10):
        frame_data = fd_in.read(f_size)
        fd_out.write(data)

