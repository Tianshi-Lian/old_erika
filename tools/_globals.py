import sys

GEN_ACTION_WINDOWS = "vs2022"
GEN_ACTION_LINUX = "gmake2"

BUILD_CFG = "debug"
BUILD_PRJ_NAME = "project"

PLATFORM = sys.platform

if 'linux' in PLATFORM: # we could be linux or linux2
    PLATFORM = 'linux'
elif 'win' in PLATFORM:
    PLATFORM = 'windows'
