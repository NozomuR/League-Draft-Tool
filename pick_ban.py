import random

from champions import Champions


class PickBan:
    def __init__(self):
        self.banned_champions = []
        self.blue_team_champions = []
        self.red_team_champions = []

    def ban_champion(self, champion_name):
        if champion_name in Champions.champions:
            if champion_name not in self.banned_champions:
                self.banned_champions.append(champion_name)
                print(f"{champion_name} banned.")
                Champions.champions.pop(champion_name, None)
            else:
                print(f"{champion_name} has already been banned.")
        else:
            print(f"{champion_name} is not a valid champion.")
            self.ban_champion(input("Enter a valid champion to ban: "))

    def pick_champion(self, champion_name, team):
        if champion_name in Champions.champions:
            if champion_name not in self.banned_champions:
                if team == "blue" and champion_name not in self.blue_team_champions:
                    self.blue_team_champions.append(champion_name)
                    print(f"{champion_name} picked for blue team.")
                    Champions.champions.pop(champion_name, None)
                elif team == "red" and champion_name not in self.red_team_champions:
                    self.red_team_champions.append(champion_name)
                    print(f"{champion_name} picked for red team.")
                    Champions.champions.pop(champion_name, None)
                else:
                    print(f"{champion_name} has already been picked for the {team} team.")
            else:
                print(f"{champion_name} has already been banned.")
        else:
            print(f"{champion_name} is not a valid champion.")
            self.pick_champion(input("Enter a valid champion to pick: "), team)

    def choose_ai_champion(self, ai_team, banned_or_picked_champions):
        # Get a list of champions that are available for the AI to pick or ban
        available_champions = [champion for champion in Champions.champions if champion not in banned_or_picked_champions]

        # Choose a random champion from the list of available champions
        ai_champion = random.choice(available_champions)
        return ai_champion


def main():
    pickban = PickBan()
    draft_portion = 1
    print("Welcome to the Pick/Ban phase! You can pick either the Blue team or the Red team.")

    # Let the player choose their team
    player_team = input("Which team do you want to play on (blue/red)? ")
    if player_team == "blue":
        ai_team = "red"
    else:
        ai_team = "blue"



    # Phase 1: Each team bans 3 champions
    bans_remaining = 6
    turn = "blue"
    while bans_remaining > 0:
        if turn == player_team:
            print(f"It's your turn to ban ({turn} team). You have {bans_remaining} bans remaining.")
            champion_name = input("Enter the name of the champion you want to ban: ")
            pickban.ban_champion(champion_name)
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            bans_remaining -= 1
            turn = ai_team
        else:
            print(f"It's the AI's turn to ban ({turn} team). {bans_remaining} bans remaining.")
            ai_champion = pickban.choose_ai_champion(ai_team, pickban.banned_champions)
            pickban.ban_champion(ai_champion)
            print(f"The AI banned {ai_champion}.")
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            bans_remaining -= 1
            turn = player_team

    # Phase 2: 3 picks each, blue goes first, red goes second and third, blue goes fourth, blue goes fifth, red goes sixth
    picks_remaining = 6
    phase_turn = 1

    while picks_remaining > 0:
        if phase_turn == 1:
            print(f"It's the blue team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "blue":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.blue_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 2

        if phase_turn == 2:
            print(f"It's the red team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "red":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.red_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 3

        if phase_turn == 3:
            print(f"It's the red team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "red":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.red_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 4

        if phase_turn == 4:
            print(f"It's the blue team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "blue":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.blue_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 5

        if phase_turn == 5:
            print(f"It's the blue team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "blue":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.blue_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 6

        if phase_turn == 6:
            print(f"It's the red team's turn to pick. {picks_remaining} picks remaining.")

            if player_team == "red":
                champion_name = input("Enter the name of the champion you want to pick: ")
                pickban.pick_champion(champion_name, player_team)
            else:
                ai_champion = pickban.choose_ai_champion(ai_team, pickban.red_team_champions)
                pickban.pick_champion(ai_champion, ai_team)
                print(f"The AI picked {ai_champion}.")

            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            phase_turn = 7

    # Phase 3: Each team bans 2 champions
    bans_remaining = 4
    turn = "red"
    while bans_remaining > 0:
        if turn == player_team:
            print(f"It's your turn to ban ({turn} team). You have {bans_remaining} bans remaining.")
            champion_name = input("Enter the name of the champion you want to ban: ")
            pickban.ban_champion(champion_name)
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            bans_remaining -= 1
            turn = ai_team
        else:
            print(f"It's the AI's turn to ban ({turn} team). {bans_remaining} bans remaining.")
            ai_champion = pickban.choose_ai_champion(ai_team, pickban.banned_champions)
            pickban.ban_champion(ai_champion)
            print(f"The AI banned {ai_champion}.")
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            bans_remaining -= 1
            turn = player_team

        # Phase 4: 2 picks each, red goes first, blue goes second and third, red goes fourth.
        picks_remaining = 4
        phase_turn = 1

        while picks_remaining > 0:
            if phase_turn == 1:
                print(f"It's the red team's turn to pick. {picks_remaining} picks remaining.")

                if player_team == "red":
                    champion_name = input("Enter the name of the champion you want to pick: ")
                    pickban.pick_champion(champion_name, player_team)
                else:
                    ai_champion = pickban.choose_ai_champion(ai_team, pickban.red_team_champions)
                    pickban.pick_champion(ai_champion, ai_team)
                    print(f"The AI picked {ai_champion}.")

                print(f"Blue team: {pickban.blue_team_champions}")
                print(f"Red team: {pickban.red_team_champions}")
                print(f"Bans: {pickban.banned_champions}")
                picks_remaining -= 1
                phase_turn = 2

            if phase_turn == 2:
                print(f"It's the blue team's turn to pick. {picks_remaining} picks remaining.")

                if player_team == "blue":
                    champion_name = input("Enter the name of the champion you want to pick: ")
                    pickban.pick_champion(champion_name, player_team)
                else:
                    ai_champion = pickban.choose_ai_champion(ai_team, pickban.blue_team_champions)
                    pickban.pick_champion(ai_champion, ai_team)
                    print(f"The AI picked {ai_champion}.")

                print(f"Blue team: {pickban.blue_team_champions}")
                print(f"Red team: {pickban.red_team_champions}")
                print(f"Bans: {pickban.banned_champions}")
                picks_remaining -= 1
                phase_turn = 3

            if phase_turn == 3:
                print(f"It's the blue team's turn to pick. {picks_remaining} picks remaining.")

                if player_team == "blue":
                    champion_name = input("Enter the name of the champion you want to pick: ")
                    pickban.pick_champion(champion_name, player_team)
                else:
                    ai_champion = pickban.choose_ai_champion(ai_team, pickban.blue_team_champions)
                    pickban.pick_champion(ai_champion, ai_team)
                    print(f"The AI picked {ai_champion}.")

                print(f"Blue team: {pickban.blue_team_champions}")
                print(f"Red team: {pickban.red_team_champions}")
                print(f"Bans: {pickban.banned_champions}")
                picks_remaining -= 1
                phase_turn = 4

            if phase_turn == 4:
                print(f"It's the red team's turn to pick. {picks_remaining} picks remaining.")

                if player_team == "red":
                    champion_name = input("Enter the name of the champion you want to pick: ")
                    pickban.pick_champion(champion_name, player_team)
                else:
                    ai_champion = pickban.choose_ai_champion(ai_team, pickban.red_team_champions)
                    pickban.pick_champion(ai_champion, ai_team)
                    print(f"The AI picked {ai_champion}.")

                print(f"Blue team: {pickban.blue_team_champions}")
                print(f"Red team: {pickban.red_team_champions}")
                print(f"Bans: {pickban.banned_champions}")
                picks_remaining -= 1
                phase_turn = 5


if __name__ == "__main__":
    main()
