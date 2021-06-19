infilename = input( "입력파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

in_path = "C:\\Users\\kcj30\\Desktop\\chEmployement\\" + infilename
out_path = "C:\\Users\\kcj30\\Desktop\\chEmployement\\" + outfilename

infile = open(in_path, "r")
outfile = open(out_path, "w")

s = infile.read()

outfile.write(s)

infile.close()
outfile.close()

