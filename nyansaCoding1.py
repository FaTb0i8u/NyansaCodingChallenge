import datetime
import pytz

# The bulk of the time used will be spent iterating through the final dictionary
# The total space complexity will just be on the order of n - the number of entries
# The total time complexity will be order of d*w - the number of unique dates * the number of websites visited on that date
def summarize(filename):
  dates = {}
  with open(filename) as f:
    for x in f.readlines():
      listafied = x.split("|")
      #convert to GMT
      date = datetime.datetime.fromtimestamp(int(listafied[0]))
      theDay = date.astimezone(pytz.timezone("GMT")).strftime("%m/%d/%Y %Z")
      #remove the newline char
      theWebsite = listafied[1].replace("\n", "")
      if theDay not in dates:
        dates[theDay] = {}
        dates[theDay][theWebsite] = 1
      else:
        if theWebsite not in dates[theDay]:
          dates[theDay][theWebsite] = 1
        else:
          dates[theDay][theWebsite] += 1
    sortedDates = sorted(dates.items(), key= lambda x:x[0])
    for x in sortedDates:
      print(x[0])
      websitesDict = x[1]
      sortedWebsites = sorted(websitesDict.items(), key=lambda z:z[1], reverse = True)
      for y in sortedWebsites:
        print(str(y[0]) + " " + str(y[1]))

summarize(input("The input file of timestamps and websites: "))