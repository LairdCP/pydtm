#
# BL5340PA Power Tables
#
# *** These channels are in logical order (not physical) because that is
# what the Nordic driver requires (C/Zephyr).
#
# SPDX-License-Identifier: LicenseRef-LairdConnectivity-Clause
#
from enum import Enum
import logging

logger = logging.getLogger(__name__)


def MPSL_FEM_POWER_REDUCE(p: int):
    """
    In the C/Zephyr code this macro returns the power at the antenna port (20 - p).
    Each type of antenna has a specific gain that isn't represented in this number.
    This format is used because it matches tables provided to engineering.

    For the DTM code, we want the power output of the nRF5340 SoC, so we return -p.
    """
    return -p


FCC_IC_EXT = {
    "CODED_PHY_S8": [
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
    ],
    "CODED_PHY_S2": [
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(7),
    ],
    "PHY_1M": [
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(7),
    ],
    "PHY_2M": [
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(12),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(12),
    ],
}

FCC_IC_INT = {
    "CODED_PHY_S8": [
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(8),
    ],
    "CODED_PHY_S2": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(5),
    ],
    "PHY_1M": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(5),
    ],
    "PHY_2M": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(8),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(8),
    ],
}

RCM_EXT = {
    "CODED_PHY_S8": [
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(7),
    ],
    "CODED_PHY_S2": [
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(7),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
    ],
    "PHY_1M": [
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
    ],
    "PHY_2M": [
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(6),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(6),
    ],
}

RCM_INT = {
    "CODED_PHY_S8": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
    ],
    "CODED_PHY_S2": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(5),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
    ],
    "PHY_1M": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
    ],
    "PHY_2M": [
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
        MPSL_FEM_POWER_REDUCE(4),
    ],
}

# strings match enumeration in dtm.py
VALID_PHY_STRINGS = ["CODED_PHY_S8", "CODED_PHY_S2", "PHY_1M", "PHY_2M"]
VALID_ANTENNA_STRINGS = ["INTERNAL", "EXTERNAL"]
VALID_REGION_STRINGS = ["FCC_IC", "RCM"]

POWER_TABLE = {
    "FCC_IC": {"INTERNAL": FCC_IC_INT, "EXTERNAL": FCC_IC_EXT},
    "RCM": {"INTERNAL": RCM_INT, "EXTERNAL": RCM_EXT},
}

# Validate the table
for region in VALID_REGION_STRINGS:
    for antenna in VALID_ANTENNA_STRINGS:
        for modulation in VALID_PHY_STRINGS:
            length = len(POWER_TABLE[region][antenna][modulation])
            if length != 40:
                logger.error(
                    "Invalid length for " f"{region}.{antenna}.{modulation} ({length})"
                )
                raise ValueError("Invalid table size")
