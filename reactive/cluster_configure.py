#!/usr/bin/env python3
#import os
#import platform
#import yaml
#from subprocess import check_call

from charms.reactive.helpers import is_state
from charms.reactive.bus import set_state
from charms.reactive.bus import get_state
from charms.reactive.bus import remove_state
from charms.reactive.decorators import hook
from charms.reactive.decorators import when
from charms.reactive.decorators import when_not

from charmhelpers.core.hookenv import (
    log,
    CRITICAL,
    ERROR,
    WARNING,
    INFO,
    DEBUG,
    remote_unit,
    status_set,
    related_units
)


from charms.layer.jujuenv import JujuEnv

#from charms.layer.hpccsystems_platform import HPCCSystemsPlatformConfig
#from charms.layer.utils import SSHKey
