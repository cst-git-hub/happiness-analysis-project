## This file was only used, to find matching countries with original ones in dataset
## "

## This code belongs here:
#from rapidfuzz import process
#import pycountry

#iso_names = [c.name for c in pycountry.countries]

#def suggest_country(name):
#    match = process.extractOne(name, iso_names)
#    return match

## This code belongs to cl_lifeexp.py, line 37 (after reordering, before writing)
#missing = df[df["icc"].isna()]["country"].unique()

#for c in missing:
#    print(c, " -> ", suggest_country(c))