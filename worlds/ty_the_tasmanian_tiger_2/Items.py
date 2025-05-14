from dataclasses import dataclass
from typing import Dict

from BaseClasses import ItemClassification, Item
from typing import Optional


class Ty2Item(Item):
    game: str = "TCG Card Shop Simulator"


@dataclass
class ItemData:
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1

def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    for item_name, item_data in item_dict.items():
        create_item(world, item_name, item_data.classification, item_data.amount)


item_dict: Dict[str, ItemData] = {
    "Lifter Bunyip Key": ItemData(0x1d, ItemClassification.progression),
    "Thermo Extreme Bunyip Key": ItemData(0x1e, ItemClassification.progression),
    "Sub Bunyip Key": ItemData(0x1f   , ItemClassification.progression),
    "Gold Paw": ItemData(0x20, ItemClassification.useful),
    "Platinum Paw": ItemData(0x21, ItemClassification.useful),
    "Missing Persons Map": ItemData(0x22, ItemClassification.useful),
    "Cog Map": ItemData(0x23, ItemClassification.useful),
    "Mysterious Anomalies Map": ItemData(0x24, ItemClassification.useful),


    "Platinum cogs": ItemData(0x00, ItemClassification.progression),
    "Chromium Orbs": ItemData(0x00, ItemClassification.progression),

    "full health": ItemData(0x00, ItemClassification.filler),
    "Opal bags": ItemData(0x00, ItemClassification.filler),



    # "fourbie speed upgrade": ItemData(0x00, ItemClassification.useful),

    "Progressive parking pad": ItemData(0x00, ItemClassification.progression),#option
    "Individual parking pad": ItemData(0x00, ItemClassification.progression),#option
}
def get_rangs(world):
    if world.options.progressive_rangs.value:
        return progressive_rangs
    else:
        return individual_rangs

individual_rangs: Dict[str, ItemData] = {
    "Boomerang": ItemData(0x00, ItemClassification.useful),
    "Multirang": ItemData(0x01, ItemClassification.useful),
    "Flamerang": ItemData(0x02, ItemClassification.progression),
    "Lavarang": ItemData(0x03, ItemClassification.progression),
    "Frostyrang": ItemData(0x04, ItemClassification.progression),
    "Freezerang": ItemData(0x05, ItemClassification.progression),
    "Zappyrang": ItemData(0x06, ItemClassification.progression),
    "Thunderang": ItemData(0x07, ItemClassification.progression),
    "Lasharang": ItemData(0x08, ItemClassification.progression),
    "Warperang": ItemData(0x09, ItemClassification.progression),
    "Infrarang": ItemData(0x0a, ItemClassification.progression),
    "X-Rang": ItemData(0x0b, ItemClassification.progression),
    "Smasharang": ItemData(0x0c, ItemClassification.progression),
    "Kaboomarang": ItemData(0x0d, ItemClassification.progression),
    "Megarang": ItemData(0xe, ItemClassification.useful),
    "Omegarang": ItemData(0x0f, ItemClassification.useful),
    "Deadlyrang": ItemData(0x10, ItemClassification.progression),
    "Doomerang": ItemData(0x11, ItemClassification.progression),
    # "Aquarang": ItemData(0x12, ItemClassification.progression),
    # "?": ItemData(0x13, ItemClassification.progression),
    "Craftyrang": ItemData(0x14, ItemClassification.useful),
    "Camerarang": ItemData(0x15, ItemClassification.useful),

}

progressive_rangs: Dict[str, ItemData] = {
    "Progressive Boomerang": ItemData(0x16, ItemClassification.useful, 3), #Boomerang - Multirang - Megarang - Omegarang
    "Progressive Flamerang": ItemData(0x17, ItemClassification.progression, 2),
    "Progressive Frostyrang": ItemData(0x18, ItemClassification.progression, 2),
    "Progressive Zappyrang": ItemData(0x19, ItemClassification.progression, 2),
    "Progressive Lasharang": ItemData(0x1a, ItemClassification.progression, 2),
    "Progressive Infrarang": ItemData(0x1b, ItemClassification.progression, 2),
    "Progressive Smasharang": ItemData(0x1c, ItemClassification.progression, 5), #Craftyrang - Smasharang - Kaboomarang - Deadlyrang - Doomerang
    "Camerarang": ItemData(0x15, ItemClassification.useful),

}

def get_

def get_filler(world):


dynamic_item_dict: Dict