# Question 16
# Population Growth Rate = ((Current Year population- Previous Year Population) / Previous Year Population) * 100
# Initializing data
state = ["Uttar Pradesh", "Maharashtra", "Bihar", " West Bengal", "Madhya Pradesh", "Tamil Nadu", "Rajasthan",
         "Karnataka", "Gujarat", "Andhra Pradesh", "Odisha", "Kerala", "Jharkhand", "Assam", "Punjab", "Haryana"]
census_2001 = [166053600, 96752500, 82879910, 80221300, 60385090, 62111390, 56473300, 52734986, 50597200, 75728400,
               36707900, 31839000, 26946070, 26638600, 24289130, 21083900]
census_2011 = [199581477, 112372972, 103804630, 91347736, 72597565, 72138958, 68621012, 61130704, 60383628, 49386799,
               41947358, 33387677, 32988134, 31169272, 27704236, 25753081]
# Defining Function


def growth_rate(current_year, previous_year):
    rate = []
    for _ in range(len(current_year)):
        d = current_year[_] - previous_year[_]
        b = d / previous_year[_]
        p = b * 100
        rate.append(round(p, 4))
    return rate


# __main__
print("Program to print Growth rate of every city\n")
r1 = growth_rate(census_2011, census_2001)
for _ in range(len(state)):
    print(state[_], "has", r1[_], "growth percentage")
