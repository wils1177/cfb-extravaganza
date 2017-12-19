import csv

team_conversion_dict = {
    "Air Force" : "721",
    "Akron" : "5",
    "Alabama" : "8",
    "Appalachian State" : "27",
    "Arizona" : "29",
    "Arizona State" : "28",
    "Arkansas" : "31",
    "Arkansas State" : "30",
    "Army" : "725",
    "Auburn" : "37",
    "Brigham Young" : "77",
    "Ball State" : "47",
    "Baylor" : "51",
    "Boise State" : "66",
    "Boston College" : "67",
    "Bowling Green" : "71",
    "Buffalo" : "86",
    "California" : "107",
    "Central Michigan" : "129",
    "Cincinnati" : "140",
    "Clemson" : "147",
    "Colorado" : "157",
    "Colorado State" : "156",
    "Connecticut" : "164",
    "Duke" : "193",
    "East Carolina" : "196",
    "Eastern Michigan" : "204",
    "Florida" : "235",
    "Florida Atlantic" : "229",
    "Florida International" : "231",
    "Florida State" : "234",
    "Fresno State" : "96",
    "Georgia" : "257",
    "Georgia Tech" : "255",
    "Hawaii" : "277",
    "Houston" : "288",
    "Idaho" : "295",
    "Illinois" : "301",
    "Indiana" : "306",
    "Iowa" : "312",
    ""
    ""

}

with open('data/Game Data 1998-2010-2.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(spamreader):
        if i == 1:
            print(row)
