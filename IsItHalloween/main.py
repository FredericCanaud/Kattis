import sys
data = sys.stdin.readline().split()
mois = str(data[0])
jour = int(data[1])
if( ( (mois == "OCT") and (jour == 31) ) or ( (mois == "DEC") and (jour == 25) )):
    print("yup")
else:
    print("nope")