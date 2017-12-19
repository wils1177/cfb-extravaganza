#! /usr/bin/env python3
import csv
from bs4 import BeautifulSoup
import requests
import os
import sqlite3


thisDir = os.path.dirname(os.path.realpath(__file__))
gameDir = "game.py"
dataDir = thisDir + "/data"



def scrape_data(field_results, team, category, year):
    address = "http://www.cfbstats.com/" + year + "/team/" + team + category + "/gamelog.html"
    response = requests.get(address)
    html_data = response.content
    soup = BeautifulSoup(html_data, 'html.parser')
    table = soup.find('table', attrs={'class': 'game-log'})

    rows = table.findAll('tr')
    for game in rows[1:-2]:

        if game.contents[1].string and len(game.contents[1].string) == 8:

            game_results = []
            for col in game.children:
                if col.string != "\n":
                    game_results.append(col)
            field_results.append(game_results)


class Game:
    def __init__(self, team):
        self.location = None
        self.date = None
        self.surface = None
        self.scored = None
        self.let_scored = None
        self.result = None
        self.opponent = None
        self.unique = None
        self.team = team

    def __str__(self):
        return """location: {} date: {} surface {}: scored: {} let_scored: {}
    result: {} opponent: {} unique: {}""".format(self.location, self.date, self.surface, self.scored, self.let_scored,
    self.result, self.opponent, self.unique)

    def create_unique(self):
        self.unique = self.date + str(self.team)

class Rushing_Offense:
    def __init__(self):
        self.att = None
        self.yards = None
        self.avg = None
        self.td = None
        self.game_unique = None
        self.table_name = "rushingOffense"


    def __str__(self):
        return "att: {} yards {}: avg: {} td: {}".format(self.att, self.yards, self.avg, self.td)

    def get_mems(self):
        return str((self.game_unique, self.att, self.yards, self.avg, self.td))

class Rushing_Defense(Rushing_Offense):
    def __init__(self):
        Rushing_Offense.__init__(self)
        self.table_name = "rushingDefense"


class Passing_Offense:
    def __init__(self):
        self.att = None
        self.comp = None
        self.pct = None
        self.yards = None
        self.yardsPerAtt = None
        self.td = None
        self.inter = None
        self.rating = None
        self.table_name = "passingOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.att, self.comp, self.pct, self.yards,
    self.yardsPerAtt, self.td, self.inter, self.rating))

class Passing_Defense(Passing_Offense):
    def __init__(self):
        Passing_Offense.__init__(self)
        self.table_name = "passingDefense"

class Receiving_Offense:
    def __init__(self):
        self.rec = None
        self.yards = None
        self.avg = None
        self.td = None
        self.game_unique = None
        self.table_name = "receivingOffense"

    def get_mems(self):
        return str((self.game_unique, self.rec, self.yards, self.avg, self.td))

class Receiving_Defense(Receiving_Offense):
    def __init__(self):
        Receiving_Offense.__init__(self)
        self.table_name = "receivingDefense"

class PuntReturn_Offense:
    def __init__(self):
        self.ret = None
        self.yards = None
        self.avg = None
        self.td = None
        self.game_unique = None
        self.table_name = "puntReturnOffense"

    def get_mems(self):
        return str((self.game_unique, self.ret, self.yards, self.avg, self.td))

class PuntReturn_Defense(PuntReturn_Offense):
    def __init__(self):
        PuntReturn_Offense.__init__(self)
        self.table_name = "puntReturnDefense"

class KickOffReturn_Offense:
    def __init__(self):
        self.ret = None
        self.yards = None
        self.avg = None
        self.td = None
        self.game_unique = None
        self.table_name = "kickoffReturnOffense"

    def get_mems(self):
        return str((self.game_unique, self.ret, self.yards, self.avg, self.td))

class KickOffReturn_Defense(KickOffReturn_Offense):
    def __init__(self):
        KickOffReturn_Offense.__init__(self)
        self.table_name = "kickoffReturnDefense"

class Punt_Offense:
    def __init__(self):
        self.punts = None
        self.yards = None
        self.avg = None
        self.game_unique = None
        self.table_name = "puntOffense"

    def get_mems(self):
        return str((self.game_unique, self.punts, self.yards, self.avg))

class Punt_Defense(Punt_Offense):
    def __init__(self):
        Punt_Offense.__init__(self)
        self.table_name = "puntDefense"

class Kickoff_Offense:
    def __init__(self):
        self.kickoffs = None
        self.yards = None
        self.avg = None
        self.touchback = None
        self.touchbackPer = None
        self.OOB = None
        self.onside = None
        self.game_unique = None
        self.table_name = "kickoffOffense"

    def get_mems(self):
        return str((self.game_unique, self.kickoffs, self.yards, self.avg,
    self.touchback, self.touchbackPer, self.OOB, self.onside))

class Kickoff_Defense(Kickoff_Offense):
    def __init__(self):
        Kickoff_Offense.__init__(self)
        self.table_name = "kickoffDefense"

class PlaceKick_Offense:
    def __init__(self):
        self.FGatt = None
        self.FGmade = None
        self.FGpct = None
        self.EPatt = None
        self.EPmade = None
        self.EPpct = None
        self.table_name = "placeKickOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.FGatt, self.FGmade, self.FGpct,
    self.EPatt, self.EPmade, self.EPpct))

class PlaceKick_Defense(PlaceKick_Offense):
    def __init__(self):
        PlaceKick_Offense.__init__(self)
        self.table_name = "placeKickDefense"


class Scoring_Offense:
    def __init__(self):
        self.td = None
        self.fg = None
        self.onexp = None
        self.twoxp = None
        self.saey = None
        self.table_name = "scoringOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.td, self.fg, self.onexp,
    self.twoxp, self.saftey))

class Scoring_Defense(Scoring_Offense):
    def __init__(self):
        Scoring_Offense.__init__(self)
        self.table_name = "scoringDefense"

class TotalOffense_Offense:
    def __init__(self):
        self.rushing = None
        self.passing = None
        self.play = None
        self.total = None
        self.ypp = None
        self.table_name = "totalOffenseOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.rushing, self.passing, self.play,
    self.total, self.ypp))

class TotalOffense_Defense(TotalOffense_Offense):
    def __init__(self):
        TotalOffense_Offense.__init__(self)
        self.table_name= "totalOffenseDefense"

class APPRunning_Offense:
    def __init__(self):
        self.rushing = None
        self.receiving= None
        self.puntret = None
        self.kickret = None
        self.intret = None
        self.plays = None
        self.total = None
        self.ypp = None
        self.ypg = None
        self.table_name = "APPRunningOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.rushing, self.receiving, self.puntret,
    self.kickret, self.intret, self.plays, self.total, self.ypp, self.ypg))

class APPRunning_Defense(APPRunning_Offense):
    def __init__(self):
        APPRunning_Offense.__init__(self)
        self.table_name = "APPRunningDefense"

class FirstDown_Offense:
    def __init__(self):
        self.rushing = None
        self.passing= None
        self.penalty = None
        self.total = None
        self.table_name = "FirstDownOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.rushing, self.passing, self.penalty, self.total))

class FirstDown_Defense(FirstDown_Offense):
    def __init__(self):
        FirstDown_Offense.__init__(self)
        self.table_name = "FirstDownDefense"

class Penalties_Offense:
    def __init__(self):
        self.penalties = None
        self.yards = None
        self.ppg = None
        self.ypg = None
        self.table_name = "PenaltiesOffense"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.penalties, self.yards, self.ppg,
    self.ypg))

class Penalties_Defense(Penalties_Offense):
    def __init__(self):
        Penalties_Offense.__init__(self)
        self.table_name = "PenaltiesDefense"

class ThirdDownConv_Offense:
    def __init__(self):
        self.att = None
        self.conv = None
        self.convp = None
        self.table_name = "ThirdDownConvOffense"

        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.att, self.conv, self.convp))

class ThirdDownConv_Defense(ThirdDownConv_Offense):
    def __init__(self):
        ThirdDownConv_Offense.__init__(self)
        self.table_name = "ThirdDownConvDefense"

class FourthDownConv_Offense:
    def __init__(self):
        self.att = None
        self.conv = None
        self.convp = None
        self.table_name = "FourthDownConvOffense"

        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.att, self.conv, self.convp))

class FourthDownConv_Defense(FourthDownConv_Offense):
    def __init__(self):
        FourthDownConv_Offense.__init__(self)
        self.table_name = "FourthDownConvDefense"

class RedZone_Offense:
    def __init__(self):
        self.att = None
        self.scores = None
        self.scorep = None
        self.td = None
        self.tdp = None
        self.fg = None
        self.fgp = None
        self.table_name = "RedzoneConvOffense"

        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.att, self.scores, self.scorep,
    self.td, self.tdp, self.fg, self.fgp))

class RedZone_Defense(RedZone_Offense):
    def __init__(self):
        RedZone_Offense.__init__(self)
        self.table_name = "RedzoneConvDefense"


class Interception:
    def __init__(self):
        self.int = None
        self.yards = None
        self.td = None
        self.table_name = "Interceptions"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.int, self.yards, self.td))

class FumbleReturn:
    def __init__(self):
        self.fr = None
        self.yards = None
        self.td = None
        self.table_name = "FumbleReturns"

        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.fr, self.yards, self.td))

class Tackles:
    def __init__(self):
        self.solo = None
        self.ass = None
        self.total = None
        self.table_name = "Tackles"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.solo, self.ass, self.total))

class TacklesForLoss:
    def __init__(self):
        self.tfl = None
        self.tflYards = None
        self.table_name = "TacklesForLoss"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.tfl, self.tflYards))

class Sack:
    def __init__(self):
        self.sacks = None
        self.sackYards = None
        self.table_name = "Sacks"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.sacks, self.sackYards))

class MiscDefense:
    def __init__(self):
        self.passBU = None
        self.QBH = None
        self.FF = None
        self.KB = None
        self.table_name = "MiscDef"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.passBU, self.QBU, self.FF,
    self.KB))

class TurnoverMargin:
    def __init__(self):
        self.fumGain = None
        self.intGain = None
        self.totalGain = None
        self.fumLost = None
        self.intLost = None
        self.totalLost = None
        self.margin = None
        self.table_name = "TurnoverMargine"
        self.game_unique = None

    def get_mems(self):
        return str((self.game_unique, self.fumGain, self.intGain, self.totalGain,
    self.fumLost, self.intLost, self.totalLost, self.margin))



def create_stat(category, team, year):

    game_list = []
    game_fields_results = []
    scrape_data(game_fields_results, team, category, year)
    game_unique = ""

    for game in game_fields_results:
        stat_results = []

        for idx, stat in enumerate(game):
            if idx == 0:
                game_unique = game_unique + stat.string + team
                stat_results.append(game_unique)
            if idx >= 4:
                if stat.string != "-":
                    stat_results.append(stat.string)
                else:
                    stat_results.append(None)

        game_unique = ""
        game_list.append(stat_results)

    return game_list

def create_rushing(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/rushing/" + side, team, year)
    for game in results:
        if side == "offense":
            new_stat = Rushing_Offense()
        else:
            new_stat = Rushing_Defense()

        new_stat.game_unique = game[0]

        new_stat.att = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        new_stat.td = int(game[4])

        stats.append(new_stat)
    return stats

def create_passing(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/passing/" + side, team, year)
    for game in results:

        if side == "offense":
            new_stat = Passing_Offense()
        else:
            new_stat = Passing_Defense()

        new_stat.game_unique = game[0]
        new_stat.att = int(game[1])
        new_stat.comp = int(game[2])
        if game[3]:
            new_stat.pct = float(game[3])
        new_stat.yards = int(game[4])
        if game[5]:
            new_stat.yardsPerAtt = float(game[5])
        new_stat.td = int(game[6])
        new_stat.inter = int(game[7])
        if game[8]:
            new_stat.rating = float(game[8])
        stats.append(new_stat)
    return stats

def create_recieving(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/receiving/" + side, team, year)
    for game in results:

        if side == "offense":
            new_stat = Receiving_Offense()
        else:
            new_stat = Receiving_Defense()

        new_stat.game_unique = game[0]

        new_stat.rec = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        new_stat.td = int(game[4])
        stats.append(new_stat)

    return stats

def create_punt_return(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/puntreturn/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = PuntReturn_Offense()
        else:
            new_stat = PuntReturn_Defense()

        new_stat.game_unique = game[0]
        new_stat.ret = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        new_stat.td = int(game[4])
        stats.append(new_stat)
    return stats

def create_kickoff_return(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/kickreturn/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = KickOffReturn_Offense()
        else:
            new_stat = KickOffReturn_Defense()

        new_stat.game_unique = game[0]
        new_stat.ret = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        new_stat.td = int(game[4])
        stats.append(new_stat)
    return stats


def create_punt(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/punting/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = Punt_Offense()
        else:
            new_stat = Punt_Defense()

        new_stat.game_unique = game[0]
        new_stat.punts = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        stats.append(new_stat)
    return stats

def create_kickoff(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/kickoff/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = Kickoff_Offense()
        else:
            new_stat = Kickoff_Defense()

        new_stat.game_unique = game[0]
        new_stat.kickoffs = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.avg = float(game[3])
        new_stat.touchback = int(game[4])
        if game[5]:
            new_stat.touchbackPer = float(game[5])
        new_stat.OOB = int(game[6])
        new_stat.onside = int(game[7])
        stats.append(new_stat)
    return stats

def create_placekick(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/kicking/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = PlaceKick_Offense()
        else:
            new_stat = PlaceKick_Defense()


        new_stat.game_unique = game[0]
        new_stat.FGatt = int(game[1])
        new_stat.FGmade = int(game[2])
        if game[3]:
            new_stat.FGpct = float(game[3])
        new_stat.EPatt = int(game[4])
        new_stat.EPmade = int(game[5])
        if game[6]:
            new_stat.EPpct = float(game[6])

        stats.append(new_stat)
    return stats

def create_scoring(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/scoring/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = Scoring_Offense()
        else:
            new_stat = Scoring_Defense()

        new_stat.game_unique = game[0]
        new_stat.td = int(game[1])
        new_stat.fg = int(game[2])
        new_stat.onexp= int(game[3])
        new_stat.twoxp = int(game[4])
        new_stat.saftey = int(game[5])

        stats.append(new_stat)
    return stats

def create_total_offense(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/total/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = TotalOffense_Offense()
        else:
            new_stat = TotalOffense_Defense()

        new_stat.game_unique = game[0]
        new_stat.rushing = int(game[1])
        new_stat.passing = int(game[2])
        new_stat.play = int(game[3])
        new_stat.total = int(game[4])
        if game[5]:
            new_stat.ypp = float(game[5])
        stats.append(new_stat)
    return stats

def create_app_running(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/allpurpose/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = APPRunning_Offense()
        else:
            new_stat = APPRunning_Defense()

        new_stat.game_unique = game[0]
        new_stat.rushing = int(game[1])
        new_stat.receiving = int(game[2])
        new_stat.puntret = int(game[3])
        new_stat.kickret = int(game[4])
        new_stat.intret = int(game[5])
        new_stat.plays = int(game[6])
        new_stat.total = int(game[7])
        if game[8]:
            new_stat.ypp = float(game[8])
        if game[9]:
            new_stat.ypg = float(game[9])
        stats.append(new_stat)
    return stats

def create_first_downs(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/firstdown/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = FirstDown_Offense()
        else:
            new_stat = FirstDown_Defense()

        new_stat.game_unique = game[0]
        new_stat.rushing = int(game[1])
        new_stat.passing = int(game[2])
        new_stat.penalty = int(game[3])
        new_stat.total = int(game[4])
        stats.append(new_stat)
    return stats

def create_penalties(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/penalty/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = Penalties_Offense()
        else:
            new_stat = Penalties_Defense()

        new_stat.game_unique = game[0]
        new_stat.penalties = int(game[1])
        new_stat.yards = int(game[2])
        if game[3]:
            new_stat.ppg = float(game[3])
        if game[4]:
            new_stat.ypg = float(game[4])
        stats.append(new_stat)
    return stats

def create_third_down_conv(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/thirddown/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = ThirdDownConv_Offense()
        else:
            new_stat = ThirdDownConv_Defense()

        new_stat.game_unique = game[0]
        new_stat.att = int(game[1])
        new_stat.conv = int(game[2])
        if game[3]:
            new_stat.convp = float(game[3])

        stats.append(new_stat)
    return stats

def create_fourth_down_conv(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/fourthdown/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = FourthDownConv_Offense()
        else:
            new_stat = FourthDownConv_Defense()

        new_stat.game_unique = game[0]
        new_stat.att = int(game[1])
        new_stat.conv = int(game[2])
        if game[3]:
            new_stat.convp = float(game[3])

        stats.append(new_stat)
    return stats

def create_redzone_conv(team, year, side):
    assert side in ["offense", "defense"]
    stats = []
    results = create_stat("/redzone/" + side, team, year)

    for game in results:

        if side == "offense":
            new_stat = RedZone_Offense()
        else:
            new_stat = RedZone_Defense()

        new_stat.game_unique = game[0]
        new_stat.att = int(game[1])
        new_stat.scores = int(game[2])
        if game[3]:
            new_stat.scorep = float(game[3])
        new_stat.td = int(game[4])
        if game[5]:
            new_stat.tdp = float(game[5])
        new_stat.fg = int(game[6])
        if game[7]:
            new_stat.fgp = float(game[7])

        stats.append(new_stat)
    return stats

def create_interceptions(team, year):
    stats = []
    results = create_stat("/interception/", team, year)

    for game in results:
        new_stat = Interception()
        new_stat.game_unique = game[0]
        new_stat.int = int(game[1])
        new_stat.yards = int(game[2])
        new_stat.td = int(game[3])
        stats.append(new_stat)
    return stats

def create_fumble_returns(team, year):
    stats = []
    results = create_stat("/fumblereturn/", team, year)

    for game in results:
        new_stat = FumbleReturn()
        new_stat.game_unique = game[0]
        new_stat.fr = int(game[1])
        new_stat.yards = int(game[2])
        new_stat.td = int(game[3])
        stats.append(new_stat)
    return stats

def create_tackles(team, year):
    stats = []
    results = create_stat("/tackle/", team, year)

    for game in results:
        new_stat = Tackles()
        new_stat.game_unique = game[0]
        new_stat.solo = int(game[1])
        new_stat.ass = int(game[2])
        new_stat.total = int(game[3])
        stats.append(new_stat)
    return stats

def create_tackles_for_loss(team, year):
    stats = []
    results = create_stat("/tackleforloss/", team, year)

    for game in results:
        new_stat = TacklesForLoss()
        new_stat.game_unique = game[0]
        if game[1]:
            new_stat.tfl = float(game[1])
        new_stat.tflYards = int(game[2])

        stats.append(new_stat)
    return stats

def create_sacks(team, year):
    stats = []
    results = create_stat("/sack/", team, year)

    for game in results:
        new_stat = Sack()
        new_stat.game_unique = game[0]
        if game[1]:
            new_stat.sacks = float(game[1])
        new_stat.sackYards = int(game[2])

        stats.append(new_stat)
    return stats

def create_misc_def(team, year):
    stats = []
    results = create_stat("/miscdefense/", team, year)

    for game in results:
        new_stat = MiscDefense()
        new_stat.game_unique = game[0]
        new_stat.passBU= int(game[1])
        new_stat.QBU = int(game[2])
        new_stat.FF = int(game[3])
        new_stat.KB = int(game[4])

        stats.append(new_stat)
    return stats

def create_turnover_margin(team, year):
    stats = []
    results = create_stat("/turnovermargin/", team, year)

    for game in results:
        new_stat = TurnoverMargin()
        new_stat.game_unique = game[0]
        new_stat.fumGain = int(game[1])
        new_stat.intGain = int(game[2])
        new_stat.totalGain = int(game[3])
        new_stat.fumLost = int(game[4])
        new_stat.intLost = int(game[5])
        new_stat.totalLost = int(game[6])
        new_stat.margin = int(game[7])

        stats.append(new_stat)
    return stats





def create_rushing_offense_and_games(team, year):
    games = []
    game_fields_names = ["date", "opponent", "surface", "result", "att", "yards", "avg", "td"]
    game_field_results = []
    rushes = []
    category = "/rushing/offense"
    scrape_data(game_field_results, team, category, year)

    for game in game_field_results:
        new_game = Game(int(team))
        new_rushing = Rushing_Offense()
        for idx, stat in enumerate(game):
            if game_fields_names[idx] == "date":
                new_game.date = stat.string
            elif game_fields_names[idx] == "opponent":
                if stat.string is not None:
                    new_game.opponent = stat.string
                    new_game.location = int(get_location(stat.string))
                else:

                    new_game.location = int(get_location(stat.contents[0]))
                    new_game.opponent = stat.contents[1].string

            elif game_fields_names[idx] == "surface":
                new_game.surface = stat.a.string
            elif game_fields_names[idx] == "result":
                results = stat.string

                if "L" in results:
                    new_game.result = "L"
                else:
                    new_game.result = "W"

                scores = get_points(results)
                new_game.scored = int(scores[0])
                new_game.let_scored = int(scores[1])
            elif game_fields_names[idx] == "att":
                new_rushing.att = stat.string
            elif game_fields_names[idx] == "yards":
                new_rushing.yards = stat.string
            elif game_fields_names[idx] == "avg":
                new_rushing.avg = stat.string
            elif game_fields_names[idx] == "td":
                new_rushing.td = stat.string

        new_game.create_unique()
        new_rushing.game_unique = new_game.create_unique()
        games.append(new_game)
        rushes.append(new_rushing)

    return games, rushes

def get_points(score_string):

    score = ""
    scores = []
    for char in score_string:

        if char.isdigit():
            score = score + char
        if char == "-":
            scores.append(score)
            score = ""
    scores.append(score)
    return scores

def get_location(loc):

    if "@" in loc:
        return 1
    elif "+" in loc:
        return 2
    else:
        return 0
