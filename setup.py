from setuptools import setup, find_packages

setup(
    name="graphrag",
    version="1.1.0",  # You might want to handle versioning differently
    description="GraphRAG: A graph-based retrieval-augmented generation (RAG) system.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Microsoft",
    author_email="alonsog@microsoft.com",  # Using first author as contact
    url="https://github.com/microsoft/graphrag",
    packages=find_packages(),
    python_requires=">=3.10,<3.13",
    install_requires=[
        "environs>=11.0.0",
        "azure-search-documents>=11.5.2",
        "lancedb>=0.17.0",
        "aiofiles>=24.1.0",
        "openai>=1.57.0",
        "nltk==3.9.1",
        "tiktoken>=0.8.0",
        "numpy>=1.25.2",
        "graspologic>=3.4.1",
        "networkx>=3.4.2",
        "pandas>=2.2.3",
        "matplotlib>=3.9.3",
        "pyarrow>=15.0.0",
        "umap-learn>=0.5.6",
        "pyyaml>=6.0.2",
        "pyaml-env>=1.2.1",
        "python-dotenv>=1.0.1",
        "pydantic>=2.10.3",
        "rich>=13.9.4",
        "devtools>=0.12.2",
        "typing-extensions>=4.12.2",
        "azure-cosmos>=4.9.0",
        "azure-identity>=1.19.0",
        "azure-storage-blob>=12.24.0",
        "future>=1.0.0",
        "typer>=0.12.0,<=0.15.1",
        "fnllm>=0.0.10",
        "tenacity>=9.0.0",
        "json-repair>=0.30.3",
        "tqdm>=4.67.1",
        "httpx>=0.27",
    ],
    extras_require={
        "dev": [
            "coverage>=7.6.9",
            "ipykernel>=6.29.5",
            "jupyter>=1.1.1",
            "nbconvert>=7.16.4",
            "poethepoet>=0.31.1",
            "pyright>=1.1.390",
            "pytest>=8.3.4",
            "pytest-asyncio>=0.24.0",
            "pytest-timeout>=2.3.1",
            "ruff>=0.8.2",
            "semversioner>=2.0.5",
            "update-toml>=0.2.1",
            "deptry>=0.21.1",
            "mkdocs-material>=9.5.48",
            "mkdocs-jupyter>=0.25.1",
            "mkdocs-exclude-search>=0.6.6",
            "pytest-dotenv>=0.5.2",
            "mkdocs-typer>=0.0.3",
        ]
    },
    entry_points={
        "console_scripts": [
            "graphrag=graphrag.cli.main:app",
        ],
    },
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
