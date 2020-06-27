# Supplementary material to "New Binary Black Hole Mergers in the Second Observing Run of Advanced LIGO and Advanced Virgo"

Tejaswi Venumadhav, Barak Zackay, Javier Roulet, Liang Dai, Matias Zaldarriaga

This repository provides posterior samples for 7 binary black hole merger events found in public LIGO/Virgo O1 and O2 data and reported in https://arxiv.org/abs/1904.07214 and https://arxiv.org/abs/1902.10331, as well as for the 10 binary black holes reported by the LIGO and Virgo Collaborations.

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

The prior used to generate all these posteriors is described in https://arxiv.org/abs/1902.10331 , it is uniform in component masses, effective spin and luminosity volume. The waveform model used was IMRPhenomD [10.1103/PhysRevD.93.044007]. 

A snippet `load_samples.py` is provided, that loads the samples into python dictionaries:
```
import load_samples
ev_samples_dic = load_samples.load_samples()
```

### 2020/06/26 edit
* We update the parameter estimation samples following improvements in our parameter estimation code. The improvement consisted in adopting a parametrization of the sampled space in which the posterior distributions are better behaved. The main effect is a mild change in the mass ratio distributions, especially close to $q \approx 1$. The new samples should be preferred and are loaded by default with the above snippet.
* We now include data from the Virgo detector in the parameter estimation of GW170729. The Virgo data for GW170729 was overlooked in the previous release.
* The previous version of the samples was moved to `legacy/`.
* Note about `vphi` and `psi`: for non-precessing waveform models with quadrupolar radiation $(\ell, m) = (2, \pm2)$ such as IMRPhenomD there is a discrete symmetry $\varphi, \psi \to \varphi + \pi/2, \psi + \pi/2$. We exploit this symmetry by sampling in the variables $\varphi + \psi$ and $\varphi - \psi$ from 0 to $\pi$. For this reason the 2d posterior in $\varphi, \psi$ variables is truncated, and the 1d posterior is distorted. If these distributions are of interest, one may duplicate the set of samples, and transform the copy as follows: $\varphi, \psi \to \varphi + \pi/2, \psi + \pi/2$ and fold $\varphi, \psi$ to $(0, \pi)$.

### Acknowledgement

This research has made use of data, software and/or web tools obtained from the Gravitational Wave Open Science Center (https://www.gw-openscience.org), a service of LIGO Laboratory, the LIGO Scientific Collaboration and the Virgo Collaboration. LIGO is funded by the U.S. National Science Foundation. Virgo is funded by the French Centre National de Recherche Scientifique (CNRS), the Italian Istituto Nazionale della Fisica Nucleare (INFN) and the Dutch Nikhef, with contributions by Polish and Hungarian institutes.