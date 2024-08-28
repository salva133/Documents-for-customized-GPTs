import random

# Regel 1: Münzwurf für tägliche Patrouillenanforderung
def patrol_required():
    return random.randint(1, 10) > 1  # 90% Wahrscheinlichkeit, dass eine Patrouille angefordert wird

# Regel 2: Zufällige Teameinteilung vor jeder Mission
def assign_teams(members):
    random.shuffle(members)
    return members[:2], members[2:]  # Zwei Zweierteams

# Regel 3: Münzwurf für Feindkontakt bei jeder Mission
def enemy_encounter():
    return random.choice([True, False])  # 50% Wahrscheinlichkeit für Feindkontakt

# Regel 4: Zufallsfeinde bei Feindkontakt
def determine_enemy_faction():
    roll = random.randint(1, 100)
    if roll <= 5:
        return "Clan Truppen"  # 5% Wahrscheinlichkeit für Clantruppen
    elif roll <= 75:
        return "Piraten"  # 70% Wahrscheinlichkeit für Piraten
    else:
        return "Feindliche Söldner"  # 25% Wahrscheinlichkeit für feindliche Söldner

# Regel 5: Münzwurf für hidden_flaw_roll bei Systemchecks
def hidden_flaw_roll():
    return random.choice([True, False])  # 50% Wahrscheinlichkeit für eine versteckte Macke

# Regel 6: Pre-Mission Gespräch wird während der Mission geführt
def during_mission_conversation(team):
    return f"Smalltalk während der Mission zwischen {team[0]} und {team[1]}"

# Regel 7: Tägliches Ereignis während des Frühstücks vor dem Briefing
def generate_breakfast_event():
    events = [
        "Ein Kollege verschüttet Kaffee",
        "Leichte Diskussion über das Wetter",
        "Kurze Unterhaltung über die letzte Mission",
        "Ein kurzes Lachen über einen alten Witz",
        "Ein unerwarteter Besucher tritt in die Kantine"
    ]
    return random.choice(events)

# Regel 8: Patrouillen dauern immer bis in den Nachmittag hinein
def mission_duration():
    return "Mission dauert bis zum Nachmittag"

# Regel 9: 50% Wahrscheinlichkeit für Feindkontakt
def fifty_percent_enemy_encounter():
    return random.choice([True, False])  # 50% Wahrscheinlichkeit für Feindkontakt

# Regel 10: 50% Wahrscheinlichkeit für hidden_flaw_roll
def fifty_percent_hidden_flaw():
    return random.choice([True, False])  # 50% Wahrscheinlichkeit für eine versteckte Macke

# Skill Check: Allgemeiner Check für Fähigkeiten
def skill_check(skill_level, difficulty):
    roll = random.randint(1, 12) + skill_level
    return roll >= difficulty

# Mech System Check: Überprüfung eines Mech-Systems
def mech_system_check(system_reliability, mechanic_skill):
    roll = random.randint(1, 12) + mechanic_skill
    return roll >= system_reliability

# Perform Mech Check: Überprüfung auf versteckte Macken
def perform_mech_check(hidden_flaw_roll, mech_system_check):
    if hidden_flaw_roll:
        return mech_system_check
    return "No hidden flaws detected"

# Tactic Check: Wurf für taktische Entscheidungen
def tactic_check(tactic_skill, enemy_tactic_level):
    roll = random.randint(1, 12) + tactic_skill
    return roll >= enemy_tactic_level

# Port Moresby Attack: Bestimmung, ob Port Moresby angegriffen wird
def port_moresby_attack():
    roll = random.randint(1, 100)
    if roll <= 5:
        return "Clan Angriff"
    elif roll <= 30:
        return "Angriff durch Draconis-Kombinat"
    elif roll <= 60:
        return "Angriff durch Söldner"
    else:
        return "Keine Angriffe"

