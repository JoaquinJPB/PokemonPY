
#Pokemon stats

HP = "HP"
ATTACK = "Attack"
DEFENSE = "Defense"
SPATK = "Sp.Attack"
SPDEF = "Sp.Defense"
SPEED = "Speed"

#Command
DO_ATTACK = "attack"
DO_ATTACK_SELECTION = "selected_attack"

#Attack Categories
PHYSICAL = "physical"
SPECIAL = "special"

NATURES = [
    "Hardy",
    "Lonely",
    "Brave",
    "Adamant",
    "Naughty",
    "Bold",
    "Docile",
    "Relaxed",
    "Impish",
    "Lax",
    "Timid",
    "Hasty",
    "Serious",
    "Jolly",
    "Naive",
    "Modest",
    "Mild",
    "Quiet",
    "Bashful",
    "Rash",
    "Calm",
    "Gentle",
    "Sassy",
    "Careful",
    "Quirky"
]

NATURE_MATRIX = [
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1},         # Hardy
    {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPATK: 1, SPDEF: 1, SPEED: 1},     # Lonely
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 0.9},     # Brave
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATK: 0.9, SPDEF: 1, SPEED: 1},     # Adamant
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATK: 1, SPDEF: 0.9, SPEED: 1},     # Naughty
    {HP: 1, ATTACK: 0.9, DEFENSE: 1.1, SPATK: 1, SPDEF: 1, SPEED: 1},     # Bold
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1},         # Docile
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATK: 1, SPDEF: 1, SPEED: 0.9},     # Relaxed
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATK: 0.9, SPDEF: 1, SPEED: 1},     # Impish
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATK: 1, SPDEF: 0.9, SPEED: 1},     # Lax
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1.1},     # Timid
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATK: 1, SPDEF: 1, SPEED: 1.1},     # Hasty
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1},         # Serious
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 0.9, SPDEF: 1, SPEED: 1.1},     # Jolly
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 0.9, SPEED: 1.1},     # Naive
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATK: 1.1, SPDEF: 1, SPEED: 1},     # Modest
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATK: 1.1, SPDEF: 1, SPEED: 1},     # Mild
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1.1, SPDEF: 1, SPEED: 0.9},     # Quiet
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1},         # BashFul
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1.1, SPDEF: 0.9, SPEED: 1},     # Rash
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATK: 1, SPDEF: 1.1, SPEED: 1},     # Calm
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATK: 1, SPDEF: 1.1, SPEED: 1},     # Gentle
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1.1, SPEED: 0.9},     # Sassy
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 0.9, SPDEF: 1.1, SPEED: 1},     # Careful
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATK: 1, SPDEF: 1, SPEED: 1}          # Quirky
]

TYPES = [
    "Normal",
    "Fighting",
    "Flying",
    "Poison",
    "Ground",
    "Rock",
    "Bug",
    "Ghost",
    "Steel",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Psychic",
    "Ice",
    "Dragon",
    "Dark",
    "Fairy"
    ]

TYPE_CHART = [
    [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,2],
    [1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,1],
    [1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,.5],
    [1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,1],
    [.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,1],
    [1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,1],
    [0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,1],
    [.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,.5],
    [1,1,1,1,2,2,.5,1,.5,.5,2,.5,1,1,.5,1,1,.5],
    [1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1],
    [1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,1],
    [1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,1],
    [1,.5,1,1,1,1,2,2,1,1,1,1,1,.5,1,1,2,1],
    [1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1],
    [1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,2],
    [1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,2],
    [1,.5,1,2,1,1,.5,1,2,1,1,1,1,1,1,0,.5,1]
    ]