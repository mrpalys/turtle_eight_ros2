from setuptools import find_packages, setup

package_name = 'turtle_eight'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mrpalys',
    maintainer_email='mrpalys@todo.todo',
    description='ROS2 node to move turtlesim in a figure-eight',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_eight_node = turtle_eight.turtle_eight_node:main',
        ],
    },
)

