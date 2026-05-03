---
title: "ddinteract: Double-Demeaned Interactions Estimator"
summary: A Python package for estimating two-way fixed-effects models with interaction terms via the double-demeaning (within) transformation.
date: 2026-05-03
type: docs
weight: 1
tags:
  - Python
  - Econometrics
  - Panel Data
  - Fixed Effects
  - Interactions
links:
  - name: PyPI
    url: https://pypi.org/project/ddinteract/
    icon: python
    icon_pack: fab
  - name: GitHub
    url: https://github.com/nkoutoun/dd-ie
    icon: github
    icon_pack: fab
---

## Overview

`ddinteract` is a Python package that implements the **double-demeaned interactions estimator** for two-way fixed-effects panel models with interaction terms. It provides a fast, transparent way to estimate interaction effects in panel data settings while properly absorbing unit and time fixed effects.

- **PyPI:** [pypi.org/project/ddinteract](https://pypi.org/project/ddinteract/)
- **GitHub:** [github.com/nkoutoun/dd-ie](https://github.com/nkoutoun/dd-ie#readme)

## Installation

```bash
pip install ddinteract
```

## Use in My Research

I have used `ddinteract` in the following papers:

- [Assessing the heterogeneous impact of COVID-19 on consumption using bank transactions](/publication/pub-covid/) — *Journal of Macroeconomics*, 2025.
- [Shale Production and the Transmission of Oil Supply Shocks: Evidence from U.S. States](/publication/wip-oil/) — Work in progress.

In both projects, the estimator is used to recover heterogeneous effects across units (households, U.S. states) by interacting a shock or policy variable with unit-level characteristics, while absorbing two-way fixed effects.

## Documentation and Source Code

Full documentation, usage examples, and the source code are available on the [GitHub repository](https://github.com/nkoutoun/dd-ie#readme). Issues and contributions are welcome.
