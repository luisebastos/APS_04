from setuptools import setup, find_packages

# setup(
#     name="Cubo e Pirâmide 3D",
#     version="0.1.0",
#     packages=find_packages(),
#     install_requires=["opencv-python", "numpy"],
#     author="Luise Pessoa Bastos",
#     author_email="luise@gustavobastos.com.br",
#     description="Uma biblioteca de criptografia.",
#     long_description=open('README.md').read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/luisebastos/APS_03",
#     entry_points={
#         'console_scripts': [
#             'APS_03=APS_03.main:main',
#         ],
#     },
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',
# )

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
        "License :: OSI Approved :: MIT License",  # Tipo de licença
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
    install_requires=[  # Dependências que serão instaladas automaticamente
        "pygame>=2.0.0",
        "numpy>=1.19.0"
    ],
    entry_points={  # Criar um ponto de entrada para o jogo
        'console_scripts': [
            'APS_04=APS_04.game:game',  # Comando para rodar o jogo (troque 'nome_do_arquivo' pelo nome do seu arquivo principal)
        ],
    },
    include_package_data=True,  # Inclui arquivos não-Python, como imagens e sons, se houver
)
