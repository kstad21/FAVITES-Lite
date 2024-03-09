#! /usr/bin/env python3
from .. import *
from os import environ
from subprocess import call

# simulate contact network using NiemaGraphGen
def ngg(exe, params, out_fn, config, GLOBAL, verbose=True):
    env = dict(environ); env['NGG_RNG_SEED'] = str(GLOBAL['RNG_SEED'])
    if exe == 'ngg_barabasi_albert':
        command = [exe, str(params['n']), str(params['m'])]
    elif exe == 'ngg_barbell':
        command = [exe, str(params['m1']), str(params['m2'])]
    elif exe in {'ngg_complete', 'ngg_cycle', 'ngg_empty', 'ngg_path'}:
        command = [exe, str(params['n'])]
    elif exe == 'ngg_erdos_renyi':
        command = [exe, str(params['n']), str(params['p'])]
    elif exe == 'ngg_newman_watts_strogatz':
        command = [exe, str(params['n']), str(params['k']), str(params['p'])]
    elif exe == 'ngg_ring_lattice':
        command = [exe, str(params['n']), str(params['k'])]
    else:
        error("Invalid NiemaGraphGen exe: %s" % exe)
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(out_fn['contact_network'], 'w')
    try:
        call(command, stdout=f, env=env)
    except FileNotFoundError as e:
        error("Unable to run NiemaGraphGen. Make sure all ngg_* executables are in your PATH (e.g. /usr/local/bin)")
    f.close()
    if verbose:
        print_log("Contact Network written to: %s" % out_fn['contact_network'])
def ngg_barabasi_albert(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_barabasi_albert", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_barbell(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_barbell", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_complete(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_complete", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_cycle(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_cycle", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_empty(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_empty", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_erdos_renyi(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_erdos_renyi", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_newman_watts_strogatz(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_newman_watts_strogatz", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_path(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_path", params, out_fn, config, GLOBAL, verbose=verbose)
def ngg_ring_lattice(params, out_fn, config, GLOBAL, verbose=True):
    ngg("ngg_ring_lattice", params, out_fn, config, GLOBAL, verbose=verbose)
