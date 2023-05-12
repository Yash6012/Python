# Question 13
# Defining function


def average_duration(v, f):
    av = []
    for _ in range(len(f)):
        s = v[_] / f[_]
        av.append(s)
    return av


# __main__
# Initializing data array
freq = [20, 5, 10, 5, 10, 15]
site_inf = ["https://github.com/", "https://dodi-repacks.site/", "https://filecr.com/en/?id=022771040000",
            "http://olamovies.cloud/", "https://www.tinkercad.com/", "https://www.youtube.com/"]
visiting_hours = [12, 1, 1, 2, 1, 4]
print("Program to calculate average duration per page\n")
r1 = average_duration(visiting_hours, freq)
for _ in range(len(freq)):
    print("User visited", site_inf[_], "with an average of", r1[_], "and frequency of", freq[_])
