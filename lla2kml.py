import rosbag
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

def extract_lla_from_bag(bag_path, topic_name):
    """
    从指定的 ROS bag 文件中提取 receiver_lla 数据。
    """
    lla_data = []
    with rosbag.Bag(bag_path, 'r') as bag:
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
            # 检查NavSatFix消息是否有效（纬度和经度不为0）
            if msg.latitude != 0 and msg.longitude != 0:
                lla_data.append((msg.latitude, msg.longitude, msg.altitude))
    return lla_data

def generate_kml(lla_data, output_path):
    """
    根据提取的 LLA 数据生成 KML 文件。
    """
    kml_doc = KML.kml(
        KML.Document(
            KML.name("GPS轨迹"),
            KML.Style(
                KML.LineStyle(
                    KML.color("ff0000ff"),  # 红色轨迹线 (AABBGGRR格式)
                    KML.width("3")  # 轨迹线宽度
                ),
                id="trackStyle"
            ),
            KML.Placemark(
                KML.name("GPS轨迹路径"),
                KML.styleUrl("#trackStyle"),
                KML.LineString(
                    KML.extrude("1"),
                    KML.tessellate("1"),
                    KML.altitudeMode("absolute"),
                    KML.coordinates(
                        " ".join([f"{lon},{lat},{alt}" for lat, lon, alt in lla_data])
                    )
                )
            )
        )
    )
    with open(output_path, 'wb') as f:
        f.write(etree.tostring(kml_doc, pretty_print=True))

def main():
    bag_path = input("请输入 ROS bag 文件路径: ")
    topic_name = "/ublox_driver/receiver_lla"  
    output_path = input("请输入输出 KML 文件路径: ")

    lla_data = extract_lla_from_bag(bag_path, topic_name)
    
    # 添加数据验证
    if not lla_data:
        print(f"警告：从topic {topic_name} 中未提取到有效的GPS数据")
        return
    
    print(f"成功提取到 {len(lla_data)} 个GPS数据点")
    generate_kml(lla_data, output_path)
    print(f"KML 文件已保存到 {output_path}")

if __name__ == "__main__":
    main()
