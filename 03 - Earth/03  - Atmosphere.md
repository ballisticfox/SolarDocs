
*Sources: 
U.S. Standard Atmosphere 1976: https://ntrs.nasa.gov/api/citations/19770009539/downloads/19770009539.pdf
The 1976 Standard Atmosphere Above 86-km Altitude https://ntrs.nasa.gov/api/citations/19770003812/downloads/19770003812.pdf

Gas Species - Molecular Weights - Fractional Volume @ sea-level, dry air

| Gas Species | Molecular Weight (kg/kmol) | Fractional Volume, (*dimensionless*) |
| ----------- | -------------------------- | ------------------------------------ |
| $N_2$       | 28.0134                    | 0.78084                              |
| $O_2$       | 31.9988                    | 0.209476                             |
| $Ar$        | 39.948                     | 0.00934                              |
| $CO_2$      | 44.00995                   | 0.000314                             |
| $Ne$        | 20.183                     | 0.00001818                           |
| $He$        | 4.0026                     | 0.00000524                           |
| $Kr$        | 83.80                      | 0.00000114                           |
| $Xe$        | 131.30                     | 0.000000087                          |
| $CH_4$      | 16.04303                   | 0.000002                             |
| $H_2$       | 2.01594                    | 0.0000005                            |


Defined Reference Levels for the 7 different atmospheric profiles

| Subscript ($b$) | Geopotential Height (km) | Molecular Scale Temperature Gradient $L_M,b$ (K/km) | For $T\to H$ |
| --------------- | ------------------------ | --------------------------------------------------- | ------------ |
| 0               | 0                        | -6.5                                                | Linear       |
| 1               | 11                       | 0.0                                                 | Linear       |
| 2               | 20                       | +1.0                                                | Linear       |
| 3               | 32                       | +2.8                                                | Linear       |
| 4               | 47                       | 0.0                                                 | Linear       |
| 5               | 51                       | -2.8                                                | Linear       |
| 6               | 71                       | -2.0                                                | Linear       |
| 7               | 86                       |                                                     |              |

Calculator Found here:
https://www.digitaldutch.com/atmoscalc/table.htm



```js
let altitude;
let temperature;
let pressure;
let density;
let speedOfSound;
let viscosities;
let deltaTemperature = 0;  // Deviation from standard temperature

/**
 * All calculations are in SI units
 * @return {string}
 */
function calculateAtmosphere(){
  const airMolWeight  = 28.9644;  // Molecular weight of air
  const densitySL     = 1.225;    // Density at sea level [kg/m3]
  const pressureSL    = 101325;   // Pressure at sea level [Pa]
  const temperatureSL = 288.15;   // Temperature at sea level [deg K]
  const gamma         = 1.4;
  const gravity       = 9.80665;  // Acceleration of gravity [m/s2]
  const RGas          = 8.31432;  // Gas constant [kg/Mol/K]
  const R             = 287.053;  //

  const altitudes    = [0, 11000, 20000, 32000, 47000, 51000, 71000, 84852];
  const pressuresRel = [1, 2.23361105092158e-1, 5.403295010784876e-2, 8.566678359291667e-3, 1.0945601337771144e-3, 6.606353132858367e-4, 3.904683373343926e-5, 3.6850095235747942e-6];
  const temperatures = [288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.946];
  const tempGrads    = [-6.5, 0, 1, 2.8, 0, -2.8, -2, 0]; // Temperature gradient [deg K/m]
  const gMR          = gravity * airMolWeight / RGas;

  // Make sure altitude is within range
  if ((altitude < -5000) || (altitude > 86000)) {
    altitude     = 0;
    temperature  = 0;
    pressure     = 0;
    density      = 0;
    speedOfSound = 0;
    viscosities  = 0;

    return "Error: Altitude must be between -5000 and 86000 meter.";
  }

  if (isNaN(deltaTemperature)) deltaTemperature = 0;

  // Find correct altitude region
  let i = 0;
  if (altitude > 0) {
    while (altitude > altitudes[i+1]) {
      i++;
    }
  }

  const baseTemp        = temperatures[i];
  const tempGrad        = tempGrads[i] / 1000;
  const pressureRelBase = pressuresRel[i];
  const deltaAltitude   = altitude - altitudes[i];
  temperature           = baseTemp + tempGrad * deltaAltitude;

  // Calculate relative pressure
  let pressureRelative;
  if (Math.abs(tempGrad) < 1e-10) 
	  pressureRelative = pressureRelBase * Math.exp(-gMR * deltaAltitude/1000 / baseTemp);
  else                            
	  pressureRelative = pressureRelBase * Math.pow(baseTemp / temperature, gMR/tempGrad/1000);

  
  // Add temperature offset
  temperature  = temperature + deltaTemperature;

  speedOfSound = Math.sqrt(gamma * R * temperature);
  pressure     = pressureRelative * pressureSL;
  density      = densitySL * pressureRelative * temperatureSL / temperature ;
  viscosities  = 1.512041288 * Math.pow(temperature, 1.5) / ((temperature) + 120) / 1000000.0;
}
```