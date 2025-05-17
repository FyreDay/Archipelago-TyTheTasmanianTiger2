from typing import NamedTuple, Optional, Dict

from BaseClasses import Location


class Ty2Location(Location):
    game: str = "Ty the Tasmanian Tiger 2"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1

def create_ty2_locations(world):
    all_locations ={**shop_location_dict, **platinum_cog_dict, **kromium_orb_dict, **bilby_dict, **mission_dict}
    if world.options.frill_sanity.value:
        all_locations.update(disguised_frill_dict)
    if world.options.steve_sanity.value:
        all_locations.update(steve_dict)
    if world.options.frame_sanity.value:
        all_locations.update(steve_dict)
    return all_locations

shop_location_dict = {
    "Rang Shop 1": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 2": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 3": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 4": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 5": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 6": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 7": LocData(0x00, "Burramudgee Town"),
    "Rang Shop 8": LocData(0x00, "Burramudgee Town"),
    "Sly's Shack 1": LocData(0x00, "SR - sly"),
    "Sly's Shack 2": LocData(0x00, "SR - sly"),
    "Sly's Shack 3": LocData(0x00, "SR - sly"),
    "Sly's Shack 4": LocData(0x00, "SR - sly"),
    "Sly's Shack 5": LocData(0x00, "SR - sly"),
    "Sly's Shack 6": LocData(0x00, "SR - sly"),
    "Sly's Shack 7": LocData(0x00, "SR - sly"),
    "Sly's Shack 8": LocData(0x00, "SR - sly"),
    "Sly's Shack 9": LocData(0x00, "SR - sly"),
    "Sly's Shack 10": LocData(0x00, "SR - sly"),
    "Sly's Shack 11": LocData(0x00, "SR - sly"),
    "Trader Bob's 1": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's 2": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's 3": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's 4": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's 5": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 1": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 2": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 3": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 4": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 5": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 6": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 7": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 8": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 9": LocData(0x00, "Burramudgee Town"),
    "Trader Bob's Cog 10": LocData(0x00, "Burramudgee Town"),
    "Madam Mopoke's 1": LocData(0x00, "Burramudgee Town"),
    "Madam Mopoke's 2": LocData(0x00, "Burramudgee Town"),
    "Madam Mopoke's 3": LocData(0x00, "Burramudgee Town"),

}

platinum_cog_dict: Dict[str, LocData] = {
    "Platinum Cog 0": LocData(0x00, "Never Never"),
    "Platinum Cog 1": LocData(0x00, "Outback Oasis"), #smasharang
    "Platinum Cog 2": LocData(0x00, "Outback Oasis"),
    "Platinum Cog 3": LocData(0x00, "Outback Oasis"), #smasharang
    "Platinum Cog 4": LocData(0x00, "Outback Oasis"),
    "Platinum Cog 5": LocData(0x00, "Never Never"), #smasharang
    "Platinum Cog 6": LocData(0x00, "Never Never"),
    "Platinum Cog 7": LocData(0x00, "Never Never"),
    "Platinum Cog 8": LocData(0x00, "Never Never"),
    "Platinum Cog 9": LocData(0x00, "Never Never"),
    "Platinum Cog 10": LocData(0x00, "Never Never"),
    "Platinum Cog 11": LocData(0x00, "Never Never"),#thermo, lash, OR frosty
    "Platinum Cog 12": LocData(0x00, "Never Never"),
    "Platinum Cog 13": LocData(0x00, "Never Never"),
    "Platinum Cog 14": LocData(0x00, "Never Never"),
    "Platinum Cog 15": LocData(0x00, "Never Never"),
    "Platinum Cog 16": LocData(0x00, "Never Never"), #infra
    "Platinum Cog 17": LocData(0x00, "Never Never"), #lasharang
    "Platinum Cog 18": LocData(0x00, "Never Never"),
    "Platinum Cog 19": LocData(0x00, "Never Never"), #smasharang
    "Platinum Cog 20": LocData(0x00, "Faire Dinkum"), #smasharang
    "Platinum Cog 21": LocData(0x00, "Faire Dinkum"),
    "Platinum Cog 22": LocData(0x00, "Faire Dinkum"),
    "Platinum Cog 23": LocData(0x00, "Sulfur rocks"), #frosty
    "Platinum Cog 24": LocData(0x00, "Sulfur rocks"), #lifter bunyip key
    "Platinum Cog 25": LocData(0x00, "Sulfur rocks"),
    "Platinum Cog 26": LocData(0x00, "Sulfur rocks"), #lasharang
    "Platinum Cog 27": LocData(0x00, "Sulfur rocks"),
    "Platinum Cog 28": LocData(0x00, "Sulfur rocks"),
    "Platinum Cog 29": LocData(0x00, "Sulfur rocks"),
    "Platinum Cog 30": LocData(0x00, "Sulfur rocks"),
    "Platinum Cog 31": LocData(0x00, "Sulfur rocks"), #warparang
    "Platinum Cog 32": LocData(0x00, "Burramudgee Town"),
    "Platinum Cog 33": LocData(0x00, "Burramudgee Town"),
    "Platinum Cog 34": LocData(0x00, "Burramudgee Town"),
    "Platinum Cog 35": LocData(0x00, "Cass' Run"),
    "Platinum Cog 36": LocData(0x00, "Frill neck"),
    "Platinum Cog 37": LocData(0x00, "Mount Boom"),#warparang #thermo
    "Platinum Cog 38": LocData(0x00, "Mount Boom"), #thermo
    "Platinum Cog 39": LocData(0x00, "Mount Boom"),#warparang #thermo
    "Platinum Cog 40": LocData(0x00, "Wetlands"),
    "Platinum Cog 41": LocData(0x00, "Wetlands"), #smasharang
    "Platinum Cog 42": LocData(0x00, "Wetlands"),
    "Platinum Cog 43": LocData(0x00, "Wetlands"),
    "Platinum Cog 44": LocData(0x00, "Wetlands web area"), #flamerang
    "Platinum Cog 45": LocData(0x00, "Wetlands"),
    "Platinum Cog 46": LocData(0x00, "SR - Beach"),
    "Platinum Cog 47": LocData(0x00, "SR - Beach"),
    "Platinum Cog 48": LocData(0x00, "SR - Beach"),
    "Platinum Cog 49": LocData(0x00, "Burramudgee HQ"), #infra
}

kromium_orb_dict: Dict[str, LocData] = {
    "Chromium Orb 0": LocData(0x00, "Burramudgee Town"),#lasharang
    "Chromium Orb 1": LocData(0x00, "Burramudgee Town"),
    "Chromium Orb 2": LocData(0x00, "Sulfur rocks"), #lasharang
    "Chromium Orb 3": LocData(0x00, "Sulfur rocks"), #lasharang #frostyrang
    "Chromium Orb 4": LocData(0x00, "Sulfur rocks"),
    "Chromium Orb 5": LocData(0x00, "SR- Sulfur rocks"),
    "Chromium Orb 6": LocData(0x00, "Mount Boom"), #thermo
    "Chromium Orb 7": LocData(0x00, "Mount Boom"),#warparang #thermo smash
    "Chromium Orb 8": LocData(0x00, "SR - Beach"),
    "Chromium Orb 9": LocData(0x00, "Outback Oasis"), #smasharang
    "Chromium Orb 10": LocData(0x00, "SR - Sly"),
    "Chromium Orb 11": LocData(0x00, "Outback Oasis"),
    "Chromium Orb 12": LocData(0x00, "Sulfur rocks"),
    "Chromium Orb 13": LocData(0x00, "Sulfur rocks"), #infra
    "Chromium Orb 14": LocData(0x00, "Sulfur rocks"), #infra
    "Chromium Orb 15": LocData(0x00, "Never Never"), #smasharang
    "Chromium Orb 16": LocData(0x00, "Never Never"), #lasharang
    "Chromium Orb 17": LocData(0x00, "Never Never"),
    "Chromium Orb 18": LocData(0x00, "Never Never"),
    "Chromium Orb 19": LocData(0x00, "Never Never"),
    "Chromium Orb 20": LocData(0x00, "Never Never"),
    "Chromium Orb 21": LocData(0x00, "Never Never"),
    "Chromium Orb 22": LocData(0x00, "Wetlands"), #lasharang
    "Chromium Orb 23": LocData(0x00, "Frill neck"),
    "Chromium Orb 24": LocData(0x00, "Burramudgee Town"),
    "Chromium Orb 25": LocData(0x00, "Sulfur rocks"), #lasharang
    "Chromium Orb 26": LocData(0x00, "Faire Dinkum"),
    "Chromium Orb 27": LocData(0x00, "Faire Dinkum"), #smasharang
    "Chromium Orb 28": LocData(0x00, "Faire Dinkum"),
    "Chromium Orb 29": LocData(0x00, "SR - Beach"),
} #what is the orb at freeway

bilby_dict: Dict[str, LocData] = {
    "Bilby 0": LocData(0x00, "Outback Oasis"), #smasharang
    "Bilby 1": LocData(0x00, "Outback Oasis"),
    "Bilby 2": LocData(0x00, "Outback Oasis"),
    "Bilby 3": LocData(0x00, "Never Never"),
    "Bilby 4": LocData(0x00, "Never Never"),#thermo, lash, OR frosty
    "Bilby 5": LocData(0x00, "Never Never"),
    "Bilby 6": LocData(0x00, "Never Never"),
    "Bilby 7": LocData(0x00, "Faire Dinkum"),
    "Bilby 8": LocData(0x00, "Faire Dinkum"),
    "Bilby 9": LocData(0x00, "Faire Dinkum"),
    "Bilby 10": LocData(0x00, "Sulfur rocks"),
    "Bilby 11": LocData(0x00, "Sulfur rocks"),
    "Bilby 12": LocData(0x00, "Sulfur rocks"),
    "Bilby 13": LocData(0x00, "Sulfur rocks"),
    "Bilby 14": LocData(0x00, "Sulfur rocks"),
    "Bilby 15": LocData(0x00, "Faire Dinkum"), #(infra)
    "Bilby 16": LocData(0x00, "Frill neck"), #lasharang - possible without
    "Bilby 17": LocData(0x00, "Frill neck"),
    "Bilby 18": LocData(0x00, "Mount Boom"), #lasharang #thermo
    "Bilby 19": LocData(0x00, "Mount Boom"), #warparang #thermo
    "Bilby 20": LocData(0x00, "Wetlands"),
    "Bilby 21": LocData(0x00, "Wetlands"), #flamerang
    "Bilby 22": LocData(0x00, "Wetlands web area"), #flamerang
    "Bilby 23": LocData(0x00, "Burramudgee HQ"),
    "Bilby 24": LocData(0x00, "Burramudgee HQ"),
    "Bilby 25": LocData(0x00, "Burramudgee HQ"),    #dennis freeway #warparang
    "Bilby 26": LocData(0x00, "Burramudgee HQ"),
    "Bilby 27": LocData(0x00, "Burramudgee HQ"), #optional frostyrang
    "Bilby 28": LocData(0x00, "SR - Beach"),
    "Bilby 29": LocData(0x00, "SR - Beach"),
}

disguised_frill_dict: Dict[str, LocData] = {
    "Disguised Frill 0": LocData(0x00, "Outback Oasis"), #smasharang
    "Disguised Frill 1": LocData(0x00, "Outback Oasis"),
    "Disguised Frill 2": LocData(0x00, "Outback Oasis"),
    "Disguised Frill 3": LocData(0x00, "Never Never"),
    "Disguised Frill 4": LocData(0x00, "Never Never"),
    "Disguised Frill 5": LocData(0x00, "Never Never"),
    "Disguised Frill 6": LocData(0x00, "Wetlands"),
    "Disguised Frill 7": LocData(0x00, "Wetlands"),
    "Disguised Frill 8": LocData(0x00, "Faire Dinkum"),
    "Disguised Frill 9": LocData(0x00, "Sulfur rocks"), #infra
    "Disguised Frill 10": LocData(0x00, "Sulfur rocks"),
    "Disguised Frill 11": LocData(0x00, "Sulfur rocks"),#lasharang, not needed
    "Disguised Frill 12": LocData(0x00, "Burramudgee Town"),
    "Disguised Frill 13": LocData(0x00, "Burramudgee Town"),
    "Disguised Frill 14": LocData(0x00, "Dennis Freeway"),
    "Disguised Frill 15": LocData(0x00, "Outback Oasis"),
    "Disguised Frill 16": LocData(0x00, "Past patchy"),
    "Disguised Frill 17": LocData(0x00, "Lake Barramugee"), #tnt mission
    "Disguised Frill 18": LocData(0x00, "SR - Frill neck"),
    "Disguised Frill 19": LocData(0x00, "Broken down truck"),
    "Disguised Frill 20": LocData(0x00, "SR - Never Never"),
    "Disguised Frill 21": LocData(0x00, "Sheep Dip"),
    "Disguised Frill 22": LocData(0x00, "Frill neck"),
    "Disguised Frill 23": LocData(0x00, "Mount Boom"),
    "Disguised Frill 24": LocData(0x00, "Mount Boom end"),
}

steve_dict: Dict[str, LocData] = {
    "Steve 0": LocData(0x00, "SR - Sly"),
    "Steve 1": LocData(0x00, "Sewer"),
    "Steve 2": LocData(0x00, "Outback Oasis"), #REQUIRES INFRA OR CAMERA OR
    "Steve 3": LocData(0x00, "Sulfur rocks"),
    "Steve 4": LocData(0x00, "Mount Boom"), #thermo
    "Steve 5": LocData(0x00, "SR - Training north of dennis"),
    "Steve 6": LocData(0x00, "Never Never"), #thermo
    "Steve 7": LocData(0x00, "Wetlands"),
    "Steve 8": LocData(0x00, "SR - Frill neck"),
    "Steve 9": LocData(0x00, "SR - Beach"),
}

picture_frame_dict: Dict[str, LocData] = {
    "Picture Frame 0": LocData(0x00, "Outback Oasis"), #warparang
    "Picture Frame 1": LocData(0x00, "Outback Oasis"),#warparang
    "Picture Frame 2": LocData(0x00, "Outback Oasis"),#warparang
    "Picture Frame 3": LocData(0x00, "Never Never"),
    "Picture Frame 4": LocData(0x00, "Never Never"), #lasharang
    "Picture Frame 5": LocData(0x00, "Never Never"),
    "Picture Frame 6": LocData(0x00, "Never Never"), #thermo OR lash OR frosty
    "Picture Frame 7": LocData(0x00, "Never Never"),
    "Picture Frame 8": LocData(0x00, "Never Never"),
    "Picture Frame 9": LocData(0x00, "Never Never"),
    "Picture Frame 10": LocData(0x00, "Never Never"),
    "Picture Frame 11": LocData(0x00, "Never Never"),
    "Picture Frame 12": LocData(0x00, "Never Never"), #smasharang
    "Picture Frame 13": LocData(0x00, "Never Never"), #infra
    "Picture Frame 14": LocData(0x00, "Never Never"),#infra
    "Picture Frame 15": LocData(0x00, "Never Never"),#infra
    "Picture Frame 16": LocData(0x00, "Never Never"),#infra
    "Picture Frame 17": LocData(0x00, "Never Never"),#infra
    "Picture Frame 18": LocData(0x00, "Wetlands tree"),#warparang
    "Picture Frame 19": LocData(0x00, "Wetlands tree"),#warparang
    "Picture Frame 20": LocData(0x00, "Wetlands tree"),#warparang
    "Picture Frame 21": LocData(0x00, "Wetlands tree"),#warparang
    "Picture Frame 22": LocData(0x00, "Wetlands tree"), #warparang
    "Picture Frame 23": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 24": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 25": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 26": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 27": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 28": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 29": LocData(0x00, "Faire Dinkum"),
    "Picture Frame 30": LocData(0x00, "Faire Dinkum"), #smasharang
    "Picture Frame 31": LocData(0x00, "Faire Dinkum"), #smasharang
    "Picture Frame 32": LocData(0x00, "Sulfur rocks"),
    "Picture Frame 33": LocData(0x00, "Sulfur rocks"),
    "Picture Frame 34": LocData(0x00, "Sulfur rocks"),
    "Picture Frame 35": LocData(0x00, "Sulfur rocks"),#lasharang, not needed
    "Picture Frame 36": LocData(0x00, "Sulfur rocks"), #lasharang, not needed
    "Picture Frame 37": LocData(0x00, "Sulfur rocks"),#lasharang, not needed
    "Picture Frame 38": LocData(0x00, "Sulfur rocks"),
    "Picture Frame 39": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 40": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 41": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 42": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 43": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 44": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 45": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 46": LocData(0x00, "Frill neck"),
    "Picture Frame 47": LocData(0x00, "Frill neck"),
    "Picture Frame 48": LocData(0x00, "Frill neck"),
    "Picture Frame 49": LocData(0x00, "Frill neck"),
    "Picture Frame 50": LocData(0x00, "Frill neck"),
    "Picture Frame 51": LocData(0x00, "Frill neck"),
    "Picture Frame 52": LocData(0x00, "Frill neck"),
    "Picture Frame 53": LocData(0x00, "Frill neck"),
    "Picture Frame 54": LocData(0x00, "Frill neck"),
    "Picture Frame 55": LocData(0x00, "Frill neck"),
    "Picture Frame 56": LocData(0x00, "Frill neck"),
    "Picture Frame 57": LocData(0x00, "Frill neck"),
    "Picture Frame 58": LocData(0x00, "Frill neck"),
    "Picture Frame 59": LocData(0x00, "Frill neck"),
    "Picture Frame 60": LocData(0x00, "Frill neck"),
    "Picture Frame 61": LocData(0x00, "Mount Boom"),
    "Picture Frame 62": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 63": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 64": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 65": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 66": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 67": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 68": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 69": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 70": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 71": LocData(0x00, "Outback Oasis"), #infra
    "Picture Frame 72": LocData(0x00, "Never Never"), #infra
    "Picture Frame 73": LocData(0x00, "Never Never"),#infra
    "Picture Frame 74": LocData(0x00, "Never Never"),#infra
    "Picture Frame 75": LocData(0x00, "Never Never"),#infra
    "Picture Frame 76": LocData(0x00, "Never Never"),#infra
    "Picture Frame 77": LocData(0x00, "Never Never"), #infra
    "Picture Frame 78": LocData(0x00, "Never Never"), #infra
    "Picture Frame 79": LocData(0x00, "Never Never"), #infra
    "Picture Frame 80": LocData(0x00, "Never Never"), #infra
    "Picture Frame 81": LocData(0x00, "Never Never"), #infra
    "Picture Frame 82": LocData(0x00, "Never Never"),#infra
    "Picture Frame 83": LocData(0x00, "Never Never"),#infra
    "Picture Frame 84": LocData(0x00, "Never Never"),#infra
    "Picture Frame 85": LocData(0x00, "Never Never"),#infra
    "Picture Frame 86": LocData(0x00, "Never Never"),#infra
    "Picture Frame 87": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 88": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 89": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 90": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 91": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 92": LocData(0x00, "Wetlands"), #infra
    "Picture Frame 93": LocData(0x00, "Wetlands"),#infra
    "Picture Frame 94": LocData(0x00, "Wetlands"),#infra
    "Picture Frame 95": LocData(0x00, "Faire Dinkum"), #infra
    "Picture Frame 96": LocData(0x00, "Faire Dinkum"), #infra
    "Picture Frame 97": LocData(0x00, "Faire Dinkum"), #infra
    "Picture Frame 98": LocData(0x00, "Faire Dinkum"), #infra
    "Picture Frame 99": LocData(0x00, "Faire Dinkum"), #infra
    "Picture Frame 100": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 101": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 102": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 103": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 104": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 105": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 106": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 107": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 108": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 109": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 110": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 111": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 112": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 113": LocData(0x00, "Sulfur rocks"), #infra
    "Picture Frame 114": LocData(0x00, "Sewer"),
    "Picture Frame 115": LocData(0x00, "Sewer"),
    "Picture Frame 116": LocData(0x00, "Sewer"),
    "Picture Frame 117": LocData(0x00, "Sewer"),
    "Picture Frame 118": LocData(0x00, "Sewer"),
    "Picture Frame 119": LocData(0x00, "Sewer"),
    "Picture Frame 120": LocData(0x00, "Sewer"),
    "Picture Frame 121": LocData(0x00, "Sewer"),
    "Picture Frame 122": LocData(0x00, "Sewer"),
    "Picture Frame 123": LocData(0x00, "Sewer"),
    "Picture Frame 124": LocData(0x00, "Sewer"),
    "Picture Frame 125": LocData(0x00, "Sewer"),
    "Picture Frame 126": LocData(0x00, "Sewer"),
    "Picture Frame 127": LocData(0x00, "Sewer"),
    "Picture Frame 128": LocData(0x00, "Sewer"),
    "Picture Frame 129": LocData(0x00, "Sewer"),
    "Picture Frame 130": LocData(0x00, "Sewer"),
    "Picture Frame 131": LocData(0x00, "Sewer"),
    "Picture Frame 132": LocData(0x00, "Sewer"),
    "Picture Frame 133": LocData(0x00, "Sewer"),
    "Picture Frame 134": LocData(0x00, "Sewer"),
    "Picture Frame 135": LocData(0x00, "Sewer"),
    "Picture Frame 136": LocData(0x00, "Sewer"),
    "Picture Frame 137": LocData(0x00, "Sewer"),
    "Picture Frame 138": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 139": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 140": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 141": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 142": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 143": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 144": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 145": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 146": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 147": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 148": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 149": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 150": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 151": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 152": LocData(0x00, "Burramudgee HQ"),
    "Picture Frame 153": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 154": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 155": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 156": LocData(0x00, "Burramudgee HQ"), #smashrang
    "Picture Frame 157": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 158": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 159": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 160": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 161": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 162": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 163": LocData(0x00,"Burramudgee HQ"),#smashrang
    "Picture Frame 164": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 165": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 166": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 167": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 168": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 169": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 170": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 171": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 172": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 173": LocData(0x00, "Burramudgee HQ"),#smashrang
    "Picture Frame 174": LocData(0x00, "Sulfur rocks"),
}

mission_dict: Dict[str, LocData] = {
    "750 Metal Menace": LocData(0x00, "", 1),
    "Explosive Cargo": LocData(0x00, "", 2), #didnt get set to 5+
    "Boss Cass Bust-Up": LocData(0x00, "", 83),
    "Haunted Hassle": LocData(0x00, "Burramudgee Town", 4), #infrarang
    "Tree Rescue": LocData(0x00, "Burramudgee Town", 5),
    "Crouching Birrel, Hidden Squeaver": LocData(0x00, "first ninja", 6),
    "Refinery Run": LocData(0x00, "race", 7), #
    "Currawong Jail Break": LocData(0x00, "", 84),
    "Dennis Dash": LocData(0x00, "Never Never", 9),
    "Rocky Road": LocData(0x00, "Never Never", 10),
    "Lava Chill Out": LocData(0x00, "Never Never", 11), #thermo, lash, OR frosty
    "Canopy Capers": LocData(0x00, "Frill neck", 12),
    "Croc Stock Pile": LocData(0x00, "", 13), #didnt send
    "Fire Fight": LocData(0x00, "", 14),
    "Truck Tragedy": LocData(0x00, "", 16), #lifter bunyip
    "Plutonium Panic": LocData(0x00, "By Never Never", 17),
    "Need A Spare": LocData(0x00, "Past patchy", 18),
    # "TEXT_MISSION_19_DESC": LocData(0x00, "", 19),
    "King Squeaver and Birrel Hood": LocData(0x00, "", 20),
    # "TEXT_MISSION_21_DESC": LocData(0x00, "", 21),
    "Lava Falls": LocData(0x00, "", 22),
    "Hearty Beach": LocData(0x00, "Race", 23),
    "Musical Mommy": LocData(0x00, "Never Never", 24),
    "Tourist Trap": LocData(0x00, "SR - Fairdinkum", 25),
    "Crocodile Chaos": LocData(0x00, "Wetlands", 26),
    # "TEXT_MISSION_27_DESC": LocData(0x00, "", 27),
    "Sheep Dip": LocData(0x00, "", 28), #doesnt send
    "Danger Lab": LocData(0x00, "", 29),
    # "TEXT_MISSION_30_DESC": LocData(0x00, "", 30),
    # "TEXT_MISSION_31_DESC": LocData(0x00, "", 31),
    # "TEXT_MISSION_32_DESC": LocData(0x00, "", 32),
    "Dennis Freeway": LocData(0x00, "", 33), #didnt update
    "Teeter Tottering Inferno": LocData(0x00, "Sulfur rocks", 34), #
    "Up the Creek": LocData(0x00, "", 35),
    "Grindstone Cowboy": LocData(0x00, "Sulfur rocks", 36),
    "Volcano Rescue": LocData(0x00, "", 37), #thermo
    "Bush Fire": LocData(0x00, "", 38),
    "Truck Stop": LocData(0x00, "SR", 39), #stupid long mission #lifter bunyip
    "Sea Lab": LocData(0x00, "", 40),
    "Grub Grab": LocData(0x00, "SR - Beach", 41), #talk to dennis sunscreen
    "Big Bang": LocData(0x00, "", 42),
    "Parrotbeard Cove": LocData(0x00, "SR - Beach", 43),
    # "TEXT_MISSION_44_DESC": LocData(0x00, "", 44),
    "Never Never Road": LocData(0x00, "Race", 45),
    "Snake Eyes": LocData(0x00, "", 46),
    "Hidden Danger": LocData(0x00, "Burramudgee Town", 47), #infrarang
    # "TEXT_MISSION_48_DESC": LocData(0x00, "", 48),
    "Chopper Challenge": LocData(0x00, "", 49),
    # "TEXT_MISSION_50_DESC": LocData(0x00, "", 50),
    # "TEXT_MISSION_51_DESC": LocData(0x00, "", 51),
    "Oil Rig Fire": LocData(0x00, "", 52), #done before buster
    "Training Grounds 1": LocData(0x00, "", 53), #didnt count
    "Training Grounds 2": LocData(0x00, "", 54),
    "Ripper Nipper": LocData(0x00, "SR - Beach", 55), #sunscreen
    "Frill Attack": LocData(0x00, "", 56),
    # "TEXT_MISSION_57_DESC": LocData(0x00, "", 57),
    # "TEXT_MISSION_58_DESC": LocData(0x00, "", 58),
    "Attack of the 50 Foot Squeaver": LocData(0x00, "By never never", 59),
    "Outback Dash": LocData(0x00, "Race", 60),
    # "TEXT_MISSION_61_DESC": LocData(0x00, "", 61),
    "Mech Mayhem": LocData(0x00, "", 62),
    # "TEXT_MISSION_63_DESC": LocData(0x00, "", 63),
    "Deep Sea Scare": LocData(0x00, "", 64), #didnt show, save rex
    # "TEXT_MISSION_65_DESC": LocData(0x00, "", 65),
    # "TEXT_MISSION_66_DESC": LocData(0x00, "", 66),
    # "TEXT_MISSION_67_DESC": LocData(0x00, "", 67),
    "Turbo Track": LocData(0x00, "Race", 68),
    # "TEXT_MISSION_69_DESC": LocData(0x00, "", 69),
    "Killer Koala": LocData(0x00, "", 70),
    # "TEXT_MISSION_71_DESC": LocData(0x00, "", 71),
    # "TEXT_MISSION_72_DESC": LocData(0x00, "", 72),
    # "TEXT_MISSION_73_DESC": LocData(0x00, "", 73),
    # "TEXT_MISSION_74_DESC": LocData(0x00, "", 74),
    # "TEXT_MISSION_75_DESC": LocData(0x00, "", 75),
    # "TEXT_MISSION_76_DESC": LocData(0x00, "", 76),
    # "TEXT_MISSION_77_DESC": LocData(0x00, "", 77),
    # "TEXT_MISSION_78_DESC": LocData(0x00, "", 78),
    # "TEXT_MISSION_79_DESC": LocData(0x00, "", 79),
    "Bush Rescue Training Program": LocData(0x00, "Burramudgee HQ", 85), #
    "That's A Croc": LocData(0x00, "Burramudgee Town", 98),
    "Patchy": LocData(0x00, "", 80),
    "Fluffy": LocData(0x00, "", 81),
    "Buster the Nanobots": LocData(0x00, "", 82),

    #mission 86 is get into car
    #patchy is m980
    # is m981
    #nano is m982
    #mission 100 spawns warp flower at sly
    #mission 371 gate 1 mount boom
    #mission 373 is warprang spot button
    #mission 372 is gate

}

race_dict: Dict[str, LocData] = {
    # "Races": 0x00, #sanity
}

sign_dict: Dict[str, LocData] = {
    # "sign sanity": 0x00 #sanity
}