#! /usr/bin/env python3
from .. import *
from random import choice, uniform
try:
    from numpy.random import gamma
except:
    error("Unable to import numpy. Install with: pip install numpy")
try:
    from scipy.stats import truncexpon
except:
    error("Unable to import scipy. Install with: pip install scipy")

# sample individuals according to some distribution in their time windows
def time_windows(model, params, out_fn, config, GLOBAL, verbose=True):
    end_time = config["Transmission Network"]['param']['duration']
    states_to_sample = {s.strip() for s in params['sampled_states'].split(',')}
    windows = dict() # windows[node] = list of [state, start, end]
    curr_state = dict()
    for l in open(out_fn['all_state_transitions']):
        node, from_s, to_s, t = [v.strip() for v in l.split('\t')]; t = float(t)
        if from_s in states_to_sample:
            windows[node][-1][2] = t
        if to_s in states_to_sample:
            if node not in windows:
                windows[node] = list()
            windows[node].append([to_s, t, end_time])
    sample_times = list(); tot_num_samples = len(windows)*params['num_samples']
    if model == "Truncated Exponential":
        variates = list(truncexpon.rvs(1, size=tot_num_samples))
    elif model == "Truncated Normal":
        variates = list(truncnorm_rvs(loc=params['mu'], scale=params['sigma'], a_min=0, b_max=1, size=tot_num_samples))
    for node in windows:
        for _ in range(params['num_samples']):
            state, start, end = choice(windows[node]); length = end - start; delta = None
            if model in {"Truncated Exponential", "Truncated Normal"}:
                delta = variates.pop() * length
            elif model == "Truncated Gamma":
                for i in range(100): # 100 attempts
                    tmp = gamma(params['k'], params['theta'])
                    if tmp <= length:
                        delta = tmp; break
                if tmp is None:
                    raise RuntimeError("Failed to sample truncated Gamma in 100 attempts")
            elif model == "Uniform":
                delta = uniform(0, length)
            else:
                error("Model not yet implemented: %s" % model)
            if delta is None:
                error("Failed to generate sample time for individual: %s" % node)
            sample_times.append((start+delta, node))
    sample_times.sort()
    f = open(out_fn['sample_times'], 'w')
    for t, node in sample_times:
        f.write("%s\t%s\n" % (node, t))
    f.close()

# model-specific functions
def time_windows_trunc_expon(params, out_fn, config, GLOBAL, verbose=True):
    time_windows("Truncated Exponential", params, out_fn, config, GLOBAL, verbose=verbose)
def time_windows_trunc_gamma(params, out_fn, config, GLOBAL, verbose=True):
    time_windows("Truncated Gamma", params, out_fn, config, GLOBAL, verbose=verbose)
def time_windows_trunc_normal(params, out_fn, config, GLOBAL, verbose=True):
    time_windows("Truncated Normal", params, out_fn, config, GLOBAL, verbose=verbose)
def time_windows_uniform(params, out_fn, config, GLOBAL, verbose=True):
    time_windows("Uniform", params, out_fn, config, GLOBAL, verbose=verbose)
