from nfl_stat_explorer.Team import Team, League
import pathlib


def test_winning_percentage_for_season():
    files = list(pathlib.Path.cwd().joinpath("nfl_stat_explorer", "data", "games_data", "regular_season").glob('*.csv'))

    league09 = League(files)
    oak09 = league09.get_team("OAK")

    assert(oak09.winning_percentage_for_season(2009) == .3125)
