from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class Goal(Choice):
    """
    Determines the goal of the seed

    Boss Cass Bust-Up: Boss Cass must be beaten-up
    """
    display_name = "Goal"
    option_final_battle = 0
    default = 0

class GoalRequiresBosses(Toggle):
    """
    Determines if beating all bosses is a requirement to go to Boss Cass Bust-Up
    """
    display_name = "Goal Requires Bosses"

class TotalMissionsForGoal(Range):
    """
    How Many Missions do you need to get the plane for cass's run.
    """
    display_name = "Missions For Goal"
    range_start = 0
    range_end = 44
    default = 20

class SouthernRiversBarrierUnlock(Choice):
    """
    When should the barriers in Southern rivers be unlocked?
    Vanilla: On Boss Defeat open up the next part of the map
    On Item Receive: Unlocks when you receive AP Items
    Open World: Southern rivers is completely open
    """
    display_name = "Barrier Unlock Conditions"
    option_vanilla = 0
    option_items = 1
    option_open_world = 2
    default = 0

class ShopPrices(Choice):
    """
    Determines how expensive the shops are
    """
    display_name = "Shop Prices"
    option_cheap = 0
    option_normal = 1
    option_expensive = 2
    default = 1

class ExtraCogs(Range):
    """
    Sets number of additional platinum cogs to add to the pool
    """
    display_name = "Extra Cogs"
    range_start = 0
    range_end = 40
    default = 20

class ExtraOrbs(Range):
    """
    Sets number of additional chromium orbs to add to the pool
    """
    display_name = "Extra Orbs"
    range_start = 0
    range_end = 20
    default = 10

class StartWithMaps(Toggle):
    """
    Determines if you begin with the collectable maps
    The Maps still require infrarang or x-rang to be held
    """
    display_name = "Start With Maps"

class ProgressiveRangs(DefaultOnToggle):
    """
    Determines if each rang and their upgrade are progressive
    """
    display_name = "Progressive Rangs"

# class ConnectorRandomization(Toggle):
#     """
#     Determines whether the Connectors are randomized
#     """
#     display_name = "Connector Randomization"

class RacesAreMissions(DefaultOnToggle):
    """
    Determines if winning races grants checks and counts towards missions complete
    """
    display_name = "Races"

class ChecksRequireInfra(Toggle):
    """
    Determines whether the generator considers checks using invisible objects logically require the Infrarang

    This also affects Frame Sanity
    """
    display_name = "Frames Require Infra"

class FrameSanity(Toggle):
    """
    Determines if collecting Picture Frames grants checks
    """
    display_name = "Frame Sanity"

class SteveSanity(Toggle):
    """
    Determines if talking to Steve grants checks
    """
    display_name = "Steve Sanity"

class FrillSanity(Toggle):
    """
    Determines if finding disguised frills grants checks
    """
    display_name = "Frill Sanity"


# class Signsanity(Toggle):
#     """
#     Determines whether hitting each Maurie signpost with a boomerang grants a check.
#     """
#     display_name = "Signsanity"

# class TrapFill(Range):
#     """
#     Determines the percentage of the junk fill which is filled with traps.
#     """
#     display_name = "Trap Fill Percentage"
#     range_start = 0
#     range_end = 100
#     default = 0
#
# class GravityTrapWeight(Range):
#     """The weight of Gravity Traps in the trap pool.
#     Gravity Traps cause Ty to fall much faster, and limit his jump height."""
#     display_name = "Gravity Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20
#
#
# class KnockedDownTrapWeight(Range):
#     """The weight of Knocked Down Traps in the trap pool.
#     Knocked Down Traps knock you over and set your health to 1"""
#     display_name = "Knocked Down Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20
#
#
# class SlowTrapWeight(Range):
#     """The weight of Slow Traps in the trap pool.
#     Slow Traps cause Ty to move slower."""
#     display_name = "Slow Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20

@dataclass
class ty2_option_groups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        Goal,
        TotalMissionsForGoal,
        GoalRequiresBosses,
        SouthernRiversBarrierUnlock,
    ]),
    OptionGroup("General Options", [
        ProgressiveRangs,
        ShopPrices,
        ExtraCogs,
        ExtraOrbs,
        ChecksRequireInfra,
        StartWithMaps
    ]),
    OptionGroup("Sanity Options", [
        FrameSanity,
        SteveSanity,
        FrillSanity
    ]),
    # OptionGroup("Traps", [
    # ]),
    OptionGroup("Death Link", [
        DeathLink
    ])

@dataclass
class Ty2Options(PerGameCommonOptions):
    goal: Goal
    missions_for_goal: TotalMissionsForGoal
    require_bosses: GoalRequiresBosses
    barrier_unlock: SouthernRiversBarrierUnlock

    race_checks: RacesAreMissions
    progressive_rangs: ProgressiveRangs
    shop_difficulty: ShopPrices
    extra_cogs: ExtraCogs
    extra_orbs: ExtraOrbs
    require_infra: ChecksRequireInfra
    start_with_maps: StartWithMaps

    frame_sanity: FrameSanity
    steve_sanity: SteveSanity
    frill_sanity: FrillSanity

    death_link: DeathLink