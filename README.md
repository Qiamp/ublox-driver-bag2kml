# ROS Bag to KML Converter

## 项目简介

该项目提供了一个 Python 脚本，用于从[gnss_driver](https://github.com/JIAHAO-FUHUA/gnss_driver) 录取的ROS bag 文件中针对receiver_lla Topic提取 GPS 数据（latitude, longitude, altitude），并将其转换为 KML 文件，以便在地理信息软件（如 Google Earth）中可视化。

## 文件结构

- `lla2kml.py`: 主脚本文件，包含数据提取和 KML 文件生成的逻辑。

## 依赖项

运行该脚本需要以下 Python 库：

- `rosbag`: 用于读取 ROS bag 文件。
- `pykml`: 用于生成 KML 文件。
- `lxml`: 用于处理 XML 数据。

可以使用以下命令安装依赖项：

```bash
pip install rosbag pykml lxml
```

## 使用方法

1. 确保安装了所有依赖项。
2. 运行脚本：
   ```bash
   python lla2kml.py
   ```
3. 按提示输入 ROS bag 文件路径和输出 KML 文件路径。
4. 脚本会从指定的 ROS bag 文件中提取 `receiver_lla` 主题的数据，并生成对应的 KML 文件。

## 示例

假设有一个 ROS bag 文件路径为 `/path/to/bagfile.bag`，输出的 KML 文件路径为 `/path/to/output.kml`，运行脚本后会生成一个包含 GPS 数据的 KML 文件。

## 注意事项

- 脚本默认提取 `receiver_lla` 主题的数据。如果需要提取其他主题，请修改脚本中的 `topic_name`。
- 确保 ROS bag 文件中包含有效的 GPS 数据。

## 许可证

该项目遵循MIT开源许可
