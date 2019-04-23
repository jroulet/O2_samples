# Supplementary material to "New Binary Black Hole Mergers in the Second Observing Run of Advanced LIGO and Advanced Virgo"

Tejaswi Venumadhav, Barak Zackay, Javier Roulet, Liang Dai, Matias Zaldarriaga

This repository provides posterior samples for events found in public LIGO/Virgo O2 data and reported in https://arxiv.org/abs/1904.07214

The samples are provided as numpy arrays, the 11 columns are:
```
['mchirp', 'eta', 's1z', 's2z', 'RA', 'DEC', 'psi', 'iota', 'vphi', 'tc', 'DL']
```
defined as follows:
* `mchirp`: chirp mass
* `eta`: mass ratio
* `s1z`: aligned spin of primary
* `s2z`: aligned spin of secondary
* `RA`: right ascension
* `DEC`: declination
* `psi`: polarization angle
* `iota`: inclination
* `vphi`: orbital phase
* `tc`: arrival time, with arbitrary offset
* `DL`: luminosity distance

The prior used to generate these posteriors is described in https://arxiv.org/abs/1902.10331 , it is uniform in component masses, effective spin and luminosity volume.

An example code `example_loading.ipynb` is provided, that loads the samples into python dictionaries.