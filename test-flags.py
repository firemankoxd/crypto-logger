import sys

print(sys.argv)

if '-email' in sys.argv:
  index = sys.argv.index("-email")
  val = sys.argv[index+1]
  print(f"{val}")
else:
  print("nothing:(")

# python flags.py -aaaa -a -a -a -a -30 -email 40 -bra