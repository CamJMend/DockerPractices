import random
import time

def simulate_match():
    chivas_score = 0
    atlas_score = 0

    print("Simulación del partido Chivas vs Atlas\n")

    for minute in range(1, 91):
        team_turn = "Chivas" if random.choice([True, False]) else "Atlas"
        action = random.randint(1, 350)

        if 1 <= action <= 100:
            event = f"{team_turn} dispara desviado."
        elif 101 <= action <= 200:
            event = f"{team_turn} dispara y el portero ataja."
        elif 201 <= action <= 250:
            event = f"{team_turn} anota un gol de cabeza!"
            if team_turn == "Chivas":
                chivas_score += 1
            else:
                atlas_score += 1
        elif 251 <= action <= 300:
            event = f"{team_turn} anota un gol de penal!"
            if team_turn == "Chivas":
                chivas_score += 1
            else:
                atlas_score += 1
        elif 301 <= action <= 350:
            event = f"{team_turn} anota un gol con el pie!"
            if team_turn == "Chivas":
                chivas_score += 1
            else:
                atlas_score += 1

        print(f"Min {minute}: {event}")
        time.sleep(0.05)

    print(f"\nMarcador final: Chivas {chivas_score} - {atlas_score} Atlas")

if __name__ == "__main__":
    simulate_match()
