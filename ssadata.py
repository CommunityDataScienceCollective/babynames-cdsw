import glob
import re

def import_yob_file(filename):
    boys = {}
    girls = {}

    with open(filename, "r") as f:
        for line in f.readlines():
            name, gender, count = line.strip().split(",")
            count = int(count)
            if gender == "F":
                girls[name.lower()] = count
            elif gender == "M":
                boys[name.lower()] = count
                
    return((boys, girls))

years = {}
for filename in glob.glob('yob*.txt'):
    year = re.match(r'yob(\d{4})\.txt$', filename).group(1)
    tmp_boys, tmp_girls = import_yob_file(filename)
    years[year] = {'girls' : tmp_girls,
                   'boys' : tmp_boys}

## resort by year
years = dict(sorted(years.items()))

girls = years["2021"]["girls"]
boys = years["2021"]["boys"]


    
    
