from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_2.Items import Ty2Item
from worlds.ty_the_tasmanian_tiger_2.Locations import Ty2Location, mission_dict


def has_infra(world, state):
    state.has("Progressive Infrarang", world.player) or state.has("Infrarang", world.player) or state.has("X-Rang", world.player)
def can_smash_crate(world, state):
    (state.has("Progressive Smasharang", world.player, 1) or state.has("Craftyrang", world.player) or state.has("Smasharang", world.player)
     or state.has("Kaboomarang", world.player) or state.has("Deadlyrang", world.player) or state.has("Deadlyrang", world.player))
def can_smash_wall(world, state):
    (state.has("Progressive Smasharang", world.player, 2) or state.has("Smasharang", world.player)
     or state.has("Kaboomarang", world.player) or state.has("Deadlyrang", world.player) or state.has("Deadlyrang", world.player))

def get_rules(world):
    rules = {
        "locations": {
            "Platinum Cog 5": lambda state: can_smash_wall(world, state),
        },
        "entrances": {
            "Burramudgee Town -> Infra":
                lambda state: has_infra(world, state),
        }
    }
    return rules

mission_locations = []

def set_rules(world):
    mission_locations.clear()
    for mission_name, mission_data in mission_dict.items():
        mission_locations.append(world.get_location(mission_name, world.player))

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    world.multiworld.get_location(f"Boss Cass Bust-Up", world.player).place_locked_item(
        Ty2Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)