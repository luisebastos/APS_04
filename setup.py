from setuptools import setup, find_packages

setup(
    name="cubo_piramide",  
    version="1.0.0",  
    author="Luise Bastos", 
    author_email="luise@gustavobastos.com.br",  
    description="Um jogo de projeção 3D de cubo e pirâmide em wireframe usando Pygame", 
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown",  
    url="https://github.com/luisebastos/APS_04",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        "pygame>=2.0.0",
        "numpy>=1.19.0"
    ],
    entry_points={  
        'console_scripts': [
            'APS_04=APS_04.game:game',  
        ],
    },
    include_package_data=True, 
)
