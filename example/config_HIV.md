# FAVITES Configuration File for MSM Population in San Diego, 2017

## Contact Network:
#### Through nodes (people) and edges (interactions), describe social interactions.
#### Model: `Barabasi-Albert (BA)`
- Uses preferential attachment, so nodes with more connections are likely to make connections (think about how someone with lots of friends might be more likely to make even more friends).
#### Number of nodes: `10000`
- Picked an even, easy to work with number.
#### m (number of edges attached from new to existing nodes): `2`
- There are estimates of between 3-4 sexual partners over 10 years: ~3 in [Wertheim et al. (2018)](https://scholar.google.com/scholar_lookup?title=Growth%20of%20HIV-1%20molecular%20transmission%20clusters%20in%20New%20York%20city&author=J.O.%20Wertheim&publication_year=2018&journal=J.%20Infect.%20Dis&volume=218&pages=1943-1953) and 3-4 in [Rosenberg et al. (2011)](https://scholar.google.com/scholar_lookup?title=Number%20of%20casual%20male%20sexual%20partners%20and%20associated%20factors%20among%20men%20who%20have%20sex%20with%20men%3A%20results%20from%20the%20National%20HIV%20Behavioral%20Surveillance%20system&author=E.S.%20Rosenberg&publication_year=2011&journal=BMC%20Public%20Health&volume=11&pages=189). Expected degree (number of partners) is equal to 2*m, so we set m to 2.
___


## Transmission Network: 
#### Describe how the virus moves through the contact network, based on transition rates for individuals in our simulation. Transition rates are based on the reciprocal of expected time to arrival (make sure to keep track of your 'time' units!).
#### Model: `Granich et al. (2008)`
- The model uses states based on HIV progression, including states for indidividuals on ART (antiretroviral therapy) and states for those who are not. Whether or not a node is on ART, there are 4 stages of progression: 1, 2, 3 and 4 [(Granich et al., 2008)](https://www.sciencedirect.com/science/article/pii/S0140673608616979?via%3Dihub)
#### Duration: `10`
#### N_NS: `0`
- This configuration file only looks at susceptible nodes, so there are no non-susceptible nodes in the network.
#### N_S: `9999`
- Every node that is not starting as infected will fall into the susceptible category.
#### N_I1: `1`
- Chose starting with 1 person in I1 to emphasize progression of the pandemic but this is easily changeable. Initial counts may have little to no effect on overall counts if the duration of the epidemic is long enough.
#### N_I2, N_I3, N_I4, N_A1, N_A2, N_A3, N_A4: `0`
- Nodes at the start are either susceptible or infected in this configuration file. This can be easily changed to include numbers of people in any of the above states.
#### R_S-I1: `2`
- Transition rate from susceptible to infected stage 1.
- Based on MSM populations [(Grey et al., 2016)](https://publichealth.jmir.org/2016/1/e14/), with San Diego County's estimation being 1,204,728. Between 2017 and 2021 in California, an average of 70% of new diagnoses came from male-to-male sexual contact (MMSC) [(California HIV Suveillance Report - 2021)](https://www.cdph.ca.gov/Programs/CID/DOA/CDPH%20Document%20Library/California_HIV_Surveillance_Report2021_ADA.pdf). In 2021, there were 379 new HIV diagnoses in San Diego [(California HIV Surveillance Report - 2021)](https://www.cdph.ca.gov/Programs/CID/DOA/CDPH%20Document%20Library/California_HIV_Surveillance_Report2021_ADA.pdf). So out of 379 diagnoses and an estimated 70% of those coming from MMSC, we can estimate there are about 265 diagnoses for MSM. Looking at the whole population: 265/1,204,728 = 0.00022. Scaling this to our chosen number of nodes: $`10,000 * 0.00022 = 2.2`$ diagnoses a year. In a Poisson distribution, the expected value (2) will be equal to the reciprocal of the time until next arrival.
#### R_S-I1_I1: `0.1125`
- The transition rate from susceptible to infected stage 1 induced by infected stage 1 neighbors. 
- In the [FAVITES](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084) paper, relative rates were scaled so that number of new cases over ten years was roughly accurate. This yielded a rate of infectiousness 0.1125. Expected time for arrival would be $`1/(0.1125 * n)`$, n being the number of nodes in state I1 that are neighbors to the current node.
#### R_S_I1_I2: `0.0225`
#### R_S-I1_I3: `0.0225`
#### R_S-I1_I4: `0.0225`
-The transition rate from susceptible to infected stage 1 induced by infected stage 2, 3, 4 (respectively) neighbors.
- In the [FAVITES](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084) paper, relative rates were scaled so that number of new cases over ten years was roughly accurate.
- Non-acute stages of HIV were used for baseline. We kept I2, I3, and I4 as having the same rates of infectiousness, but these parameters can easily be reset. Given infectivity `a` and number of neighbor nodes in "inducing" state `n`, expected time for next infection arrival would be $`1/(a * n)`$.

#### R_S-I1_A1: `0.005625`
- The transition rate from susceptible to infected stage 1 induced by neigbors on [ART](https://hivinfo.nih.gov/understanding-hiv/fact-sheets/hiv-treatment-basics), stage 1.
- Those in the acute treated stage were found to have 1/20 the infectiousness of chronic untreated individuals [(Cohen et al., 2011)](https://scholar.google.com/scholar_lookup?title=Prevention%20of%20HIV-1%20infection%20with%20early%20antiretroviral%20therapy&author=M.S.%20Cohen&publication_year=2011&journal=N.%20Engl.%20J.%20Med.&volume=365&pages=493-505). Expected time for arrival would be $`1/(0.0.005625 * n)`$, n being the number of nodes in state A1 that are neighbors to the current node.
#### R_S-I1_A2: `0`
#### R_S-I1_A3: `0`
#### R_S-I1_A4: `0`
- The transition rate from susceptible to infected stage 1 induced by neighbors in ART stage 2, 3, 4 (respectively).
- Individuals on ART stage 2 and beyond had extremely low infectivity.
#### R_I1-D: `0`
- The transition rate from infected stage 1 to death.
- In this configuration, death is only a possible transition in either I4 or A4.
#### R_I1-I2: `6`
- The transition rate from infected stage 1 to infected stage 2.
- Individuals spend an expected 2 months in the acute state [(Granich et. al)](https://www.sciencedirect.com/science/article/pii/S0140673608616979?via%3Dihub). Transition rates are in unit of reciprocal of next arrival so $`2`$ months = $`1/6`$ year; reciprocal of $`1/6`$ is $`6`$.
#### R_I1-A1: `1`
- The transition rate from infected stage 1 to ART stage 1.
- Expected 1 year to start ART [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322).
#### R_A1-D: `0`
- The transition rate from ART stage 1 to death.
- In this configuration, death is only a possible transition in either I4 or A4. 
#### R_A1-A2: `0.0883`
- The transition rate from ART stage 1 to ART stage 2.
- Length of stay in A1 is expected to be 11.33 years, find the reciprocal [(Zingoni et al., 2019)](https://pubmed.ncbi.nlm.nih.gov/31803702/).
#### R_A1-I1: `0.481`
- The transition rate from ART stage 1 to infected stage 1.
- Expected time to stop ART is 25 months, find the reciprocal [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322).
#### R_I2-D: `0`
- The transition rate from infected stage 2 to death.
- In this configuration, death is only a possible transition in either I4 or A4. 
#### R_I2-I3: `0.125`
- The transition rate from infected stage 2 to infected stage 3.
- Expected time in chronic state is 8 years [(Granich et al., 2008)](https://www.sciencedirect.com/science/article/pii/S0140673608616979?via%3Dihub). Find the reciprocal: $`1/8 = 0.125`$.
#### R_I2-A2: `1`
- The transition rate from infected stage 2 to ART stage 2.
- Expected time to start ART is 1 year [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322).
#### R_A2-D: `0`
- The transition rate from ART stage to to death.
- In this configuration, death is only a possible transition in either I4 or A4. 
#### R_A2-A3: `0.181`
- The transition rate from ART stage 2 to ART stage 3. 
- Length of stay in A2 is estimated to be 5.51 years [(Zingoni et al., 2019)](https://pubmed.ncbi.nlm.nih.gov/31803702/). Find the reciprocal: $`1/5.51 = 0.181`$
#### R_A2-I2: `0.481`
- The transition rate from ART stage 1 to infected stage 1.
- Expected time to stop ART is 25 months, find the reciprocal [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322).
#### R_I3-D: `0`
- The transition rate from infected stage 3 to death.
- In this configuration, death is only a possible transition in either I4 or A4.
#### R_I3-I4: `0.5`
- The transition rate from infected stage 3 to infected stage 4.
- Expected time in stage 3 is 2 years without ART [(Granich et al., 2008)](https://www.sciencedirect.com/science/article/pii/S0140673608616979?via%3Dihub). Find the reciprocal: $`1/2 = 0.5`$.
#### R_A3-D: `0`
- The transition rate from ART stage 3 to death.
- In this configuration, death is only a possible transition in either I4 or A4. 
#### R_A3-A4: `0.139`
- The transition rate from ART stage 3 to ART stage 4. 
- Length of stay in A3 is estimated to be 7.17 years [(Zingoni et al., 2019)](https://pubmed.ncbi.nlm.nih.gov/31803702/).
#### R_I4-D: `1.82`
- The transition rate from infected stage 4 to death.
- Expected time in stage 4 is 5% of survival time without ART, with mean survival time without ART being 11 years [(Zingoni et al., 2019)](https://pubmed.ncbi.nlm.nih.gov/31803702/). $`0.05 * 11 = 0.55`$; $`1/0.55 = 1.8181`$.
#### R_I4-A4: `0.481`
- The transition rate from infected stage 4 to ART stage 4.
- Expected time to stop ART is 25 months, find the reciprocal [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322).
#### R_A4-D: `0.146`
- The transition rate from infected stage 4 to death.
- Length of stay in A4 is expected to be 6.86 years [(Zingoni et al., 2019)](https://pubmed.ncbi.nlm.nih.gov/31803702/). Find the reciprocal: $`1/6.86 = 0.146`$.
#### R_A4-I4: `0.481`
- Expected time to stop ART is 25 months [(McCreesh et al., 2017)](https://scholar.google.com/scholar_lookup?title=Universal%20test%2C%20treat%2C%20and%20keep%3A%20improving%20ART%20retention%20is%20key%20in%20cost-effective%20HIV%20control%20in%20uganda&author=N.%20McCreesh&publication_year=2017&journal=BMC%20Infect.%20Dis.&volume=17&pages=322). Find the reciprocal: $`1/(25/12) = 0.481`$.

## Sample Times: 
#### How are individuals in the transmission network sampled?
#### Model: `End`
- End was chosen to get a good idea of every node's state at the end of the simulation.
#### sampled_states: `I1,I2,I3,I4,A1,A2,A3,A4`
- Comma-separated list of states in which individuals are sampled.
- For this configuration, all states were sampled to get as much information as possible.
#### num_samples: `1`
- With this sampling configuration, we choose to sample every single individual once at the end of the simulation.

## Viral Phylogeny (Transmissions): 
#### With a coalescent framework, describe topology and branch lengths (in unit of time) of the viral phylogeny throughout the epidemic under the constraints of our chosen transmission network.
#### Model: `Transmission Tree`
- In a transmission tree, nodes are infected hosts; edges are transmission events. Coalescent events occur as late in time as possible.

## Viral Phylogeny (Seeds): 
#### Describe the topology and branch lengths (in unit of time) of the viral phylogeny of the seed individuals.
#### Model: `Non-Homogeneous Yule`
- Real HIV trees have short internal branches close to the root and long leaves (cite or link to pic?). Since most phylogenetic models don't produce this shape easily, a rate function that is high early in the timeline, decreasing as time progresses, can be used in non-homogeneous Yule processes to replicate a pattern reminiscent of real HIV trees.
#### rate_func (Rate function of the initial tree): $`e^-(t^2)+1`$
- Chosen to emulate short branches close to the base of the tree.
#### height: `36`
- Scaled so that height matches the 1980 tMRCA estimate using SD [(Moshiri et al., 2019)](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084).

## Mutation Rates: 
#### How are mutation rates sampled along each branch of the viral time phylogeny?
#### Model: `Truncated Normal`
- Other distributions deviate significantly from real distributions, so we use Truncated Normal.
#### mu: `0.0008`
- Location parameter of the Truncated Normal distribution.
- With the scale parameter (see below), branch lengths were scaled from years to expected number of per-site mutations [(Moshiri et al., 2019)](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084).
#### sigma: `0.0005`
- Scale parameter of the Truncated Normal distribution.
- Chosen to scale branch lengths from years to expected number of per-site mutations [(Moshiri et al., 2019)](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084).
#### a: `0`
#### b: `infinity`
- Minimum, maximum (respectively) of the Truncated Normal distribution.

## Ancestral Sequence: 
#### Describe how ancestral (root) sequence is generated/selected.
#### Model: `Exact Base Frequencies`
- A simple option with the ability to define the frequency of each base.
#### k (Length of ancestral sequence): `9200`
- The length of the HIV genome is about 9200 bases.
- Frequences (see below) were calculated using the [NCBI reference sequence for HIV-1, complete genome](https://www.ncbi.nlm.nih.gov/nuccore/NC_001802.1?report=genbank).
#### p_A: `0.3564`
#### p_C: `0.1788`
#### p_G: `0.2424`
#### p_T: `0.2224`
- Frequency of A, C, G, T bases (respectively).

## Sequence Evolution: 
#### Describe how sequences evolve down the phylogeny.
#### Model: `General Time-Reversible (GTR) + Gamma`
- General Time-Reversible "doesn't care" whether a sequence is an ancestor or descendent. The Gamma parameter allows the number of substitutions per site to change, as sampled from the Gamma distribution.
#### p_A (Frequency of A): `0.3564`
#### p_C (Frequency of C): `0.1788`
#### p_G (Frequency of G): `0.2424`
#### p_T (Frequency of T): `0.2224`
#### r_A-C (Transition rate between A and C): `1.812`
#### r_A-G (Transition rate between A and G): `9.934`
#### r_A-T (Transition rate between A and T): `0.718`
#### r_C-G (Transition rate between C and G): `0.971`
#### r_C-T (Transition rate between C and T): `9.934`
#### r_G-T (Transition rate between G and T): `1.000`
- These frequencies and transition rates were pulled from the FAVITES paper, which used parameters inferred by IQ-TREE [(Moshiri et al., 2019)](https://academic.oup.com/bioinformatics/article/35/11/1852/5161084).
#### alpha: `0.405`
- The shape parameter of Gamma model of rate heterogeneity.
- We pull substitution probabilities from a Gamma distribution. An alpha of < 1 tells us that there is a lot of variance between substitution sites. 
#### num_cats: `0`
- Number of categories in discrete Gamma model (or 0 for continuous).
#### prop_invariable (Proportion of invariable sites): `0`
- Proportion of invariable sites. 
