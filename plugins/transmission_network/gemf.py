#! /usr/bin/env python3
from .. import *
from os import makedirs
from random import choice
from shutil import move
from subprocess import call

# determine initial states
def gemf_determine_initial_states(params, input_cn_fn, initial_states_fn):
    state_counts = {p[2:].strip():params[p] for p in params if p.startswith('N_')}
    nonzero_states = [p for p,c in state_counts.items() if c != 0]; state_counts_sum = sum(state_counts.values())
    nodes = [l.split('\t')[1].strip() for l in open(input_cn_fn) if l.startswith('NODE')]
    if state_counts_sum != len(nodes):
        error("Contact network has %d nodes, but total of state counts is: %d" % (len(nodes), state_counts_sum))
    f = open(initial_states_fn, 'w')
    for node in nodes:
        state = choice(nonzero_states); state_counts[state] -= 1
        if state_counts[state] == 0:
            nonzero_states.remove(state)
        f.write("%s\t%s\n" % (node, state))
    f.close()

# write infected states
def gemf_write_infected_states(model, infected_states_fn, GLOBAL):
    TN_MODELS = GLOBAL["MODELS"]["Transmission Network"]
    if model not in TN_MODELS:
        error("Invalid GEMF model: %s" % model)
    f = open(infected_states_fn, 'w')
    for s in TN_MODELS[model]["INF_STATES"]:
        f.write('%s\n' % s)
    f.close()

# write transition rates
def gemf_write_transition_rates(params, transition_rates_fn):
    f = open(transition_rates_fn, 'w')
    for p in params:
        if not p.startswith('R_'):
            continue
        parts = [s.strip() for s in p[2:].replace('-','_').split('_')]
        if len(parts) == 2:
            parts.append(None)
        parts.append(params[p])
        f.write("%s\t%s\t%s\t%s\n" % tuple(parts))
    f.close()

# simulate an epidemic using GEMF_FAVITES
def gemf_favites(model, params, out_fn, config, GLOBAL, verbose=True):
    # set things up
    intermediate_gemf = "%s/GEMF_FAVITES" % out_fn['intermediate']; makedirs(intermediate_gemf)
    initial_states_fn = "%s/initial_states.tsv" % intermediate_gemf
    infected_states_fn ="%s/infected_states.txt" % intermediate_gemf
    transition_rates_fn = "%s/transition_rates.tsv" % intermediate_gemf
    gemf_out = "%s/output" % intermediate_gemf

    # run
    gemf_determine_initial_states(params, out_fn['contact_network'], initial_states_fn)
    gemf_write_infected_states(model, infected_states_fn, GLOBAL)
    gemf_write_transition_rates(params, transition_rates_fn)
    command = [
        'GEMF_FAVITES.py',
        '-c', out_fn['contact_network'],
        '-s', initial_states_fn,
        '-i', infected_states_fn,
        '-r', transition_rates_fn,
        '-t', str(params['duration']),
        '-o', gemf_out,
        '--output_all_transitions',
        '--rng_seed', str(GLOBAL['RNG_SEED']),
        '--quiet',
    ]
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    try:
        call(command)
    except FileNotFoundError as e:
        error("Unable to run GEMF_FAVITES. Make sure GEMF_FAVITES.py and GEMF executables are in your PATH (e.g. /usr/local/bin)")
    move('%s/transmission_network.txt' % gemf_out, out_fn['transmission_network'])
    if verbose:
        print_log("Transmission Network written to: %s" % out_fn['transmission_network'])
    move('%s/all_state_transitions.txt' % gemf_out, out_fn['all_state_transitions'])
    if verbose:
        print_log("All State Transitions written to: %s" % out_fn['all_state_transitions'])

# model-specific functions
def gemf_favites_granich(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Granich et al. (2008)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_hethcote_yorke(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Hethcote and Yorke (1984)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_sais(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Susceptible-Alert-Infected-Susceptible (SAIS)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_saapphiire(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("SAAPPHIIRE", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_saphire(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("SAPHIRE", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_seir(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Susceptible-Exposed-Infected-Removed (SEIR)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_si(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Susceptible-Infected (SI)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_sir(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Susceptible-Infected-Removed (SIR)", params, out_fn, config, GLOBAL, verbose=verbose)
def gemf_favites_sis(params, out_fn, config, GLOBAL, verbose=True):
    gemf_favites("Susceptible-Infected-Susceptible (SIS)", params, out_fn, config, GLOBAL, verbose=verbose)
