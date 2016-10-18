import numpy as np
import pylab as plt

import omnium as om

# What this shows: that q[-1] - q[-2] (==dq) is equal to the total inc over this time.
# This is not what I was expecting.
# Later... Should this be a surprise?
# Thinking: non-cons would happen in adv (OK), so should appear as adv incr of eg q.
# This will be included in the total q incr, which then gets applied to model.
# This is surprising because it is different from ND (i.e. SW's Moisture budget HTML paper).
# Upshot is still that I need to check this for each qvar.
config = om.ConfigChecker.load_config()
process_classes = om.get_process_classes()
dag = om.NodeDAG(config, process_classes)
proc_eng = om.ProcessEngine(False, config, process_classes, dag)
stash = om.Stash()

for profile in ['profiles_MC_on', 'profiles_MC_off']:
    group = dag.get_group(profile)
    q = proc_eng.load(group.nodes[-1])[0]
    print(q.name())
    q_inc_tot = proc_eng.load(group.nodes[-2])[0]
    print(q_inc_tot.name())
    dq = q[-1].data - q[-2].data
    print(np.allclose(dq[1:], q_inc_tot[-1].data * 60))
