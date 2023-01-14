import random

from champions import Champions


class PickBan:
    def __init__(self):
        self.banned_champions = []
        self.blue_team_champions = []
        self.red_team_champions = []

    def ban_champion(self, champion_name):
        if champion_name in Champions.champions:
            self.banned_champions.append(champion_name)
        else:
            print(f"{champion_name} is not a valid champion.")

    def pick_champion(self, champion_name, team):
        if champion_name in Champions.champions and champion_name not in self.banned_champions:
            if team == "blue" and champion_name not in self.blue_team_champions:
                self.blue_team_champions.append(champion_name)
            elif team == "red" and champion_name not in self.red_team_champions:
                self.red_team_champions.append(champion_name)
            else:
                print(f"{champion_name} has already been picked for the {team} team.")
        elif champion_name in self.banned_champions:
            print(f"{champion_name} has already been banned.")
        else:
            print(f"{champion_name} is not a valid champion.")

    def choose_ai_champion(self, ai_team, banned_or_picked_champions):
        # Get a list of champions that are available for the AI to pick or ban
        available_champions = [champion for champion in Champions.champions if champion not in banned_or_picked_champions]

        # Choose a random champion from the list of available champions
        ai_champion = random.choice(available_champions)
        return ai_champion


def main():
    pickban = PickBan()
    print("Welcome to the Pick/Ban phase! You can pick either the Blue team or the Red team.")

    # Let the player choose their team
    player_team = input("Which team do you want to play on (blue/red)? ")
    if player_team == "blue":
        ai_team = "red"
    else:
        ai_team = "blue"

    # The Pick/Ban phase starts with 5 bans each
    bans_remaining = 10
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

    # Once the Pick/Ban phase is over, start the champion selection phase
    picks_remaining = 5
    turn = "blue"
    while picks_remaining > 0:
        if turn == player_team:
            print(f"It's your turn to pick ({turn} team). You have {picks_remaining} picks remaining.")
            champion_name = input("Enter the name of the champion you want to pick: ")
            pickban.pick_champion(champion_name, player_team)
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            turn = ai_team
        else:
            print(f"It's the AI's turn to pick ({turn} team). {picks_remaining} picks remaining.")
            ai_champion = pickban.choose_ai_champion(ai_team,
                                                     pickban.banned_champions + pickban.blue_team_champions + pickban.red_team_champions)
            pickban.pick_champion(ai_champion, ai_team)
            print(f"The AI picked {ai_champion}.")
            print(f"Blue team: {pickban.blue_team_champions}")
            print(f"Red team: {pickban.red_team_champions}")
            print(f"Bans: {pickban.banned_champions}")
            picks_remaining -= 1
            turn = player_team


if __name__ == "__main__":
    main()
