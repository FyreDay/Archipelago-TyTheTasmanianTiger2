from dataclasses import dataclass
from typing import Dict

from BaseClasses import ItemClassification, Item
from typings.schema import Optional


class Ty2Item(Item):
    game: str = "TCG Card Shop Simulator"


@dataclass
class ItemData:
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1

item_dict: Dict[str, ItemData] = {
    "Platinum cogs": ItemData(0x00, ItemClassification.progression),
    "Chromium Orbs": ItemData(0x00, ItemClassification.progression),
    "Opal bags": ItemData(0x00, ItemClassification.filler),
    "full health": ItemData(0x00, ItemClassification.filler),
    "Progressive elemental rangs": ItemData(0x00, ItemClassification.progression),#option
    "individual rangs": ItemData(0x00, ItemClassification.progression), #option
    "maps": ItemData(0x00, ItemClassification.progression), #option to start with
    "Bunyip Keys": ItemData(0x00, ItemClassification.progression),
    "fourbie speed upgrade": ItemData(0x00, ItemClassification.useful),
    "Health Upgrades": ItemData(0x00, ItemClassification.useful),
    "Progressive parking pad": ItemData(0x00, ItemClassification.progression),#option
    "Individual parking pad": ItemData(0x00, ItemClassification.progression),#option
}