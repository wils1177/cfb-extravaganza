#! /usr/bin/env python3
import sqlite3

conn = sqlite3.connect('game_data.db')
c = conn.cursor()

c.execute("""CREATE TABLE Game (game_id TEXT, location_id INT, date TEXT, surface TEXT, scored INT, let_scored INT,
 result TEXT, opponent TEXT, team INT )""")

c.execute("""CREATE TABLE rushingOffense (game_id TEXT, att INT, yards Int, avg REAL, td INT)""")
c.execute("""CREATE TABLE rushingDefense (game_id TEXT, att INT, yards Int, avg REAL, td INT)""")

c.execute("""CREATE TABLE passingOffense (game_id TEXT, att INT, comp Int, pct REAL, yards INT, yardsPerAtt REAL,
td INT, inter INT, rating REAL)""")
c.execute("""CREATE TABLE passingDefense (game_id TEXT, att INT, comp Int, pct REAL, yards INT, yardsPerAtt REAL,
td INT, inter INT, rating REAL)""")

c.execute("""CREATE TABLE receivingOffense (game_id TEXT, rec INT, yards Int, avg REAL, td INT)""")
c.execute("""CREATE TABLE receivingDefense (game_id TEXT, rec INT, yards Int, avg REAL, td INT)""")

c.execute("""CREATE TABLE puntReturnOffense (game_id TEXT, ret INT, yards Int, avg REAL, td INT)""")
c.execute("""CREATE TABLE puntReturnDefense (game_id TEXT, ret INT, yards Int, avg REAL, td INT)""")

c.execute("""CREATE TABLE kickoffReturnOffense (game_id TEXT, ret INT, yards Int, avg REAL, td INT)""")
c.execute("""CREATE TABLE kickoffReturnDefense (game_id TEXT, ret INT, yards Int, avg REAL, td INT)""")

c.execute("""CREATE TABLE puntOffense (game_id TEXT, punt INT, yards Int, avg REAL)""")
c.execute("""CREATE TABLE puntDefense (game_id TEXT, punt INT, yards Int, avg REAL)""")

c.execute("""CREATE TABLE kickoffOffense (game_id TEXT, kickoffs INT, yards Int, avg REAL, touchback INT,
touchbackPer REAL, OOB INT, onside INT)""")
c.execute("""CREATE TABLE kickoffDefense (game_id TEXT, kickoffs INT, yards Int, avg REAL, touchback INT,
touchbackPer REAL, OOB INT, onside INT)""")

c.execute("""CREATE TABLE placeKickOffense (game_id TEXT, FGatt INT, FGmade Int, FGpct REAL, EPatt INT,
EPmade INT, EPpct REAL)""")
c.execute("""CREATE TABLE placeKickDefense (game_id TEXT, FGatt INT, FGmade Int, FGpct REAL, EPatt INT,
EPmade INT, EPpct REAL)""")

c.execute("""CREATE TABLE scoringOffense (game_id TEXT, td INT, fg INT, onexp INT, twoexp INT,
saftey INT)""")
c.execute("""CREATE TABLE scoringDefense (game_id TEXT, td INT, fg INT, onexp INT, twoexp INT,
saftey INT)""")

c.execute("""CREATE TABLE totalOffenseOffense (game_id TEXT, rushing INT, passing INT, plays INT, total INT,
ypp REAL)""")
c.execute("""CREATE TABLE totalOffenseDefense (game_id TEXT, rushing INT, passing INT, plays INT, total INT,
ypp REAL)""")

c.execute("""CREATE TABLE APPRunningOffense (game_id TEXT, rushing INT, receiving INT, puntret INT, kickret INT,
intret INT, plays INT, total INT,ypp REAL, ypg REAL)""")
c.execute("""CREATE TABLE APPRunningDefense (game_id TEXT, rushing INT, receiving INT, puntret INT, kickret INT,
intret INT, plays INT, total INT,ypp REAL, ypg REAL)""")

c.execute("""CREATE TABLE FirstDownOffense (game_id TEXT, rushing INT, passing INT, penalty INT, total INT)""")
c.execute("""CREATE TABLE FirstDownDefense (game_id TEXT, rushing INT, passing INT, penalty INT, total INT)""")

c.execute("""CREATE TABLE PenaltiesOffense (game_id TEXT, penalties INT, yards INT, ppg REAL, ypg REAL)""")
c.execute("""CREATE TABLE PenaltiesDefense (game_id TEXT, penalties INT, yards INT, ppg REAL, ypg REAL)""")

c.execute("""CREATE TABLE ThirdDownConvOffense (game_id TEXT, att INT, conver INT, convp REAL)""")
c.execute("""CREATE TABLE ThirdDownConvDefense (game_id TEXT, att INT, conver INT, convp REAL)""")

c.execute("""CREATE TABLE FourthDownConvOffense (game_id TEXT, att INT, conver INT, convp REAL)""")
c.execute("""CREATE TABLE FourthDownConvDefense (game_id TEXT, att INT, conver INT, convp REAL)""")

c.execute("""CREATE TABLE RedzoneConvOffense (game_id TEXT, att INT, scores INT, scorep REAL, td INT, tdp REAL,
fg INT, fgp REAL)""")
c.execute("""CREATE TABLE RedzoneConvDefense (game_id TEXT, att INT, scores INT, scorep REAL, td INT, tdp REAL,
fg INT, fgp REAL)""")

c.execute("""CREATE TABLE Interceptions (game_id TEXT, inter INT, yards INT, td INT)""")

c.execute("""CREATE TABLE FumbleReturns (game_id TEXT, fr INT, yards INT, td INT)""")

c.execute("""CREATE TABLE Tackles (game_id TEXT, solo INT, ass INT, total INT)""")

c.execute("""CREATE TABLE TacklesForLoss (game_id TEXT, tfl INT, tflYards INT)""")

c.execute("""CREATE TABLE Sacks (game_id TEXT, sacks INT, sackYards INT)""")

c.execute("""CREATE TABLE MiscDef (game_id TEXT, passBU INT, QBU INT, FF INT, KB INT)""")

c.execute("""CREATE TABLE TurnoverMargine (game_id TEXT, fumGain INT, intGain INT, totalGain INT,
 fumLost INT, intLost INT, totalLost INT, margin INT)""")
