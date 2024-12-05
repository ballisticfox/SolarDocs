

The first section of this document will cover NRLMSIS model and generating tabular values via the NASA CCMC instant run system.

The NRLMSIS model can be found here: https://kauai.ccmc.gsfc.nasa.gov/instantrun/nrlmsis/

The second section will be an addendum which includes the US Standard Atmosphere model used to generate tabular values and derivatives. 

---
### NRLMSIS
[Paper](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EA001321)
[Model](https://ccmc.gsfc.nasa.gov/models/NRLMSIS~2.0)
[Instant Run](https://kauai.ccmc.gsfc.nasa.gov/instantrun/nrlmsis/)


NRLMSIS or the NRL Mass Spectrometer and Incoherent Scatter model is an empirical atmospheric model that extends from the ground to the exobase and describes the average observed behavior of temperature, eight species densities, and mass density via a parametric analytic formulation. The model inputs are location, day of year, time of day, solar activity, and geomagnetic activity.


##### Section 1: Geopotential Height

Due to gravity not falling off in a linear fashion but in a 2nd order fashion ($\frac{GM}{r^2}$) any integrals using a standard vertical coordinate can become increasingly complex. To remedy this, MSIS uses the geopotential height $\zeta$ as the vertical coordinate which drastically simplifies the equations in section 3. 

MSIS calculates the geopotential height as a function of the geodetic altitude and latitude, relative to the [WGS-84 reference ellipsoid](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS_84)and its associated gravity model which excludes both longitudinal variations and zonal harmonics higher than order 2.

MSIS also has a standard gravity value of $g_0=9.80665 \text{ m/s}^2$



##### Section 2: Vertical Temperature Profile

The local temperature profile is parameterized as a linear combination of cubic B-splines below 122.5 km and a Bates thermospheric temperature profile above 122.5km

$$
\frac{1}{T(\zeta)}=
\begin{cases} 
      \{T_{ex}-(T_{ex}-T_B)\exp[-\sigma(\zeta-\zeta_B])\}^{-1} &;& \zeta\geq\zeta_B \\\\
      \sum^{N_s-1}_{i=0}\alpha_iS_i(\zeta) &;&\zeta<\zeta_B

   \end{cases}
$$
$T(\zeta)$ - Temperature profile as a function of geopotential height
$\zeta_B=122.5\text{ km}$ - Bates profile reference height and joining height
$T_{ex}$ - Exospheric Temperature (fitting parameter)
$\sigma=\frac{T_B'}{T_{ex}-T_B}$ - Shape parameter
$T_B'=\left.\frac{dT}{d\zeta}\right|_{\zeta=\zeta_B}$ - Temperature gradient at $\zeta_B$ (fitting parameter)
$N_s=24$ - Number of B-spline basis functions
$\alpha_i$ - Coefficients on B‐spline basis functions (fitting parameters)
$S_i$ - Cubic B-splines with nodes at heights $\zeta_{S,i};i=0$ to $N_s+3$
$\zeta_{s,i}=\{-15, -10, -5, 0, 5, ..., 80, 85, 92.5, 102.5, 112.5, 132.5, 142.5, 152.5\} \text{ km}$

Node spacing is 5km below 85km, and increases to 10km at 102.5km. At the joining altitude of 122.5km ($\zeta_B$), the profile is C2 continuous (continuous on the zeroth, first and second derivatives).

The profile is defined by 24 parameters, the first 21 spline coefficients and the 3 Bates parameters.

This simple profile represents the 'global average' which is defined by MSIS to include only the lead term of the expansion described in section 4, that is, the average over an entire annual cycle, with moderate solar activity ($F_{10.7}=150$) and quiet geomagnetic activity $(Ap=4)$



##### Section 3: Vertical Density Profile
The basic local number density profile is parameterized assuming hydrostatic balance in the lower and middle atmosphere and species-by-species hydrostatic equilibrium in the upper thermosphere, using an effective mass profile to transition smoothly between the two regimes. Chemical and dynamical correction terms are also applied to some species. The formulas presented in this section describe the profile of any single species for simplicity, species subscripts are omitted.

$$\ln(n(\zeta))=\ln(n_0)-\frac{g_0}{k}\int^\zeta_{\zeta_0}\frac{M(\zeta')}{T(\zeta')}d\zeta'-\ln(\frac{T(\zeta)}{T(\zeta_0)}-Ce^{-(\zeta-\zeta_C)/H_C}+R\left[1+\tanh\left(\frac{\zeta-\zeta_R}{\gamma(\zeta)H_R}\right)\right]$$

$n(\zeta)$ - Number density of a particular species
$n_0=n(\zeta_0)$ - Reference density (defined below)
$\zeta_0$ - Reference geopotential height
$g_0$ - Reference gravitational constant
$k$ - Boltzmann constant
$M(\zeta)$ - Effective mass profile (defined below)
$C,\zeta_C,H_c$ - Chemical loss term paramters
$R,\zeta_R,H_R$ Chemical/dynamical correction parameters
$\gamma(\zeta)=\frac{1}{2}\{1+\tanh(\frac{\zeta-\zeta_\gamma}{H_\gamma})\}$
$\zeta_\gamma$ - 70km
$H_\gamma$ = 40km

The first term $n_0$ on the right-hand side of Eq 2 scales the entire profile and (in the absence of chemical and dynamical corrections) is equal to the species density at the fiducial height of $\zeta_0$. The second term is the hydrostatic integral, which includes an effective mass profile is described below. The third term represents the ideal gas law; this term and the hydrostatic integral couple the temperature profile to the density profile. The fourth term is a Chapman-like bottom-side chemical loss function; the model applies this term to O, H, and N, which experience photochemical production and loss similar to that of the ionosphere. The last term  
is a logistic function (expressed in hyperbolic tangent form) used for chemical and/or dynamical perturbations.
##### Section 4: Expansion of Vertical Proﬁle Parameters








Pressure as a function of height ($h$) where $\rho$ is the density at that location and $g$ is the gravity at that location.
$$\int_h^\infty\rho(\theta,\phi,r)g(\theta,\phi,r)dr$$

$$T_T(\theta,g,r)=T(r)+(T_{LatSunMult}(\theta)+T_{LatBias}(\theta,g))\cdot T_{SunMult}(r)$$

$\$
