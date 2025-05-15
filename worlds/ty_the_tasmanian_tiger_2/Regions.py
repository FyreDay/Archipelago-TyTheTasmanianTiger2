from typing import Dict

from BaseClasses import Region, Location, Entrance

ty1_levels: Dict[str, str] = {
    "z1": "Burramudgee HQ",
    "z2": "Burramudgee Town",
    "z3": "Currawong",
    "z4": "Southern Rivers",
    "a1": "Outback Oasis",
    "a2": "She'll Be Right",
    "a3": "Faire Dinkum",
    "a4": "Patchy",
    "b1": "No Man Groves",
    "b2": "Cassopolis Now",
    "b3": "Whoop Whoop Walkabout",
    "b4": "Fluffy's Fortress",
    "c2": "Cassopolis Redux",
    "c3": "Dinky Dino Saurus",
    "c4": "Buster the Nanobot Boss",
    "e1": "Cass' Run",
    # "e4": "Final Battle",

    "m2": "Explosive Cargo",
    "m8": "Surfing Safari",
    "m12": "Canopy Capers",
    "m13": "Croc Stock Pile",
    "m14": "Fire Fight",
    "m15": "Pirate Panic",
    "m27": "Ripper Rita",
    "m28": "Sheep Dip",
    "m33": "Dennis Freeway",
    "m40": "Sea Lab",
    "m49": "Chopper Challenge",
    "m50": "Robot Bug Battle",
    "m64": "Deep Sea Scare",
    "m69": "Surf's Up",

    "m35": "Up The Creek",
    "m52": "Oil Rig Fire",
    "m56": "Attack of the RoboCrabs",

    # "r1": "Refinery Run ",
    # "r2": "Lava Falls",
    # "r3": "Hearty Beach Races",
    # "r4": "Parrotbeard Cove",
    # "r6": "Never Never Road",
    # "r7": "Outback Dash",
    # "r9": "Turbo Track",

}

def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)
    region.locations.append(location)

def create_locations(world, region, loc_dict):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, key, data.code)

def create_region(world, name: str, location_dict):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region, location_dict)
    world.multiworld.regions.append(region)
    return region

def create_ty2_regions(world, location_dict):
    create_region(world, "Menu", location_dict)
    create_region(world, "Burramudgee HQ", location_dict)
    create_region(world, "Currawong", location_dict)
    create_region(world, "Burramudgee HQ - Infra", location_dict)
    create_region(world, "Burramudgee Town", location_dict)
    create_region(world, "Burramudgee Town - Infra", location_dict)
    create_region(world, "Outback Oasis", location_dict)
    create_region(world, "Outback Oasis - Infra", location_dict)
    create_region(world, "She'll Be Right", location_dict)
    create_region(world, "She'll Be Right - Infra", location_dict)
    create_region(world, "Faire Dinkum", location_dict)
    create_region(world, "Faire Dinkum - Infra", location_dict)
    create_region(world, "Patchy", location_dict)
    create_region(world, "No Man Groves", location_dict)
    create_region(world, "No Man Groves - Infra", location_dict)
    create_region(world, "Cassopolis Now", location_dict)
    create_region(world, "Cassopolis Now - Infra", location_dict)
    create_region(world, "Whoop Whoop Walkabout", location_dict)
    create_region(world, "Whoop Whoop Walkabout - Infra", location_dict)
    create_region(world, "Fluffy's Fortress", location_dict)
    create_region(world, "Cassopolis Redux", location_dict)
    create_region(world, "Cassopolis Redux - Infra", location_dict)
    create_region(world, "Dinky Dino Saurus", location_dict)
    create_region(world, "Dinky Dino Saurus - Infra", location_dict)
    create_region(world, "Buster the Nanobot Boss", location_dict)
    create_region(world, "Cass' Run", location_dict)
    create_region(world, "Southern Rivers", location_dict)
    create_region(world, "SR - Burramudgee Town", location_dict)

def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0) -> Entrance:
    entrance_region = world.get_region(from_name, world.player)
    exit_region = world.get_region(to_name, world.player)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.randomization_group = entrance_group;
    return entrance

def connect_ty2_regions(world):
    connect_regions(world, "Menu", "Burramudgee HQ", "Start", 3)
    connect_regions(world, "Burramudgee HQ", "Cass' Run", "Bush Rescue Plane", 1)
    connect_regions(world, "Burramudgee HQ", "Currawong", "Picture", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee HQ - Infra", "Burramudgee HQ -> Infra", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee Town", "Burramudgee Tunnel")
    connect_regions(world, "Burramudgee Town", "Burramudgee Town - Infra", "Burramudgee Town -> Infra", 1)
    connect_regions(world, "Burramudgee Town", "SR - Burramudgee Town", "SR - Burramudgee Connector")
    connect_regions(world, "Southern Rivers", "SR - Burramudgee Town", "Burramudgee ParkingBay", 1)
    connect_regions(world, "Southern Rivers", "SR - Min Min Plains", "Min Min Plains ParkingBay", 1)
    connect_regions(world, "Southern Rivers", "SR - Training Grounds 03", "Training Grounds 03 ParkingBay", 1) #3688
    connect_regions(world, "SR - Training Grounds 03", "Training Grounds 03", "Training Grounds 03 Connector")
    connect_regions(world, "Southern Rivers", "SR - Dennis Freeway", "Dennis Freeway ParkingBay", 1) #3692
    connect_regions(world, "SR - Dennis Freeway", "Dennis Freeway", "Dennis Freeway Connector")
    connect_regions(world, "Southern Rivers", "SR - Muddy Bottom", "Muddy Bottom ParkingBay", 1)  # 3306
    connect_regions(world, "Southern Rivers", "SR - Training Grounds 08", "Training Grounds 08 ParkingBay", 1)  # 4092
    connect_regions(world, "SR - Training Grounds 08", "Training Grounds 08", "Training Grounds 08 Connector")
    connect_regions(world, "Southern Rivers", "SR - Buster the Nanobot Boss", "Buster the Nanobot Boss ParkingBay", 1)  # 3285
    connect_regions(world, "SR - Buster the Nanobot Boss", "Buster the Nanobot Boss", "Buster the Nanobot Boss Connector")
    connect_regions(world, "Southern Rivers", "SR - Beach", "Beach ParkingBay", 1)  # 3287
    connect_regions(world, "SR - Beach", "Beach Sub", "Beach Mission Sub Connector")
    connect_regions(world, "SR - Beach", "Beach Rex", "Beach Mission Rex Connector")
    connect_regions(world, "Southern Rivers", "SR - r3 ", "r3 ParkingBay", 1)  # 3712
    connect_regions(world, "Southern Rivers", "SR - MountBoom End", "MountBoom End ParkingBay", 1)  # 3735
    connect_regions(world, "SR - MountBoom End", "MountBoom", "MountBoom End Connector")
    connect_regions(world, "Southern Rivers", "SR - MountBoom Start", "MountBoom Start ParkingBay", 1)  # 3694
    connect_regions(world, "SR - MountBoom Start", "MountBoom", "MountBoom Start Connector")
    connect_regions(world, "Southern Rivers", "SR - Frill Neck Forest", "Frill Neck Forest ParkingBay", 1)  # 3693
    connect_regions(world, "SR - Frill Neck Forest", "Frill Neck Forest", "Frill Neck Forest Load Zone")
    connect_regions(world, "Southern Rivers", "SR - Sheep Dip", "Sheep Dip ParkingBay", 1)  # 3292
    connect_regions(world, "SR - Sheep Dip", "Sheep Dip", "Sheep Dip Connector")
    connect_regions(world, "Southern Rivers", "SR - Camping", "Camping ParkingBay", 1)  # 4130
    connect_regions(world, "Southern Rivers", "SR - Oasis", "Oasis ParkingBay", 1)  # 3685
    connect_regions(world, "SR - Oasis", "Outback Oasis", "Oasis Connector")
    connect_regions(world, "Southern Rivers", "SR - r1", "r1 ParkingBay", 1)  # 3687
    connect_regions(world, "Southern Rivers", "SR - Fire Fight", "Fire Fight ParkingBay", 1)  # 3983
    connect_regions(world, "SR - Fire Fight", "Fire Fight", "Fire Fight Connector")
    connect_regions(world, "Southern Rivers", "SR - sly", "sly ParkingBay", 1)  # 3244
    connect_regions(world, "Southern Rivers", "SR - d7", "r7 ParkingBay", 1)  # 3714
    connect_regions(world, "Southern Rivers", "SR - car trouble", "car trouble ParkingBay", 1)  # 3702
    connect_regions(world, "Southern Rivers", "SR - r6", "r6 ParkingBay", 1)  # 3713
    connect_regions(world, "Southern Rivers", "SR - m17", "m17 ParkingBay", 1)  # 3284
    connect_regions(world, "Southern Rivers", "SR - m59", "m59 ParkingBay", 1)  # 3709
    connect_regions(world, "Southern Rivers", "SR - Never Never", "Never Never ParkingBay", 1)  # 3710
    connect_regions(world, "SR - Never Never", "Never Never", "Never Never Connector")
    connect_regions(world, "Southern Rivers", "SR - r2", "r2 ParkingBay", 1)  # 3711
    connect_regions(world, "Southern Rivers", "SR - m42", "m42 ParkingBay", 1)  # 4035
    connect_regions(world, "Southern Rivers", "SR - r9", "r9 ParkingBay", 1)  # 3300
    connect_regions(world, "Southern Rivers", "SR - Patchy", "Patchy ParkingBay", 1)  # 3951
    connect_regions(world, "SR - Patchy", "Patchy", "Patchy Connector")
    connect_regions(world, "Southern Rivers", "SR - m2", "m2 ParkingBay", 1)  # 3686
    connect_regions(world, "SR - m2", "m2", "m2 Connector")
    connect_regions(world, "Southern Rivers", "SR - m38", "m38 ParkingBay", 1)  # 3733
    connect_regions(world, "SR - m38", "m38", "m38 Connector")
    connect_regions(world, "Southern Rivers", "SR - b3", "b3 ParkingBay", 1)  # 3967
    connect_regions(world, "SR - b3", "b3", "b3 Connector")
    connect_regions(world, "Southern Rivers", "SR - m20", "m20 ParkingBay", 1)  # 3690
    connect_regions(world, "Southern Rivers", "SR - M66", "M66 ParkingBay", 1)  # 3691
    connect_regions(world, "SR - m66", "m66", "m66 Connector")
    connect_regions(world, "Southern Rivers", "SR - Faire Dinkum", "Faire Dinkum ParkingBay", 1)  # 3277
    connect_regions(world, "SR - Faire Dinkum", "Faire Dinkum", "Faire Dinkum Connector")
    connect_regions(world, "Southern Rivers", "SR - a5", "a5 ParkingBay", 1)  # 3954
    connect_regions(world, "SR - a5", "a5", "a5 Connector")


# name ParkingBay
#   pos -13993.49 3732.76 11135.69
#   ID 3736 Z4_StartParking
#   vehicleID 100 FOURBIE
#   rot 0.022 0.871 6.270
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 3598 Z2ExitPoint
#   missionID none
#   afterMissionID none
#
# name ParkingBay
#   pos -22219.84 6096.46 -2688.79
#   ID 3689 Z4_M06Parking
#   vehicleID 100 FOURBIE
#   rot 6.270 2.050 6.159
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 4131 Z4_M6TyOut
#   missionID m6
#   afterMissionID m6
#
# name ParkingBay
#   pos -93114.32 10212.45 -15368.73
#   ID 3732 Z4_M39Parking2
#   vehicleID 100 FOURBIE
#   rot 0.153 4.950 0.180
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 4058 Z4_M39TyOut2
#   missionID m39
#   afterMissionID none
#
# name ParkingBay
#   pos -95361.77 9723.55 -1579.37
#   ID 3708 Z4_M39Parking
#   vehicleID 100 FOURBIE
#   rot 5.838 1.225 0.436
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 4057 Z4_M39TyOut1
#   missionID m39
#   afterMissionID none
#
#
# name ParkingBay
#   pos 54745.79 3371.66 45134.44
#   ID 3954 Z4_A5Parking
#   vehicleID 100 FOURBIE
#   rot 5.731 4.118 5.705
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 4050 z4_A5TyOut
#   missionID none
#   afterMissionID none
#
#
#
# name ParkingBay
#   pos 53191.69 2323.19 39256.43
#   ID 3972 Z4_M55Parking
#   vehicleID 100 FOURBIE
#   rot 6.230 3.143 0.108
#   scale 1.000 1.000 1.000
#   zone 1
#   TargetID 4052 z4_m55TyOut
#   missionID m55
#   afterMissionID none
