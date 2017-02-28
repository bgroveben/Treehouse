import sys

start_movie = input("Do you want to start the movie? Y/n ").lower()
if start_movie != 'n':
    print("Enjoy the show!")
else:
    sys.exit()
