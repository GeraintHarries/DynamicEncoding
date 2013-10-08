#import StringIO

#fileName = raw_input('Enter the File Name (Including Extension): ')

piece_size = 4096 # 4 KiB

with open("file.bin", "rb") as in_file:
        while True:
            piece = in_file.read(6)
	    print piece
            if piece == "":
                break # end of file
