from typing import ClassVar, Dict, Optional, Any

from BaseClasses import Tutorial, Item, ItemClassification, CollectionState, Location
from Utils import visualize_regions
from entrance_rando import disconnect_entrance_for_randomization, randomize_entrances
from worlds.AutoWorld import WebWorld, World
from worlds.ty_the_tasmanian_tiger_2.Items import create_ty2_items, full_item_dict, Ty2Item, junk_weights
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
    game = "Ty the Tasmanian Tiger 2"
    web = Ty2Web()
    options_dataclass = Ty2Options
    options: Ty2Options
    option_groups = ty2_option_groups
    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name, item_data in full_item_dict.items()}
    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.code for loc_name, loc_data in full_location_dict.items()}

    # UT Stuff Here
    ut_can_gen_without_yaml = True

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itempool = []
        self.locations = {}
        self.items = {}
        self.trap_weights = {}

        self.rang_prices = []
        self.sly_prices = []
        self.cop_prices = []

        self.cog_prices = []
        self.orb_prices = []

        self.hints = {}

    def generate_early(self) -> None:

        # UT Stuff Here
        self.handle_ut_yamless(None)

        self.locations = create_ty2_locations(self)

        min_price, max_price = 1000, 3000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 1000, 5000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 3000, 7000

        self.rang_prices = self.generate_shop(8, 1000000, min_price, max_price)
        self.rang_prices.sort()

        min_price, max_price = 4000, 10000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 7500, 15000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 10000, 25000
        self.sly_prices = self.generate_shop(11, 1000000, min_price, max_price)
        self.sly_prices.sort()

        min_price, max_price = 1000, 4000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 3000, 6000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 4000, 7500

        self.cop_prices = self.generate_shop(5, 1000000, min_price, max_price)
        self.cop_prices.sort()

        min_price, max_price = 1, 3
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 2, 4
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 3, 6
        self.cog_prices = self.generate_shop(10, 50, min_price, max_price)
        self.cog_prices.sort()

        min_price, max_price = 3, 6
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 5, 8
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 7, 10
        self.orb_prices = self.generate_shop(3, 30, min_price, max_price)
        self.orb_prices.sort()

    def create_regions(self):
        create_ty2_regions(self, self.locations)
        connect_ty2_regions(self)


    def connect_entrances(self) -> None:
        print("Connect Entrance")
        # result = randomize_entrances(self, True, {0: [0]})

    def create_item(self, item: str) -> Ty2Item:
        return Ty2Item(item, full_item_dict[item].classification, self.item_name_to_id[item], self.player)

    def create_items(self):
        create_ty2_items(self)

        self.push_precollected(Item("Burramudgee Town ParkingBay", ItemClassification.progression,
                                    self.item_name_to_id["Burramudgee Town ParkingBay"], self.player))

        self.push_precollected(Item("Boomerang", ItemClassification.progression,
                                        self.item_name_to_id["Boomerang"], self.player))


        if self.options.start_with_maps.value:
            self.push_precollected(Item("Missing Persons Map", ItemClassification.useful,
                                        self.item_name_to_id["Missing Persons Map"], self.player))
            self.push_precollected(Item("Cog Map", ItemClassification.useful,
                                        self.item_name_to_id["Cog Map"], self.player))
            self.push_precollected(Item("Mysterious Anomalies Map", ItemClassification.useful,
                                        self.item_name_to_id["Mysterious Anomalies Map"], self.player))

        if self.options.barrier_unlock.value == 2:
            self.push_precollected(Item("Patchy Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Patchy Barriers"], self.player))
            self.push_precollected(Item("Buster Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Buster Barriers"], self.player))
            self.push_precollected(Item("Fluffy Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Fluffy Barriers"], self.player))


    def set_rules(self):
        set_rules(self)

    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "0.1.2",
            "Goal": self.options.goal.value,
            "MissionsToGoal": self.options.missions_for_goal.value,
            "SkipCurrawong" : self.options.skip_currawong.value,
            "ReqBosses": self.options.require_bosses.value,
            "BarrierUnlock": self.options.barrier_unlock.value,
            "RaceChecks": self.options.race_checks.value,
            "ProgressiveRangs": self.options.progressive_rangs.value,
            "ShopDifficulty": self.options.shop_difficulty.value,
            "RangPrices": self.rang_prices,
            "SlyPrices": self.sly_prices,
            "CopPrices": self.cop_prices,
            "CogPrices": self.cog_prices,
            "OrbPrices": self.orb_prices,
            "ExtraCogs": self.options.extra_cogs.value,
            "ExtraOrbs": self.options.extra_orbs.value,
            "ChecksRequireInfra": self.options.require_infra.value,
            "FrameSanity": self.options.frame_sanity.value,
            "SteveSanity": self.options.steve_sanity.value,
            "FrillSanity": self.options.frill_sanity.value,
            "DeathLink": self.options.death_link.value,
        }

    def generate_shop(self, item_count, total_currency, min_price, max_price):
        shop_prices = []

        remaining_currency = total_currency

        for i in range(item_count):
            items_left = item_count - i

            # Calculate the max possible price for this item so remaining items can still be at min_price
            max_affordable_price = min(max_price, remaining_currency - min_price * (items_left - 1))

            # If we can't afford even the min price, force remaining items to min price
            if max_affordable_price < min_price:

                shop_prices.extend([2] * items_left)
                break

            price = self.random.randint(min_price, max_affordable_price)
            shop_prices.append(price)
            remaining_currency -= price

        return shop_prices

    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:

        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]

        if not slot_data:
            return None

        # fill in options
        self.options.goal.value = slot_data["Goal"]
        self.options.missions_for_goal.value = slot_data["MissionsToGoal"]
        self.options.skip_currawong.value = slot_data["SkipCurrawong"]
        self.options.require_bosses.value = slot_data["ReqBosses"]
        self.options.barrier_unlock.value = slot_data["BarrierUnlock"]
        self.options.race_checks.value = slot_data["RaceChecks"]
        self.options.progressive_rangs.value = slot_data["ProgressiveRangs"]
        self.options.shop_difficulty.value = slot_data["ShopDifficulty"]
        self.rang_prices = slot_data["RangPrices"]
        self.sly_prices = slot_data["SlyPrices"]
        self.cop_prices = slot_data["CopPrices"]
        self.cog_prices = slot_data["CogPrices"]
        self.orb_prices = slot_data["OrbPrices"]
        self.options.extra_cogs.value = slot_data["ExtraCogs"]
        self.options.extra_orbs.value = slot_data["ExtraOrbs"]
        self.options.require_infra.value = slot_data["ChecksRequireInfra"]
        self.options.frame_sanity.value = slot_data["FrameSanity"]
        self.options.steve_sanity.value = slot_data["SteveSanity"]
        self.options.frill_sanity.value = slot_data["FrillSanity"]
        self.options.death_link.value = slot_data["DeathLink"]

        return slot_data