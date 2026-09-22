# 核桃派2代

[English](README.md) | **中文**

![CanMV-K230 banner](assets/banner_zh.png)

## 支持产品

| 产品 | 处理器 | NPU | 内存 | 存储 | 无线网络 | 有线网络 | 显示 | 尺寸 | 购买 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [核桃派 2B][1] | T527 | 2TOPS | 1/2/4GB LPDDR4 | EMMC/MicroSD | 双频WiFi6+BT5.0 | 千兆 | HDMI / MIPI DSI 4lane| 85×56×21mm | [🛒][4] |
| [核桃派 CM2][2] | K230 | 2TOPS | 1/2/4GB LPDDR4 | EMMC/MicroSD | 双频WiFi6+BT5.0 | 千兆 | HDMI / MIPI DSI 4lane | 55x40x4mm | [🛒][5] |

[1]: https://wiki.walnutpi.com/docs/walnutpi_2/intro/hw-parameter/#%E6%A0%B8%E6%A1%83%E6%B4%BE2b
[2]: https://wiki.walnutpi.com/docs/walnutpi_2/intro/hw-parameter/#%E6%A0%B8%E6%A1%83%E6%B4%BEcm2

[4]: https://item.taobao.com/item.htm?id=884822853972
[5]: https://item.taobao.com/item.htm?id=1083412062313

## 目录结构

```
walnutpi-2/
├── examples/          # 示例代码（按功能分类）
│   ├── 01_python_embedded/ # Python嵌入式
│   ├── 02_opencv/      # 机器视觉
│   ├── 03_pyqt5/       # 图形化显示
│   ├── 04_sensor/      # 传感器
│   └── 05_yolo11/      # 扩展应用
├── hardware/          # 硬件设计资料（原理图、封装、3D 模型）
├── CHANGELOG.md       # 更新日志
├── LICENSE
├── README.md          # 英文说明
└── README_zh.md       # 中文说明
```

## 快速上手

1. 到仓库 [Releases](https://github.com/walnutpi/walnutpi-2/releases) 页面下载最新镜像；
2. 镜像烧录教程：https://wiki.walnutpi.com/docs/walnutpi_2/getting_start/os-install

## 开发资源

- [Wiki（教程文档）](https://wiki.walnutpi.com/docs/walnutpi_2)
- [AI在线训练模型平台 (YOLO11)](https://ai.01studio.cc)

## 更新日志

请参阅 [CHANGELOG.md](CHANGELOG.md)。

## 技术支持

遇到问题可通过以下方式获取支持：

1. **GitHub Discussions**：前往 [WalnutPi-2 Discussions](https://github.com/walnutpi/walnutpi-2/discussions) 提问交流；
2. **邮件联系**：发送邮件至 [walnutpi@qq.com](mailto:walnutpi@qq.com)。