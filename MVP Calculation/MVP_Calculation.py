def kda_calculation(kills, deaths, assists):
        
    if deaths == 0:
        effective_death = 1
    else:
        effective_death = deaths
        
    kda = (kills + assists) / effective_death
    return kda

def mvp_calculation(kills, deaths, assists):
    kill_point = kills * 5
    assist_point = assists * 3
    death_penality = deaths * 2

    total_score = (kill_point + assist_point) - death_penality
    return total_score

try:
    kills = int(input("Enter your total kills: "))
    deaths = int(input("Enter your total deaths: "))
    assists = int(input("Enter your total assists: "))

    print(f"Your KDA: {kda_calculation(kills, deaths, assists)}")
    print(f"MVP score: {mvp_calculation(kills, deaths, assists)}")

except ValueError:
    print("Please enter a valid num")