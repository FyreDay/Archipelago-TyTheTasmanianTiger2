from typing import Dict

from BaseClasses import Region, Location, Entrance

ty1_levels: Dict[str, str] = {
    "z1": "Burramudgee HQ",
    "z2": "Burramudgee Town",
    "z3": "Currawong",
    "z4": "Southern Rivers",
    "a1": "Outback Oasis",
    "a2": "Never Never",
    "a3": "Wetlands",
    "a4": "Patchy",
    "a5": "Faire Dinkum",
    # "b2": "Cassopolis Now",
    "b3": "Sulphur Rocks",
    "b4": "Fluffy's Fortress",
    # "c2": "Cassopolis Redux",
    # "c3": "Dinky Dino Saurus",
    "c4": "Buster the Nanobot Boss",
    "e1": "Cass' Run",
    "e4": "Final Battle",

    "m2": "Explosive Cargo",
    # "m8": "Surfing Safari",
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

    "r1": "Refinery Run ",
    "r2": "Lava Falls",
    "r3": "Hearty Beach Races",
    "r4": "Parrotbeard Cove", # in SR - Beach
    "r6": "Never Never Road",
    "r7": "Outback Dash",
    "r9": "Turbo Track",



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
    create_region(world, "Burramudgee HQ - Crates", location_dict)
    create_region(world, "Currawong", location_dict)
    create_region(world, "Burramudgee HQ - Infra", location_dict)
    create_region(world, "Burramudgee Town", location_dict)
    create_region(world, "Burramudgee Town - Infra", location_dict)
    create_region(world, "SR - Burramudgee Town", location_dict)
    create_region(world, "SR - Outback Oasis", location_dict)
    create_region(world, "Outback Oasis", location_dict)
    create_region(world, "Outback Oasis - Infra", location_dict)
    create_region(world, "SR - Never Never", location_dict)
    create_region(world, "Never Never", location_dict)
    create_region(world, "Never Never - Infra", location_dict)
    create_region(world, "SR - Faire Dinkum", location_dict)
    create_region(world, "Faire Dinkum", location_dict)
    create_region(world, "Faire Dinkum - Infra", location_dict)
    create_region(world, "Sulphur Rocks", location_dict)
    create_region(world, "Sulphur Rocks - Infra", location_dict)
    create_region(world, "SR - Wetlands", location_dict)
    create_region(world, "Wetlands", location_dict)
    create_region(world, "Wetlands Tree", location_dict)
    create_region(world, "Wetlands - Infra", location_dict)
    create_region(world, "Fluffy's Fortress", location_dict)
    create_region(world, "SR - Fluffy's Fortress", location_dict)
    create_region(world, "Buster the Nanobot Boss", location_dict)
    create_region(world, "Cass' Run", location_dict)
    create_region(world, "Southern Rivers", location_dict)
    create_region(world, "SR - Min Min Plains", location_dict)
    create_region(world, "SR - Training Grounds 03", location_dict)
    create_region(world, "Training Grounds 03", location_dict)
    create_region(world, "SR - Dennis Freeway", location_dict)
    create_region(world, "Dennis Freeway", location_dict)
    create_region(world, "SR - Croc Stock Pile", location_dict)
    create_region(world, "Croc Stock Pile", location_dict)
    create_region(world, "SR - Muddy Bottom", location_dict)
    create_region(world, "SR - Training Grounds 08", location_dict)
    create_region(world, "Training Grounds 08", location_dict)
    create_region(world, "SR - Oil Rig", location_dict)
    create_region(world, "Oil Rig", location_dict)
    create_region(world, "SR - Beach", location_dict)
    create_region(world, "Beach Sub", location_dict)
    create_region(world, "Deep Sea Scare", location_dict)
    create_region(world, "SR - Lava Falls Race", location_dict)
    create_region(world, "SR - MountBoom End", location_dict)
    create_region(world, "MountBoom", location_dict)
    create_region(world, "MountBoom -> Infra", location_dict)
    create_region(world, "SR - MountBoom Start", location_dict)
    create_region(world, "MountBoom Start", location_dict)
    create_region(world, "MountBoom End", location_dict)
    create_region(world, "SR - Frill Neck Forest", location_dict)
    create_region(world, "Frill Neck Forest", location_dict)
    create_region(world, "Frill Neck Forest - Infra", location_dict)
    create_region(world, "SR - Sheep Dip", location_dict)
    create_region(world, "Sheep Dip", location_dict)
    create_region(world, "SR - Camping", location_dict)
    create_region(world, "SR - Refinery Run", location_dict)
    create_region(world, "SR - Fire Fight", location_dict)
    create_region(world, "Fire Fight", location_dict)
    create_region(world, "SR - Sly", location_dict)
    create_region(world, "SR - Outback Dash", location_dict)
    create_region(world, "SR - Truck Tragedy", location_dict)
    create_region(world, "SR - Never Never Road", location_dict)
    create_region(world, "SR - Plutonium Panic", location_dict)
    create_region(world, "SR - 50 Foot Squeaver", location_dict)
    create_region(world, "SR - Lava Falls", location_dict)
    create_region(world, "SR - Min Min Mining", location_dict)
    create_region(world, "SR - Turbo Track", location_dict)
    create_region(world, "SR - Patchy", location_dict)
    create_region(world, "Patchy", location_dict)
    create_region(world, "SR - Explosive Cargo", location_dict) #m2
    create_region(world, "Explosive Cargo", location_dict)
    create_region(world, "SR - Bush Fire", location_dict)
    create_region(world, "Bush Fire", location_dict)
    create_region(world, "SR - Sulphur Rocks", location_dict)
    create_region(world, "SR - King Squeaver", location_dict)
    create_region(world, "SR - m66", location_dict)
    create_region(world, "m66", location_dict)
    create_region(world, "SR - Hearty Beach", location_dict)
    create_region(world, "SR - Truck Stop", location_dict)
    create_region(world, "SR - Cul De Sac", location_dict)


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.randomization_group = entrance_group
    # if entrance.randomization_group == 0:
    #     world.disconnect_entrance_for_randomization(entrance)
    return entrance

def connect_ty2_regions(world):
    connect_regions(world, "Menu", "Burramudgee HQ",
                    "Start", 3)
    connect_regions(world, "Burramudgee HQ", "Cass' Run",
                    "Bush Rescue Plane", 1)
    connect_regions(world, "Burramudgee HQ", "Currawong",
                    "Picture", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee HQ - Infra",
                    "Burramudgee HQ -> Infra", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee HQ - Crates",
                    "Burramudgee HQ -> Crates", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee Town",
                    "Burramudgee Tunnel")
    connect_regions(world, "Burramudgee Town", "Burramudgee Town - Infra",
                    "Burramudgee Town -> Infra", 1)
    connect_regions(world, "Burramudgee Town", "SR - Burramudgee Town",
                    "Burramudgee Connector")
    connect_regions(world, "SR - Burramudgee Town", "Southern Rivers",
                    "Burramudgee ParkingBay", 1)
    connect_regions(world, "Southern Rivers", "SR - Min Min Plains",
                    "Min Min Plains ParkingBay", 1) #3689
    connect_regions(world, "Southern Rivers", "SR - Training Grounds 03",
                    "Training Grounds 03 ParkingBay", 1) #3688
    connect_regions(world, "SR - Training Grounds 03", "Training Grounds 03",
                    "Training Grounds 03 Connector")
    connect_regions(world, "Southern Rivers", "SR - Dennis Freeway",
                    "Dennis Freeway ParkingBay", 1) #3692
    connect_regions(world, "SR - Dennis Freeway", "Dennis Freeway",
                    "Dennis Freeway Connector")
    connect_regions(world, "Southern Rivers", "SR - Croc Stock Pile",
                    "Croc Stock Pile ParkingBay", 1) #3692
    connect_regions(world, "SR - Croc Stock Pile", "Croc Stock Pile",
                    "Croc Stock Pile Connector")
    connect_regions(world, "Southern Rivers", "SR - Muddy Bottom",
                    "Muddy Bottom ParkingBay", 1)  # 3306
    connect_regions(world, "Southern Rivers", "SR - Training Grounds 08",
                    "Training Grounds 08 ParkingBay", 1)  # 4092
    connect_regions(world, "SR - Training Grounds 08", "Training Grounds 08",
                    "Training Grounds 08 Connector")
    connect_regions(world, "Southern Rivers", "SR - Oil Rig",
                    "Oil Rig ParkingBay", 1)  # 3285
    connect_regions(world, "SR - Oil Rig", "Oil Rig",
                    "Oil Rig Connector")
    connect_regions(world, "Southern Rivers", "SR - Beach",
                    "Beach ParkingBay", 1)  # 3287
    connect_regions(world, "SR - Beach", "Beach Sub",
                    "Beach Mission Sub Connector")
    connect_regions(world, "SR - Beach", "Deep Sea Scare",
                    "Deep Sea Scare Connector")
    connect_regions(world, "Southern Rivers", "SR - Lava Falls Race",
                    "Lava Falls Race ParkingBay", 1)  # 3712
    connect_regions(world, "SR - MountBoom End", "Southern Rivers",
                    "MountBoom End ParkingBay", 1)  # 3735
    connect_regions(world, "MountBoom End", "SR - MountBoom End",
                    "MountBoom End Connector")
    connect_regions(world, "Southern Rivers", "SR - MountBoom Start",
                    "MountBoom Start ParkingBay", 1)  # 3694
    connect_regions(world, "SR - MountBoom Start", "MountBoom Start",
                    "MountBoom Start Connector")
    connect_regions(world, "MountBoom Start", "MountBoom",
                    "MountBoom Start Lava")
    connect_regions(world, "MountBoom", "MountBoom End",
                    "MountBoom End Lava")
    connect_regions(world, "MountBoom", "MountBoom -> Infra",
                    "MountBoom -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Frill Neck Forest",
                    "Frill Neck Forest ParkingBay", 1)  # 3693
    connect_regions(world, "SR - Frill Neck Forest", "Frill Neck Forest",
                    "Frill Neck Forest Load Zone")
    connect_regions(world, "Frill Neck Forest", "Frill Neck Forest - Infra",
                    "Frill Neck Forest -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Sheep Dip",
                    "Sheep Dip ParkingBay", 1)  # 3292
    connect_regions(world, "SR - Sheep Dip", "Sheep Dip",
                    "Sheep Dip Connector")
    connect_regions(world, "Southern Rivers", "SR - Camping",
                    "Camping ParkingBay", 1)  # 4130
    connect_regions(world, "Southern Rivers", "SR - Outback Oasis",
                    "Outback Oasis ParkingBay", 1)  # 3685
    connect_regions(world, "SR - Outback Oasis", "Outback Oasis",
                    "Outback Oasis Connector")
    connect_regions(world, "Outback Oasis", "Outback Oasis - Infra",
                    "Outback Oasis -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Refinery Run",
                    "Refinery Run ParkingBay", 1)  # 3687
    connect_regions(world, "Southern Rivers", "SR - Fire Fight",
                    "Fire Fight ParkingBay", 1)  # 3983
    connect_regions(world, "SR - Fire Fight", "Fire Fight",
                    "Fire Fight Connector")
    connect_regions(world, "Southern Rivers", "SR - Sly",
                    "Sly ParkingBay", 1)  # 3244
    connect_regions(world, "Southern Rivers", "SR - Outback Dash",
                    "Outback Dash ParkingBay", 1)  # 3714
    connect_regions(world, "Southern Rivers", "SR - Truck Tragedy",
                    "Truck Tragedy ParkingBay", 1)   # north 3708  #south 3732
    connect_regions(world, "Southern Rivers", "SR - Never Never Road",
                    "Never Never Road ParkingBay", 1)  # 3713
    connect_regions(world, "Southern Rivers", "SR - Plutonium Panic",
                    "Plutonium Panic ParkingBay", 1)  # 3284
    connect_regions(world, "Southern Rivers", "SR - 50 Foot Squeaver",
                    "50 Foot Squeaver ParkingBay", 1)  # 3709
    connect_regions(world, "Southern Rivers", "SR - Never Never",
                    "Never Never ParkingBay", 1)  # 3710
    connect_regions(world, "SR - Never Never", "Never Never",
                    "Never Never Connector")
    connect_regions(world, "Never Never", "Never Never - Infra",
                    "Never Never -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Lava Falls",
                    "Lava Falls ParkingBay", 1)  # 3711
    connect_regions(world, "Southern Rivers", "SR - Min Min Mining",
                    "Min Min Mining ParkingBay", 1)  # 4035
    connect_regions(world, "Southern Rivers", "SR - Turbo Track",
                    "Turbo Track ParkingBay", 1)  # 3300
    connect_regions(world, "Southern Rivers", "SR - Patchy",
                    "Patchy ParkingBay", 1)  # 3951
    connect_regions(world, "SR - Patchy", "Patchy",
                    "Patchy Connector")
    connect_regions(world, "Southern Rivers", "SR - Explosive Cargo",
                    "Explosive Cargo ParkingBay", 1)  # 3686
    connect_regions(world, "SR - Explosive Cargo", "Explosive Cargo",
                    "Explosive Cargo Connector")
    connect_regions(world, "Southern Rivers", "SR - Bush Fire",
                    "Bush Fire ParkingBay", 1)  # 3733
    connect_regions(world, "SR - Bush Fire", "Bush Fire",
                    "Bush Fire Connector")
    connect_regions(world, "Southern Rivers", "SR - Sulphur Rocks",
                    "Sulphur Rocks ParkingBay", 1)  # 3967
    connect_regions(world, "SR - Sulphur Rocks", "Sulphur Rocks",
                    "Sulphur Rocks Connector")
    connect_regions(world, "Sulphur Rocks", "Sulphur Rocks - Infra",
                    "Sulphur Rocks -> Infra")
    connect_regions(world, "Southern Rivers", "SR - King Squeaver",
                    "King Squeaver ParkingBay", 1)  # 3690 # King Squeaver and Birrel Hood
    connect_regions(world, "Southern Rivers", "SR - m66",
                    "M66 ParkingBay", 1)  # 3691
    connect_regions(world, "SR - m66", "m66",
                    "m66 Connector")
    connect_regions(world, "Southern Rivers", "SR - Faire Dinkum",
                    "Faire Dinkum ParkingBay", 1)  # 3277
    connect_regions(world, "SR - Faire Dinkum", "Faire Dinkum",
                    "Faire Dinkum Connector")
    connect_regions(world, "Faire Dinkum", "Faire Dinkum - Infra",
                    "Faire Dinkum -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Wetlands",
                    "Wetlands ParkingBay", 1)
    connect_regions(world, "SR - Wetlands", "Wetlands",
                    "Wetlands Connector")
    connect_regions(world, "Wetlands", "Wetlands Tree",
                    "Wetlands Teleport", 2)
    connect_regions(world, "Wetlands", "Wetlands - Infra",
                    "Wetlands -> Infra")
    connect_regions(world, "Southern Rivers", "SR - Truck Stop",
                    "Truck Stop ParkingBay")  # 3702
    connect_regions(world, "Southern Rivers", "SR - Cul De Sac",
                    "Cul De Sac ParkingBay")
    connect_regions(world, "Oil Rig", "Buster the Nanobot Boss",
                    "Oil Rig Button", 2)
    connect_regions(world, "Southern Rivers", "SR - Fluffy's Fortress",
                    "Fluffy ParkingBay")
    connect_regions(world, "SR - Fluffy's Fortress", "Fluffy's Fortress",
                    "Fluffy Connector")
    connect_regions(world, "Southern Rivers", "SR - Hearty Beach",
                    "Hearty Beach ParkingBay")


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
