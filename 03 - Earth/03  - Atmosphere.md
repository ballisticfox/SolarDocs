

The first section of this document will cover NRLMSIS model and generating tabular values via the NASA CCMC instant run system.

The NRLMSIS model can be found here: https://kauai.ccmc.gsfc.nasa.gov/instantrun/nrlmsis/

The second section will be an addendum which includes the US Standard Atmosphere model used to generate tabular values and derivatives. 





Pressure as a function of height ($h$) where $\rho$ is the density at that location and $g$ is the gravity at that location.
$$\int_h^\infty\rho(\theta,\phi,r)g(\theta,\phi,r)dr$$

$$T_T(\theta,g,r)=T(r)+(T_{LatSunMult}(\theta)+T_{LatBias}(\theta,g))\cdot T_{SunMult}(r)$$

