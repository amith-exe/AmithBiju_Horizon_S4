from setuptools import find_packages, setup

package_name = "distance_sensor"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(include=["distance_sensor", "distance_sensor.*"]),
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
            "distance_publisher = distance_sensor.distance_publisher:main",
            "distance_subscriber = distance_sensor.distance_subscriber:main",
        ],
    },
)
