#! /usr/bin/env python3
import sqlite3
from scraper import *

if __name__ == "__main__":
    teams = ['416']
    years = ["2013"]

    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    for team in teams:
        for year in years:
            games, rushing_offense = create_rushing_offense_and_games(team, year)
            rushing_offense = create_rushing(team, year, "offense")
            rushing_defense = create_rushing(team, year, "defense")
            passing_offense = create_passing(team, year, "offense")
            passing_defense = create_passing(team, year, "defense")
            receiving_offense = create_recieving(team, year, "offense")
            receiving_defense = create_recieving(team, year, "defense")
            punt_return_offense = create_punt_return(team, year, "offense")
            punt_return_defense = create_punt_return(team, year, "defense")
            kickoff_return_offense = create_kickoff_return(team, year, "offense")
            kickoff_return_defense = create_kickoff_return(team, year, "defense")
            punt_offense = create_punt(team, year, "offense")
            punt_defense = create_punt(team, year, "defense")
            kickoff_offense = create_kickoff(team, year, "offense")
            kickoff_defense = create_kickoff(team, year, "defense")
            placekick_offense = create_placekick(team, year, "offense")
            placekick_defense = create_placekick(team, year, "defense")
            scoring_offense = create_scoring(team, year, "offense")
            scoring_defense = create_scoring(team, year, "defense")
            total_offense_offense = create_total_offense(team, year, "offense")
            total_offense_defense = create_total_offense(team, year, "defense")
            app_running_offense = create_app_running(team, year, "offense")
            app_running_defense = create_app_running(team, year, "defense")
            first_down_offense = create_first_downs(team, year, "offense")
            first_down_defense = create_first_downs(team, year, "defense")
            penalties_offense = create_penalties(team, year, "offense")
            penalties_defense = create_penalties(team, year, "defense")
            third_down_offense = create_third_down_conv(team, year, "offense")
            third_down_defense = create_third_down_conv(team, year, "defense")
            fourth_down_offense = create_fourth_down_conv(team, year, "offense")
            fourth_down_defense = create_fourth_down_conv(team, year, "defense")
            redzone_offense = create_redzone_conv(team, year, "offense")
            redzone_defense = create_redzone_conv(team, year, "defense")
            interceptions = create_interceptions(team, year)
            fumble_returns = create_fumble_returns(team, year)
            tackles = create_tackles(team, year)
            tackles_for_loss = create_tackles_for_loss(team, year)
            sacks = create_sacks(team, year)
            misc_def = create_misc_def(team, year)
            turnovers = create_turnover_margin(team, year)


            for game in games:

                c.executemany("""INSERT INTO Game VALUES (?,?,?,?,?,?,?,?,?) """,
                [(game.unique , game.location, game.date, game.surface, game.scored, game.let_scored,
                game.result, game.opponent, int(game.team))])


            for i in range(0, len(games)):


                statement = """INSERT INTO {} VALUES {}""".format(rushing_offense[i].table_name,
                rushing_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(rushing_defense[i].table_name,
                rushing_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(passing_offense[i].table_name,
                passing_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(passing_defense[i].table_name,
                passing_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)


                statement = """INSERT INTO {} VALUES {}""".format(receiving_offense[i].table_name,
                receiving_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(receiving_defense[i].table_name,
                receiving_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(punt_return_offense[i].table_name,
                punt_return_offense[i].get_mems())

                statement = statement.replace('None', "NULL")

                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(punt_return_defense[i].table_name,
                punt_return_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(kickoff_return_offense[i].table_name,
                kickoff_return_offense[i].get_mems())
                statement = statement.replace('None', "NULL")

                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(kickoff_return_defense[i].table_name,
                kickoff_return_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(punt_offense[i].table_name,
                punt_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(punt_defense[i].table_name,
                punt_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(kickoff_offense[i].table_name,
                kickoff_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(kickoff_defense[i].table_name,
                kickoff_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(placekick_offense[i].table_name,
                placekick_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(placekick_defense[i].table_name,
                placekick_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(scoring_offense[i].table_name,
                scoring_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(scoring_defense[i].table_name,
                scoring_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(total_offense_offense[i].table_name,
                total_offense_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(total_offense_defense[i].table_name,
                total_offense_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)


                statement = """INSERT INTO {} VALUES {}""".format(app_running_offense[i].table_name,
                app_running_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(app_running_defense[i].table_name,
                app_running_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(first_down_offense[i].table_name,
                first_down_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(first_down_defense[i].table_name,
                first_down_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(penalties_offense[i].table_name,
                penalties_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(penalties_defense[i].table_name,
                penalties_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(third_down_offense[i].table_name,
                third_down_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(third_down_defense[i].table_name,
                third_down_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(fourth_down_offense[i].table_name,
                fourth_down_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(fourth_down_defense[i].table_name,
                fourth_down_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(redzone_offense[i].table_name,
                redzone_offense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)
                statement = """INSERT INTO {} VALUES {}""".format(redzone_defense[i].table_name,
                redzone_defense[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(interceptions[i].table_name,
                interceptions[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(fumble_returns[i].table_name,
                fumble_returns[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(tackles[i].table_name,
                tackles[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(tackles_for_loss[i].table_name,
                tackles_for_loss[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(sacks[i].table_name,
                sacks[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(misc_def[i].table_name,
                misc_def[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

                statement = """INSERT INTO {} VALUES {}""".format(turnovers[i].table_name,
                turnovers[i].get_mems())
                statement = statement.replace('None', "NULL")
                c.execute(statement)

    conn.commit()
    conn.close()
