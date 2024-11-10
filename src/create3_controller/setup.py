from setuptools import find_packages, setup

package_name = 'create3_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/goal.yaml']),
    ],
    install_requires=[
        'setuptools',
        'rclpy',
        'irobot_create_msgs',
        'action_msgs',
        'geometry_msgs',
        'nav_msgs',
        'tf_transformations',
        'PyYAML',
    ],
    zip_safe=True,
    maintainer='julien',
    maintainer_email='julienstocker@icloud.com',
    description='Create 3 Controller Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'undock_node = create3_controller.undock_node:main',
            'move_robot = create3_controller.move_robot:main',
            'dock_node = create3_controller.dock_node:main',
        ],
    },
)
