# -*- coding: utf-8 -*-
"""
mkinit xdoctest --nomods
"""
__version__ = '0.5.1'  # nocover

from xdoctest import docstr

# Expose only select submodules
__submodules__ = [
    'runner',
    'exceptions',
]


from xdoctest.runner import (doctest_module,)
from xdoctest.exceptions import (DoctestParseError, ExitTestException,
                                 MalformedDocstr,)

__all__ = ['DoctestParseError', 'ExitTestException', 'MalformedDocstr',
           'doctest_module', 'docstr']
