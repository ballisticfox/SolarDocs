

The first section of this document will cover NRLMSIS model and generating tabular values via the NASA CCMC instant run system.

The NRLMSIS model can be found here: https://kauai.ccmc.gsfc.nasa.gov/instantrun/nrlmsis/

The second section will be an addendum which includes the US Standard Atmosphere model used to generate tabular values and derivatives. 

---
### NRLMSIS
[Paper](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EA001321)
[Model](https://ccmc.gsfc.nasa.gov/models/NRLMSIS~2.0)
[Instant Run](https://kauai.ccmc.gsfc.nasa.gov/instantrun/nrlmsis/)


NRLMSIS or the NRL Mass Spectrometer and Incoherent Scatter model is an empirical atmospheric model that extends from the ground to the exobase and describes the average observed behavior of temperature, eight species densities, and mass density via a parametric analytic formulation. The model inputs are location, day of year, time of day, solar activity, and geomagnetic activity.


##### Section 1: Temperature B-splines
#####








Pressure as a function of height ($h$) where $\rho$ is the density at that location and $g$ is the gravity at that location.
$$\int_h^\infty\rho(\theta,\phi,r)g(\theta,\phi,r)dr$$

$$T_T(\theta,g,r)=T(r)+(T_{LatSunMult}(\theta)+T_{LatBias}(\theta,g))\cdot T_{SunMult}(r)$$

$\$
