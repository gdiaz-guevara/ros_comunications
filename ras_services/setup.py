from setuptools import find_packages, setup

package_name = 'ras_services'

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
    maintainer='DanielFLopez1620',
    maintainer_email='dfelipe.lopez@gmail.com',
    description='Package to learn about services in ROS 2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sum_server = ras_services.sum_server:main',
            'sum_client = ras_services.sum_client:main',
        ],
    },
)
