import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   header = ''

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=","hopt="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-help':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-h", "--hopt"):
         header = arg   
   print ('Input file is: ', inputfile)
   print ('Output file is: ', outputfile)
   print ('Headers exist: ', header)

if __name__ == "__main__":
   main(sys.argv[1:])