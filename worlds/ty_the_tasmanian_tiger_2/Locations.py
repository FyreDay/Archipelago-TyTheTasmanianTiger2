from typing import NamedTuple, Optional, Dict

from BaseClasses import Location


class Ty2Location(Location):
    game: str = "Ty the Tasmanian Tiger 2"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1

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
    "Rang Shop Item 8": LocData(26, "Burramudgee Town"),# Camerarang
    "Rang Shop Item 1": LocData(8, "Burramudgee Town"), #frosty
    "Rang Shop Item 2": LocData(9, "Burramudgee Town"), #flame
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
    "Never Never Cog 0 - Descending Platform": LocData(0x4300, "Never Never"),
    "Outback Oasis Cog 1 - Dunny Rock Wall": LocData(0x4301, "Outback Oasis"), #smasharang
    "Outback Oasis Cog 2 - Over Wall": LocData(0x4302, "Outback Oasis"),
    "Outback Oasis Cog 3 - Near Trampoline": LocData(0x4303, "Outback Oasis"), #smasharang
    "Outback Oasis Cog 4 - Platform Parkour": LocData(0x4304, "Outback Oasis"),
    "Never Never Cog 5 - Vanishing Platforms": LocData(0x4305, "Never Never"), #smasharang
    "Never Never Cog 6 - On Platform": LocData(0x4306, "Never Never"),
    "Never Never Cog 7 - On Tree": LocData(0x4307, "Never Never"),
    "Never Never Cog 8 - Hidden Button": LocData(0x4308, "Never Never"),
    "Never Never Cog 9 - In Trees": LocData(0x4309, "Never Never"),
    "Never Never Cog 10 - Tree Ladder": LocData(0x430A, "Never Never"),
    "Never Never Cog 11 - Lava Chill Out": LocData(0x430B, "Never Never"),#thermo, lash, OR frosty
    "Never Never Cog 12 - Hidden Flower": LocData(0x430C, "Never Never"),
    "Never Never Cog 13 - Rocky Road": LocData(0x430D, "Never Never"),
    "Never Never Cog 14 - Rope Slide": LocData(0x430E, "Never Never"),
    "Never Never Cog 15 - Rope Race": LocData(0x430F, "Never Never"),
    "Never Never Cog 16 - Hut Button Required": LocData(0x4310, "Never Never - Infra"), #infra
    "Never Never Cog 17 - Hut": LocData(0x4311, "Never Never"), #lasharang
    "Never Never Cog 18 - Moving Platform": LocData(0x4312, "Never Never"),
    "Never Never Cog 19 - End Wall": LocData(0x4313, "Never Never"), #smasharang
    "Faire Dinkum Cog 20 - End of Level": LocData(0x4314, "Faire Dinkum"), #smasharang
    "Faire Dinkum Cog 21 - Smash Wall": LocData(0x4315, "Faire Dinkum"),
    "Faire Dinkum Cog 22 - Long Ride In The Trees": LocData(0x4316, "Faire Dinkum"),
    "Sulphur Rocks Cog 23 - Snake Eyes Challenge": LocData(0x4317, "Sulphur Rocks"), #frosty
    "Sulphur Rocks Cog 24 - Boulder Lift": LocData(0x4318, "Sulphur Rocks"), #lifter bunyip key
    "Sulphur Rocks Cog 25 - Swinging Around": LocData(0x4319, "Sulphur Rocks"),
    "Sulphur Rocks Cog 26": LocData(0x431A, "Sulphur Rocks"), #lasharang
    "Sulphur Rocks Cog 27": LocData(0x431B, "Sulphur Rocks"),
    "Sulphur Rocks Cog 28": LocData(0x431C, "Sulphur Rocks"),
    "Sulphur Rocks Cog 29 - Beyond Saw": LocData(0x431D, "Sulphur Rocks"),
    "Sulphur Rocks Cog 30 - Sulpher Start": LocData(0x431E, "Sulphur Rocks"),
    "Sulphur Rocks Cog 31": LocData(0x431F, "Sulphur Rocks"), #warparang
    "Burramudgee Cog 32 - Across the Camera Eggs": LocData(0x4320, "Burramudgee Town"),
    "Burramudgee Cog 33 - Rope Timer Race": LocData(0x4321, "Burramudgee Town"),
    "Burramudgee Cog 34 - On Haunted Mansion": LocData(0x4322, "Burramudgee Town"),
    "Cass's Run Cog 35": LocData(0x4323, "Cass' Run"),
    "Frill Neck Cog 36 - Start Trunk Glide": LocData(0x4324, "Frill Neck Forest"),
    "MountBoom Cog 37": LocData(0x4325, "MountBoom"),#warparang #thermo
    "MountBoom Cog 38": LocData(0x4326, "MountBoom"), #thermo
    "MountBoom Cog 39": LocData(0x4327, "MountBoom"),#warparang #thermo
    "Wetlands Cog 40 - Button Platform": LocData(0x4328, "Wetlands"),
    "Wetlands Cog 41 - Rock Wall": LocData(0x4329, "Wetlands"), #smasharang
    "Wetlands Cog 42 - Timer": LocData(0x432A, "Wetlands"),
    "Wetlands Cog 43 - Camera Eggs": LocData(0x432B, "Wetlands"),
    "Wetlands Cog 44 - Bunyip": LocData(0x432C, "Wetlands"), #flamerang optional
    "Wetlands Cog 45 - Crocs": LocData(0x432D, "Wetlands"),
    "Wobbygon Cog 46 - Central Ocean": LocData(0x432E, "SR - Wobbygon Bay"),
    "Wobbygon Cog 47 - In Seaweed": LocData(0x432F, "SR - Wobbygon Bay"),
    "Wobbygon Cog 48 - Cassopolis": LocData(0x4330, "SR - Wobbygon Bay"),
    "Burramudgee Cog 49 - Floating Above HQ": LocData(0x4331, "Burramudgee HQ - Infra"),
}

kromium_orb_dict: Dict[str, LocData] = {
    "Burramudgee Orb 0 - High Above Burramudgee": LocData(0x4B00, "Burramudgee Town"),#lasharang
    "Burramudgee Orb 1 - Above the Canal": LocData(0x4B01, "Burramudgee Town"),
    "Sulphur Rocks Orb 2 - Swinging Over the Pond": LocData(0x4B02, "Sulphur Rocks"), #lasharang
    "Sulphur Rocks Orb 3 - Sulphur Lava": LocData(0x4B03, "Sulphur Rocks"), #lasharang #frostyrang
    "Sulphur Rocks Orb 4 - Exploding Pillars": LocData(0x4B04, "Sulphur Rocks"),
    "Sulphur Rocks Orb 5 - Jumping Maze": LocData(0x4B05, "SR - Sulphur Rocks"),
    "MountBoom Orb 6": LocData(0x4B06, "MountBoom"), #thermo
    "MountBoom Orb 7": LocData(0x4B07, "MountBoom"),#warperang #thermo smash
    "Wobbygon Orb 8 - Water Near Warps": LocData(0x4B08, "SR - Wobbygon Bay"),
    "Outback Oasis Orb 9 - Super Frill Beat Up":  LocData(0x4B09, "Outback Oasis"), #smasharang
    "Sly Orb 10 - Sly Shack": LocData(0x4B0A, "SR - Sly Shack"),
    "Outback Oasis Orb 11 - Spinning Platforms": LocData(0x4B0B, "Outback Oasis"),
    "Sulphur Rocks Orb 12 - Sulpher Overlook": LocData(0x4B0C, "Sulphur Rocks"),
    "Sulphur Rocks Orb 13": LocData(0x4B0D, "Sulphur Rocks"), #infra
    "Sulphur Rocks Orb 14 - On Invisible Platforms": LocData(0x4B0E, "Sulphur Rocks"), #infra
    "Never Never Orb 15 - Behind Wall": LocData(0x4B0F, "Never Never"), #smasharang
    "Never Never Orb 16 - In Trees": LocData(0x4B10, "Never Never"), #lasharang OPTIONAL
    "Never Never Orb 17 - Swinging Fence": LocData(0x4B11, "Never Never"),
    "Never Never Orb 18 - By Fence": LocData(0x4B12, "Never Never"),
    "Never Never Orb 19 - Rope Slide": LocData(0x4B13, "Never Never"),
    "Never Never Orb 20 - Swinging Under": LocData(0x4B14, "Never Never"),
    "Never Never Orb 21 - WaterWheel": LocData(0x4B15, "Never Never"),
    "Wetlands Orb 22 - Crocs": LocData(0x4B16, "Wetlands"), #lasharang
    "Frill Neck Orb 23 - Side Platform": LocData(0x4B17, "Frill Neck Forest"),
    "Burramudgee Orb 24 - Town Overlook": LocData(0x4B18, "Burramudgee HQ"),
    "Dennis Freeway Orb 25": LocData(0x4B19, "SR - Dennis Freeway"), #warparang
    "Faire Dinkum Orb 26 - Moving Platform": LocData(0x4B1A, "Faire Dinkum"),
    "Burramudgee Orb 27 - Frosty Tutorial": LocData(0x4B1B, "Burramudgee HQ"), #smasharang
    "Faire Dinkum Orb 28 - Behind Dunny": LocData(0x4B1C, "Faire Dinkum"),
    "Wobbygon Orb 29 - Corner Seaweed": LocData(0x4B1D, "SR - Wobbygon Bay"),
} #what is the orb at freeway

bilby_dict: Dict[str, LocData] = {
    "Outback Oasis Bilby 0 - Trampoline": LocData(0x4200, "Outback Oasis"), #smasharang
    "Outback Oasis Bilby 1 - Hanging On Entrance": LocData(0x4201, "Outback Oasis"),
    "Outback Oasis Bilby 2 - Cave": LocData(0x4202, "Outback Oasis"),
    "Never Never Bilby 3": LocData(0x4203, "Never Never"),
    "Never Never Bilby 4 - Lava Chill Out": LocData(0x4204, "Never Never"),#thermo, lash, OR frosty
    "Never Never Bilby 5 - Rope Slide": LocData(0x4205, "Never Never"),
    "Never Never Bilby 6 - Moving Platform": LocData(0x4206, "Never Never"),
    "Faire Dinkum Bilby 7 - Secret Button": LocData(0x4207, "Faire Dinkum"),
    "Faire Dinkum Bilby 8 - Town Overlook": LocData(0x4208, "Faire Dinkum"),
    "Faire Dinkum Bilby 9 - Half Under Webs": LocData(0x4209, "Faire Dinkum"),
    "Sulphur Rocks Bilby 10 - Sulpher Overlook": LocData(0x420A, "Sulphur Rocks"),
    "Sulphur Rocks Bilby 11": LocData(0x420B, "Sulphur Rocks"),
    "Sulphur Rocks Bilby 12 - Floating Over Sulpher": LocData(0x420C, "Sulphur Rocks"),
    "Sulphur Rocks Bilby 13": LocData(0x420D, "Sulphur Rocks"),
    "Sulphur Rocks Bilby 14 - Over pond": LocData(0x420E, "Sulphur Rocks"),
    "Faire Dinkum Bilby 15": LocData(0x420F, "Faire Dinkum"), #(infra)
    "Frill Neck Bilby 16 - End Trunk": LocData(0x4210, "Frill Neck Forest"), #lasharang - possible without
    "Frill Neck Bilby 17": LocData(0x4211, "Frill Neck Forest"),
    "MountBoom Bilby 18 - Beginning": LocData(0x4212, "MountBoom"), #lasharang and thermo - MountBoom Beginning
    "MountBoom Bilby 19 - Warp": LocData(0x4213, "MountBoom"), #warparang #thermo
    "Wetlands Bilby 20 - In Log": LocData(0x4214, "Wetlands"),
    "Wetlands Bilby 21 - Webbed": LocData(0x4215, "Wetlands"), #flamerang
    "Wetlands Bilby 22 - Bunyip": LocData(0x4216, "Wetlands"), #todo: flamerang
    "Burramudgee Bilby 23 - Under Ramp": LocData(0x4217, "Burramudgee HQ"),
    "Burramudgee Bilby 24 - Cliffside": LocData(0x4218, "Burramudgee HQ"),
    "Burramudgee Bilby - Top of HQ": LocData(0x4219, "Burramudgee HQ"), #25
    "Burramudgee Bilby 26 - Watch Tower": LocData(0x421A, "Burramudgee HQ"),
    "Wobbygon Bilby 27 - Warp Tree": LocData(0x421B, "SR - Wobbygon Bay"),
    "Wobbygon Bilby 28 - Race Island": LocData(0x421C, "SR - Wobbygon Bay"),
    "Wobbygon Bilby 29 - Underwater South Boathouse": LocData(0x421D, "SR - Wobbygon Bay"),
}


disguised_frill_dict: Dict[str, LocData] = {
    "Outback Oasis Frill 0 - By Bunyip": LocData(0x4600, "Outback Oasis"), #smasharang
    "Outback Oasis Frill 1 - Start": LocData(0x4601, "Outback Oasis"),
    "Outback Oasis Frill 2 - Cave Overlook": LocData(0x4602, "Outback Oasis"),
    "Outback Oasis Frill 3 - By Wall": LocData(0x4603, "Never Never"),
    "Never Never Frill 4 - Rocky Road": LocData(0x4604, "Never Never"),
    "Never Never Frill 5 - Vine Climb": LocData(0x4605, "Never Never"),
    "Wetlands Frill 6 - By Button": LocData(0x4606, "Wetlands"),
    "Wetlands Frill 7 - Crocs": LocData(0x4607, "Wetlands"),
    "Faire Dinkum Frill 8 - Under Walkway": LocData(0x4608, "Faire Dinkum"),
    "Sulphur Rocks Frill 9 - Start": LocData(0x4609, "Sulphur Rocks"),
    "Sulphur Rocks Frill 10 - In Hole": LocData(0x460A, "Sulphur Rocks"),
    "Sulphur Rocks Frill 11 - Behind Fence": LocData(0x460B, "Sulphur Rocks"),#lasharang, not needed
    "Burramudgee Frill 12 - Near Police": LocData(0x460C, "Burramudgee Town"),
    "Burramudgee Frill 13 - Near Canal": LocData(0x460D, "Burramudgee Town"),
    "Dennis Freeway - Disguised Frill 14": LocData(0x460E, "SR - Dennis Freeway"),
    "Outback Oasis Frill 15 - Picnik": LocData(0x460F, "SR - Outback Oasis"),
    "50 Foot Squeaver Frill 16": LocData(0x4610, "SR - 50 Foot Squeaver"),
    "Lake Burramudgee Frill 17": LocData(0x4611, "SR - Lake Burramudgee"),
    "Frill Neck Frill 18": LocData(0x4612, "SR - Frill Neck Forest"),
    "Truck Tragedy Frill 19": LocData(0x4613, "SR - Truck Tragedy"),
    "Never Never Frill 20 - Never Never Entrance": LocData(0x4614, "SR - Never Never"), #didnt send
    "Sheep Dip Frill 21": LocData(0x4615, "SR - Old Stony Creek"),
    "Frill Neck Frill 22": LocData(0x4616, "Frill Neck Forest"),
    "MountBoom Frill 23": LocData(0x4617, "MountBoom Start"),
    "MountBoom Frill 24": LocData(0x4618, "MountBoom End"),
}

steve_dict: Dict[str, LocData] = {
    "Steve - Sly Shack": LocData(0x5300, "SR - Sly Shack"),
    "Steve - Burramudgee Town": LocData(0x5301, "Burramudgee Town"),
    "Steve - Outback Oasis": LocData(0x5302, "Outback Oasis"), #todo:Lash #infra
    "Steve - Sulphur Rocks": LocData(0x5303, "Sulphur Rocks"),
    "Steve - MountBoom": LocData(0x5304, "MountBoom"), #thermo
    "Steve - Freeway Training": LocData(0x5305, "SR - Freeway Training Grounds"),
    "Steve - Never Never": LocData(0x5306, "Never Never"), #thermo
    "Steve - Wetlands": LocData(0x5307, "Wetlands"),
    "Steve - Fill Neck": LocData(0x5308, "SR - Frill Neck Forest"),
    "Steve - Wobbygon Bay": LocData(0x5309, "SR - Wobbygon Bay"),
}

picture_frame_dict: Dict[str, LocData] = {
    "Outback Oasis Frame 0 - Warp": LocData(0x5000, "Outback Oasis"), #warparang
    "Outback Oasis Frame 1 - Warp": LocData(0x5001, "Outback Oasis"),#warparang
    "Outback Oasis Frame 2 - Warp": LocData(0x5002, "Outback Oasis"),#warparang
    "Never Never Frame 3 - On Rock": LocData(0x5003, "Never Never"),
    "Never Never Frame 4 - In Trees": LocData(0x5004, "Never Never"), #lasharang
    "Never Never Frame 5 - In Trees": LocData(0x5005, "Never Never"),
    "Never Never Frame 6 - Lava Chill Out": LocData(0x5006, "Never Never"), #thermo OR lash OR frosty
    "Never Never Frame 7 - Alien Cliff Corner": LocData(0x5007, "Never Never"),
    "Never Never Frame 8 - Underwater Alien": LocData(0x5008, "Never Never"),
    "Never Never Frame 9 - Alien Corner": LocData(0x5009, "Never Never"),
    "Never Never Frame 10 - Underwater Alien": LocData(0x500A, "Never Never"),
    "Never Never Frame 11 - Rope Slide": LocData(0x500B, "Never Never"),
    "Never Never Frame 12 - Dennis Rock Wall": LocData(0x500C, "Never Never"), #smasharang
    "Never Never Frame 13 - Swinging Under": LocData(0x500D, "Never Never - Infra"), #infra
    "Never Never Frame 14 - Vine Climb": LocData(0x500E, "Never Never - Infra"),#infra
    "Never Never Frame 15 - Vine Climb": LocData(0x500F, "Never Never - Infra"),#infra
    "Never Never Frame 16 - Vine Climb": LocData(0x5010, "Never Never - Infra"),#infra
    "Never Never Frame 17 - Vine Climb": LocData(0x5011, "Never Never - Infra"),#infra
    "Wetlands Frame 18 - Warp Tree": LocData(0x5012, "Wetlands Tree"),#warparang
    "Wetlands Frame 19 - Warp Tree": LocData(0x5013, "Wetlands Tree"),#warparang
    "Wetlands Frame 20 - Warp Tree": LocData(0x5014, "Wetlands Tree"),#warparang
    "Wetlands Frame 21 - Warp Tree": LocData(0x5015, "Wetlands Tree"),#warparang
    "Wetlands Frame 22 - Warp Tree": LocData(0x5016, "Wetlands Tree"), #warparang
    "Faire Dinkum Frame 23 - In tree": LocData(0x5017, "Faire Dinkum"),
    "Faire Dinkum Frame 24 - Town Roofs": LocData(0x5018, "Faire Dinkum"),
    "Faire Dinkum Frame 25 - Town Roofs": LocData(0x5019, "Faire Dinkum"),
    "Faire Dinkum Frame 26 - Town Roofs": LocData(0x501A, "Faire Dinkum"),
    "Faire Dinkum Frame 27 - Town Roofs": LocData(0x501B, "Faire Dinkum"),
    "Faire Dinkum Frame 28 - Town Roofs": LocData(0x501C, "Faire Dinkum"),
    "Faire Dinkum Frame 29 - Behind End Croc": LocData(0x501D, "Faire Dinkum"),
    "Faire Dinkum Frame 30 - Smash Wall": LocData(0x501E, "Faire Dinkum"), #smasharang
    "Faire Dinkum Frame 31 - Smash Wall": LocData(0x501F, "Faire Dinkum"), #smasharang
    "Sulphur Rocks Frame 32 - Sulpher Start": LocData(0x5020, "Sulphur Rocks"),
    "Sulphur Rocks Frame 33 - Sulpher Start": LocData(0x5021, "Sulphur Rocks"),
    "Sulphur Rocks Frame 34 - In Hole": LocData(0x5022, "Sulphur Rocks"),
    "Sulphur Rocks Frame 35 - Behind Fence": LocData(0x5023, "Sulphur Rocks"),#lasharang, not needed
    "Sulphur Rocks Frame 36 - Behind Fence": LocData(0x5024, "Sulphur Rocks"), #lasharang, not needed
    "Sulphur Rocks Frame 37 - Behind Fence": LocData(0x5025, "Sulphur Rocks"),#lasharang, not needed
    "Sulphur Rocks Frame 38 - In Hole": LocData(0x5026, "Sulphur Rocks"),
    "Burramudgee Frame 39 - Floating Above HQ": LocData(0x5027, "Burramudgee HQ"),
    "Burramudgee Frame 40 - Floating Above HQ": LocData(0x5028, "Burramudgee HQ"),
    "Burramudgee Frame 41 - Floating Above HQ": LocData(0x5029, "Burramudgee HQ"),
    "Burramudgee Frame 42 - Watch Tower": LocData(0x502A, "Burramudgee HQ"),
    "Burramudgee Frame 43 - Watch Tower": LocData(0x502B, "Burramudgee HQ"),
    "Burramudgee Frame 44 - Watch Tower": LocData(0x502C, "Burramudgee HQ"),
    "Burramudgee Frame 45 - Watch Tower": LocData(0x502D, "Burramudgee HQ"),
    "Frill Neck Frame 46 - Trunk Vines": LocData(0x502E, "Frill Neck Forest"),
    "Frill Neck Frame 47 - Trunk Vines": LocData(0x502F, "Frill Neck Forest"),
    "Frill Neck Frame 48 - Trunk Vines": LocData(0x5030, "Frill Neck Forest"),
    "Frill Neck Frame 49 - Trunk Vines": LocData(0x5031, "Frill Neck Forest"),
    "Frill Neck Frame 50 - Trunk Vines": LocData(0x5032, "Frill Neck Forest"),
    "Frill Neck Frame 51 - On Tree": LocData(0x5033, "Frill Neck Forest"),
    "Frill Neck Frame 52 - Rope Start": LocData(0x5034, "Frill Neck Forest"),
    "Frill Neck Frame 53 - Rope Log": LocData(0x5035, "Frill Neck Forest"),
    "Frill Neck Frame 54": LocData(0x5036, "Frill Neck Forest"),
    "Frill Neck Frame 55 - Up Ladder": LocData(0x5037, "Frill Neck Forest"),
    "Frill Neck Frame 56 - On net": LocData(0x5038, "Frill Neck Forest"),
    "Frill Neck Frame 57 - Up Ladder": LocData(0x5039, "Frill Neck Forest"),
    "Frill Neck Frame 58 - Below Money Bag": LocData(0x503A, "Frill Neck Forest"),
    "Frill Neck Frame 59 - Above Dunny": LocData(0x503B, "Frill Neck Forest"),
    "Frill Neck Frame 60 - Side Platform": LocData(0x503C, "Frill Neck Forest"),
    "MountBoom Frame 61 - End": LocData(0x503D, "MountBoom End"), #Lasharang
    "Outback Oasis Frame 62 - Cave Invisa-crates": LocData(0x503E, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 63 - Cave Invisa-crates": LocData(0x503F, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 64 - Cave Invisa-crates": LocData(0x5040, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 65 - Cave Invisa-crates": LocData(0x5041, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 66 - Cave Invisa-crates": LocData(0x5042, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 67 - Cave Invisa-crates": LocData(0x5043, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 68 - Cave Invisa-crates": LocData(0x5044, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 69 - Cave Invisa-crates": LocData(0x5045, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 70 - Cave Invisa-crates": LocData(0x5046, "Outback Oasis - Infra"), #infra
    "Outback Oasis Frame 71 - Cave Invisa-crates": LocData(0x5047, "Outback Oasis - Infra"), #infra
    "Never Never Frame 72 - Start": LocData(0x5048, "Never Never - Infra"), #infra
    "Never Never Frame 73 - Start": LocData(0x5049, "Never Never - Infra"),#infra
    "Never Never Frame 74 - Start": LocData(0x504A, "Never Never - Infra"),#infra
    "Never Never Frame 75 - Start": LocData(0x504B, "Never Never - Infra"),#infra
    "Never Never Frame 76 - Start": LocData(0x504C, "Never Never - Infra"),#infra
    "Never Never Frame 77 - Invisa-crate": LocData(0x504D, "Never Never - Infra"), #infra
    "Never Never Frame 78 - Invisa-crate": LocData(0x504E, "Never Never - Infra"), #infra
    "Never Never Frame 79 - Invisa-crate": LocData(0x504F, "Never Never - Infra"), #infra
    "Never Never Frame 80 - Invisa-crate": LocData(0x5050, "Never Never - Infra"), #infra
    "Never Never Frame 81 - Invisa-crate": LocData(0x5051, "Never Never - Infra"), #infra
    "Never Never Frame 82 - Island Invisa-crate": LocData(0x5052, "Never Never - Infra"),#infra
    "Never Never Frame 83 - Island Invisa-crate": LocData(0x5053, "Never Never - Infra"),#infra
    "Never Never Frame 84 - Island Invisa-crate": LocData(0x5054, "Never Never - Infra"),#infra
    "Never Never Frame 85 - Island Invisa-crate": LocData(0x5055, "Never Never - Infra"),#infra
    "Never Never Frame 86 - Island Invisa-crate": LocData(0x5056, "Never Never - Infra"),#infra
    "Wetlands Frame 87 - Invisa-crates": LocData(0x5057, "Wetlands - Infra"), #infra
    "Wetlands Frame 88 - Invisa-crates": LocData(0x5058, "Wetlands - Infra"), #infra
    "Wetlands Frame 89 - Invisa-crates": LocData(0x5059, "Wetlands - Infra"), #infra
    "Wetlands Frame 90 - Invisa-crates": LocData(0x505A, "Wetlands - Infra"), #infra
    "Wetlands Frame 91 - Invisa-crates": LocData(0x505B, "Wetlands - Infra"), #infra
    "Wetlands Frame 92 - Invisa-crates": LocData(0x505C, "Wetlands - Infra"), #infra
    "Wetlands Frame 93 - Invisa-crates": LocData(0x505D, "Wetlands - Infra"),#infra
    "Wetlands Frame 94 - Invisa-crates": LocData(0x505E, "Wetlands - Infra"),#infra
    "Faire Dinkum Frame 95 - Town Invisa-crates": LocData(0x505F, "Faire Dinkum - Infra"), #infra
    "Faire Dinkum Frame 96 - Town Invisa-crates": LocData(0x5060, "Faire Dinkum - Infra"), #infra
    "Faire Dinkum Frame 97 - End Invisa-crates": LocData(0x5061, "Faire Dinkum - Infra"), #infra
    "Faire Dinkum Frame 98 - End Invisa-crates": LocData(0x5062, "Faire Dinkum - Infra"), #infra
    "Faire Dinkum Frame 99 - End Invisa-crates": LocData(0x5063, "Faire Dinkum - Infra"), #infra
    "Sulphur Rocks Frame 100 - Start Invisa-crates": LocData(0x5064, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 101 - Start Invisa-crates": LocData(0x5065, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 102 - Start Invisa-crates": LocData(0x5066, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 103 - Start Invisa-crates": LocData(0x5067, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 104 - Start Invisa-crates": LocData(0x5068, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 105 - Start Invisa-crates": LocData(0x5069, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 106 - Start Invisa-crates": LocData(0x506A, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 107 - Start Invisa-crates": LocData(0x506B, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 108 - Start Invisa-crates": LocData(0x506C, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 109 - Start Invisa-crates": LocData(0x506D, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 110 - Snake Eyes Invisa-crates": LocData(0x506E, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 111 - Snake Eyes Invisa-crates": LocData(0x506F, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 112 - Snake Eyes Invisa-crates": LocData(0x5070, "Sulphur Rocks - Infra"), #infra
    "Sulphur Rocks Frame 113 - Snake Eyes Invisa-crates": LocData(0x5071, "Sulphur Rocks - Infra"), #infra
    "Burramudgee Frame 114 - Sewer Grid": LocData(0x5072, "Burramudgee Town - Infra"),
    "Burramudgee Frame 115 - Sewer Grid": LocData(0x5073, "Burramudgee Town - Infra"),
    "Burramudgee Frame 116 - Sewer Grid": LocData(0x5074, "Burramudgee Town - Infra"),
    "Burramudgee Frame 117 - Sewer Grid": LocData(0x5075, "Burramudgee Town - Infra"),
    "Burramudgee Frame 118 - Sewer Grid": LocData(0x5076, "Burramudgee Town - Infra"),
    "Burramudgee Frame 119 - Sewer CrossWay": LocData(0x5077, "Burramudgee Town - Infra"),
    "Burramudgee Frame 120 - Sewer Steve": LocData(0x5078, "Burramudgee Town - Infra"),
    "Burramudgee Frame 121 - Sewer CrossWay": LocData(0x5079, "Burramudgee Town - Infra"),
    "Burramudgee Frame 122 - Sewer CrossWay": LocData(0x507A, "Burramudgee Town - Infra"),
    "Burramudgee Frame 123 - Sewer CrossWay": LocData(0x507B, "Burramudgee Town - Infra"),
    "Burramudgee Frame 124 - Sewer CrossWay Dead End": LocData(0x507C, "Burramudgee Town - Infra"),
    "Burramudgee Frame 125 - Sewer CrossWay Dead End": LocData(0x507D, "Burramudgee Town - Infra"),
    "Burramudgee Frame 126 - Sewer CrossWay Dead End": LocData(0x507E, "Burramudgee Town - Infra"),
    "Burramudgee Frame 127 - Sewer Steve": LocData(0x507F, "Burramudgee Town - Infra"),
    "Burramudgee Frame 128 - Sewer CrossWay": LocData(0x5080, "Burramudgee Town - Infra"),
    "Burramudgee Frame 129 - Sewer CrossWay": LocData(0x5081, "Burramudgee Town - Infra"),
    "Burramudgee Frame 130 - Sewer CrossWay": LocData(0x5082, "Burramudgee Town - Infra"),
    "Burramudgee Frame 131 - Sewer CrossWay": LocData(0x5083, "Burramudgee Town - Infra"),
    "Burramudgee Frame 132 - Sewer CrossWay": LocData(0x5084, "Burramudgee Town - Infra"),
    "Burramudgee Frame 133 - Sewer Entrance": LocData(0x5085, "Burramudgee Town - Infra"),
    "Burramudgee Frame 134 - Sewer Grid": LocData(0x5086, "Burramudgee Town - Infra"),
    "Burramudgee Frame 135 - Sewer Grid": LocData(0x5087, "Burramudgee Town - Infra"),
    "Burramudgee Frame 136 - Sewer Steve": LocData(0x5088, "Burramudgee Town - Infra"),
    "Burramudgee Frame 137 - Sewer Grid": LocData(0x5089, "Burramudgee Town - Infra"),
    "Burramudgee Frame 138 - HQ Balcony Boxes": LocData(0x508A, "Burramudgee HQ"),
    "Burramudgee Frame 139 - HQ Balcony Boxes": LocData(0x508B, "Burramudgee HQ"),
    "Burramudgee Frame 140 - HQ Balcony Boxes": LocData(0x508C, "Burramudgee HQ"),
    "Burramudgee Frame 141 - HQ Balcony Boxes": LocData(0x508D, "Burramudgee HQ"),
    "Burramudgee Frame 142 - HQ Balcony Boxes": LocData(0x508E, "Burramudgee HQ"),
    "Burramudgee Frame 143 - HQ Balcony Boxes": LocData(0x508F, "Burramudgee HQ"),
    "Burramudgee Frame 144 - HQ Balcony Boxes": LocData(0x5090, "Burramudgee HQ"),
    "Burramudgee Frame 145 - HQ Balcony Boxes": LocData(0x5091, "Burramudgee HQ"),
    "Burramudgee Frame 146 - HQ Balcony Boxes": LocData(0x5092, "Burramudgee HQ"),
    "Burramudgee Frame 147 - HQ Balcony Boxes": LocData(0x5093, "Burramudgee HQ"),
    "Burramudgee Frame 148 - HQ Balcony Boxes": LocData(0x5094, "Burramudgee HQ"),
    "Burramudgee Frame 149 - HQ Balcony Boxes": LocData(0x5095, "Burramudgee HQ"),
    "Burramudgee Frame 150 - HQ Balcony Boxes": LocData(0x5096, "Burramudgee HQ"),
    "Burramudgee Frame 151 - HQ Balcony Boxes": LocData(0x5097, "Burramudgee HQ"),
    "Burramudgee Frame 152 - HQ Balcony Boxes": LocData(0x5098, "Burramudgee HQ"),
    "Burramudgee Frame 153 - HQ Warparang Tutorial": LocData(0x5099, "Burramudgee HQ"),#Smasharang
    "Burramudgee Frame 154 - HQ Warparang Tutorial": LocData(0x509A, "Burramudgee HQ"),#Smasharang
    "Burramudgee Frame 155 - HQ Warparang Tutorial": LocData(0x509B, "Burramudgee HQ"),#Smasharang
    "Burramudgee Frame 156 - HQ Hanger Boxes": LocData(0x509C, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 157 - HQ Hanger Boxes": LocData(0x509D, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 158 - HQ Hanger Boxes": LocData(0x509E, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 159 - HQ Roof Box": LocData(0x509F, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 160 - HQ Roof Box": LocData(0x50A0, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 161 - HQ Roof Box": LocData(0x50A1, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 162 - HQ Roof Box": LocData(0x50A2, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 163 - HQ Roof Box": LocData(0x50A3, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 164 - HQ Meeting Room Box": LocData(0x50A4, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 165 - HQ Meeting Room Box": LocData(0x50A5, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 166 - HQ Meeting Room Box": LocData(0x50A6, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 167 - HQ Meeting Room Box": LocData(0x50A7, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 168 - HQ Meeting Room Box": LocData(0x50A8, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 169 - HQ Hanger Boxes": LocData(0x50A9, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 170 - HQ Hanger Boxes": LocData(0x50AA, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 171 - HQ Hanger Boxes": LocData(0x50AB, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 172 - HQ Hanger Boxes": LocData(0x50AC, "Burramudgee HQ - Crates"),#Smasharang
    "Burramudgee Frame 173 - HQ Hanger Boxes": LocData(0x50AD, "Burramudgee HQ - Crates"),#Smasharang
    "Sulphur Rocks Frame 174 - Start": LocData(0x50AE, "Sulphur Rocks"),
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

    if world.options.barrier_unlock.value == 0:
        complete_mission_dict["Beat Patchy"] = LocData(None, "Patchy", 980)
        complete_mission_dict["Beat Fluffy"] = LocData(None, "Fluffy's Fortress", 981)
        complete_mission_dict["Beat Buster"] = LocData(None, "Buster the Nanobot Boss", 982)
    return complete_mission_dict

mission_dict: Dict[str, LocData] = {
    "Metal Menace": LocData(0x6d000001, "Outback Oasis", 1),
    "Explosive Cargo": LocData(0x6d000002, "Lake Burramudgee", 2), #didnt get set to 5+
    "Boss Cass Bust-Up": LocData(None, "Cass' Run", 83), #0x6d000053
    "Haunted Hassle": LocData(0x6d000004, "Burramudgee Town", 4), #infrarang
    "Tree Rescue": LocData(0x6d000005, "Burramudgee Town", 5),
    "Crouching Birrel, Hidden Squeaver": LocData(0x6d000006, "SR - Min Min Plains", 6),

    "Currawong Jail Break": LocData(0x6d000054, "Menu", 84),
    "Dennis Dash": LocData(0x6d000009, "Never Never", 9),# need requirements removed
    "Rocky Road": LocData(0x6d00000a, "Never Never", 10), # need requirements removed
    "Lava Chill Out": LocData(0x6d00000b, "Never Never", 11), #thermo, lash, OR frosty # need requirements removed
    "Canopy Capers": LocData(0x6d00000c, "Frill Neck Forest", 12),
    "Croc Stock Pile": LocData(0x6d00000d, "Muddy Bottom", 13), #didnt send
    "Fire Fight": LocData(0x6d00000e, "Fire Fight", 14),
    "Truck Tragedy": LocData(0x6d000010, "SR - Truck Tragedy", 16), #lifter bunyip
    "Plutonium Panic": LocData(0x6d000011, "SR - Plutonium Panic", 17),
    "Need A Spare": LocData(0x6d000012, "SR - Dusty Barrows", 18),
    # "TEXT_MISSION_19_DESC": LocData(0x6d000013, "", 19),
    "King Squeaver and Birrel Hood": LocData(0x6d000014, "SR - King Squeaver", 20),
    # "TEXT_MISSION_21_DESC": LocData(0x6d000015, "", 21),
    "Musical Mommy": LocData(0x6d000018, "Never Never", 24), #needs requirements removed
    "Tourist Trap": LocData(0x6d000019, "Faire Dinkum", 25),
    "Crocodile Chaos": LocData(0x6d00001a, "Wetlands", 26),
    # "TEXT_MISSION_27_DESC": LocData(0x6d00001b, "", 27),
    "Sheep Dip": LocData(0x6d00001c, "Old Stony Creek", 28), #doesnt send
    # "Danger Lab": LocData(0x6d00001d, "", 29),
    # "TEXT_MISSION_30_DESC": LocData(0x6d00001e, "", 30),
    # "TEXT_MISSION_31_DESC": LocData(0x6d00001f, "", 31),
    # "TEXT_MISSION_32_DESC": LocData(0x6d000020, "", 32),
    "Dennis Freeway": LocData(0x6d000021, "Dennis Freeway", 33), #didnt update
    "Teeter Tottering Inferno": LocData(0x6d000022, "Sulphur Rocks", 34), #
    # "Up the Creek": LocData(0x6d000023, "", 35),
    "Grindstone Cowboy": LocData(0x6d000024, "Sulphur Rocks", 36),
    "Volcano Rescue": LocData(0x6d000025, "MountBoom End", 37), #thermo
    "Bush Fire": LocData(0x6d000026, "Bush Fire", 38), #thermo
    "Truck Stop": LocData(0x6d000027, "SR - Truck Stop", 39), #stupid long mission #lifter bunyip
    "Sea Lab": LocData(0x6d000028, "Beach Sub", 40), #sub bunyip
    "Grub Grab": LocData(0x6d000029, "SR - Wobbygon Bay", 41), #talk to dennis sunscreen
    "Big Bang": LocData(0x6d00002a, "SR - Min Min Mining", 42),

    # "TEXT_MISSION_44_DESC": LocData(0x6d00002c, "", 44),
    "Snake Eyes": LocData(0x6d00002e, "Sulphur Rocks", 46),
    "Hidden Danger": LocData(0x6d00002f, "Burramudgee Town", 47), #infrarang
    # "TEXT_MISSION_48_DESC": LocData(0x6d000030, "", 48),
    # "Chopper Challenge": LocData(0x6d000031, "", 49),
    # "TEXT_MISSION_50_DESC": LocData(0x6d000032, "", 50),
    # "TEXT_MISSION_51_DESC": LocData(0x6d000033, "", 51),
    "Oil Rig Fire": LocData(0x6d000034, "Oil Rig", 52), #done before buster
    "Freeway Training Grounds": LocData(0x6d000035, "Freeway Training Grounds", 53), #didnt count
    "Beach Training Grounds": LocData(0x6d000036, "Beach Training Grounds", 54),
    "Ripper Nipper": LocData(0x6d000037, "SR - Wobbygon Bay", 55), #sunscreen
    # "Frill Attack": LocData(0x6d000038, "", 56), does not exist
    # "TEXT_MISSION_57_DESC": LocData(0x6d000039, "", 57),
    # "TEXT_MISSION_58_DESC": LocData(0x6d00003a, "", 58),
    "Attack of the 50 Foot Squeaver": LocData(0x6d00003b, "SR - 50 Foot Squeaver", 59),

    # "TEXT_MISSION_61_DESC": LocData(0x6d00003d, "", 61),
    # "Mech Mayhem": LocData(0x6d00003e, "", 62),
    # "TEXT_MISSION_63_DESC": LocData(0x6d00003f, "", 63),
    "Deep Sea Scare": LocData(0x6d000040, "Deep Sea Scare", 64), #didnt show, save rex sub bunyip
    # "TEXT_MISSION_65_DESC": LocData(0x6d000041, "", 65),
    # "TEXT_MISSION_66_DESC": LocData(0x6d000042, "", 66),
    # "TEXT_MISSION_67_DESC": LocData(0x6d000043, "", 67),

    # "TEXT_MISSION_69_DESC": LocData(0x6d000045, "", 69),
    "Killer Koala": LocData(0x6d000046, "Burramudgee Town", 70),
    # "TEXT_MISSION_71_DESC": LocData(0x6d000047, "", 71),
    # "TEXT_MISSION_72_DESC": LocData(0x6d000048, "", 72),
    # "TEXT_MISSION_73_DESC": LocData(0x6d000049, "", 73),
    # "TEXT_MISSION_74_DESC": LocData(0x6d00004a, "", 74),
    # "TEXT_MISSION_75_DESC": LocData(0x6d00004b, "", 75),
    # "TEXT_MISSION_76_DESC": LocData(0x6d00004c, "", 76),
    # "TEXT_MISSION_77_DESC": LocData(0x6d00004d, "", 77),
    # "TEXT_MISSION_78_DESC": LocData(0x6d00004e, "", 78),
    # "TEXT_MISSION_79_DESC": LocData(0x6d00004f, "", 79),
    "Near Freeway Julius Training": LocData(0x6d000058, "SR - Freeway Training Grounds", 88), # nned sr - traing freeway
    "Bush Rescue Training Program": LocData(0x6d000055, "Burramudgee HQ", 85), #
    "That's A Croc": LocData(0x6d000062, "Burramudgee Town", 98),
    "Patchy": LocData(0x6d000050, "Patchy", 80),
    "Fluffy": LocData(0x6d000051, "Fluffy's Fortress", 81),
    "Buster the Nanobot Boss": LocData(0x6d000052, "Buster the Nanobot Boss", 82),

    #99 is see julius
    #mission 86 is get into car
    #patchy is m980
    # is m981
    #nano is m982
    #mission 100 spawns warp flower at sly
    #mission 371 gate 1 MountBoom
    #mission 373 is warperang spot button
    #mission 372 is gate

}



sign_dict: Dict[str, LocData] = {
    # "sign sanity": 0x00 #sanity
}

full_location_dict: Dict[str, LocData] = {**shop_location_dict,
                                          **platinum_cog_dict,
                                          **kromium_orb_dict,
                                          **bilby_dict,
                                          **steve_dict,
                                          **disguised_frill_dict,
                                          **picture_frame_dict,
                                          **mission_dict,
                                          **race_dict}