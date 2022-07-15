![16bb](images/readme/ep16-best.jpg)
![32bb](images/readme/ep32-best.jpg)
![64bb](images/readme/ep64-best.jpg)
![128bb](images/readme/ep128-best.jpg)
![256bb](images/readme/ep256-best.jpg)
![512bb](images/readme/ep512-best.jpg)
![1024bb](images/readme/ep1024-best.jpg)

![16bb](images/readme/ep16-worst.jpg)
![32bb](images/readme/ep32-worst.jpg)
![64bb](images/readme/ep64-worst.jpg)
![128bb](images/readme/ep128-worst.jpg)
![256bb](images/readme/ep256-worst.jpg)
![512bb](images/readme/ep512-worst.jpg)
![1024bb](images/readme/ep1024-worst.jpg)

# 🎨 painter-ga

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](./)
[![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](./)

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/MartinKondor/painter-ga/)
[![version](https://img.shields.io/badge/version-v1.1-brightgreen.svg)](https://github.com/MartinKondor/painter-ga)
[![GitHub Issues](https://img.shields.io/github/issues/MartinKondor/painter-ga.svg)](https://github.com/MartinKondor/painter-ga/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

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
POP_SIZE = 100  # Number of starting images
PERSON_SIZE = (32, 32,)  # Size of images
```

The ```EPOCH``` parameter varies row by row.

| No. of evolution steps  |  Best (brightest) painting |  Worst (darkest) painting | Time to finish
|---|---|---|---|
| 16 | ![16b](images/readme/ep16-best.jpg) | ![16w](images/readme/ep16-worst.jpg)  | 00:03 |
| 32 | ![32b](images/readme/ep32-best.jpg)  | ![32w](images/readme/ep32-worst.jpg) | 00:06 |
| 64 | ![64b](images/readme/ep64-best.jpg)  | ![64w](images/readme/ep64-worst.jpg) | 00:12 |
| 128 |  ![128b](images/readme/ep128-best.jpg) | ![128w](images/readme/ep128-worst.jpg) | 00:24 |
| 256 |  ![256b](images/readme/ep256-best.jpg) | ![256w](images/readme/ep256-worst.jpg) | 00:48 |
| 512 |  ![512b](images/readme/ep512-best.jpg) | ![512w](images/readme/ep512-worst.jpg) | 01:37 |
| 1024 | ![1024b](images/readme/ep1024-best.jpg)  | ![1024w](images/readme/ep1024-worst.jpg) | 03:18 |

_On average 5.25 it/s._

Their improval with each step:

<p align="center">
    <img src="images/readme/ep16.png" alt="ep16" width="400px">
    <img src="images/readme/ep32.png" alt="ep32" width="400px">
    <img src="images/readme/ep64.png" alt="ep64" width="400px">
    <img src="images/readme/ep128.png" alt="ep128" width="400px">
    <img src="images/readme/ep256.png" alt="ep256" width="400px">
    <img src="images/readme/ep512.png" alt="ep512" width="400px">
    <img src="images/readme/ep1024.png" alt="ep1024" width="800px">
</p>

## Authors

* **[Martin Kondor](https://github.com/MartinKondor)**

<p align="center">
<a title="Fiverr" href="https://www.fiverr.com/martinkondor">
<img id="fiverr-img" class="img-responsive" alt="Hire me on fiverr!" title="Hire me on fiverr!" src="https://martinkondor.github.io/img/hire_me_on_fiverr_button.png" width="222">
</a>
</p>

# License

Copyright &copy; 2022 Martin Kondor.

See the [LICENSE](LICENSE) file for details.
