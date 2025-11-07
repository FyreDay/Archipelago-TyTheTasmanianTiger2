from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_2.Items import Ty2Item
from worlds.ty_the_tasmanian_tiger_2.Locations import Ty2Location, mission_dict


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
            "Oil Rig Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Truck Tragedy": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Truck Stop": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Bush Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Killer Koala": lambda state:
                has_infra(world, state),
            "Grub Grab": lambda state:
                state.has("Burramudgee Town ParkingBay", world.player) and (state.has("Patchy Barriers", world.player) or state.has("Buster Barriers", world.player)),
            "Ripper Nipper": lambda state:
                state.has("Wobbygon Bay ParkingBay", world.player) and state.has("Ripper Nipper ParkingBay", world.player),
            "Complete Haunted Hassle": lambda state:
                has_infra(world, state),
            "Complete Lava Chill Out": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Complete Hidden Danger": lambda state:
                has_infra(world, state),
            "Complete Deep Sea Scare": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Complete Sea Lab": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Complete Oil Rig Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Complete Truck Tragedy": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Complete Truck Stop": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Complete Bush Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Complete Killer Koala": lambda state:
                has_infra(world, state),
            "Complete Grub Grab": lambda state:
                state.has("Burramudgee Town ParkingBay", world.player) and (state.has("Patchy Barriers", world.player) or state.has("Buster Barriers", world.player)),
            "Complete Ripper Nipper": lambda state:
                state.has("Wobbygon Bay ParkingBay", world.player) and state.has("Ripper Nipper ParkingBay", world.player),
            #Cogs
            "Platinum Cog 1": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 3": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 5": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 11": lambda state:
            (can_swing(world, state)  or can_cold(world, state)) and state.has("Thermo Bunyip Key", world.player),
            "Platinum Cog 16": lambda state:
                has_infra(world, state),
            "Platinum Cog 17": lambda state:
                can_swing(world, state),
            "Platinum Cog 19": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 20 - End of Level": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 23 - Snake Eyes Challenge": lambda state:
                can_freeze(world, state),
            "Platinum Cog 24 - Boulder Lift": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Platinum Cog 26": lambda state:
                can_swing(world, state),
            "Platinum Cog 31": lambda state:
                can_tp(world, state),
            "Platinum Cog 33 - Rope Timer Race": lambda state:
                can_smash_crate(world, state),
            "Platinum Cog 34 - On Haunted Mansion": lambda state:
                has_infra(world, state),
            "Platinum Cog 37": lambda state:
                can_tp(world, state),
            "Platinum Cog 39": lambda state:
                can_tp(world, state),
            "Platinum Cog 41": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 44": lambda state:
                can_burn(world, state),
            #Orbs
            "Kromium Orb 0 - High Above Burramudgee": lambda state:
                can_swing(world, state),
            "Kromium Orb 2 - Swinging Over the Pond": lambda state:
                can_swing(world, state),
            "Kromium Orb 3 - Sulphur Lava": lambda state:
                can_swing(world, state)  or can_freeze(world, state),
            "Kromium Orb 7": lambda state:
                can_tp(world, state) and can_smash_wall(world, state),
            "Kromium Orb 9": lambda state:
                can_smash_wall(world, state),
            "Kromium Orb 13": lambda state:
                has_infra(world, state),
            "Kromium Orb 14 - On Invisible Platforms": lambda state:
                has_infra(world, state) or (world.options.require_infra.value != 0),
            "Kromium Orb 15": lambda state:
                can_smash_wall(world, state),
            "Kromium Orb 16": lambda state:
                can_swing(world, state),
            "Kromium Orb 22": lambda state:
                can_swing(world, state),
            "Kromium Orb 25": lambda state:
                can_swing(world, state),
            "Kromium Orb 27 - Frosty Tutorial": lambda state:
                can_freeze(world, state),
            #Bilbies
            "Bilby 0": lambda state:
                can_smash_wall(world,state),
            "Bilby 4": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Bilby 15": lambda state:
                has_infra(world, state) or (world.options.require_infra.value != 0),
            "Bilby 16": lambda state:
                can_swing(world, state),
            "Bilby 18": lambda state:
                can_swing(world, state) and state.has("Thermo Bunyip Key", world.player),
            "Bilby 19": lambda state:
                can_swing(world, state),
            "Bilby 21": lambda state:
                can_burn(world, state),
            #Frills
            "Disguised Frill 0": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_smash_wall(world, state),
            "Disguised Frill 1": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 2": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 3": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 4": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 5": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 6": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 7": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 8 - Under Walkway": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 9 - Sulpher Start": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 10 - In Hole": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 11 - Behind Fence": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_swing(world, state),
            "Disguised Frill 12 - Near Police": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 13 - Near Canal": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 14": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 15": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 16": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 17": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 18": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 19": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 20": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 21": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 22": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 23": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 24": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),

            #Steves
            "Steve - Outback Oasis": lambda state:
                can_swing(world, state),
            "Steve - MountBoom": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            #Frames
            "Picture Frame 0": lambda state:
                can_tp(world, state),
            "Picture Frame 1": lambda state:
                can_tp(world, state),
            "Picture Frame 2": lambda state:
                can_tp(world, state),
            "Picture Frame 4": lambda state:
                can_swing(world, state),
            "Picture Frame 6": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Picture Frame 12": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 30 - Smash Wall": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 31 - Smash Wall": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 35 - Behind Fence": lambda state:
                can_swing(world, state),
            "Picture Frame 36 - Behind Fence": lambda state:
                can_swing(world, state),
            "Picture Frame 37 - Behind Fence": lambda state:
                can_swing(world, state),
            "Picture Frame 61": lambda state:
                can_swing(world, state),
            "Picture Frame 153 - HQ Warparang Tutorial": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
            "Picture Frame 154 - HQ Warparang Tutorial": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
            "Picture Frame 155 - HQ Warparang Tutorial": lambda state:
            can_smash_crate(world, state) and can_tp(world, state),
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
            "MountBoom -> Infra":
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
            "MountBoom Start ParkingBay":
                lambda state: state.has("MountBoom Start ParkingBay", world.player),
            "MountBoom Start Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "MountBoom End Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "MountBoom End ParkingBay":
                lambda state: state.has("MountBoom End ParkingBay", world.player) and state.has("MountBoom Start ParkingBay", world.player) and state.has("Thermo Bunyip Key", world.player),
            "Burramudgee ParkingBay":
                lambda state: state.has("Burramudgee Town ParkingBay", world.player),
            "Min Min Plains ParkingBay":
                lambda state: state.has("Min Min Plains ParkingBay", world.player),
            "Freeway Training Grounds ParkingBay":
                lambda state: state.has("Freeway Training Grounds ParkingBay", world.player),
            "Beach Training Grounds ParkingBay":
                lambda state: state.has("Beach Training Grounds ParkingBay", world.player),
            "Dennis Freeway ParkingBay":
                lambda state: state.has("Dennis Freeway ParkingBay", world.player),
            "Wobbygon Bay ParkingBay":
                lambda state: state.has("Wobbygon Bay ParkingBay", world.player),
            "Lava Falls Race ParkingBay":
                lambda state: state.has("Lava Falls Race ParkingBay", world.player),
            "Frill Neck Forest ParkingBay":
                lambda state: state.has("Frill Neck Forest ParkingBay", world.player),
            "Old Stony Creek ParkingBay":
                lambda state: state.has("Old Stony Creek ParkingBay", world.player),
            "Camping ParkingBay":
                lambda state: state.has("Camping ParkingBay", world.player),
            "Outback Oasis ParkingBay":
                lambda state: state.has("Outback Oasis ParkingBay", world.player),
            "Refinery Run ParkingBay":
                lambda state: state.has("Refinery Run ParkingBay", world.player),
            "Fire Fight ParkingBay":
                lambda state: state.has("Fire Fight ParkingBay", world.player),
            "Sly ParkingBay":
                lambda state: state.has("Sly ParkingBay", world.player),
            "Outback Dash ParkingBay":
                lambda state: state.has("Outback Dash ParkingBay", world.player),
            "Never Never Road ParkingBay":
                lambda state: state.has("Never Never Road ParkingBay", world.player),
            "Truck Tragedy ParkingBay":
                lambda state: state.has("Truck Tragedy ParkingBay", world.player),
            "Truck Stop ParkingBay South":
                lambda state: state.has("Truck Stop ParkingBay", world.player),
            "Truck Stop ParkingBay North":
                lambda state: state.has("Truck Stop ParkingBay", world.player),
            "Plutonium Panic ParkingBay":
                lambda state: state.has("Plutonium Panic ParkingBay", world.player),
            "50 Foot Squeaver ParkingBay":
                lambda state: state.has("50 Foot Squeaver ParkingBay", world.player),
            "Never Never ParkingBay":
                lambda state: state.has("Never Never ParkingBay", world.player),
            "Min Min Mining ParkingBay":
                lambda state: state.has("Min Min Mining ParkingBay", world.player),
            "Turbo Track ParkingBay":
                lambda state: state.has("Turbo Track ParkingBay", world.player),
            "King Squeaver ParkingBay":
                lambda state: state.has("King Squeaver ParkingBay", world.player),
            "Bush Fire ParkingBay":
                lambda state: state.has("Bush Fire ParkingBay", world.player),
            "Sulphur Rocks ParkingBay":
                lambda state: state.has("Sulphur Rocks ParkingBay", world.player),
            "Lake Burramudgee ParkingBay":
                lambda state: state.has("Lake Burramudgee ParkingBay", world.player),
            "Muddy Bottom ParkingBay":
                lambda state: state.has("Muddy Bottom ParkingBay", world.player),
            "Dusty Barrows ParkingBay":
                lambda state: state.has("Dusty Barrows ParkingBay", world.player),
            "Ripper Nipper ParkingBay":
                lambda state: state.has("Ripper Nipper ParkingBay", world.player),

            "Faire Dinkum ParkingBay":
                lambda state: state.has("Faire Dinkum ParkingBay", world.player),
            "Wetlands ParkingBay":
                lambda state: state.has("Wetlands ParkingBay", world.player),
            "Hearty Beach ParkingBay":
                lambda state: state.has("Hearty Beach ParkingBay", world.player),
            "Patchy Barriers West":
                lambda state: state.has("Patchy Barriers", world.player),
            "Patchy Barriers South":
                lambda state: state.has("Patchy Barriers", world.player),
            "Fluffy Barriers South":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Fluffy Barriers North":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Buster Barriers West":
                lambda state: state.has("Buster Barriers", world.player),
            "Buster Barriers East":
                lambda state: state.has("Buster Barriers", world.player),
            "Truck Stop Clear":
                lambda state: state.has("Truck Stop ParkingBay", world.player),
            "Patchy ParkingBay":
                lambda state: state.has("Patchy ParkingBay", world.player),
            "Oil Rig ParkingBay":
                lambda state: state.has("Oil Rig ParkingBay", world.player),
            "Oil Rig Button":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "Fluffy ParkingBay":
                lambda state: state.has("Fluffy ParkingBay", world.player),
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

    world.multiworld.get_location(f"Boss Cass Bust-Up", world.player).place_locked_item(
        Ty2Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)