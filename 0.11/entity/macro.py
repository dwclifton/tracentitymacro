""" @package EntityMacro
    @file macro.py
    @brief The EntityMacro class

    Return numeric character reference from entity name.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.0
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.api import parse_args
from entity import entity

__all__ = ['EntityMacro']

class EntityMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        """Return numeric character reference from entity name."""

        name = ''
        args, kw = parse_args(args)

        if args:
            name = args.pop(0).strip()
        elif kw:
            if 'name' in kw: name = kw['name'].strip()

        if name in entity:
            return '&#%d;' % entity[name]
        return ''
