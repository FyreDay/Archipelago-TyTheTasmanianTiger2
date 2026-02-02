from enum import Enum
from typing import NamedTuple, Optional, Dict

from BaseClasses import Location, ItemClassification

class Ty2Location(Location):
    game: str = "Ty the Tasmanian Tiger 2"


class Ty2Level(Enum):
    Burramudgee = 0
    OutbackOasis = 1
    NeverNever = 2
    SulphurRocks = 3
    SouthernRivers = 4
    Wetlands = 5
    FrillNeckForest = 6
    MountBoom = 7
    FaireDinkum = 8


class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1
    hint_info: Optional[str] = None
    level: Ty2Level = None


def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)
    region.locations.append(location)


def create_locations(world, region, loc_dict):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, key, data.code)


def create_ty2_locations(world):
    all_locations = {**shop_location_dict, **platinum_cog_dict, **kromium_orb_dict, **bilby_dict, **mission_dict}
    all_locations.update(get_mission_complete_events(world))

    if world.options.race_checks.value:
        all_locations.update(race_dict)

    if world.options.frill_sanity.value:
        all_locations.update(disguised_frill_dict)
    if world.options.steve_sanity.value:
        all_locations.update(steve_dict)
    if world.options.frame_sanity.value:
        all_locations.update(picture_frame_dict)

    return all_locations


shop_location_dict: Dict[str, LocData] = {
    "Rang Shop Item 8": LocData(26, "Burramudgee Town"), #Camerang
    "Rang Shop Item 1": LocData(8, "Burramudgee Town"),  #frosty
    "Rang Shop Item 2": LocData(9, "Burramudgee Town"),  #flame
    "Rang Shop Item 3": LocData(18, "Burramudgee Town"), #zappy
    "Rang Shop Item 4": LocData(12, "Burramudgee Town"), #infra
    "Rang Shop Item 5": LocData(11, "Burramudgee Town"), #lash
    "Rang Shop Item 6": LocData(13, "Burramudgee Town"),
    "Rang Shop Item 7": LocData(14, "Burramudgee Town"),

    "Sly's Shack Item 1": LocData(17, "SR - Sly Shack"), #freeze
    "Sly's Shack Item 2": LocData(16, "SR - Sly Shack"), #lava
    "Sly's Shack Item 3": LocData(15, "SR - Sly Shack"), #multi
    "Sly's Shack Item 4": LocData(19, "SR - Sly Shack"), #warp
    "Sly's Shack Item 5": LocData(10, "SR - Sly Shack"), #thunder
    "Sly's Shack Item 6": LocData(20, "SR - Sly Shack"), #X
    "Sly's Shack Item 7": LocData(21, "SR - Sly Shack"), #kaboom
    "Sly's Shack Item 8": LocData(22, "SR - Sly Shack"), #omega
    "Sly's Shack Item 9": LocData(23, "SR - Sly Shack"), #deadly
    "Sly's Shack Item 10": LocData(24, "SR - Sly Shack"), #doom
    "Sly's Shack Item 11": LocData(25, "SR - Sly Shack"), #crafty
    "Trader Bob's Opal Item 1": LocData(1, "Burramudgee Town"), #lifter
    "Trader Bob's Opal Item 2": LocData(2, "Burramudgee Town"), #thermo
    "Trader Bob's Opal Item 3": LocData(59, "Burramudgee Town"), #sub
    "Trader Bob's Opal Item 4": LocData(77, "Burramudgee Town"), #gold paw
    "Trader Bob's Opal Item 5": LocData(78, "Burramudgee Town"), #plat paw
    "Trader Bob's Cog Item 1": LocData(79, "Burramudgee Town"),
    "Trader Bob's Cog Item 2": LocData(80, "Burramudgee Town"),
    "Trader Bob's Cog Item 3": LocData(81, "Burramudgee Town"),
    "Trader Bob's Cog Item 4": LocData(82, "Burramudgee Town"),
    "Trader Bob's Cog Item 5": LocData(83, "Burramudgee Town"),
    "Trader Bob's Cog Item 6": LocData(84, "Burramudgee Town"),
    "Trader Bob's Cog Item 7": LocData(85, "Burramudgee Town"),
    "Trader Bob's Cog Item 8": LocData(86, "Burramudgee Town"),
    "Trader Bob's Cog Item 9": LocData(87, "Burramudgee Town"),
    "Trader Bob's Cog Item 10": LocData(88, "Burramudgee Town"),
    "Madam Mopoke's Orb Item 1": LocData(5, "Burramudgee Town"),
    "Madam Mopoke's Orb Item 2": LocData(6, "Burramudgee Town"),
    "Madam Mopoke's Orb Item 3": LocData(7, "Burramudgee Town"),
}


platinum_cog_dict: Dict[str, LocData] = {
    "Outback Oasis Cog 1":  LocData(0x4301, "Outback Oasis", hint_info="Dunny Rock Wall", level=Ty2Level.OutbackOasis), #smasharang
    "Outback Oasis Cog 2":  LocData(0x4302, "Outback Oasis", hint_info="Over Wall", level=Ty2Level.OutbackOasis),
    "Outback Oasis Cog 3":  LocData(0x4303, "Outback Oasis", hint_info="Near Trampoline", level=Ty2Level.OutbackOasis), #smasharang
    "Outback Oasis Cog 4":  LocData(0x4304, "Outback Oasis", hint_info="Platform Parkour", level=Ty2Level.OutbackOasis),
    "Never Never Cog 1":  LocData(0x4300, "Never Never", hint_info="Descending Platform", level=Ty2Level.NeverNever),
    "Never Never Cog 2":  LocData(0x4305, "Never Never", hint_info="Vanishing Platforms", level=Ty2Level.NeverNever), #smasharang
    "Never Never Cog 3":  LocData(0x4306, "Never Never", hint_info="On Platform", level=Ty2Level.NeverNever),
    "Never Never Cog 4":  LocData(0x4307, "Never Never", hint_info="On Tree", level=Ty2Level.NeverNever),
    "Never Never Cog 5":  LocData(0x4308, "Never Never", hint_info="Hidden Button", level=Ty2Level.NeverNever),
    "Never Never Cog 6":  LocData(0x4309, "Never Never", hint_info="In Trees", level=Ty2Level.NeverNever),
    "Never Never Cog 7":  LocData(0x430A, "Never Never", hint_info="Tree Ladder", level=Ty2Level.NeverNever),
    "Never Never Cog 8":  LocData(0x430B, "Never Never", hint_info="Lava Chill Out", level=Ty2Level.NeverNever),#thermo, lash, OR frosty
    "Never Never Cog 9":  LocData(0x430C, "Never Never", hint_info="Hidden Flower", level=Ty2Level.NeverNever),
    "Never Never Cog 10":  LocData(0x430D, "Never Never", hint_info="Rocky Road", level=Ty2Level.NeverNever),
    "Never Never Cog 11":  LocData(0x430E, "Never Never", hint_info="Rope Slide", level=Ty2Level.NeverNever),
    "Never Never Cog 12":  LocData(0x430F, "Never Never", hint_info="Rope Race", level=Ty2Level.NeverNever),
    "Never Never Cog 13":  LocData(0x4310, "Never Never - Infra", hint_info="Hut Button Required", level=Ty2Level.NeverNever), #infra
    "Never Never Cog 14":  LocData(0x4311, "Never Never", hint_info="Hut", level=Ty2Level.NeverNever), #lasharang
    "Never Never Cog 15":  LocData(0x4312, "Never Never", hint_info="Moving Platform", level=Ty2Level.NeverNever),
    "Never Never Cog 16":  LocData(0x4313, "Never Never", hint_info="End Wall", level=Ty2Level.NeverNever), #smasharang
    "Faire Dinkum Cog 1":  LocData(0x4314, "Faire Dinkum", hint_info="End of Level", level=Ty2Level.FaireDinkum), #smasharang
    "Faire Dinkum Cog 2":  LocData(0x4315, "Faire Dinkum", hint_info="Smash Wall", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Cog 3":  LocData(0x4316, "Faire Dinkum", hint_info="Long Ride In The Trees", level=Ty2Level.FaireDinkum),
    "Sulphur Rocks Cog 1":  LocData(0x4317, "Sulphur Rocks", hint_info="Snake Eyes Challenge", level=Ty2Level.SulphurRocks), #frosty
    "Sulphur Rocks Cog 2":  LocData(0x4318, "Sulphur Rocks", hint_info="Boulder Lift", level=Ty2Level.SulphurRocks), #lifter bunyip key
    "Sulphur Rocks Cog 3":  LocData(0x4319, "Sulphur Rocks", hint_info="Swinging Around", level=Ty2Level.SulphurRocks), #lasharang
    "Sulphur Rocks Cog 4": LocData(0x431A, "Sulphur Rocks", level=Ty2Level.SulphurRocks), #lasharang
    "Sulphur Rocks Cog 5": LocData(0x431B, "Sulphur Rocks", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Cog 6": LocData(0x431C, "Sulphur Rocks", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Cog 7":  LocData(0x431D, "Sulphur Rocks", hint_info="Beyond Saw", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Cog 8":  LocData(0x431E, "Sulphur Rocks", hint_info="Sulphur Start", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Cog 9":  LocData(0x431F, "Sulphur Rocks", level=Ty2Level.SulphurRocks), #warparang
    "Burramudgee Cog 1":  LocData(0x4320, "Burramudgee Town", hint_info="Across the Camera Eggs", level=Ty2Level.Burramudgee),
    "Burramudgee Cog 2":  LocData(0x4321, "Burramudgee Town", hint_info="Rope Timer Race", level=Ty2Level.Burramudgee),
    "Burramudgee Cog 3":  LocData(0x4322, "Burramudgee Town", hint_info="On Haunted Mansion", level=Ty2Level.Burramudgee),
    "Burramudgee Cog 4":  LocData(0x4331, "Burramudgee HQ - Infra", hint_info="Floating Above HQ", level=Ty2Level.Burramudgee),
    "Cass' Run Cog": LocData(0x4323, "Cass' Run"),
    "Frill Neck Cog":  LocData(0x4324, "Frill Neck Forest", hint_info="Start Trunk Glide", level=Ty2Level.FrillNeckForest),
    "Mount Boom Cog 2": LocData(0x4325, "Mount Boom", level=Ty2Level.MountBoom),#warparang thermo
    "Mount Boom Cog 3": LocData(0x4326, "Mount Boom", level=Ty2Level.MountBoom),#warperang thermo
    "Mount Boom Cog 4": LocData(0x4327, "Mount Boom", level=Ty2Level.MountBoom),#warparang thermo
    "Wetlands Cog 1":  LocData(0x4328, "Wetlands", hint_info="Button Platform", level=Ty2Level.Wetlands),
    "Wetlands Cog 2":  LocData(0x4329, "Wetlands", hint_info="Rock Wall", level=Ty2Level.Wetlands), #smasharang
    "Wetlands Cog 3":  LocData(0x432A, "Wetlands", hint_info="Timer", level=Ty2Level.Wetlands),
    "Wetlands Cog 4":  LocData(0x432B, "Wetlands", hint_info="Camera Eggs", level=Ty2Level.Wetlands),
    "Wetlands Cog 5":  LocData(0x432C, "Wetlands", hint_info="Bunyip", level=Ty2Level.Wetlands), #flamerang optional
    "Wetlands Cog 6":  LocData(0x432D, "Wetlands", hint_info="Crocs", level=Ty2Level.Wetlands),
    "Wobbygon Cog 1":  LocData(0x432E, "SR - Wobbygon Bay", hint_info="Central Ocean", level=Ty2Level.SouthernRivers),
    "Wobbygon Cog 2":  LocData(0x432F, "SR - Wobbygon Bay", hint_info="In Seaweed", level=Ty2Level.SouthernRivers),
    "Wobbygon Cog 3":  LocData(0x4330, "SR - Wobbygon Bay", hint_info="Cassopolis", level=Ty2Level.SouthernRivers),
}


kromium_orb_dict: Dict[str, LocData] = {
    "Burramudgee Orb 1":  LocData(0x4B00, "Burramudgee Town", hint_info="High Above Burramudgee", level=Ty2Level.Burramudgee),#lasharang
    "Burramudgee Orb 2":  LocData(0x4B01, "Burramudgee Town", hint_info="Above the Canal", level=Ty2Level.Burramudgee),
    "Burramudgee Orb 3": LocData(0x4B18, "Burramudgee Town", hint_info="Town Overlook", level=Ty2Level.Burramudgee),
    "Burramudgee Orb 4": LocData(0x4B1B, "Burramudgee HQ",   hint_info="Frosty Tutorial", level=Ty2Level.Burramudgee),  # smasharang
    "Sulphur Rocks Orb 1":  LocData(0x4B02, "Sulphur Rocks", hint_info="Swinging Over the Pond", level=Ty2Level.SulphurRocks), #lasharang
    "Sulphur Rocks Orb 2":  LocData(0x4B03, "Sulphur Rocks", hint_info="Sulphur Lava", level=Ty2Level.SulphurRocks), #lasharang #frostyrang
    "Sulphur Rocks Orb 3":  LocData(0x4B04, "Sulphur Rocks", hint_info="Exploding Pillars", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Orb 4":  LocData(0x4B05, "SR - Sulphur Rocks", hint_info="Jumping Maze", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Orb 5": LocData(0x4B0C, "Sulphur Rocks", hint_info="Sulphur Overlook", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Orb 6": LocData(0x4B0D, "Sulphur Rocks - Infra", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Orb 7": LocData(0x4B0E, "Sulphur Rocks - Infra", hint_info="On Invisible Platforms", level=Ty2Level.SulphurRocks),  # infra
    "Mount Boom Orb 1": LocData(0x4B06, "Mount Boom", level=Ty2Level.MountBoom), #thermo
    "Mount Boom Orb 2": LocData(0x4B07, "Mount Boom", level=Ty2Level.MountBoom),#warperang #thermo smash
    "Wobbygon Orb 1":  LocData(0x4B08, "SR - Wobbygon Bay", hint_info="Water Near Warps", level=Ty2Level.SouthernRivers),
    "Wobbygon Orb 2": LocData(0x4B1D, "SR - Wobbygon Bay", hint_info="Corner Seaweed", level=Ty2Level.SouthernRivers),
    "Outback Oasis Orb 1":   LocData(0x4B09, "Outback Oasis", hint_info="Super Frill Beat Up", level=Ty2Level.OutbackOasis), #smasharang
    "Outback Oasis Orb 2": LocData(0x4B0B, "Outback Oasis - Infra", hint_info="Spinning Platforms", level=Ty2Level.OutbackOasis),
    "Sly's Shack Orb":  LocData(0x4B0A, "SR - Sly Shack", hint_info="Sly Shack", level=Ty2Level.SouthernRivers),
    "Never Never Orb 1":  LocData(0x4B0F, "Never Never", hint_info="Behind Wall", level=Ty2Level.NeverNever), #smasharang
    "Never Never Orb 2":  LocData(0x4B10, "Never Never", hint_info="In Trees", level=Ty2Level.NeverNever), #lasharang OPTIONAL
    "Never Never Orb 3":  LocData(0x4B11, "Never Never", hint_info="Swinging Fence", level=Ty2Level.NeverNever),
    "Never Never Orb 4":  LocData(0x4B12, "Never Never", hint_info="By Fence", level=Ty2Level.NeverNever),
    "Never Never Orb 5":  LocData(0x4B13, "Never Never", hint_info="Rope Slide", level=Ty2Level.NeverNever),
    "Never Never Orb 6":  LocData(0x4B14, "Never Never", hint_info="Swinging Under", level=Ty2Level.NeverNever),
    "Never Never Orb 7":  LocData(0x4B15, "Never Never", hint_info="Water Wheel", level=Ty2Level.NeverNever),
    "Wetlands Orb":  LocData(0x4B16, "Wetlands", hint_info="Crocs", level=Ty2Level.Wetlands), #lasharang
    "Frill Neck Orb":  LocData(0x4B17, "Frill Neck Forest", hint_info="Side Platform", level=Ty2Level.FrillNeckForest),
    "Dennis Freeway Orb": LocData(0x4B19, "SR - Dennis Freeway", level=Ty2Level.SouthernRivers), #warparang
    "Faire Dinkum Orb 1":  LocData(0x4B1A, "Faire Dinkum", hint_info="Moving Platform", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Orb 2":  LocData(0x4B1C, "Faire Dinkum", hint_info="Behind Dunny", level=Ty2Level.FaireDinkum),
}


bilby_dict: Dict[str, LocData] = {
    "Outback Oasis Bilby 1":  LocData(0x4200, "Outback Oasis", hint_info="Trampoline", level=Ty2Level.OutbackOasis), #smasharang
    "Outback Oasis Bilby 2":  LocData(0x4201, "Outback Oasis", hint_info="Hanging On Entrance", level=Ty2Level.OutbackOasis),
    "Outback Oasis Bilby 3":  LocData(0x4202, "Outback Oasis", hint_info="Cave", level=Ty2Level.OutbackOasis),
    "Never Never Bilby 1": LocData(0x4203, "Never Never", level=Ty2Level.NeverNever),
    "Never Never Bilby 2":  LocData(0x4204, "Never Never", hint_info="Lava Chill Out", level=Ty2Level.NeverNever),#thermo, lash, OR frosty
    "Never Never Bilby 3":  LocData(0x4205, "Never Never", hint_info="Rope Slide", level=Ty2Level.NeverNever),
    "Never Never Bilby 4":  LocData(0x4206, "Never Never", hint_info="Moving Platform", level=Ty2Level.NeverNever),
    "Faire Dinkum Bilby 1":  LocData(0x4207, "Faire Dinkum", hint_info="Secret Button", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Bilby 2":  LocData(0x4208, "Faire Dinkum", hint_info="Town Overlook", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Bilby 3":  LocData(0x4209, "Faire Dinkum", hint_info="Half Under Webs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Bilby 4": LocData(0x420F, "Faire Dinkum - Infra", level=Ty2Level.FaireDinkum),  # (infra)
    "Sulphur Rocks Bilby 1":  LocData(0x420A, "Sulphur Rocks", hint_info="Sulphur Overlook", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Bilby 2": LocData(0x420B, "Sulphur Rocks", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Bilby 3":  LocData(0x420C, "Sulphur Rocks", hint_info="Floating Over Sulphur", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Bilby 4": LocData(0x420D, "Sulphur Rocks", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Bilby 5":  LocData(0x420E, "Sulphur Rocks", hint_info="Over pond", level=Ty2Level.SulphurRocks),
    "Frill Neck Bilby 1":  LocData(0x4210, "Frill Neck Forest", hint_info="End Trunk", level=Ty2Level.FrillNeckForest), #lasharang - possible without
    "Frill Neck Bilby 2": LocData(0x4211, "Frill Neck Forest", level=Ty2Level.FrillNeckForest),
    "Mount Boom Bilby 1":  LocData(0x4212, "Mount Boom", hint_info="Beginning", level=Ty2Level.MountBoom), #lasharang and thermo - Mount Boom Beginning
    "Mount Boom Bilby 2":  LocData(0x4213, "Mount Boom", hint_info="Warp", level=Ty2Level.MountBoom), #warparang #thermo
    "Wetlands Bilby 1":  LocData(0x4214, "Wetlands", hint_info="In Log", level=Ty2Level.Wetlands),
    "Wetlands Bilby 2":  LocData(0x4215, "Wetlands", hint_info="Webbed", level=Ty2Level.Wetlands), #flamerang
    "Wetlands Bilby 3":  LocData(0x4216, "Wetlands", hint_info="Bunyip", level=Ty2Level.Wetlands), #flamerang
    "Burramudgee Bilby 1":  LocData(0x4217, "Burramudgee HQ", hint_info="Under Ramp", level=Ty2Level.Burramudgee),
    "Burramudgee Bilby 2":  LocData(0x4218, "Burramudgee HQ", hint_info="Cliffside", level=Ty2Level.Burramudgee),
    "Burramudgee Bilby 3":  LocData(0x4219, "Burramudgee HQ", hint_info="Top of HQ", level=Ty2Level.Burramudgee), #25
    "Burramudgee Bilby 4":  LocData(0x421A, "Burramudgee HQ", hint_info="Watch Tower", level=Ty2Level.Burramudgee),
    "Wobbygon Bilby 1":  LocData(0x421B, "SR - Wobbygon Bay", hint_info="Warp Tree", level=Ty2Level.SouthernRivers),
    "Wobbygon Bilby 2":  LocData(0x421C, "SR - Wobbygon Bay", hint_info="Race Island", level=Ty2Level.SouthernRivers),
    "Wobbygon Bilby 3":  LocData(0x421D, "SR - Wobbygon Bay", hint_info="Underwater South Boathouse", level=Ty2Level.SouthernRivers),
}


disguised_frill_dict: Dict[str, LocData] = {
    "Outback Oasis Frill 1":  LocData(0x4600, "Outback Oasis", hint_info="By Bunyip", level=Ty2Level.OutbackOasis), #smasharang
    "Outback Oasis Frill 2":  LocData(0x4601, "Outback Oasis", hint_info="Start", level=Ty2Level.OutbackOasis),
    "Outback Oasis Frill 3":  LocData(0x4602, "Outback Oasis", hint_info="Cave Overlook", level=Ty2Level.OutbackOasis),
    "Outback Oasis Frill 4": LocData(0x460F, "SR - Outback Oasis", hint_info="Picnic", level=Ty2Level.OutbackOasis),
    "Never Never Frill 1":  LocData(0x4603, "Never Never", hint_info="By Wall", level=Ty2Level.NeverNever),
    "Never Never Frill 2":  LocData(0x4604, "Never Never", hint_info="Rocky Road", level=Ty2Level.NeverNever),
    "Never Never Frill 3":  LocData(0x4605, "Never Never", hint_info="Vine Climb", level=Ty2Level.NeverNever),
    "Never Never Frill 4": LocData(0x4614, "SR - Never Never", hint_info="Never Never Entrance", level=Ty2Level.NeverNever),
    "Wetlands Frill 1":  LocData(0x4606, "Wetlands", hint_info="By Button", level=Ty2Level.Wetlands),
    "Wetlands Frill 2":  LocData(0x4607, "Wetlands", hint_info="Crocs", level=Ty2Level.Wetlands),
    "Faire Dinkum Frill":  LocData(0x4608, "Faire Dinkum", hint_info="Under Walkway", level=Ty2Level.FaireDinkum),
    "Sulphur Rocks Frill 1":  LocData(0x4609, "Sulphur Rocks", hint_info="Start", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frill 2":  LocData(0x460A, "Sulphur Rocks", hint_info="In Hole", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frill 3":  LocData(0x460B, "Sulphur Rocks", hint_info="Behind Fence", level=Ty2Level.SulphurRocks), #lasharang, not needed
    "Burramudgee Frill 1":  LocData(0x460C, "Burramudgee Town", hint_info="Near Police", level=Ty2Level.Burramudgee),
    "Burramudgee Frill 2":  LocData(0x460D, "Burramudgee Town", hint_info="Near Canal", level=Ty2Level.Burramudgee),
    "Dennis Freeway Frill": LocData(0x460E, "SR - Dennis Freeway", level=Ty2Level.SouthernRivers),
    "Dusty Burrows Frill": LocData(0x4610, "SR - Dusty Burrows", level=Ty2Level.SouthernRivers),
    "Lake Burramudgee Frill": LocData(0x4611, "SR - Lake Burramudgee", level=Ty2Level.SouthernRivers),
    "Frill Neck Frill 1": LocData(0x4612, "SR - Frill Neck Forest", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frill 2": LocData(0x4616, "Frill Neck Forest", level=Ty2Level.FrillNeckForest),
    "Truck Tragedy Frill": LocData(0x4613, "SR - Truck Tragedy", level=Ty2Level.SouthernRivers),
    "Sheep Dip Frill": LocData(0x4615, "SR - Old Stony Creek", level=Ty2Level.SouthernRivers),
    "Mount Boom Frill 1": LocData(0x4617, "Mount Boom Start", level=Ty2Level.MountBoom),
    "Mount Boom Frill 2": LocData(0x4618, "Mount Boom End", level=Ty2Level.MountBoom),
    "Killer Koala": LocData(0x6d000046, "Burramudgee Town", 70),
}


steve_dict: Dict[str, LocData] = {
    "Steve - Sly Shack": LocData(0x5300, "SR - Sly Shack", level=Ty2Level.SouthernRivers),
    "Steve - Burramudgee Sewers": LocData(0x5301, "Burramudgee Town", level=Ty2Level.Burramudgee),
    "Steve - Outback Oasis": LocData(0x5302, "Outback Oasis", level=Ty2Level.OutbackOasis),
    "Steve - Sulphur Rocks": LocData(0x5303, "Sulphur Rocks", level=Ty2Level.SulphurRocks),
    "Steve - Mount Boom": LocData(0x5304, "Mount Boom", level=Ty2Level.MountBoom), #thermo
    "Steve - Freeway Training Grounds": LocData(0x5305, "SR - Freeway Training Grounds", level=Ty2Level.SouthernRivers),
    "Steve - Never Never": LocData(0x5306, "Never Never", level=Ty2Level.NeverNever), #thermo
    "Steve - The Wetlands": LocData(0x5307, "Wetlands", level=Ty2Level.Wetlands),
    "Steve - Frill Neck Forest": LocData(0x5308, "SR - Frill Neck Forest", level=Ty2Level.FrillNeckForest),
    "Steve - Wobbygon Bay": LocData(0x5309, "SR - Wobbygon Bay", level=Ty2Level.SouthernRivers),
}


picture_frame_dict: Dict[str, LocData] = {
    "Outback Oasis Frame 1":  LocData(0x5000, "Outback Oasis", hint_info="Warp", level=Ty2Level.OutbackOasis), #warparang
    "Outback Oasis Frame 2":  LocData(0x5001, "Outback Oasis", hint_info="Warp", level=Ty2Level.OutbackOasis),#warparang
    "Outback Oasis Frame 3":  LocData(0x5002, "Outback Oasis", hint_info="Warp", level=Ty2Level.OutbackOasis),#warparang
    "Outback Oasis Frame 4": LocData(0x503E, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 5": LocData(0x503F, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 6": LocData(0x5040, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 7": LocData(0x5041, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 8": LocData(0x5042, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 9": LocData(0x5043, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 10": LocData(0x5044, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 11": LocData(0x5045, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 12": LocData(0x5046, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Outback Oasis Frame 13": LocData(0x5047, "Outback Oasis - Infra", hint_info="Cave Invisi-crates", level=Ty2Level.OutbackOasis),  # infra
    "Never Never Frame 1":  LocData(0x5003, "Never Never", hint_info="On Rock", level=Ty2Level.NeverNever),
    "Never Never Frame 2":  LocData(0x5004, "Never Never", hint_info="In Trees", level=Ty2Level.NeverNever), #lasharang
    "Never Never Frame 3":  LocData(0x5005, "Never Never", hint_info="In Trees", level=Ty2Level.NeverNever),
    "Never Never Frame 4":  LocData(0x5006, "Never Never", hint_info="Lava Chill Out", level=Ty2Level.NeverNever), #thermo OR lash OR frosty
    "Never Never Frame 5":  LocData(0x5007, "Never Never", hint_info="Alien Cliff Corner", level=Ty2Level.NeverNever),
    "Never Never Frame 6":  LocData(0x5008, "Never Never", hint_info="Underwater Alien", level=Ty2Level.NeverNever),
    "Never Never Frame 7":  LocData(0x5009, "Never Never", hint_info="Alien Corner", level=Ty2Level.NeverNever),
    "Never Never Frame 8":  LocData(0x500A, "Never Never", hint_info="Underwater Alien", level=Ty2Level.NeverNever),
    "Never Never Frame 9":  LocData(0x500B, "Never Never", hint_info="Rope Slide", level=Ty2Level.NeverNever),
    "Never Never Frame 10":  LocData(0x500C, "Never Never", hint_info="Dennis Rock Wall", level=Ty2Level.NeverNever), #smasharang
    "Never Never Frame 11":  LocData(0x500D, "Never Never", hint_info="Swinging Under", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 12":  LocData(0x500E, "Never Never", hint_info="Vine Climb", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 13":  LocData(0x500F, "Never Never", hint_info="Vine Climb", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 14":  LocData(0x5010, "Never Never", hint_info="Vine Climb", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 15":  LocData(0x5011, "Never Never", hint_info="Vine Climb", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 16":  LocData(0x5048, "Never Never - Infra", hint_info="Start", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 17":  LocData(0x5049, "Never Never - Infra", hint_info="Start", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 18":  LocData(0x504A, "Never Never - Infra", hint_info="Start", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 19":  LocData(0x504B, "Never Never - Infra", hint_info="Start", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 20":  LocData(0x504C, "Never Never - Infra", hint_info="Start", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 21":  LocData(0x504D, "Never Never - Infra", hint_info="Invisi-crate", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 22":  LocData(0x504E, "Never Never - Infra", hint_info="Invisi-crate", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 23":  LocData(0x504F, "Never Never - Infra", hint_info="Invisi-crate", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 24":  LocData(0x5050, "Never Never - Infra", hint_info="Invisi-crate", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 25":  LocData(0x5051, "Never Never - Infra", hint_info="Invisi-crate", level=Ty2Level.NeverNever), #infra
    "Never Never Frame 26":  LocData(0x5052, "Never Never - Infra", hint_info="Island Invisi-crate", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 27":  LocData(0x5053, "Never Never - Infra", hint_info="Island Invisi-crate", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 28":  LocData(0x5054, "Never Never - Infra", hint_info="Island Invisi-crate", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 29":  LocData(0x5055, "Never Never - Infra", hint_info="Island Invisi-crate", level=Ty2Level.NeverNever),#infra
    "Never Never Frame 30":  LocData(0x5056, "Never Never - Infra", hint_info="Island Invisi-crate", level=Ty2Level.NeverNever),#infra
    "Wetlands Frame 1":  LocData(0x5012, "Wetlands Tree", hint_info="Warp Tree", level=Ty2Level.Wetlands),#warparang
    "Wetlands Frame 2":  LocData(0x5013, "Wetlands Tree", hint_info="Warp Tree", level=Ty2Level.Wetlands),#warparang
    "Wetlands Frame 3":  LocData(0x5014, "Wetlands Tree", hint_info="Warp Tree", level=Ty2Level.Wetlands),#warparang
    "Wetlands Frame 4":  LocData(0x5015, "Wetlands Tree", hint_info="Warp Tree", level=Ty2Level.Wetlands),#warparang
    "Wetlands Frame 5":  LocData(0x5016, "Wetlands Tree", hint_info="Warp Tree", level=Ty2Level.Wetlands), #warparang
    "Wetlands Frame 6":  LocData(0x5057, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 7":  LocData(0x5058, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 8":  LocData(0x5059, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 9":  LocData(0x505A, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 10":  LocData(0x505B, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 11":  LocData(0x505C, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands), #infra
    "Wetlands Frame 12":  LocData(0x505D, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands),#infra
    "Wetlands Frame 13":  LocData(0x505E, "Wetlands - Infra", hint_info="Invisi-crates", level=Ty2Level.Wetlands),#infra
    "Faire Dinkum Frame 1":  LocData(0x5017, "Faire Dinkum", hint_info="In tree", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 2":  LocData(0x5018, "Faire Dinkum", hint_info="Town Roofs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 3":  LocData(0x5019, "Faire Dinkum", hint_info="Town Roofs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 4":  LocData(0x501A, "Faire Dinkum", hint_info="Town Roofs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 5":  LocData(0x501B, "Faire Dinkum", hint_info="Town Roofs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 6":  LocData(0x501C, "Faire Dinkum", hint_info="Town Roofs", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 7":  LocData(0x501D, "Faire Dinkum", hint_info="Behind End Croc", level=Ty2Level.FaireDinkum),
    "Faire Dinkum Frame 8":  LocData(0x501E, "Faire Dinkum", hint_info="Smash Wall", level=Ty2Level.FaireDinkum), #smasharang
    "Faire Dinkum Frame 9":  LocData(0x501F, "Faire Dinkum", hint_info="Smash Wall", level=Ty2Level.FaireDinkum), #smasharang
    "Faire Dinkum Frame 10":  LocData(0x505F, "Faire Dinkum - Infra", hint_info="Town Invisi-crates", level=Ty2Level.FaireDinkum), #infra
    "Faire Dinkum Frame 11":  LocData(0x5060, "Faire Dinkum - Infra", hint_info="Town Invisi-crates", level=Ty2Level.FaireDinkum), #infra
    "Faire Dinkum Frame 12":  LocData(0x5061, "Faire Dinkum - Infra", hint_info="End Invisi-crates", level=Ty2Level.FaireDinkum), #infra
    "Faire Dinkum Frame 13":  LocData(0x5062, "Faire Dinkum - Infra", hint_info="End Invisi-crates", level=Ty2Level.FaireDinkum), #infra
    "Faire Dinkum Frame 14":  LocData(0x5063, "Faire Dinkum - Infra", hint_info="End Invisi-crates", level=Ty2Level.FaireDinkum), #infra
    "Sulphur Rocks Frame 1":  LocData(0x5020, "Sulphur Rocks", hint_info="Sulphur Start", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frame 2":  LocData(0x5021, "Sulphur Rocks", hint_info="Sulphur Start", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frame 3":  LocData(0x5022, "Sulphur Rocks", hint_info="In Hole", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frame 4":  LocData(0x5023, "Sulphur Rocks", hint_info="Behind Fence", level=Ty2Level.SulphurRocks),#lasharang, not needed
    "Sulphur Rocks Frame 5":  LocData(0x5024, "Sulphur Rocks", hint_info="Behind Fence", level=Ty2Level.SulphurRocks), #lasharang, not needed
    "Sulphur Rocks Frame 6":  LocData(0x5025, "Sulphur Rocks", hint_info="Behind Fence", level=Ty2Level.SulphurRocks),#lasharang, not needed
    "Sulphur Rocks Frame 7":  LocData(0x5026, "Sulphur Rocks", hint_info="In Hole", level=Ty2Level.SulphurRocks),
    "Sulphur Rocks Frame 8": LocData(0x5064,  "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 9": LocData(0x5065,  "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 10": LocData(0x5066, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 11": LocData(0x5067, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 12": LocData(0x5068, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 13": LocData(0x5069, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 14": LocData(0x506A, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 15": LocData(0x506B, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 16": LocData(0x506C, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 17": LocData(0x506D, "Sulphur Rocks - Infra", hint_info="Start Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 18": LocData(0x506E, "Sulphur Rocks - Infra", hint_info="Trial Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 19": LocData(0x506F, "Sulphur Rocks - Infra", hint_info="Trial Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 20": LocData(0x5070, "Sulphur Rocks - Infra", hint_info="Trial Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 21": LocData(0x5071, "Sulphur Rocks - Infra", hint_info="Trial Invisi-crates", level=Ty2Level.SulphurRocks),  # infra
    "Sulphur Rocks Frame 22": LocData(0x50AE, "Sulphur Rocks", hint_info="Start", level=Ty2Level.SulphurRocks),
    "Burramudgee Frame 1":  LocData(0x5027, "Burramudgee HQ - Infra", hint_info="Floating Above HQ", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 2":  LocData(0x5028, "Burramudgee HQ - Infra", hint_info="Floating Above HQ", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 3":  LocData(0x5029, "Burramudgee HQ - Infra", hint_info="Floating Above HQ", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 4":  LocData(0x502A, "Burramudgee HQ", hint_info="Watch Tower", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 5":  LocData(0x502B, "Burramudgee HQ", hint_info="Watch Tower", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 6":  LocData(0x502C, "Burramudgee HQ", hint_info="Watch Tower", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 7":  LocData(0x502D, "Burramudgee HQ", hint_info="Watch Tower", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 8":  LocData(0x5072, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 9":  LocData(0x5073, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 10":  LocData(0x5074, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 11":  LocData(0x5075, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 12":  LocData(0x5076, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 13":  LocData(0x5077, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 14":  LocData(0x5078, "Burramudgee Town - Infra", hint_info="Sewer Steve", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 15":  LocData(0x5079, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 16":  LocData(0x507A, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 17":  LocData(0x507B, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 18":  LocData(0x507C, "Burramudgee Town - Infra", hint_info="Sewer CrossWay Dead End", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 19":  LocData(0x507D, "Burramudgee Town - Infra", hint_info="Sewer CrossWay Dead End", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 20":  LocData(0x507E, "Burramudgee Town - Infra", hint_info="Sewer CrossWay Dead End", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 21":  LocData(0x507F, "Burramudgee Town - Infra", hint_info="Sewer Steve", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 22":  LocData(0x5080, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 23":  LocData(0x5081, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 24":  LocData(0x5082, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 25":  LocData(0x5083, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 26":  LocData(0x5084, "Burramudgee Town - Infra", hint_info="Sewer CrossWay", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 27":  LocData(0x5085, "Burramudgee Town - Infra", hint_info="Sewer Entrance", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 28":  LocData(0x5086, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 29":  LocData(0x5087, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 30":  LocData(0x5088, "Burramudgee Town - Infra", hint_info="Sewer Steve", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 31":  LocData(0x5089, "Burramudgee Town - Infra", hint_info="Sewer Grid", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 32":  LocData(0x508A, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 33":  LocData(0x508B, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 34":  LocData(0x508C, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 35":  LocData(0x508D, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 36":  LocData(0x508E, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 37":  LocData(0x508F, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 38":  LocData(0x5090, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 39":  LocData(0x5091, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 40":  LocData(0x5092, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 41":  LocData(0x5093, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 42":  LocData(0x5094, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 43":  LocData(0x5095, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 44":  LocData(0x5096, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 45":  LocData(0x5097, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 46":  LocData(0x5098, "Burramudgee HQ", hint_info="HQ Balcony Boxes", level=Ty2Level.Burramudgee),
    "Burramudgee Frame 47":  LocData(0x5099, "Burramudgee HQ", hint_info="HQ Warparang Tutorial", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 48":  LocData(0x509A, "Burramudgee HQ", hint_info="HQ Warparang Tutorial", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 49":  LocData(0x509B, "Burramudgee HQ", hint_info="HQ Warparang Tutorial", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 50":  LocData(0x509C, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 51":  LocData(0x509D, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 52":  LocData(0x509E, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 53":  LocData(0x509F, "Burramudgee HQ - Crates", hint_info="HQ Roof Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 54":  LocData(0x50A0, "Burramudgee HQ - Crates", hint_info="HQ Roof Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 55":  LocData(0x50A1, "Burramudgee HQ - Crates", hint_info="HQ Roof Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 56":  LocData(0x50A2, "Burramudgee HQ - Crates", hint_info="HQ Roof Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 57":  LocData(0x50A3, "Burramudgee HQ - Crates", hint_info="HQ Roof Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 58":  LocData(0x50A4, "Burramudgee HQ - Crates", hint_info="HQ Meeting Room Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 59":  LocData(0x50A5, "Burramudgee HQ - Crates", hint_info="HQ Meeting Room Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 60":  LocData(0x50A6, "Burramudgee HQ - Crates", hint_info="HQ Meeting Room Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 61":  LocData(0x50A7, "Burramudgee HQ - Crates", hint_info="HQ Meeting Room Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 62":  LocData(0x50A8, "Burramudgee HQ - Crates", hint_info="HQ Meeting Room Box", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 63":  LocData(0x50A9, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 64":  LocData(0x50AA, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 65":  LocData(0x50AB, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 66":  LocData(0x50AC, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Burramudgee Frame 67":  LocData(0x50AD, "Burramudgee HQ - Crates", hint_info="HQ Hangar Boxes", level=Ty2Level.Burramudgee),#Smasharang
    "Frill Neck Frame 1":  LocData(0x502E, "Frill Neck Forest", hint_info="Trunk Vines", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 2":  LocData(0x502F, "Frill Neck Forest", hint_info="Trunk Vines", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 3":  LocData(0x5030, "Frill Neck Forest", hint_info="Trunk Vines", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 4":  LocData(0x5031, "Frill Neck Forest", hint_info="Trunk Vines", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 5":  LocData(0x5032, "Frill Neck Forest", hint_info="Trunk Vines", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 6":  LocData(0x5033, "Frill Neck Forest", hint_info="On Tree", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 7":  LocData(0x5034, "Frill Neck Forest", hint_info="Rope Start", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 8":  LocData(0x5035, "Frill Neck Forest", hint_info="Rope Log", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 9":  LocData(0x5036, "Frill Neck Forest", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 10": LocData(0x5037, "Frill Neck Forest", hint_info="Up Ladder", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 11": LocData(0x5038, "Frill Neck Forest", hint_info="On net", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 12": LocData(0x5039, "Frill Neck Forest", hint_info="Up Ladder", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 13": LocData(0x503A, "Frill Neck Forest", hint_info="Below Money Bag", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 14": LocData(0x503B, "Frill Neck Forest", hint_info="Above Dunny", level=Ty2Level.FrillNeckForest),
    "Frill Neck Frame 15": LocData(0x503C, "Frill Neck Forest", hint_info="Side Platform", level=Ty2Level.FrillNeckForest),
    "Mount Boom Frame":  LocData(0x503D, "Mount Boom End", hint_info="End", level=Ty2Level.MountBoom), #Lasharang
}


race_dict: Dict[str, LocData] = {
    "Refinery Run": LocData(0x6d000007, "SR - Refinery Run", 7),
    "Lava Falls": LocData(0x6d000016, "SR - Lava Falls Race", 22),
    "Hearty Beach": LocData(0x6d000017, "SR - Hearty Beach", 23),
    "Parrotbeard Cove": LocData(0x6d00002b, "SR - Wobbygon Bay", 43),
    "Never Never Road": LocData(0x6d00002d, "SR - Never Never Road", 45),
    "Outback Dash": LocData(0x6d00003c, "SR - Outback Dash", 60),
    "Turbo Track": LocData(0x6d000044, "SR - Turbo Track", 68),
}


def get_mission_complete_events(world):
    complete_mission_dict = {}
    for name, loc_data in mission_dict.items():
        if loc_data.code is None:
            continue

        new_name = f"Complete {name}"
        new_ingame_id = loc_data.id + 100  # Add 100 to ingame ID
        complete_mission_dict[new_name] = LocData(None, loc_data.region, new_ingame_id)

    if world.options.frill_sanity:
        complete_mission_dict["Complete Killer Koala"] = LocData(None, "Burramudgee Town", 170)

    if world.options.barrier_unlock.value == 0:
        complete_mission_dict["Beat Patchy"] = LocData(None, "Patchy", 980)
        complete_mission_dict["Beat Fluffy"] = LocData(None, "Fluffy's Fortress", 981)
        complete_mission_dict["Beat Buster"] = LocData(None, "Buster the Nanobot Boss", 982)

    return complete_mission_dict


mission_dict: Dict[str, LocData] = {
    "Metal Menace": LocData(0x6d000001, "Outback Oasis", 1, level=Ty2Level.OutbackOasis),
    "Explosive Cargo": LocData(0x6d000002, "Lake Burramudgee", 2, level=Ty2Level.SouthernRivers), #didnt get set to 5+
    "Boss Cass Bust-Up": LocData(None, "Cass' Run", 83), #0x6d000053
    "Haunted Hassle": LocData(0x6d000004, "Burramudgee Town", 4, level=Ty2Level.Burramudgee), #infrarang
    "Tree Rescue": LocData(0x6d000005, "Burramudgee Town", 5, level=Ty2Level.Burramudgee),
    "Crouching Birrel, Hidden Squeaver": LocData(0x6d000006, "SR - Min Min Plains", 6, level=Ty2Level.SouthernRivers),

    "Currawong Jail Break": LocData(0x6d000054, "Menu", 84),
    "Dennis Dash": LocData(0x6d000009, "Never Never", 9, level=Ty2Level.NeverNever), # need requirements removed
    "Rocky Road": LocData(0x6d00000a, "Never Never", 10, level=Ty2Level.NeverNever), # need requirements removed
    "Lava Chill Out": LocData(0x6d00000b, "Never Never", 11, level=Ty2Level.NeverNever), #thermo, lash, OR frosty # need requirements removed
    "Canopy Capers": LocData(0x6d00000c, "Frill Neck Forest", 12, level=Ty2Level.FrillNeckForest),
    "Croc Stock Pile": LocData(0x6d00000d, "Muddy Bottom", 13, level=Ty2Level.SouthernRivers), #didnt send
    "Fire Fight": LocData(0x6d00000e, "Fire Fight", 14, level=Ty2Level.SouthernRivers),
    "Truck Tragedy": LocData(0x6d000010, "SR - Truck Tragedy", 16, level=Ty2Level.SouthernRivers), #lifter bunyip
    "Plutonium Panic": LocData(0x6d000011, "SR - Plutonium Panic", 17, level=Ty2Level.SouthernRivers),
    "Need A Spare": LocData(0x6d000012, "SR - Dusty Burrows", 18, level=Ty2Level.SouthernRivers),
    "King Squeaver and Birrel Hood": LocData(0x6d000014, "SR - King Squeaver", 20, level=Ty2Level.SouthernRivers),
    "Musical Mommy": LocData(0x6d000018, "Never Never", 24, level=Ty2Level.NeverNever), #needs requirements removed
    "Tourist Trap": LocData(0x6d000019, "Faire Dinkum", 25, level=Ty2Level.FaireDinkum),
    "Crocodile Chaos": LocData(0x6d00001a, "Wetlands", 26, level=Ty2Level.Wetlands),
    "Sheep Dip": LocData(0x6d00001c, "Old Stony Creek", 28, level=Ty2Level.SouthernRivers), #doesnt send
    "Dennis Freeway": LocData(0x6d000021, "Dennis Freeway", 33, level=Ty2Level.SouthernRivers), #didnt update
    "Teeter Tottering Inferno": LocData(0x6d000022, "Sulphur Rocks", 34, level=Ty2Level.SulphurRocks),
    "Grindstone Cowboy": LocData(0x6d000024, "Sulphur Rocks", 36, level=Ty2Level.SulphurRocks),
    "Volcano Rescue": LocData(0x6d000025, "Mount Boom End", 37, level=Ty2Level.MountBoom), #thermo
    "Bush Fire": LocData(0x6d000026, "Bush Fire", 38, level=Ty2Level.SouthernRivers), #thermo
    "Truck Stop": LocData(0x6d000027, "SR - Truck Stop", 39, level=Ty2Level.SouthernRivers), #stupid long mission #lifter bunyip
    "Sea Lab": LocData(0x6d000028, "Beach Sub", 40, level=Ty2Level.SouthernRivers), #sub bunyip
    "Grub Grab": LocData(0x6d000029, "SR - Wobbygon Bay", 41, level=Ty2Level.SouthernRivers), #talk to dennis sunscreen
    "Big Bang": LocData(0x6d00002a, "SR - Min Min Mining", 42, level=Ty2Level.SouthernRivers),

    "Snake Eyes": LocData(0x6d00002e, "Sulphur Rocks", 46, level=Ty2Level.SulphurRocks),
    "Hidden Danger": LocData(0x6d00002f, "Burramudgee Town", 47, level=Ty2Level.Burramudgee), #infrarang
    "Oil Rig Fire": LocData(0x6d000034, "Oil Rig", 52), #done before buster
    "Freeway Training Grounds": LocData(0x6d000058, "Freeway Training Grounds", 88, level=Ty2Level.SouthernRivers),
    "Beach Training Grounds": LocData(0x6d000057, "Beach Training Grounds", 87, level=Ty2Level.SouthernRivers),
    "Ripper Nipper": LocData(0x6d000037, "SR - Wobbygon Bay", 55, level=Ty2Level.SouthernRivers), #sunscreen
    "Attack of the 50 Foot Squeaver": LocData(0x6d00003b, "SR - 50 Foot Squeaver", 59, level=Ty2Level.SouthernRivers),
    "Deep Sea Scare": LocData(0x6d000040, "Deep Sea Scare", 64, level=Ty2Level.SouthernRivers), #didnt show, save rex sub bunyip
    "Bush Rescue Training Program": LocData(0x6d000055, "Burramudgee HQ", 85, level=Ty2Level.Burramudgee), #
    "That's A Croc": LocData(0x6d000062, "Burramudgee Town", 98, level=Ty2Level.Burramudgee),
    "Patchy": LocData(0x6d000050, "Patchy", 80),
    "Fluffy": LocData(0x6d000051, "Fluffy's Fortress", 81),
    "Buster the Nanobot Boss": LocData(0x6d000052, "Buster the Nanobot Boss", 82),

    #99 is see julius
    #mission 86 is get into car
    #patchy is m980
    # is m981
    #nano is m982
    #mission 100 spawns warp flower at sly
    #mission 371 gate 1 Mount Boom
    #mission 373 is warperang spot button
    #mission 372 is gate

}


sign_dict: Dict[str, LocData] = {
    # "sign sanity": 0x00 #sanity
}


full_location_dict: Dict[str, LocData] = {
    **shop_location_dict,
    **platinum_cog_dict,
    **kromium_orb_dict,
    **bilby_dict,
    **steve_dict,
    **disguised_frill_dict,
    **picture_frame_dict,
    **mission_dict,
    **race_dict
}

ty2_level_dict = {
    Ty2Level.Burramudgee: "Burramudgee",
    Ty2Level.SouthernRivers: "Southern Rivers",
    Ty2Level.SulphurRocks: "Sulphur Rocks",
    Ty2Level.Wetlands: "The Wetlands",
    Ty2Level.NeverNever: "The Never Never",
    Ty2Level.MountBoom: "Mount Boom",
    Ty2Level.FaireDinkum: "Faire Dinkum",
    Ty2Level.OutbackOasis: "Outback Oasis",
    Ty2Level.FrillNeckForest: "Frill Neck Forest"
}

def get_location_groups() -> dict[str, set[str]]:
    location_groups = {
        "Platinum Cog": set(name for name, data in platinum_cog_dict.items() if data.level is not None),
        "Bilby": set(name for name, data in bilby_dict.items() if data.level is not None),
        "Mission": set(name for name, data in mission_dict.items() if data.level is not None),
        "Kromium Orb": set(name for name, data in kromium_orb_dict.items() if data.level is not None),
        "Steve": set(name for name, data in steve_dict.items() if data.level is not None),
        "Disguised Frill": set(name for name, data in disguised_frill_dict.items() if data.level is not None)
    }
    for loc_name, loc_data in full_location_dict.items():
        if loc_data.level is None:
            continue
        level_name = ty2_level_dict[loc_data.level]
        if loc_data.level not in location_groups:
            location_groups[level_name] = set()
        location_groups[level_name].add(loc_name)
    return location_groups


ty1_location_groups = get_location_groups()