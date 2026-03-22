from setuptools import find_packages, setup

package_name = "distance_sensor_bonus"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(include=["distance_sensor_bonus", "distance_sensor_bonus.*"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="amithbiju",
    maintainer_email="amithbiju@example.com",
    description="Simple ROS 2 distance publisher and subscriber example.",
    license="Apache-2.0",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "distance_publisher = distance_sensor_bonus.distance_publisher:main",
            "rover_decision_node = distance_sensor_bonus.rover_decision_node:main",
            "command_listener = distance_sensor_bonus.command_listener:main",
        ],
    },
)
