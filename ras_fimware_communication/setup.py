from setuptools import find_packages, setup

package_name = 'ras_fimware_communication'

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
    maintainer='gabriel',
    maintainer_email='gabrieldiaz85@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'transmitter = ras_fimware_communication.transmitter:main',
            'receiver = ras_fimware_communication.receiver:main',
            'wifi_transmitter = ras_fimware_communication.wifi_transmitter:main',
            'wifi_receiver = ras_fimware_communication.wifi_receiver:main'
        ],
    },
)
