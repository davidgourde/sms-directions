from setuptools import setup

setup(
    name='sms-directions',
    version='0.1',
    description='An offline way of getting Google Maps directions.',
    long_description='SMS-Directions is a web-app that lets users query Google Maps'\
                     ' Directions API and get the results using SMS messages, without'\
                     ' the need for a Data plan.',
    license="MIT",
    author='David Gourde',
    packages=['sms_directions'],
    install_requires=[
        'flask',
        'flask_restful',
        'flask_script',
        'gunicorn',
        'nexmo',
    ]
)