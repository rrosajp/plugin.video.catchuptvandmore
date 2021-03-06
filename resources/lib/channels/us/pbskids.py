# -*- coding: utf-8 -*-
# Copyright: (c) 2018, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
import json

from codequick import Resolver
import urlquick


# TODO
# Add replay

URL_ROOT = 'http://pbskids.org'

# Live
URL_LIVE = URL_ROOT + '/api/video/v1/livestream?station=KIDS'


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    resp = urlquick.get(URL_LIVE)
    json_parser = json.loads(resp.text)
    return json_parser["livestream"]
