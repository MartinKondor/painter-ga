# 🎨 painter-ga

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/MartinKondor/painter-ga/)
[![version](https://img.shields.io/badge/version-v0.1-red.svg)](https://github.com/MartinKondor/painter-ga)
[![GitHub Issues](https://img.shields.io/github/issues/MartinKondor/painter-ga.svg)](https://github.com/MartinKondor/painter-ga/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Painter genetic algorithm.

## Getting Started

### Prerequisites

* Python 3.8.6+
* Anaconda 4.9.2+ (optional)
* Python modules from the `requirements.txt`

### Usage

To run the genetic algorithm, use the command:

```$ python .```

The generated images can be fund in the ```paintings``` directory.

To finetune the algorithm you can modify the parameters in the ```__main__.py``` file.

## Contributing

This project is open for any kind of contribution from anyone.

### Steps

1. Fork this repository
2. Create a new branch (optional)
3. Clone it
4. Make your changes
5. Upload them
6. Make a pull request here

## Examples

These test were taken with these parameters:
```python
POP_SIZE = 128  # Number of starting images
PERSON_SIZE = (32, 32,)  # Size of images
```

The ```EPOCH``` parameter varies row by row.

| No. of evolution steps  |  Best (brightest) painting |  Worst (darkest) painting | Time to finish |
|---|---|---|---|
| 16 | ![16b](images/readme/ep16-best.jpg) | ![16w](images/readme/ep16-worst.jpg)  | 00:03 |
| 32 | ![32b](images/readme/ep32-best.jpg)  | ![32w](images/readme/ep32-worst.jpg) | 00:07 |
| 64 | ![64b](images/readme/ep64-best.jpg)  | ![64w](images/readme/ep64-worst.jpg) | 00:15 |
| 128 |  ![128b](images/readme/ep128-best.jpg) | ![128w](images/readme/ep128-worst.jpg) | 00:31 |
| 256 |  ![256b](images/readme/ep256-best.jpg) | ![128w](images/readme/ep256-worst.jpg) | 01:03 |
| 1024 | ![1024b](images/readme/ep1024-best.jpg)  | ![1024w](images/readme/ep1024-worst.jpg) | 04:16 |

Their improval with each step:

<p align="center">
    <img src="images/readme/ep16.jpg" />
    <img src="images/readme/ep32.jpg" />
    <img src="images/readme/ep64.jpg" />
    <img src="images/readme/ep128.jpg" />
    <img src="images/readme/ep1024.jpg" />
</p>

## Authors

* **[Martin Kondor](https://github.com/MartinKondor)**

<p align="center">
<a title="Fiverr" href="https://www.fiverr.com/martinkondor">
<img id="fiverr-img" class="img-responsive" alt="Hire me on fiverr!" title="Hire me on fiverr!" src="https://martinkondor.github.io/img/hire_me_on_fiverr_button.png" width="222">
</a>
</p>

# License

Copyright (C) 2022 Martin Kondor.

See the [LICENSE](LICENSE) file for details.