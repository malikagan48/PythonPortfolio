from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Portfolio page'

# Setting up
setup(
    name="KaganKucukPortfolio",
    version=VERSION,
    author="Mustafa ali kağan Küçük",
    author_email="<mustafa.ali.kagan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)