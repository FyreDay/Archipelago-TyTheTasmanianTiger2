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
    print(f"location length {len(all_locations)}")

    if world.options.frill_sanity.value:
        all_locations.update(disguised_frill_dict)
    if world.options.steve_sanity.value:
        all_locations.update(steve_dict)
    if world.options.frame_sanity.value:
        all_locations.update(picture_frame_dict)

    return all_locations

shop_location_dict = {
"Rang Shop 8": LocData(26, "Burramudgee Town"),# Camerarang
    "Rang Shop 1": LocData(8, "Burramudgee Town"), #frosty
    "Rang Shop 2": LocData(9, "Burramudgee Town"), #flame
    "Rang Shop 3": LocData(10, "Burramudgee Town"), #zappy
    "Rang Shop 4": LocData(12, "Burramudgee Town"), #infra
    "Rang Shop 5": LocData(11, "Burramudgee Town"), #lash
    "Rang Shop 6": LocData(13, "Burramudgee Town"),
    "Rang Shop 7": LocData(14, "Burramudgee Town"),

    "Sly's Shack 1": LocData(17, "SR - Sly"), #freeze
    "Sly's Shack 2": LocData(16, "SR - Sly"), #lava
    "Sly's Shack 3": LocData(15, "SR - Sly"), #multi
    "Sly's Shack 4": LocData(19, "SR - Sly"), #warp
    "Sly's Shack 5": LocData(18, "SR - Sly"), #thunder
    "Sly's Shack 6": LocData(20, "SR - Sly"), #X
    "Sly's Shack 7": LocData(21, "SR - Sly"), #kaboom
    "Sly's Shack 8": LocData(22, "SR - Sly"), #omega
    "Sly's Shack 9": LocData(23, "SR - Sly"), #deadly
    "Sly's Shack 10": LocData(24, "SR - Sly"), #doom
    "Sly's Shack 11": LocData(25, "SR - Sly"), #crafty
    "Trader Bob's 1": LocData(1, "Burramudgee Town"), #lifter
    "Trader Bob's 2": LocData(2, "Burramudgee Town"), #thermo
    "Trader Bob's 3": LocData(59, "Burramudgee Town"), #sub
    "Trader Bob's 4": LocData(77, "Burramudgee Town"), #gold paw
    "Trader Bob's 5": LocData(78, "Burramudgee Town"), #plat paw
    "Trader Bob's Cog 1": LocData(79, "Burramudgee Town"),
    "Trader Bob's Cog 2": LocData(80, "Burramudgee Town"),
    "Trader Bob's Cog 3": LocData(81, "Burramudgee Town"),
    "Trader Bob's Cog 4": LocData(82, "Burramudgee Town"),
    "Trader Bob's Cog 5": LocData(83, "Burramudgee Town"),
    "Trader Bob's Cog 6": LocData(84, "Burramudgee Town"),
    "Trader Bob's Cog 7": LocData(85, "Burramudgee Town"),
    "Trader Bob's Cog 8": LocData(86, "Burramudgee Town"),
    "Trader Bob's Cog 9": LocData(87, "Burramudgee Town"),
    "Trader Bob's Cog 10": LocData(88, "Burramudgee Town"),
    "Madam Mopoke's 1": LocData(5, "Burramudgee Town"),
    "Madam Mopoke's 2": LocData(6, "Burramudgee Town"),
    "Madam Mopoke's 3": LocData(7, "Burramudgee Town"),

}

platinum_cog_dict: Dict[str, LocData] = {
    "Platinum Cog 1": LocData(0x4300, "Never Never"),
    "Platinum Cog 2": LocData(0x4301, "Outback Oasis"), #smasharang
    "Platinum Cog 3": LocData(0x4302, "Outback Oasis"),
    "Platinum Cog 4": LocData(0x4303, "Outback Oasis"), #smasharang
    "Platinum Cog 5": LocData(0x4304, "Outback Oasis"),
    "Platinum Cog 6": LocData(0x4305, "Never Never"), #smasharang
    "Platinum Cog 7": LocData(0x4306, "Never Never"),
    "Platinum Cog 8": LocData(0x4307, "Never Never"),
    "Platinum Cog 9": LocData(0x4308, "Never Never"),
    "Platinum Cog 10": LocData(0x4309, "Never Never"),
    "Platinum Cog 11": LocData(0x430A, "Never Never"),
    "Platinum Cog 12": LocData(0x430B, "Never Never"),#thermo, lash, OR frosty
    "Platinum Cog 13": LocData(0x430C, "Never Never"),
    "Platinum Cog 14": LocData(0x430D, "Never Never"),
    "Platinum Cog 15": LocData(0x430E, "Never Never"),
    "Platinum Cog 16": LocData(0x430F, "Never Never"),
    "Platinum Cog 17": LocData(0x4310, "Never Never"), #infra
    "Platinum Cog 18": LocData(0x4311, "Never Never"), #lasharang
    "Platinum Cog 19": LocData(0x4312, "Never Never"),
    "Platinum Cog 20": LocData(0x4313, "Never Never"), #smasharang
    "Platinum Cog 21": LocData(0x4314, "Faire Dinkum"), #smasharang
    "Platinum Cog 22": LocData(0x4315, "Faire Dinkum"),
    "Platinum Cog 23": LocData(0x4316, "Faire Dinkum"),
    "Platinum Cog 24": LocData(0x4317, "Sulphur Rocks"), #frosty
    "Platinum Cog 25": LocData(0x4318, "Sulphur Rocks"), #lifter bunyip key
    "Platinum Cog 26": LocData(0x4319, "Sulphur Rocks"),
    "Platinum Cog 27": LocData(0x431A, "Sulphur Rocks"), #lasharang
    "Platinum Cog 28": LocData(0x431B, "Sulphur Rocks"),
    "Platinum Cog 29": LocData(0x431C, "Sulphur Rocks"),
    "Platinum Cog 30": LocData(0x431D, "Sulphur Rocks"),
    "Platinum Cog 31": LocData(0x431E, "Sulphur Rocks"),
    "Platinum Cog 32": LocData(0x431F, "Sulphur Rocks"), #warparang
    "Platinum Cog 33": LocData(0x4320, "Burramudgee Town"),
    "Platinum Cog 34": LocData(0x4321, "Burramudgee Town"),
    "Platinum Cog 35": LocData(0x4322, "Burramudgee Town"),
    "Platinum Cog 36": LocData(0x4323, "Cass' Run"),
    "Platinum Cog 37": LocData(0x4324, "Frill Neck Forest"),
    "Platinum Cog 38": LocData(0x4325, "MountBoom"),#warparang #thermo
    "Platinum Cog 39": LocData(0x4326, "MountBoom"), #thermo
    "Platinum Cog 40": LocData(0x4327, "MountBoom"),#warparang #thermo
    "Platinum Cog 41": LocData(0x4328, "Wetlands"),
    "Platinum Cog 42": LocData(0x4329, "Wetlands"), #smasharang
    "Platinum Cog 43": LocData(0x432A, "Wetlands"),
    "Platinum Cog 44": LocData(0x432B, "Wetlands"),
    "Platinum Cog 45": LocData(0x432C, "Wetlands"), #flamerang optional
    "Platinum Cog 46": LocData(0x432D, "Wetlands"),
    "Platinum Cog 47": LocData(0x432E, "SR - Beach"),
    "Platinum Cog 48": LocData(0x432F, "SR - Beach"),
    "Platinum Cog 49": LocData(0x4330, "SR - Beach"),
    "Platinum Cog 50": LocData(0x4331, "Burramudgee HQ - Infra"),
}

kromium_orb_dict: Dict[str, LocData] = {
    "Kromium Orb 1": LocData(0x4B00, "Burramudgee Town"),#lasharang
    "Kromium Orb 2": LocData(0x4B01, "Burramudgee Town"),
    "Kromium Orb 3": LocData(0x4B02, "Sulphur Rocks"), #lasharang
    "Kromium Orb 4": LocData(0x4B03, "Sulphur Rocks"), #lasharang #frostyrang
    "Kromium Orb 5": LocData(0x4B04, "Sulphur Rocks"),
    "Kromium Orb 6": LocData(0x4B05, "SR- Sulphur Rocks"),
    "Kromium Orb 7": LocData(0x4B06, "MountBoom"), #thermo
    "Kromium Orb 8": LocData(0x4B07, "MountBoom"),#warperang #thermo smash
    "Kromium Orb 9": LocData(0x4B08, "SR - Beach"),
    "Kromium Orb 10": LocData(0x4B09, "Outback Oasis"), #smasharang
    "Kromium Orb 11": LocData(0x4B0A, "SR - Sly"),
    "Kromium Orb 12": LocData(0x4B0B, "Outback Oasis"),
    "Kromium Orb 13": LocData(0x4B0C, "Sulphur Rocks"),
    "Kromium Orb 14": LocData(0x4B0D, "Sulphur Rocks"), #infra
    "Kromium Orb 15": LocData(0x4B0E, "Sulphur Rocks"), #infra
    "Kromium Orb 16": LocData(0x4B0F, "Never Never"), #smasharang
    "Kromium Orb 17": LocData(0x4B10, "Never Never"), #lasharang
    "Kromium Orb 18": LocData(0x4B11, "Never Never"),
    "Kromium Orb 19": LocData(0x4B12, "Never Never"),
    "Kromium Orb 20": LocData(0x4B13, "Never Never"),
    "Kromium Orb 21": LocData(0x4B14, "Never Never"),
    "Kromium Orb 22": LocData(0x4B15, "Never Never"),
    "Kromium Orb 23": LocData(0x4B16, "Wetlands"), #lasharang
    "Kromium Orb 24": LocData(0x4B17, "Frill Neck Forest"),
    "Kromium Orb 25": LocData(0x4B18, "Burramudgee Town"),
    "Kromium Orb 26": LocData(0x4B19, "Sulphur Rocks"), #lasharang
    "Kromium Orb 27": LocData(0x4B1A, "Faire Dinkum"),
    "Kromium Orb 28": LocData(0x4B1B, "Faire Dinkum"), #smasharang
    "Kromium Orb 29": LocData(0x4B1C, "Faire Dinkum"),
    "Kromium Orb 30": LocData(0x4B1D, "SR - Beach"),
} #what is the orb at freeway

bilby_dict: Dict[str, LocData] = {
    "Bilby 1": LocData(0x4200, "Outback Oasis"), #smasharang
    "Bilby 2": LocData(0x4201, "Outback Oasis"),
    "Bilby 3": LocData(0x4202, "Outback Oasis"),
    "Bilby 4": LocData(0x4203, "Never Never"),
    "Bilby 5": LocData(0x4204, "Never Never"),#thermo, lash, OR frosty
    "Bilby 6": LocData(0x4205, "Never Never"),
    "Bilby 7": LocData(0x4206, "Never Never"),
    "Bilby 8": LocData(0x4207, "Faire Dinkum"),
    "Bilby 9": LocData(0x4208, "Faire Dinkum"),
    "Bilby 10": LocData(0x4209, "Faire Dinkum"),
    "Bilby 11": LocData(0x420A, "Sulphur Rocks"),
    "Bilby 12": LocData(0x420B, "Sulphur Rocks"),
    "Bilby 13": LocData(0x420C, "Sulphur Rocks"),
    "Bilby 14": LocData(0x420D, "Sulphur Rocks"),
    "Bilby 15": LocData(0x420E, "Sulphur Rocks"),
    "Bilby 16": LocData(0x420F, "Faire Dinkum"), #(infra)
    "Bilby 17": LocData(0x4210, "Frill Neck Forest"), #lasharang - possible without
    "Bilby 18": LocData(0x4211, "Frill Neck Forest"),
    "Bilby 19": LocData(0x4212, "MountBoom"), #lasharang and thermo - MountBoom Beginning
    "Bilby 20": LocData(0x4213, "MountBoom"), #warparang #thermo
    "Bilby 21": LocData(0x4214, "Wetlands"),
    "Bilby 22": LocData(0x4215, "Wetlands"), #flamerang
    "Bilby 23": LocData(0x4216, "Wetlands"), #flamerang optional
    "Bilby 24": LocData(0x4217, "Burramudgee HQ"),
    "Bilby 25": LocData(0x4218, "Burramudgee HQ"),
    "Bilby 26": LocData(0x4219, "SR - Dennis Freeway"),    #dennis freeway #warperang
    "Bilby 27": LocData(0x421A, "Burramudgee HQ"),
    "Bilby 28": LocData(0x421B, "Burramudgee HQ"), #optional frostyrang
    "Bilby 29": LocData(0x421C, "SR - Beach"),
    "Bilby 30": LocData(0x421D, "SR - Beach"),
}


disguised_frill_dict: Dict[str, LocData] = {
    "Disguised Frill 1": LocData(0x4600, "Outback Oasis"), #smasharang
    "Disguised Frill 2": LocData(0x4601, "Outback Oasis"),
    "Disguised Frill 3": LocData(0x4602, "Outback Oasis"),
    "Disguised Frill 4": LocData(0x4603, "Never Never"),
    "Disguised Frill 5": LocData(0x4604, "Never Never"),
    "Disguised Frill 6": LocData(0x4605, "Never Never"),
    "Disguised Frill 7": LocData(0x4606, "Wetlands"),
    "Disguised Frill 8": LocData(0x4607, "Wetlands"),
    "Disguised Frill 9": LocData(0x4608, "Faire Dinkum"),
    "Disguised Frill 10": LocData(0x4609, "Sulphur Rocks"),
    "Disguised Frill 11": LocData(0x460A, "Sulphur Rocks"),
    "Disguised Frill 12": LocData(0x460B, "Sulphur Rocks"),#lasharang, not needed
    "Disguised Frill 13": LocData(0x460C, "Burramudgee Town"),
    "Disguised Frill 14": LocData(0x460D, "Burramudgee Town"),
    "Disguised Frill 15": LocData(0x460E, "Dennis Freeway"),
    "Disguised Frill 16": LocData(0x460F, "Outback Oasis"),
    "Disguised Frill 17": LocData(0x460010, "SR - Cul De Sac"),
    "Disguised Frill 18": LocData(0x460011, "SR - Explosive Cargo"),
    "Disguised Frill 19": LocData(0x460012, "SR - Frill Neck Forest"),
    "Disguised Frill 20": LocData(0x460013, "SR - Truck Tragedy"),
    "Disguised Frill 21": LocData(0x460014, "SR - Never Never"), #didnt send
    "Disguised Frill 22": LocData(0x460015, "SR - Sheep Dip"),
    "Disguised Frill 23": LocData(0x460016, "Frill Neck Forest"),
    "Disguised Frill 24": LocData(0x460017, "MountBoom Start"),
    "Disguised Frill 25": LocData(0x460018, "MountBoom End"),
}

steve_dict: Dict[str, LocData] = {
    "Steve 1": LocData(0x5300, "SR - Sly"),
    "Steve 2": LocData(0x5301, "Sewer"),
    "Steve 3": LocData(0x5302, "Outback Oasis"), #Lash
    "Steve 4": LocData(0x5303, "Sulphur Rocks"),
    "Steve 5": LocData(0x5304, "MountBoom"), #thermo
    "Steve 6": LocData(0x5305, "SR - Training north of dennis"),
    "Steve 7": LocData(0x5306, "Never Never"), #thermo
    "Steve 8": LocData(0x5307, "Wetlands"),
    "Steve 9": LocData(0x5308, "SR - Frill Neck Forest"),
    "Steve 10": LocData(0x5309, "SR - Beach"),
}

picture_frame_dict: Dict[str, LocData] = {
    "Picture Frame 0": LocData(0x5000, "Outback Oasis"), #warparang
    "Picture Frame 1": LocData(0x5001, "Outback Oasis"),#warparang
    "Picture Frame 2": LocData(0x5002, "Outback Oasis"),#warparang
    "Picture Frame 3": LocData(0x5003, "Never Never"),
    "Picture Frame 4": LocData(0x5004, "Never Never"), #lasharang
    "Picture Frame 5": LocData(0x5005, "Never Never"),
    "Picture Frame 6": LocData(0x5006, "Never Never"), #thermo OR lash OR frosty
    "Picture Frame 7": LocData(0x5007, "Never Never"),
    "Picture Frame 8": LocData(0x5008, "Never Never"),
    "Picture Frame 9": LocData(0x5009, "Never Never"),
    "Picture Frame 10": LocData(0x500A, "Never Never"),
    "Picture Frame 11": LocData(0x500B, "Never Never"),
    "Picture Frame 12": LocData(0x500C, "Never Never"), #smasharang
    "Picture Frame 13": LocData(0x500D, "Never Never - Infra"), #infra
    "Picture Frame 14": LocData(0x500E, "Never Never - Infra"),#infra
    "Picture Frame 15": LocData(0x500F, "Never Never - Infra"),#infra
    "Picture Frame 16": LocData(0x5010, "Never Never - Infra"),#infra
    "Picture Frame 17": LocData(0x5011, "Never Never - Infra"),#infra
    "Picture Frame 18": LocData(0x5012, "Wetlands Tree"),#warparang
    "Picture Frame 19": LocData(0x5013, "Wetlands Tree"),#warparang
    "Picture Frame 20": LocData(0x5014, "Wetlands Tree"),#warparang
    "Picture Frame 21": LocData(0x5015, "Wetlands Tree"),#warparang
    "Picture Frame 22": LocData(0x5016, "Wetlands Tree"), #warparang
    "Picture Frame 23": LocData(0x5017, "Faire Dinkum"),
    "Picture Frame 24": LocData(0x5018, "Faire Dinkum"),
    "Picture Frame 25": LocData(0x5019, "Faire Dinkum"),
    "Picture Frame 26": LocData(0x501A, "Faire Dinkum"),
    "Picture Frame 27": LocData(0x501B, "Faire Dinkum"),
    "Picture Frame 28": LocData(0x501C, "Faire Dinkum"),
    "Picture Frame 29": LocData(0x501D, "Faire Dinkum"),
    "Picture Frame 30": LocData(0x501E, "Faire Dinkum"), #smasharang
    "Picture Frame 31": LocData(0x501F, "Faire Dinkum"), #smasharang
    "Picture Frame 32": LocData(0x5020, "Sulphur Rocks"),
    "Picture Frame 33": LocData(0x5021, "Sulphur Rocks"),
    "Picture Frame 34": LocData(0x5022, "Sulphur Rocks"),
    "Picture Frame 35": LocData(0x5023, "Sulphur Rocks"),#lasharang, not needed
    "Picture Frame 36": LocData(0x5024, "Sulphur Rocks"), #lasharang, not needed
    "Picture Frame 37": LocData(0x5025, "Sulphur Rocks"),#lasharang, not needed
    "Picture Frame 38": LocData(0x5026, "Sulphur Rocks"),
    "Picture Frame 39": LocData(0x5027, "Burramudgee HQ"),
    "Picture Frame 40": LocData(0x5028, "Burramudgee HQ"),
    "Picture Frame 41": LocData(0x5029, "Burramudgee HQ"),
    "Picture Frame 42": LocData(0x502A, "Burramudgee HQ"),
    "Picture Frame 43": LocData(0x502B, "Burramudgee HQ"),
    "Picture Frame 44": LocData(0x502C, "Burramudgee HQ"),
    "Picture Frame 45": LocData(0x502D, "Burramudgee HQ"),
    "Picture Frame 46": LocData(0x502E, "Frill Neck Forest"),
    "Picture Frame 47": LocData(0x502F, "Frill Neck Forest"),
    "Picture Frame 48": LocData(0x5030, "Frill Neck Forest"),
    "Picture Frame 49": LocData(0x5031, "Frill Neck Forest"),
    "Picture Frame 50": LocData(0x5032, "Frill Neck Forest"),
    "Picture Frame 51": LocData(0x5033, "Frill Neck Forest"),
    "Picture Frame 52": LocData(0x5034, "Frill Neck Forest"),
    "Picture Frame 53": LocData(0x5035, "Frill Neck Forest"),
    "Picture Frame 54": LocData(0x5036, "Frill Neck Forest"),
    "Picture Frame 55": LocData(0x5037, "Frill Neck Forest"),
    "Picture Frame 56": LocData(0x5038, "Frill Neck Forest"),
    "Picture Frame 57": LocData(0x5039, "Frill Neck Forest"),
    "Picture Frame 58": LocData(0x503A, "Frill Neck Forest"),
    "Picture Frame 59": LocData(0x503B, "Frill Neck Forest"),
    "Picture Frame 60": LocData(0x503C, "Frill Neck Forest"),
    "Picture Frame 61": LocData(0x503D, "MountBoom End"), #Lasharang
    "Picture Frame 62": LocData(0x503E, "Outback Oasis - Infra"), #infra
    "Picture Frame 63": LocData(0x503F, "Outback Oasis - Infra"), #infra
    "Picture Frame 64": LocData(0x5040, "Outback Oasis - Infra"), #infra
    "Picture Frame 65": LocData(0x5041, "Outback Oasis - Infra"), #infra
    "Picture Frame 66": LocData(0x5042, "Outback Oasis - Infra"), #infra
    "Picture Frame 67": LocData(0x5043, "Outback Oasis - Infra"), #infra
    "Picture Frame 68": LocData(0x5044, "Outback Oasis - Infra"), #infra
    "Picture Frame 69": LocData(0x5045, "Outback Oasis - Infra"), #infra
    "Picture Frame 70": LocData(0x5046, "Outback Oasis - Infra"), #infra
    "Picture Frame 71": LocData(0x5047, "Outback Oasis - Infra"), #infra
    "Picture Frame 72": LocData(0x5048, "Never Never - Infra"), #infra
    "Picture Frame 73": LocData(0x5049, "Never Never - Infra"),#infra
    "Picture Frame 74": LocData(0x504A, "Never Never - Infra"),#infra
    "Picture Frame 75": LocData(0x504B, "Never Never - Infra"),#infra
    "Picture Frame 76": LocData(0x504C, "Never Never - Infra"),#infra
    "Picture Frame 77": LocData(0x504D, "Never Never - Infra"), #infra
    "Picture Frame 78": LocData(0x504E, "Never Never - Infra"), #infra
    "Picture Frame 79": LocData(0x504F, "Never Never - Infra"), #infra
    "Picture Frame 80": LocData(0x5050, "Never Never - Infra"), #infra
    "Picture Frame 81": LocData(0x5051, "Never Never - Infra"), #infra
    "Picture Frame 82": LocData(0x5052, "Never Never - Infra"),#infra
    "Picture Frame 83": LocData(0x5053, "Never Never - Infra"),#infra
    "Picture Frame 84": LocData(0x5054, "Never Never - Infra"),#infra
    "Picture Frame 85": LocData(0x5055, "Never Never - Infra"),#infra
    "Picture Frame 86": LocData(0x5056, "Never Never - Infra"),#infra
    "Picture Frame 87": LocData(0x5057, "Wetlands - Infra"), #infra
    "Picture Frame 88": LocData(0x5058, "Wetlands - Infra"), #infra
    "Picture Frame 89": LocData(0x5059, "Wetlands - Infra"), #infra
    "Picture Frame 90": LocData(0x505A, "Wetlands - Infra"), #infra
    "Picture Frame 91": LocData(0x505B, "Wetlands - Infra"), #infra
    "Picture Frame 92": LocData(0x505C, "Wetlands - Infra"), #infra
    "Picture Frame 93": LocData(0x505D, "Wetlands - Infra"),#infra
    "Picture Frame 94": LocData(0x505E, "Wetlands - Infra"),#infra
    "Picture Frame 95": LocData(0x505F, "Faire Dinkum - Infra"), #infra
    "Picture Frame 96": LocData(0x5060, "Faire Dinkum - Infra"), #infra
    "Picture Frame 97": LocData(0x5061, "Faire Dinkum - Infra"), #infra
    "Picture Frame 98": LocData(0x5062, "Faire Dinkum - Infra"), #infra
    "Picture Frame 99": LocData(0x5063, "Faire Dinkum - Infra"), #infra
    "Picture Frame 100": LocData(0x5064, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 101": LocData(0x5065, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 102": LocData(0x5066, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 103": LocData(0x5067, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 104": LocData(0x5068, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 105": LocData(0x5069, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 106": LocData(0x506A, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 107": LocData(0x506B, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 108": LocData(0x506C, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 109": LocData(0x506D, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 110": LocData(0x506E, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 111": LocData(0x506F, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 112": LocData(0x5070, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 113": LocData(0x5071, "Sulphur Rocks - Infra"), #infra
    "Picture Frame 114": LocData(0x5072, "Burramudgee Town - Infra"),
    "Picture Frame 115": LocData(0x5073, "Burramudgee Town - Infra"),
    "Picture Frame 116": LocData(0x5074, "Burramudgee Town - Infra"),
    "Picture Frame 117": LocData(0x5075, "Burramudgee Town - Infra"),
    "Picture Frame 118": LocData(0x5076, "Burramudgee Town - Infra"),
    "Picture Frame 119": LocData(0x5077, "Burramudgee Town - Infra"),
    "Picture Frame 120": LocData(0x5078, "Burramudgee Town - Infra"),
    "Picture Frame 121": LocData(0x5079, "Burramudgee Town - Infra"),
    "Picture Frame 122": LocData(0x507A, "Burramudgee Town - Infra"),
    "Picture Frame 123": LocData(0x507B, "Burramudgee Town - Infra"),
    "Picture Frame 124": LocData(0x507C, "Burramudgee Town - Infra"),
    "Picture Frame 125": LocData(0x507D, "Burramudgee Town - Infra"),
    "Picture Frame 126": LocData(0x507E, "Burramudgee Town - Infra"),
    "Picture Frame 127": LocData(0x507F, "Burramudgee Town - Infra"),
    "Picture Frame 128": LocData(0x5080, "Burramudgee Town - Infra"),
    "Picture Frame 129": LocData(0x5081, "Burramudgee Town - Infra"),
    "Picture Frame 130": LocData(0x5082, "Burramudgee Town - Infra"),
    "Picture Frame 131": LocData(0x5083, "Burramudgee Town - Infra"),
    "Picture Frame 132": LocData(0x5084, "Burramudgee Town - Infra"),
    "Picture Frame 133": LocData(0x5085, "Burramudgee Town - Infra"),
    "Picture Frame 134": LocData(0x5086, "Burramudgee Town - Infra"),
    "Picture Frame 135": LocData(0x5087, "Burramudgee Town - Infra"),
    "Picture Frame 136": LocData(0x5088, "Burramudgee Town - Infra"),
    "Picture Frame 137": LocData(0x5089, "Burramudgee Town - Infra"),
    "Picture Frame 138": LocData(0x508A, "Burramudgee HQ"),
    "Picture Frame 139": LocData(0x508B, "Burramudgee HQ"),
    "Picture Frame 140": LocData(0x508C, "Burramudgee HQ"),
    "Picture Frame 141": LocData(0x508D, "Burramudgee HQ"),
    "Picture Frame 142": LocData(0x508E, "Burramudgee HQ"),
    "Picture Frame 143": LocData(0x508F, "Burramudgee HQ"),
    "Picture Frame 144": LocData(0x5090, "Burramudgee HQ"),
    "Picture Frame 145": LocData(0x5091, "Burramudgee HQ"),
    "Picture Frame 146": LocData(0x5092, "Burramudgee HQ"),
    "Picture Frame 147": LocData(0x5093, "Burramudgee HQ"),
    "Picture Frame 148": LocData(0x5094, "Burramudgee HQ"),
    "Picture Frame 149": LocData(0x5095, "Burramudgee HQ"),
    "Picture Frame 150": LocData(0x5096, "Burramudgee HQ"),
    "Picture Frame 151": LocData(0x5097, "Burramudgee HQ"),
    "Picture Frame 152": LocData(0x5098, "Burramudgee HQ"),
    "Picture Frame 153": LocData(0x5099, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 154": LocData(0x509A, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 155": LocData(0x509B, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 156": LocData(0x509C, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 157": LocData(0x509D, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 158": LocData(0x509E, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 159": LocData(0x509F, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 160": LocData(0x50A0, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 161": LocData(0x50A1, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 162": LocData(0x50A2, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 163": LocData(0x50A3, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 164": LocData(0x50A4, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 165": LocData(0x50A5, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 166": LocData(0x50A6, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 167": LocData(0x50A7, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 168": LocData(0x50A8, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 169": LocData(0x50A9, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 170": LocData(0x50AA, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 171": LocData(0x50AB, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 172": LocData(0x50AC, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 173": LocData(0x50AD, "Burramudgee HQ - Crates"),#Smasharang
    "Picture Frame 174": LocData(0x50AE, "Sulphur Rocks"),
}

mission_dict: Dict[str, LocData] = {
    # "750 Metal Menace": LocData(0x6d000001, "", 1), is this used
    "Explosive Cargo": LocData(0x6d000002, "SR - Explosive Cargo", 2), #didnt get set to 5+
    "Boss Cass Bust-Up": LocData(None, "Cass' Run", 83), #0x6d000053
    "Haunted Hassle": LocData(0x6d000004, "Burramudgee Town", 4), #infrarang
    "Tree Rescue": LocData(0x6d000005, "Burramudgee Town", 5),
    "Crouching Birrel, Hidden Squeaver": LocData(0x6d000006, "SR - Min Min Plains", 6),
    "Refinery Run": LocData(0x6d000007, "SR - Refinery Run", 7), #
    "Currawong Jail Break": LocData(0x6d000054, "Menu", 84),
    "Dennis Dash": LocData(0x6d000009, "Never Never", 9),# need requirements removed
    "Rocky Road": LocData(0x6d00000a, "Never Never", 10), # need requirements removed
    "Lava Chill Out": LocData(0x6d00000b, "Never Never", 11), #thermo, lash, OR frosty # need requirements removed
    "Canopy Capers": LocData(0x6d00000c, "Frill Neck Forest", 12),
    "Croc Stock Pile": LocData(0x6d00000d, "SR - Croc Stock Pile", 13), #didnt send
    "Fire Fight": LocData(0x6d00000e, "Fire Fight", 14),
    "Truck Tragedy": LocData(0x6d000010, "SR - Truck Tragedy", 16), #lifter bunyip
    "Plutonium Panic": LocData(0x6d000011, "SR - Plutonium Panic", 17),
    "Need A Spare": LocData(0x6d000012, "SR - Cul De Sac", 18),
    # "TEXT_MISSION_19_DESC": LocData(0x6d000013, "", 19),
    "King Squeaver and Birrel Hood": LocData(0x6d000014, "SR - King Squeaver", 20),
    # "TEXT_MISSION_21_DESC": LocData(0x6d000015, "", 21),
    "Lava Falls": LocData(0x6d000016, "SR - Lava Falls", 22),
    "Hearty Beach": LocData(0x6d000017, "SR - Hearty Beach", 23),
    "Musical Mommy": LocData(0x6d000018, "Never Never", 24), #needs requirements removed
    "Tourist Trap": LocData(0x6d000019, "Faire Dinkum", 25),
    "Crocodile Chaos": LocData(0x6d00001a, "Wetlands", 26),
    # "TEXT_MISSION_27_DESC": LocData(0x6d00001b, "", 27),
    "Sheep Dip": LocData(0x6d00001c, "Sheep Dip", 28), #doesnt send
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
    "Grub Grab": LocData(0x6d000029, "SR - Beach", 41), #talk to dennis sunscreen
    "Big Bang": LocData(0x6d00002a, "SR - Min Min Mining", 42),
    "Parrotbeard Cove": LocData(0x6d00002b, "SR - Beach", 43),
    # "TEXT_MISSION_44_DESC": LocData(0x6d00002c, "", 44),
    "Never Never Road": LocData(0x6d00002d, "SR - Never Never Road", 45),
    "Snake Eyes": LocData(0x6d00002e, "Sulphur Rocks", 46),
    "Hidden Danger": LocData(0x6d00002f, "Burramudgee Town", 47), #infrarang
    # "TEXT_MISSION_48_DESC": LocData(0x6d000030, "", 48),
    # "Chopper Challenge": LocData(0x6d000031, "", 49),
    # "TEXT_MISSION_50_DESC": LocData(0x6d000032, "", 50),
    # "TEXT_MISSION_51_DESC": LocData(0x6d000033, "", 51),
    "Oil Rig Fire": LocData(0x6d000034, "Oil Rig", 52), #done before buster
    "Training Grounds 03": LocData(0x6d000035, "Training Grounds 03", 53), #didnt count
    "Training Grounds 08": LocData(0x6d000036, "Training Grounds 08", 54),
    "Ripper Nipper": LocData(0x6d000037, "SR - Beach", 55), #sunscreen
    # "Frill Attack": LocData(0x6d000038, "", 56), does not exist
    # "TEXT_MISSION_57_DESC": LocData(0x6d000039, "", 57),
    # "TEXT_MISSION_58_DESC": LocData(0x6d00003a, "", 58),
    "Attack of the 50 Foot Squeaver": LocData(0x6d00003b, "SR - 50 Foot Squeaver", 59),
    "Outback Dash": LocData(0x6d00003c, "SR - Outback Dash", 60),
    # "TEXT_MISSION_61_DESC": LocData(0x6d00003d, "", 61),
    # "Mech Mayhem": LocData(0x6d00003e, "", 62),
    # "TEXT_MISSION_63_DESC": LocData(0x6d00003f, "", 63),
    "Deep Sea Scare": LocData(0x6d000040, "Deep Sea Scare", 64), #didnt show, save rex sub bunyip
    # "TEXT_MISSION_65_DESC": LocData(0x6d000041, "", 65),
    # "TEXT_MISSION_66_DESC": LocData(0x6d000042, "", 66),
    # "TEXT_MISSION_67_DESC": LocData(0x6d000043, "", 67),
    "Turbo Track": LocData(0x6d000044, "SR - Turbo Track", 68),
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
    "Bush Rescue Training Program": LocData(0x6d000055, "Burramudgee HQ", 85), #
    "That's A Croc": LocData(0x6d000062, "Burramudgee Town", 98),
    "Patchy": LocData(0x6d0003d4, "Patchy", 80),
    "Fluffy": LocData(0x6d0003d5, "Fluffy's Fortress", 81),
    "Buster the Nanobot Boss": LocData(0x6d0003d6, "Buster the Nanobot Boss", 82),

    #chromium orbs still increase
    # MISSION 87 IS A MISSED TRAINING GROUNDS
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

race_dict: Dict[str, LocData] = {
    # "Races": 0x00, #sanity
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
                                          **mission_dict}