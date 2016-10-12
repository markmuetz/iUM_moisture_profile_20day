import numpy as np
import pylab as plt

import omnium as om

# What this shows: that q[-1] - q[-2] (==dq) is equal to the total inc over this time.
# This is not what I was expecting.
config = om.ConfigChecker.load_config()
process_classes = om.get_process_classes()
dag = om.NodeDAG(config, process_classes)
proc_eng = om.ProcessEngine(False, config, process_classes, dag)
stash = om.Stash()

g_on = dag.get_group('profiles_MC_on')
q = proc_eng.load(g_on.nodes[-1])[0]
q_inc_tot = proc_eng.load(g_on.nodes[-2])[0]
dq = q[-1].data - q[-2].data
print(np.allclose(dq[1:], q_inc_tot[-1].data * 60))

g_off = dag.get_group('profiles_MC_off')
q2 = proc_eng.load(g_off.nodes[-1])[0]
dq2 = q2[-1].data - q2[-2].data
q_inc_tot2 = proc_eng.load(g_off.nodes[-2])[0]
print(np.allclose(dq2[1:], q_inc_tot2[-1].data * 60))
