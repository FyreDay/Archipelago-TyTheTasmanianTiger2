import copy
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

def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk

def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_ty2_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    for item_name, item_data in get_rangs(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in item_dict.items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_collectable_currencies(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_parking_pads(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)

    remaining_locations: int = total_location_count - len(world.itempool)
    # trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations - 0 #trap_count
    junk = get_junk_item_names(world.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)
    # traps = get_trap_item_names(world.worlds[player], world.random, trap_count)
    # for name in traps:
    #     create_single(name, world, player)
    world.multiworld.itempool += world.itempool


item_dict: Dict[str, ItemData] = {
    "Lifter Bunyip Key": ItemData(0x1d, ItemClassification.progression),
    "Thermo Extreme Bunyip Key": ItemData(0x1e, ItemClassification.progression),
    "Sub Bunyip Key": ItemData(0x1f   , ItemClassification.progression),
    "Gold Paw": ItemData(0x20, ItemClassification.useful),
    "Platinum Paw": ItemData(0x21, ItemClassification.useful),
    "Missing Persons Map": ItemData(0x22, ItemClassification.useful),
    "Cog Map": ItemData(0x23, ItemClassification.useful),
    "Mysterious Anomalies Map": ItemData(0x24, ItemClassification.useful),
    # "fourbie speed upgrade": ItemData(0x00, ItemClassification.useful),
}

def get_rangs(world) -> Dict[str, ItemData]:
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
    "Craftyrang": ItemData(0x14, ItemClassification.progression),
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

def get_parking_pads(world) -> Dict[str, ItemData]:
    # if world.options.progressive_parking_pads.value:
    #     return progressive_parking_pads
    # else:
    return parking_bays

parking_bays: Dict[str, ItemData] = {
    "Oasis Parking Bay": ItemData(0x00, ItemClassification.progression),
}

progressive_parking_bays: Dict[str, ItemData] = {
    "Progressive Parking Bay": ItemData(0x00, ItemClassification.progression, 100),
}

def get_collectable_currencies(world) -> Dict[str, ItemData]:
    collectibles_copy: Dict[str, ItemData] = copy.deepcopy(collectibles)
    collectibles_copy["Platinum Cog"].amount += world.options.extra_cogs.value
    collectibles_copy["Kromium Orb"].amount += world.options.extra_orbs.value
    return collectibles_copy


collectibles: Dict[str, ItemData] = {
    "Platinum Cog": ItemData(0x00, ItemClassification.progression_skip_balancing, 50),
    "Kromium Orb": ItemData(0x00, ItemClassification.progression_skip_balancing, 30),
}

def get_filler(world) -> Dict[str, ItemData]:
    return junk_items

junk_items: Dict[str, ItemData] = {
    "Opal": ItemData(0x00, ItemClassification.filler),
    "10 Opals": ItemData(0x00, ItemClassification.filler),
    "25 Opals": ItemData(0x00, ItemClassification.filler),
    "100 Opals": ItemData(0x00, ItemClassification.filler),
    "200 Opals": ItemData(0x00, ItemClassification.filler),
    "Full Pie": ItemData(0x00, ItemClassification.filler),
}

junk_weights = {
    "Opal": 50,
    "10 Opals": 30,
    "25 Opals": 20,
    "100 Opals": 10,
    "200 Opals": 5,
    "Full Pie": 20,
}