from nfl_stat_explorer.Team import Team
from nfl_stat_explorer.League import League
import pathlib


def test_lac():
    files = list(pathlib.Path.cwd().joinpath("nfl_stat_explorer", "data", "games_data", "regular_season").glob('*.csv'))

    league09 = League(files)
    lac09 = league09.get_team("LAC")

    print(lac09.winning_percentage_for_season(2009)) 


def test_winning_percentage_for_season():
    files = list(pathlib.Path.cwd().joinpath("nfl_stat_explorer", "data", "games_data", "regular_season").glob('*.csv'))

    league09 = League(files)
    oak09 = league09.get_team("OAK")

    league09.print_teams_with_strength_of_schedule(2009)
    assert(oak09.winning_percentage_for_season(2009) == .3125)


def test_get_opponent_winning_percentage():

    files = list(pathlib.Path.cwd().joinpath("nfl_stat_explorer", "data", "games_data", "regular_season").glob('*.csv'))

    league09 = League(files)

    assert(0.52734375 == league09.get_opponent_winning_percentage_for_team_name("OAK", 2009))


def test_get_list_of_opponents():
    files = list(pathlib.Path.cwd().joinpath("nfl_stat_explorer", "data", "games_data", "regular_season").glob('*.csv'))

    league09 = League(files)
    oak09 = league09.get_team("OAK")

    opponents = oak09.get_list_of_opponents(2009)

    assert(opponents == ['SD',
     'KC',
     'DEN',
     'HOU',
     'NYG',
     'PHI',
     'NYJ',
     'SD',
     'KC',
     'CIN',
     'DAL',
     'PIT',
     'WAS',
     'DEN',
     'CLE',
     'BAL'])
