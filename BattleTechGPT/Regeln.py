import random

# Regel 1: Würfelwürfe bei Fähigkeitschecks
def skill_check(skill_value, target_number):
    """
    Führt einen Würfelwurf durch, um den Erfolg einer Aktion zu bestimmen.
    :param skill_value: Der Wert der Fähigkeit
    :param target_number: Der Zielwert, der erreicht werden muss
    :return: True, wenn der Wurf erfolgreich ist, sonst False
    """
    roll = random.randint(1, 12) + skill_value  # Beispiel für 2W6 + Skill-Wert
    return roll >= target_number

# Regel 2: Systemchecks bei Mechs
def mech_system_check():
    """
    Führt einen Systemcheck bei einem Mech durch, um festzustellen, ob eine versteckte Macke vorliegt.
    :return: True, wenn eine Macke gefunden wird, sonst False
    """
    hidden_flaw_roll = random.randint(1, 100)
    return hidden_flaw_roll <= 50  # 50% Chance auf eine versteckte Macke

def perform_mech_check():
    """
    Überprüft, ob der Mechaniker-Check erfolgreich ist und die Macke entdeckt wird.
    :return: True, wenn die Macke entdeckt wird, sonst False
    """
    mech_check_success = skill_check(skill_value=3, target_number=10)  # Beispielwerte
    if mech_system_check():
        return mech_check_success
    return False

# Regel 3: Taktische Entscheidungen
def tactic_check(tactics_value, difficulty):
    """
    Führt einen Taktik-Check durch, um den Erfolg einer taktischen Entscheidung zu bestimmen.
    :param tactics_value: Der Wert der Taktik-Fähigkeit
    :param difficulty: Der Schwierigkeitsgrad (Zielwert)
    :return: True, wenn der Wurf erfolgreich ist, sonst False
    """
    return skill_check(tactics_value, difficulty)

# Regel 4: Vertrauen innerhalb der Iron Wolves (logisch, keine spezifische Implementierung notwendig)
# Diese Regel beschreibt die Dynamik zwischen den Charakteren und beeinflusst die Story-Entscheidungen.

# Regel 5: Tagespatrouillenregel
def daily_patrol():
    """
    Bestimmt, ob an diesem Tag eine Patrouille angefordert wird (10% Chance auf keine Patrouille).
    :return: True, wenn eine Patrouille angefordert wird, sonst False
    """
    return random.randint(1, 100) > 10

def assign_patrol_teams(soldiers):
    """
    Zufällige Zuweisung der Söldner zu zwei Teams.
    :param soldiers: Liste der Soldaten
    :return: Zwei Listen mit Soldaten in Team 1 und Team 2
    """
    random.shuffle(soldiers)
    mid = len(soldiers) // 2
    return soldiers[:mid], soldiers[mid:]

# Regel 6: Feindkontaktregel für Patrouillen
def encounter_check():
    """
    Münzwurf für jedes Team (50% Chance auf Feindkontakt).
    :return: True, wenn Feindkontakt, sonst False
    """
    return random.choice([True, False])

def determine_enemy():
    """
    Bestimmt den Typ des Feindes.
    :return: Typ des Feindes
    """
    roll = random.randint(1, 100)
    if roll <= 5:
        return "Clantruppen"
    elif roll <= 50:
        return "Piraten"
    else:
        return "Feindliche Söldnertruppe"

def patrol_scenario(soldiers):
    """
    Generiert das Szenario für eine Patrouille.
    :param soldiers: Liste der Soldaten
    :return: Ein Szenario-Dictionary mit den Ergebnissen für die Teams
    """
    patrol_status = daily_patrol()
    if not patrol_status:
        return "Keine Patrouille angefordert"

    team1, team2 = assign_patrol_teams(soldiers)
    scenario = {"Team 1": team1, "Team 2": team2}

    if encounter_check():
        enemy1 = determine_enemy()
        scenario["Team 1 Encounter"] = enemy1
        if enemy1 == "Clantruppen":
            scenario["Team 1 Action"] = "Zurückkehren und Bericht erstatten"
        else:
            scenario["Team 1 Action"] = "Kämpfen"
    else:
        scenario["Team 1 Encounter"] = "Keine Feinde"

    if encounter_check():
        enemy2 = determine_enemy()
        scenario["Team 2 Encounter"] = enemy2
        if enemy2 == "Clantruppen":
            scenario["Team 2 Action"] = "Zurückkehren und Bericht erstatten"
        else:
            scenario["Team 2 Action"] = "Kämpfen"
    else:
        scenario["Team 2 Encounter"] = "Keine Feinde"

    return scenario

# Regel 7: Gesellschaftliche Phase nach jeder Mission
def social_phase(soldier):
    """
    Simuliert eine gesellschaftliche Phase nach einer Mission.
    :param soldier: Der Soldat, der an der gesellschaftlichen Phase teilnimmt
    """
    interactions = [
        f"{soldier} spielt Karten mit einem anderen Söldner.",
        f"{soldier} gesellt sich zur Bar und plaudert.",
        f"{soldier} zieht sich zurück, um nachzudenken.",
        f"{soldier} führt eine lockere Unterhaltung mit der Gruppe.",
        f"{soldier} sucht das Gespräch mit Captain Mason."
    ]
    return random.choice(interactions)

# Regel 8: Konversationelle Phase während der Mission
def during_mission_conversation(soldier, teammate):
    """
    Simuliert eine kurze konversationelle Phase während einer Mission.
    :param soldier: Der Soldat
    :param teammate: Der Teampartner
    """
    conversations = [
        f"{soldier} fragt {teammate}, wie sie den Tag finden.",
        f"{soldier} diskutiert mit {teammate} über die letzte Mission.",
        f"{soldier} teilt mit {teammate} eine Erinnerung aus früheren Zeiten.",
        f"{soldier} tauscht sich mit {teammate} über ihre Pläne nach der Mission aus."
    ]
    return random.choice(conversations)
