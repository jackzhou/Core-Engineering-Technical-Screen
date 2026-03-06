# Core-Engineering-Technical-Screen

# Package Sorting Challenge

## Objective

Imagine you work in a robotic automation factory.  
Your objective is to write a function for a robotic arm that dispatches packages to the correct stack according to their **volume** and **mass**.

---

## Rules

Packages must be classified based on their **dimensions** and **mass**.

### Bulky Package

A package is considered **bulky** if:

- Its **volume** (Width × Height × Length) is **≥ 1,000,000 cm³**, OR
- **Any dimension** (width, height, or length) is **≥ 150 cm**

### Heavy Package

A package is considered **heavy** if:

- **Mass ≥ 20 kg**

---

## Sorting Criteria

Packages must be dispatched into the following stacks:

| Stack | Description |
|------|-------------|
| **STANDARD** | Packages that are **not bulky and not heavy** |
| **SPECIAL** | Packages that are **either bulky OR heavy** |
| **REJECTED** | Packages that are **both bulky AND heavy** |

---

## Implementation

Implement the following function:

sort(width, height, length, mass)

Where:

| Parameter | Unit | Description |
|----------|------|-------------|
| width | cm | Package width |
| height | cm | Package height |
| length | cm | Package length |
| mass | kg | Package mass |

The function must return a **string** indicating which stack the package should go to:

STANDARD  
SPECIAL  
REJECTED  

---

## Example

sort(50, 40, 30, 10) → STANDARD  
sort(200, 30, 30, 10) → SPECIAL  
sort(200, 200, 200, 25) → REJECTED  

---
