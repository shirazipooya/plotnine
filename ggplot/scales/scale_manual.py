from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from .scale import scale_discrete
from ..utils.exceptions import GgplotError


class _scale_manual(scale_discrete):
    """
    Abstract class for manual scales
    """
    def __init__(self, values):
        self.values

    def palette(self, n):
        msg = """\
        Insufficient values in manual scale.\
        , {}, needed but only , {},  provided.
        """
        if n > len(self.values):
            raise GgplotError(
                msg.format(n, len(self.values)))
        return values


class scale_color_manual(_scale_manual):
    aesthetics = ['color']


class scale_fill_manual(_scale_manual):
    aesthetics = ['fill']


class scale_shape_manual(_scale_manual):
    aesthetics = ['shape']


class scale_linetype_manual(_scale_manual):
    aesthetics = ['linetype']


class scale_alpha_manual(_scale_manual):
    aesthetics = ['alpha']


class scale_size_manual(_scale_manual):
    aesthetics = ['size']


# American to British spelling
scale_colour_manual = scale_color_manual