import random

# New York City (source https://popfactfinder.planning.nyc.gov/explorer/cities/NYC?censusTopics=populationSexAgeDensity&compareTo=1)
age_brackets_nyc = {
    (0, 4): 0.054,    # 5.4 % under 5, say 0–4
    (5, 9): 0.054,    # "5 to 9 years" (you’d get real share)
    (10, 14): 0.055,  # 10 to 14: 5.5%
    (15, 19): 0.060,  # ...
    (20, 24): 0.070,
    (25, 29): 0.075,
    (30, 34): 0.080,
    (35, 39): 0.085,
    (40, 44): 0.090,
    (45, 49): 0.080,
    (50, 54): 0.070,
    (55, 59): 0.060,
    (60, 64): 0.050,  # ...
    (65, 79): 0.100,  # combining 65–79
    (80, 100): 0.020,  # 80+ grouping
}

# total_pop = 8804190  #  Total population of NYC

# Sweden (source https://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__BE__BE0101__BE0101A/BefolkningR1860N/table/tableViewLayout1/?loadedQueryId=149590&timeType=item and https://www.indexmundi.com/sweden/age_structure.html)
age_brackets_sweden = { # Same Logics as before
    (0, 4): 0.0573,
    (5, 9): 0.0598,
    (10, 14): 0.0600,
    (15, 19): 0.0556,
    (20, 24): 0.0558,
    (25, 29): 0.0692,
    (30, 34): 0.0713,
    (35, 39): 0.0635,
    (40, 44): 0.0611,
    (45, 49): 0.0643,
    (50, 54): 0.0644,
    (55, 59): 0.0618,
    (60, 64): 0.0548,
    (65, 69): 0.0517,
    (70, 74): 0.0530,
    (75, 79): 0.0440,
    (80, 84): 0.0271,
    (85, 89): 0.0157,
    (90, 94): 0.0074,
    (95, 99): 0.0020,
    (100, 120): 0.0002,   # approximate grouping for 100+
}

# total_pop = 10587710 # Sweden total population

# Niger (source https://srv1.worldometers.info/world-population/niger-population/) - Roughly estimated
age_brackets_niger = {
    (0, 4):   0.195,   # ~19.5 % of population age 0-4  
    (5, 12):  0.242,   # ~24.2 % age 5-12              
    (13, 17): 0.118,   # ~11.8 % age 13-17             
    (18, 24): 0.128,   # ~12.8 % age 18-24              
    (25, 34): 0.123,   # ~12.3 % age 25-34             
    (35, 44): 0.081,   # ~8.1 % age 35-44               
    (45, 54): 0.053,   # ~5.3 % age 45-54              
    (55, 64): 0.035,   # ~3.5 % age 55-64           
    (65, 100):0.024,   # ~2.4 % age 65+              
}

total_pop = 28188365

# Japan (source https://www.indexmundi.com/japan/age_structure.html)
age_brackets_japan = {
    (0,   14): 0.1249,    # ~12.49%
    (15,  24): 0.0947,    # ~9.47%
    (25,  54): 0.3680,    # ~36.80%
    (55,  64): 0.1206,    # ~12.06%
    (65, 100): 0.2918,    # ~29.18% (65+)
}

total_pop = 123753041

# Compute counts per bracket (rounded)
bracket_counts = {br: int(prop * total_pop) for br, prop in age_brackets_japan.items()}

ages = []

# Create the age's list

for (low, high), cnt in bracket_counts.items():
    for _ in range(cnt):
        age = random.randint(low, high)
        ages.append(age)

# Optionally shuffle the group
# random.shuffle(ages)

# Write to .txt - population_nameAges.txt
with open("japanAges.txt", "w") as f:
    for age in ages:
        f.write(f"{age}\n")