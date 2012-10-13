# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# Copyright (c) 2012 dput authors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from dcut.uploader import AbstractCommand
from dput.exceptions import DcutError

class RmCommandError(DcutError):
    pass

class RmCommand(AbstractCommand):
    def __init__(self):
        super(RmCommand, self).__init__()
        self.cmd_name = "rm"
        self.cmd_purpose = "remove a file from the upload queue"

    def register(self, parser):
        parser.add_argument('file', metavar="FILENAME", action='store',
                            default=None, help="file name to be removed",
                            nargs="+")
        parser.add_argument('--searchdirs', action='store_true', default=None,
                            help="Search in all directories for the given"
                            " file. Only supported for files in the DELAYED"
                            " queue.")

    def produce(self, fh):
        print("produce")
        fh.write("produce")

    def validate(self, **kwargs):
        print("validate")

    def name_and_purpose(self):
        return (self.cmd_name, self.cmd_purpose)
