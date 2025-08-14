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
            # NavSatFix msg 包含 latitude, longitude, altitude 属性
            lla_data.append((msg.latitude, msg.longitude, msg.altitude))
    return lla_data

def generate_kml(lla_data, output_path):
    """
    根据提取的 LLA 数据生成 KML 文件。
    """
    kml_doc = KML.kml(
        KML.Document(
            KML.Placemark(
                KML.LineString(
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
    topic_name = "receiver_lla"
    output_path = input("请输入输出 KML 文件路径: ")

    lla_data = extract_lla_from_bag(bag_path, topic_name)
    generate_kml(lla_data, output_path)
    print(f"KML 文件已保存到 {output_path}")

if __name__ == "__main__":
    main()
