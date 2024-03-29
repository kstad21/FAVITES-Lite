# FAVITES-Lite ![FAVITES-Lite Tests Status](https://github.com/niemasd/FAVITES-Lite/actions/workflows/favites_lite_tests.yml/badge.svg)
FAVITES-Lite is a lightweight framework for viral transmission and evolution simulation. It is a spin-off of [FAVITES](https://github.com/niemasd/FAVITES) that is designed to be much simpler and faster, but at the expense of reduced flexibility. FAVITES-Lite was designed to incorporate the just key functionality of FAVITES that most users require. In general, we strongly recommend using FAVITES-Lite instead of FAVITES for epidemic simulation projects.

## Installation
FAVITES-Lite is written in Python and depends on the following Python packages:

* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)
* [TreeSAP](https://github.com/niemasd/treesap)
* [TreeSwift](https://github.com/niemasd/TreeSwift)

FAVITES-Lite also calls many command-line tools, which must be installed in your `PATH`:

* [CoaTran](https://github.com/niemasd/CoaTran)
* [GEMF_FAVITES](https://github.com/niemasd/GEMF)
* [NiemaGraphGen](https://github.com/niemasd/NiemaGraphGen)
* [Seq-Gen](https://github.com/rambaut/Seq-Gen)

To install FAVITES-Lite itself, you can either download the latest [release](https://github.com/niemasd/FAVITES-Lite/releases), or you can clone this GitHub repository:

```bash
git clone https://github.com/niemasd/FAVITES-Lite.git
```

FAVITES-Lite is also available on [Bioconda](https://bioconda.github.io/recipes/favites_lite/README.html). Assuming you have already installed `conda` (or equivalent) and added the `bioconda` channel, you can install FAVITES-Lite as well as all of its dependencies as follows:

```bash
conda install favites_lite
```

For convenience, you can also use the [FAVITES-Lite Docker image](https://hub.docker.com/r/niemasd/favites_lite), or you can refer to the [`Dockerfile`](https://github.com/niemasd/FAVITES-Lite/blob/main/Dockerfile#L9-L42) for installation commands.

## Usage
There are two primary components to FAVITES-Lite: the [Config Designer](https://niema.net/FAVITES-Lite) and the [FAVITES-Lite executable](favites_lite.py).

### Config Designer
The [Config Designer](https://niema.net/FAVITES-Lite) is a tool that helps users design a FAVITES-Lite configuration file for their unique simulation experiment design. Unlike the original FAVITES, in which users had to navigate the documentation to manually design a configuration file, the FAVITES-Lite Config Designer guides the user and includes detailed information about all model choices for all steps of the simulation workflow.

The Config Designer web app was developed by my students: [Grant Cheng](https://www.linkedin.com/in/grant-cheng-52171b205/), [Jenny Lam](https://www.linkedin.com/in/jwny/), Justyce Granda, Kathy Chen, [Helena Hundhausen](https://www.linkedin.com/in/helena-hundhausen), and [Daniel Ji](https://www.linkedin.com/in/danielji26).

### FAVITES-Lite Executable
The [FAVITES-Lite executable (`favites_lite.py`)](favites_lite.py) actually executes a given simulation experiment, and it can be used as follows:

```
usage: favites_lite.py [-h] -c CONFIG -o OUTPUT [--overwrite] [--quiet] [--version]

  -h, --help                   show this help message and exit
  -c CONFIG, --config CONFIG   FAVITES-Lite Config File
  -o OUTPUT, --output OUTPUT   Output Directory
  --overwrite                  Overwrite output directory if it exists (default: False)
  --quiet                      Suppress Log Messages (default: False)
  --version                    Show FAVITES-Lite version (default: False)
```

## Scripts
To aid with common downstream analyses, you can find some helper scripts in the [`scripts`](scripts) folder of this repository. The scripts will be organized by step(s) of the FAVITES-Lite simulation workflow, and each subdirectory will have a README describing the scripts in that folder.

# Citing FAVITES-Lite
We are currently working on a manuscript for FAVITES-Lite. For now, if you use FAVITES-Lite in your work, please cite the original FAVITES paper:

> **Moshiri N**, Ragonnet-Cronin M, Wertheim JO, Mirarab S (2018). "FAVITES: simultaneous simulation of transmission networks, phylogenetic trees, and sequences." *Bioinformatics*. 35(11):1852-1861. [doi:10.1093/bioinformatics/bty921](https://doi.org/10.1093/bioinformatics/bty921)
