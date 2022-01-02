from sample_midlibs import code, hungergames, zombie
import random

if __name__ == "__main__":
    m = random.choice([code, zombie, hungergames])
    m.madlib()