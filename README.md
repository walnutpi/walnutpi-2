# WalnutPi 2

**English** | [中文](README_zh.md)

![WalnutPi 2 banner](assets/banner.png)

## Supported Products

| Product | Processor | NPU | Memory | Storage | Wireless | Ethernet | Display | Dimensions | Buy |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [WalnutPi 2B][1] | T527 | 2TOPS | 1/2/4GB LPDDR4 | EMMC/MicroSD | Dual-band WiFi6 + BT5.0 | Gigabit | HDMI / MIPI DSI 4lane| 85×56×21mm | [🛒][4] |
| [WalnutPi CM2][2] | T527 | 2TOPS | 1/2/4GB LPDDR4 | EMMC/MicroSD | Dual-band WiFi6 + BT5.0 | Gigabit | HDMI / MIPI DSI 4lane | 55x40x4mm | [🛒][5] |

[1]: https://wiki.walnutpi.com/en/docs/walnutpi_2/intro/hw-parameter/#walnut-pi-2b
[2]: https://wiki.walnutpi.com/en/docs/walnutpi_2/intro/hw-parameter/#walnut-pi-cm2

[4]: https://www.aliexpress.com/item/1005008529154262.html
[5]: https://www.aliexpress.com/item/1005013243909284.html

## Repository Structure

```
walnutpi-2/
├── examples/          # Example code (grouped by function)
│   ├── 01_python_embedded/ # Python embedded
│   ├── 02_opencv/      # Machine vision
│   ├── 03_pyqt5/       # Graphical display
│   └── 04_yolo11/      # Expansion applications
├── hardware/          # Hardware design files (schematics, footprints, 3D models)
├── CHANGELOG.md       # Changelog
├── LICENSE
├── README.md          # English documentation
└── README_zh.md       # Chinese documentation
```

## Quick Start

1. Download the latest image from the repository [Releases](https://github.com/walnutpi/walnutpi-2/releases) page;
2. Image flashing tutorial: https://wiki.walnutpi.com/en/docs/walnutpi_2/getting_start/os-install

## Development Resources

- [Wiki (tutorial documentation)](https://wiki.walnutpi.com/en/docs/walnutpi_2)
- [AI online model training platform (YOLO11)](https://ai.01studio.cc)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Technical Support

If you encounter any issues, you can get support through the following channels:

1. **GitHub Discussions**: Ask questions and communicate in [WalnutPi-2 Discussions](https://github.com/walnutpi/walnutpi-2/discussions);
2. **Email**: Send an email to [walnutpi@qq.com](mailto:walnutpi@qq.com).
