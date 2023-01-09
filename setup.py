from setuptools import setup
import os
from glob import glob

package_name = 'snake_calibration'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Wenpeng Wang',
    maintainer_email='wwang153@jhu.edu',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'CapaCam_mapper = snake_calibration.snake_capa_cam_mapper:main',
        ],
    },
)
