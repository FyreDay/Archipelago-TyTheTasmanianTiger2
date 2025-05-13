from typing import ClassVar, Dict

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.ty_the_tasmanian_tiger_2.Options import ty2_option_groups, Ty2Options


class Ty2Web(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Ty the Tasmanian Tiger 2 randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"]
    )

    tutorials = [setup_en]
    option_groups = ty2_option_groups


class Ty2World(World):
    """
    Ty the Tasmanian Tiger is a 3D platformer collectathon created by Australian developers Krome Studios.
    Play as Ty and travel the Australian outback to snowy mountains to defeat Boss Cass and rescue your family from The Dreaming.
    """
    game: str = "Ty the Tasmanian Tiger 2"
    web = Ty2Web()
    options = Ty2Options

    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name, item_data in full_item_dict.items()}
    location_name_to_id: ClassVar[Dict[str, int]] = full_location_dict

    locations = {}
    items = {}
    trap_weights = {}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "0.0.0",
            "Goal": self.options.goal.value,
            "ReqBosses": self.options.require_bosses.value,
            "ProgressiveRangs": self.options.progressive_rangs.value,
            "ShopDifficulty": self.options.shop_difficulty.value,
            "ExtraCogs": self.options.extra_cogs.value,
            "ExtraOrbs": self.options.extra_orbs.value,
            "ChecksRequireInfra": self.options.require_infra.value,
            "FrameSanity": self.options.frame_sanity.value,
            "SteveSanity": self.steve_sanity.value,
            "FrillSanity": self.options.frill_sanity.value,
            "DeathLink": self.options.death_link.value,
        }

    def generate_early(self) -> None:
    def create_regions(self):
    def create_items(self):