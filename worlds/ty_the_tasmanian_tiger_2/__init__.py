from typing import ClassVar, Dict, Optional

from BaseClasses import Tutorial, Item, ItemClassification, CollectionState, Location
from Utils import visualize_regions
from entrance_rando import disconnect_entrance_for_randomization, randomize_entrances
from worlds.AutoWorld import WebWorld, World
from worlds.ty_the_tasmanian_tiger_2.Items import create_ty2_items, full_item_dict
from worlds.ty_the_tasmanian_tiger_2.Locations import create_ty2_locations, full_location_dict
from worlds.ty_the_tasmanian_tiger_2.Options import ty2_option_groups, Ty2Options
from worlds.ty_the_tasmanian_tiger_2.Regions import create_ty2_regions, connect_ty2_regions
from worlds.ty_the_tasmanian_tiger_2.Rules import set_rules


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

class Ty2World(World):
    """
    Ty the Tasmanian Tiger is a 3D platformer collectathon created by Australian developers Krome Studios.
    Play as Ty and travel the Australian outback to snowy mountains to defeat Boss Cass and rescue your family from The Dreaming.
    """
    game: str = "Ty the Tasmanian Tiger 2"
    web = Ty2Web()
    options_dataclass = Ty2Options
    options: Ty2Options
    option_groups = ty2_option_groups
    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name, item_data in full_item_dict.items()}
    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.code for loc_name, loc_data in full_location_dict.items()}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itempool = []
        self.locations = {}
        self.items = {}
        self.trap_weights = {}

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
            "SteveSanity": self.options.steve_sanity.value,
            "FrillSanity": self.options.frill_sanity.value,
            "DeathLink": self.options.death_link.value,
        }

    def generate_early(self) -> None:
        self.locations = create_ty2_locations(self)

    def create_regions(self):
        create_ty2_regions(self, self.locations)
        connect_ty2_regions(self)

    def connect_entrances(self) -> None:
        print("Connect Entrance")
        # result = randomize_entrances(self, True, {0: [0]})

    def create_items(self):
        create_ty2_items(self)

        if self.options.progressive_rangs.value:
            self.push_precollected(Item("Progressive Boomerang", ItemClassification.progression, self.item_name_to_id["Progressive Boomerang"], self.player))
        else:
            self.push_precollected(Item("Boomerang", ItemClassification.progression,
                                        self.item_name_to_id["Boomerang"], self.player))
        self.push_precollected(Item("Burramudgee Town ParkingBay", ItemClassification.progression,
                                    self.item_name_to_id["Burramudgee Town ParkingBay"], self.player))

    def set_rules(self):
        set_rules(self)

    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])

