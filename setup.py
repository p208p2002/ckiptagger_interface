import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

# with open('requirements.txt','r',encoding = 'utf-8') as f:
    # requirements = f.read().split("\n")

setuptools.setup(
    name="ckiptagger_interface", # 
    version='0.0.1',
    author="Philip Huang",
    author_email="p208p2002@gmail.com",
    description="interface for CkipTagger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p208p2002/interface-for-ckiptagger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # install_requires = requirements
)