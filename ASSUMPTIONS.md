# Core Assumptions for Bio-Energy Comparative Analysis

This document outlines the key numerical values used for comparing land‑use efficiency between solar energy generation and carbon sequestration via afforestation. All values are based on publicly available data from reputable sources.

---

## 1. Solar Energy Generation

**Average annual energy output per square meter of solar panels**  
`180 kWh/m²/year`

*Rationale*:  
- The average global horizontal irradiance in many temperate regions is approximately 1,000–1,200 kWh/m²/year.  
- Modern photovoltaic panels have a conversion efficiency of 15–20 %.  
- Using a conservative estimate of **18 %** overall system efficiency yields `1,000 × 0.18 = 180 kWh/m²/year`.

*Source*:  
- National Renewable Energy Laboratory (NREL). *“Photovoltaic System Performance”* (typical annual yield data).  
- International Energy Agency (IEA). *“Trends in Photovoltaic Applications 2023”*.

---

## 2. Carbon Sequestration by Trees

**CO₂ sequestration rate per mature tree**  
`22 kg CO₂/tree/year`

*Rationale*:  
- A mature temperate‑zone tree can absorb between 20 and 25 kg of CO₂ annually.  
- The value of **22 kg/tree/year** is a widely cited average for deciduous and coniferous trees in managed forests.

*Source*:  
- United States Department of Agriculture (USDA) Forest Service. *“Carbon Sequestration in Forests”*.  
- Intergovernmental Panel on Climate Change (IPCC) guidelines for national greenhouse gas inventories.

**Recommended tree planting density**  
`1,000 trees/hectare` (equivalent to `0.1 trees/m²`)

*Rationale*:  
- Afforestation projects often aim for a stocking density of 1,000–1,500 trees per hectare to allow adequate space for canopy development.  
- **1,000 trees/hectare** is a common target for sustainable forest management.

*Source*:  
- Food and Agriculture Organization of the United Nations (FAO). *“Forest Resources Assessment 2020”*.  
- World Resources Institute (WRI). *“Global Forest Watch”*.

---

## 3. Unit Conversions

- 1 hectare (ha) = 10,000 m²  
- 1 metric tonne (t) = 1,000 kg  

These conversions are used internally to scale calculations between square meters and hectares, and to express results in consistent units (kWh for energy, kg for CO₂).

---

## 4. Limitations and Notes

- The above figures are **averages** and will vary with local climate, soil conditions, tree species, solar‑panel technology, and maintenance practices.  
- The comparison assumes that the entire land area is either fully covered by solar panels or fully planted with trees at the given density. Real‑world layouts (access paths, spacing, infrastructure) would reduce the effective usable area.  
- The model does not account for temporal factors (growth period of trees, degradation of solar panels, seasonal variations) or secondary benefits (biodiversity, water retention, social value).  

These assumptions provide a consistent baseline for a first‑order comparison. Users are encouraged to adjust the numbers in this file to reflect local conditions or more specific project data.