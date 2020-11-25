from constants import *

from models.Pokemon import *
from models.Battle import *

#First, define pokemon with his stats
pokemon1 = Pokemon("Scrafty", 50, 1, 16)
pokemon2 = Pokemon("Tyranitar", 50, 5, 16)
pokemon1.current_hp = 172
pokemon2.current_hp = 176

#Stats
pokemon1.baseStats = {
    HP : 65,
    ATTACK : 90,
    DEFENSE: 115,
    SPATK: 45,
    SPDEF: 115,
    SPEED: 58,
}

pokemon1.ev = {
    HP: 252,
    ATTACK: 252,
    DEFENSE: 0,
    SPATK: 0,
    SPDEF: 0,
    SPEED: 4
}

pokemon1.iv = {
    HP: 31,
    ATTACK: 31,
    DEFENSE: 31,
    SPATK: 31,
    SPDEF: 31,
    SPEED: 31
}

pokemon2.baseStats = {
    HP : 100,
    ATTACK : 165,
    DEFENSE: 150,
    SPATK: 95,
    SPDEF: 120,
    SPEED: 71,
}

pokemon2.ev = {
    HP: 4,
    ATTACK: 252,
    DEFENSE: 0,
    SPATK: 0,
    SPDEF: 0,
    SPEED: 252
}

pokemon2.iv = {
    HP: 31,
    ATTACK: 31,
    DEFENSE: 31,
    SPATK: 31,
    SPDEF: 31,
    SPEED: 31
}
pokemon1.compute_stats()
pokemon2.compute_stats()
print(pokemon1.stats)
print(pokemon2.stats)

#Attacks
pokemon1.attacks = [Attack("Close Combat", 1, PHYSICAL, 5, 120, 100)]
pokemon2.attacks = [Attack("Rock Slide", 5, PHYSICAL, 10, 75, 90)]

#Start_battle
battle = Battle(pokemon1,pokemon2)


def ask_command(pokemon):
    command = None
    while not command:
        #DO ATTACK -> attack 0
        tmp_command = input("What should "+pokemon.name+" do? ").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


while not battle.is_finished() :
    #First ask for command
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        battle.execute_turn(turn)
        battle.print_current_status()

