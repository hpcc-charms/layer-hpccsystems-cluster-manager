#!/usr/bin/env python3

import amulet



print ("Start ... ")
d = amulet.Deployment(series="trusty")

d.add('mgr', charm='$JUJU_REPOSITORY/trusty/hpccsystems-cluster-manager')
#d.add('roxie', charm='$JUJU_REPOSITORY/trusty/hpccsystems-cluster-node')

d.setup()
d.sentry.wait()


