import os
os.environ["PARSE_API_ROOT"] = "http://3.135.223.18:80/parse/"

# Everything else same as usual

from parse_rest.datatypes import Function, Object, GeoPoint
from parse_rest.connection import register
from parse_rest.query import QueryResourceDoesNotExist
from parse_rest.connection import ParseBatcher
from parse_rest.core import ResourceRequestBadRequest, ParseError

APPLICATION_ID = '2bb89472aeb69b347279ce4c534f392961203eda'
REST_API_KEY = '30e8fc949092a866bebac18d891f189dc37d22fd'
MASTER_KEY = '8dc377c20d1987961d32c04d00cdd40e795f5380'

register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)
