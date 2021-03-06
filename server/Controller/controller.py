import database


class Controller:
    def __init__(self):
        self.data_b = database.Database("gamedatabase.db")

    def add_new_game(self, new_id, name, release_date, genre, publisher, developer, pc, ps4, xbox_one, user_rate, critic_rate):
        self.data_b.write("games", "id, name, release_date, genre", ", ".join([new_id, name, release_date, genre]))
        if pc == "Available":
            pc = 1
        else:
            pc = 0
        if ps4 == "Available":
            ps4 = 1
        else:
            ps4 = 0
        if xbox_one == "Available":
            xbox_one = 1
        else:
            xbox_one = 0
        self.data_b.write("platforms", "id, name, pc, ps4, xbox_one", ", ".join([new_id, name, str(pc), str(ps4), str(xbox_one)]))
        self.data_b.write("publishers", "id, name, publisher, developer", ", ".join([new_id, name, publisher, developer]))
        self.data_b.write("rates", "id, name, critic_rate, user_rate", ", ".join([new_id, name, critic_rate, user_rate]))
        self.data_b.write("feedback", "id, name, \
                                       one_star_review, two_star_review, three_star_review, \
                                       four_star_review, five_star_review", ", ".join([new_id, name, "0", "0", "0", "0", "0"]))

    def get_all_games(self):
        raw_list_games = self.data_b.get_all("games")
        complete_list_games = []
        for game in raw_list_games:
            game_info = []
            game_info.extend([game[1], str(game[0]), game[2], game[3]])
            game_info.extend(self.get_game_info(game[0]))
            game_info.extend(self.get_game_platform_info(game[0]))
            game_info.append(self.get_user_rate_info(game[0]))
            complete_list_games.append("/".join(game_info))
        return ":".join(complete_list_games)

    def get_game_info(self, game_id):
        publisher = self.data_b.get("publishers", "publisher", "id", game_id)
        developer = self.data_b.get("publishers", "developer", "id", game_id)
        critic_rate = str(self.data_b.get("rates", "critic_rate", "id", game_id))
        user_rate = str(self.data_b.get("rates", "user_rate", "id", game_id))
        data = [publisher, developer, critic_rate, user_rate]
        return data

    def get_game_platform_info(self, game_id):
        pc_info = self.data_b.get("platforms", "pc", "id", game_id)
        ps4_info = self.data_b.get("platforms", "ps4", "id", game_id)
        xone_info = self.data_b.get("platforms", "xbox_one", "id", game_id)
        pc = "Available" if pc_info == 1 else "None"
        ps4 = "Available" if ps4_info == 1 else "None"
        xone = "Available" if xone_info == 1 else "None"
        data = [pc, ps4, xone]
        return data

    def update_user_rate(self, rate, game_id):
        str_rate = ""
        if rate == 1:
            str_rate = "one"
        elif rate == 2:
            str_rate = "two"
        elif rate == 3:
            str_rate = "three"
        elif rate == 4:
            str_rate = "four"
        else:
            str_rate = "five"
        column = str_rate + "_star_review"
        number_of_rates = int(self.data_b.get("feedback", column, "id", game_id)) + 1
        self.data_b.update("feedback", column, number_of_rates, "id", game_id)

    def get_user_rate_info(self, game_id):
        one_star_count = int(self.data_b.get("feedback", "one_star_review", "id", game_id))
        two_star_count = int(self.data_b.get("feedback", "two_star_review", "id", game_id))
        three_star_count = int(self.data_b.get("feedback", "three_star_review", "id", game_id))
        four_star_count = int(self.data_b.get("feedback", "four_star_review", "id", game_id))
        five_star_count = int(self.data_b.get("feedback", "five_star_review", "id", game_id))
        all_reviews_count = one_star_count + two_star_count \
                            + three_star_count + four_star_count \
                            + five_star_count
        try:
            average_user_score = (1 * one_star_count + 2 * two_star_count
                              + 3 * three_star_count + 4 * four_star_count
                              + 5 * five_star_count) / all_reviews_count
            return str(round(average_user_score, 2))
        except ZeroDivisionError:
            average_user_score = "No rates"
            return average_user_score


