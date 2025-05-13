from typing import NamedTuple, Optional

from BaseClasses import Location


class Ty2Location(Location):
    game: str = "Ty the Tasmanian Tiger 2"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]

locations = {
    "Platinum Cogs": 0x00,
    "Chromium Orbs": 0x00,
    "Bilbies": 0x00,
    "Disguised Frills": 0x00,  # sanity?
    "Steve": 0x00, #sanity
    "Picture Frames": 0x00, #sanity
    "Mission Complete": 0x00,
    "rang shop Items": 0x00, # randomize cost
    "Sly shop Items": 0x00,
    "Cop shop Items": 0x00, # all cog costs are 3 or randomize based on classification
    "Madam shop Items": 0x00,
    "Races": 0x00, #sanity
    "sign sanity": 0x00 #sanity
}

chromium_orb_dict = {

}