from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_2.Items import Ty2Item
from worlds.ty_the_tasmanian_tiger_2.Locations import Ty2Location, mission_dict, full_location_dict

def has_infra(world, state):
    return (state.has("Progressive Infrarang", world.player)
            or state.has("Infrarang", world.player)
            or state.has("X-Rang", world.player))

def can_cold(world, state):
    return (can_freeze(world, state)
            or state.has("Thermo Bunyip Key", world.player))

def can_smash_crate(world, state):
    return (state.has("Progressive Smasharang", world.player, 1)
            or state.has("Craftyrang", world.player)
            or can_smash_wall(world, state))

def can_smash_wall(world, state):
    return (state.has("Progressive Smasharang", world.player, 2)
            or state.has("Smasharang", world.player)
            or state.has("Kaboomarang", world.player)
            or state.has("Deadlyrang", world.player)
            or state.has("Doomerang", world.player))

def can_burn(world, state):
    return (state.has("Progressive Flamerang", world.player, 1)
            or state.has("Flamerang", world.player)
            or state.has("Lavarang", world.player))

def can_freeze(world, state):
    return (state.has("Progressive Frostyrang", world.player, 1)
    or state.has("Frostyrang", world.player)
    or state.has("Freezerang", world.player))

def can_zap(world, state):
    return (state.has("Progressive Zappyrang", world.player, 1)
    or state.has("Zappyrang", world.player)
    or state.has("Thunderang", world.player))

def can_swing(world, state):
    return (state.has("Progressive Lasharang", world.player, 1)
     or state.has("Lasharang", world.player)
     or state.has("Warperang", world.player))

def can_tp(world, state):
    return (state.has("Progressive Lasharang", world.player, 2)
            or state.has("Warperang", world.player))

def get_rules(world):
    rules = {
        "locations": {
            #collectable shops
            "Trader Bob's Cog Item 1": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:1])),
            "Trader Bob's Cog Item 2": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:2])),
            "Trader Bob's Cog Item 3": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:3])),
            "Trader Bob's Cog Item 4": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:4])),
            "Trader Bob's Cog Item 5": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:5])),
            "Trader Bob's Cog Item 6": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:6])),
            "Trader Bob's Cog Item 7": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:7])),
            "Trader Bob's Cog Item 8": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:8])),
            "Trader Bob's Cog Item 9": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:9])),
            "Trader Bob's Cog Item 10": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:10])),
            "Madam Mopoke's Orb Item 1": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:1])),
            "Madam Mopoke's Orb Item 2": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:2])),
            "Madam Mopoke's Orb Item 3": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:3])),
            #Missions
            "Haunted Hassle": lambda state:
                has_infra(world, state),
            "Lava Chill Out": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Hidden Danger": lambda state:
                has_infra(world, state),
            "Deep Sea Scare": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Sea Lab": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Snake Eyes": lambda state:
                can_freeze(world, state),
            "Oil Rig Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Truck Tragedy": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Truck Stop": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Bush Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Killer Koala": lambda state:
                has_infra(world, state) and state.has("Disguised Frill Found", world.player, 25),
            "Grub Grab": lambda state:
                state.has("Parking Bay - Burramudgee Town", world.player) and (state.has("Patchy Barriers", world.player) or state.has("Buster Barriers", world.player)),
            "Ripper Nipper": lambda state:
                state.has("Parking Bay - Wobbygon Bay", world.player) and state.has("Parking Bay - Ripper Nipper", world.player),
            #Cogs
            "Outback Oasis Cog 1": lambda state:
                can_smash_wall(world, state),
            "Outback Oasis Cog 3": lambda state:
                can_smash_wall(world, state),
            "Never Never Cog 2": lambda state:
                can_smash_wall(world, state),
            "Never Never Cog 8": lambda state:
                (can_swing(world, state)  or can_cold(world, state)) and state.has("Thermo Bunyip Key", world.player),
            "Never Never Cog 16": lambda state:
                can_smash_wall(world, state),
            "Faire Dinkum Cog 1": lambda state:
                can_smash_wall(world, state),
            "Faire Dinkum Cog 2": lambda state:
                can_smash_wall(world, state),
            "Sulphur Rocks Cog 1": lambda state:
                can_freeze(world, state),
            "Sulphur Rocks Cog 2": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Sulphur Rocks Cog 3": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Cog 4": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Cog 9": lambda state:
                can_tp(world, state),
            "Burramudgee Cog 2": lambda state:
                can_smash_crate(world, state),
            "Burramudgee Cog 3": lambda state:
                has_infra(world, state),
            "Mount Boom Cog 2": lambda state:
                can_tp(world, state),
            "Mount Boom Cog 3": lambda state:
                can_tp(world, state),
            "Mount Boom Cog 4": lambda state:
                can_tp(world, state),
            "Wetlands Cog 2": lambda state:
                can_smash_wall(world, state),
            "Wetlands Cog 5": lambda state:
                can_burn(world, state),
            #Orbs
            "Burramudgee Orb 1": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Orb 1": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Orb 2": lambda state:
                can_swing(world, state) and can_freeze(world, state),
            "Mount Boom Orb 2": lambda state:
                can_tp(world, state) and can_smash_wall(world, state),
            "Outback Oasis Orb 1": lambda state:
                can_smash_wall(world, state),
            "Never Never Orb 1": lambda state:
                can_smash_wall(world, state),
            "Never Never Orb 2": lambda state:
                can_swing(world, state),
            "Never Never Orb 3": lambda state:
                can_swing(world, state),
            "Never Never Orb 6": lambda state:
                can_swing(world, state),
            "Never Never Orb 7": lambda state:
                can_swing(world, state),
            "Wetlands Orb": lambda state:
                can_swing(world, state),
            "Dennis Freeway Orb": lambda state:
                can_tp(world, state),
            "Burramudgee Orb 4": lambda state:
                can_freeze(world, state),
            #Bilbies
            "Outback Oasis Bilby 1": lambda state:
                can_smash_wall(world,state),
            "Never Never Bilby 2": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Frill Neck Bilby 1": lambda state:
                can_swing(world, state),
            "Mount Boom Bilby 1": lambda state:
                can_swing(world, state) and state.has("Thermo Bunyip Key", world.player),
            "Mount Boom Bilby 2": lambda state:
                can_tp(world, state),
            "Wetlands Bilby 2": lambda state:
                can_burn(world, state),
            "Wetlands Bilby 3": lambda state:
                can_burn(world, state),
            #Frills
            "Outback Oasis Frill 1": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_smash_wall(world, state),
            "Outback Oasis Frill 2": lambda state:
                has_infra(world, state),
            "Outback Oasis Frill 3": lambda state:
                has_infra(world, state),
            "Never Never Frill 1": lambda state:
                has_infra(world, state),
            "Never Never Frill 2": lambda state:
                has_infra(world, state),
            "Never Never Frill 3": lambda state:
                has_infra(world, state),
            "Wetlands Frill 1": lambda state:
                has_infra(world, state),
            "Wetlands Frill 2": lambda state:
                has_infra(world, state),
            "Faire Dinkum Frill": lambda state:
                has_infra(world, state),
            "Sulphur Rocks Frill 1": lambda state:
                has_infra(world, state),
            "Sulphur Rocks Frill 2": lambda state:
                has_infra(world, state),
            "Sulphur Rocks Frill 3": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_swing(world, state),
            "Burramudgee Frill 1": lambda state:
                has_infra(world, state),
            "Burramudgee Frill 2": lambda state:
                has_infra(world, state),
            "Dennis Freeway Frill": lambda state:
                has_infra(world, state),
            "Outback Oasis Frill 4": lambda state:
                has_infra(world, state),
            "Dusty Burrows Frill": lambda state:
                has_infra(world, state),
            "Lake Burramudgee Frill": lambda state:
                has_infra(world, state),
            "Frill Neck Frill 1": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Truck Tragedy Frill": lambda state:
                has_infra(world, state),
            "Never Never Frill 4": lambda state:
                has_infra(world, state),
            "Sheep Dip Frill": lambda state:
                has_infra(world, state),
            "Frill Neck Frill 2": lambda state:
                has_infra(world, state),
            "Mount Boom Frill 1": lambda state:
                has_infra(world, state) and state.has("Thermo Bunyip Key", world.player),
            "Mount Boom Frill 2": lambda state:
                has_infra(world, state),
            #Steves
            "Steve - Outback Oasis": lambda state:
                can_swing(world, state),
            "Steve - Mount Boom": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Steve - Never Never": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            #Frames
            "Outback Oasis Frame 1": lambda state:
                can_tp(world, state),
            "Outback Oasis Frame 2": lambda state:
                can_tp(world, state),
            "Outback Oasis Frame 3": lambda state:
                can_tp(world, state),
            "Never Never Frame 1": lambda state:
                can_swing(world, state),
            "Never Never Frame 4": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Never Never Frame 10": lambda state:
                can_smash_wall(world, state),
            "Never Never Frame 11": lambda state:
                can_swing(world, state),
            "Faire Dinkum Frame 8": lambda state:
                can_smash_wall(world, state),
            "Faire Dinkum Frame 9": lambda state:
                can_smash_wall(world, state),
            "Sulphur Rocks Frame 4": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Frame 5": lambda state:
                can_swing(world, state),
            "Sulphur Rocks Frame 6": lambda state:
                can_swing(world, state),
            "Mount Boom Frame": lambda state:
                can_swing(world, state),
            "Burramudgee Frame 47": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
            "Burramudgee Frame 48": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
            "Burramudgee Frame 49": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
        },
        "events": {
            "Complete Haunted Hassle": lambda state:
                state.can_reach_location("Haunted Hassle", world.player),
            "Complete Lava Chill Out": lambda state:
                state.can_reach_location("Lava Chill Out", world.player),
            "Complete Hidden Danger": lambda state:
                state.can_reach_location("Hidden Danger", world.player),
            "Complete Deep Sea Scare": lambda state:
                state.can_reach_location("Deep Sea Scare", world.player),
            "Complete Sea Lab": lambda state:
                state.can_reach_location("Sea Lab", world.player),
            "Complete Snake Eyes": lambda state:
                state.can_reach_location("Snake Eyes", world.player),
            "Complete Oil Rig Fire": lambda state:
                state.can_reach_location("Oil Rig Fire", world.player),
            "Complete Truck Tragedy": lambda state:
                state.can_reach_location("Truck Tragedy", world.player),
            "Complete Truck Stop": lambda state:
                state.can_reach_location("Truck Stop", world.player),
            "Complete Bush Fire": lambda state:
                state.can_reach_location("Bush Fire", world.player),
            "Complete Grub Grab": lambda state:
                state.can_reach_location("Grub Grab", world.player),
            "Complete Ripper Nipper": lambda state:
                state.can_reach_location("Ripper Nipper", world.player),
        },
        "entrances": {
            "Burramudgee HQ -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Burramudgee HQ -> Crates":
                lambda state: can_smash_crate(world, state),
            "Burramudgee Town -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Outback Oasis -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Mount Boom -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Frill Neck Forest -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Wetlands -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Faire Dinkum -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Never Never -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Sulphur Rocks -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Wetlands Teleport":lambda state:
                can_tp(world, state),
            "Mount Boom Start Parking Bay":
                lambda state: state.has("Parking Bay - Mount Boom Start", world.player),
            "Mount Boom Start Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "Mount Boom End Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "Mount Boom End Parking Bay":
                lambda state: state.has("Parking Bay - Mount Boom End", world.player) and state.has("Parking Bay - Mount Boom Start", world.player) and state.has("Thermo Bunyip Key", world.player),
            "Burramudgee Parking Bay":
                lambda state: state.has("Parking Bay - Burramudgee Town", world.player),
            "Min Min Plains Parking Bay":
                lambda state: state.has("Parking Bay - Min Min Plains", world.player),
            "Freeway Training Grounds Parking Bay":
                lambda state: state.has("Parking Bay - Freeway Training Grounds", world.player),
            "Beach Training Grounds Parking Bay":
                lambda state: state.has("Parking Bay - Beach Training Grounds", world.player),
            "Dennis Freeway Parking Bay":
                lambda state: state.has("Parking Bay - Dennis Freeway", world.player),
            "Wobbygon Bay Parking Bay":
                lambda state: state.has("Parking Bay - Wobbygon Bay", world.player),
            "Lava Falls Race Parking Bay":
                lambda state: state.has("Parking Bay - Lava Falls Race", world.player),
            "Frill Neck Forest Parking Bay":
                lambda state: state.has("Parking Bay - Frill Neck Forest", world.player),
            "Old Stony Creek Parking Bay":
                lambda state: state.has("Parking Bay - Old Stony Creek", world.player),
            "Camping Parking Bay":
                lambda state: state.has("Parking Bay - Camping", world.player),
            "Outback Oasis Parking Bay":
                lambda state: state.has("Parking Bay - Outback Oasis", world.player),
            "Refinery Run Parking Bay":
                lambda state: state.has("Parking Bay - Refinery Run", world.player),
            "Fire Fight Parking Bay":
                lambda state: state.has("Parking Bay - Fire Fight", world.player),
            "Sly Parking Bay":
                lambda state: state.has("Parking Bay - Sly", world.player),
            "Outback Dash Parking Bay":
                lambda state: state.has("Parking Bay - Outback Dash", world.player),
            "Never Never Road Parking Bay":
                lambda state: state.has("Parking Bay - Never Never Road", world.player),
            "Truck Tragedy Parking Bay":
                lambda state: state.has("Parking Bay - Truck Tragedy", world.player),
            "Truck Stop Parking Bay South":
                lambda state: state.has("Parking Bay - Truck Stop", world.player),
            "Truck Stop Parking Bay North":
                lambda state: state.has("Parking Bay - Truck Stop", world.player),
            "Plutonium Panic Parking Bay":
                lambda state: state.has("Parking Bay - Plutonium Panic", world.player),
            "50 Foot Squeaver Parking Bay":
                lambda state: state.has("Parking Bay - 50 Foot Squeaver", world.player),
            "Never Never Parking Bay":
                lambda state: state.has("Parking Bay - Never Never", world.player),
            "Min Min Mining Parking Bay":
                lambda state: state.has("Parking Bay - Min Min Mining", world.player),
            "Turbo Track Parking Bay":
                lambda state: state.has("Parking Bay - Turbo Track", world.player),
            "King Squeaver Parking Bay":
                lambda state: state.has("Parking Bay - King Squeaver", world.player),
            "Bush Fire Parking Bay":
                lambda state: state.has("Parking Bay - Bush Fire", world.player),
            "Sulphur Rocks Parking Bay":
                lambda state: state.has("Parking Bay - Sulphur Rocks", world.player),
            "Lake Burramudgee Parking Bay":
                lambda state: state.has("Parking Bay - Lake Burramudgee", world.player),
            "Muddy Bottom Parking Bay":
                lambda state: state.has("Parking Bay - Muddy Bottom", world.player),
            "Dusty Burrows Parking Bay":
                lambda state: state.has("Parking Bay - Dusty Burrows", world.player),
            "Ripper Nipper Parking Bay":
                lambda state: state.has("Parking Bay - Ripper Nipper", world.player),

            "Faire Dinkum Parking Bay":
                lambda state: state.has("Parking Bay - Faire Dinkum", world.player),
            "Wetlands Parking Bay":
                lambda state: state.has("Parking Bay - Wetlands", world.player),
            "Hearty Beach Parking Bay":
                lambda state: state.has("Parking Bay - Hearty Beach", world.player),
            "Patchy Barriers West":
                lambda state: state.has("Patchy Barriers", world.player),
            "Patchy Barriers West Backwards":
                lambda state: state.has("Patchy Barriers", world.player),
            "Patchy Barriers South":
                lambda state: state.has("Patchy Barriers", world.player),
            "Patchy Barriers South Backwards":
                lambda state: state.has("Patchy Barriers", world.player),
            "Fluffy Barriers South":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Fluffy Barriers South Backwards":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Fluffy Barriers North":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Fluffy Barriers North Backwards":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Buster Barriers West":
                lambda state: state.has("Buster Barriers", world.player),
            "Buster Barriers West Backwards":
                lambda state: state.has("Buster Barriers", world.player),
            "Buster Barriers East":
                lambda state: state.has("Buster Barriers", world.player),
            "Buster Barriers East Backwards":
                lambda state: state.has("Buster Barriers", world.player),
            "Truck Stop Clear":
                lambda state: state.has("Parking Bay - Truck Stop", world.player),
            "Truck Stop Clear Backwards":
                lambda state: state.has("Parking Bay - Truck Stop", world.player),
            "Patchy Parking Bay":
                lambda state: state.has("Parking Bay - Patchy", world.player),
            "Oil Rig Parking Bay":
                lambda state: state.has("Parking Bay - Oil Rig", world.player),
            "Oil Rig Button":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "Fluffy Parking Bay":
                lambda state: state.has("Parking Bay - Fluffy", world.player),
            "Bush Rescue Plane":
                lambda state: (state.has("Mission Complete", world.player, world.options.missions_for_goal.value)
                               and state.has("Patchy Defeated", world.player)
                               and state.has("Buster Defeated", world.player)
                               and state.has("Fluffy Defeated", world.player)
                               ) if world.options.require_bosses.value else state.has("Mission Complete", world.player, world.options.missions_for_goal.value),
        }
    }
    return rules


def set_rules(world):

    rules_lookup = get_rules(world)

    world.explicit_indirect_conditions = False

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

    for event_name, rule in rules_lookup["events"].items():
        try:
            world.get_location(event_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    if world.options.frill_sanity:
        world.get_location("Complete Killer Koala").access_rule \
            = lambda state: state.can_reach_location("Killer Koala", world.player)

    world.multiworld.get_location(f"Boss Cass Bust-Up", world.player).place_locked_item(
        Ty2Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)