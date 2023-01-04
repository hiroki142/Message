from setuptools import setup

package_name = 'Message'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hiroki Nukui',
    maintainer_email='s21C1092OD@s.chibakoudai.jp',
    description='a package for task',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = Message.talker:main',
            'listener = Message.listener:main',
        ],
    },
)
