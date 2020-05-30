from setuptools import setup
OPTIONS = {'iconfile': 'miner_app_icon.icns'}
setup(
    app = ['CPR_Autominer.py'],
    options = {'py2app': OPTIONS},
    setup_requires = ["py2app"]
)

