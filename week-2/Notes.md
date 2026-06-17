comparing the pip and uv workflows :-

pip:-
* pip (Pip Installs Packages) is the default package manager for Python
* It is used to download, install, upgrade, and manage Python packages from the Python Package Index (PyPI).
* pip install requests
* Uses venv separately




uv :-
* uv is a modern, high-performance Python package and project manager written in Rust.
* It can create virtual environments, install packages, and manage dependencies much faster than traditional tools like pip.
* uv pip install requests
* Can create environments directly (uv venv)


* requirements.txt 
certifi==2026.6.17
charset-normalizer==3.4.7
idna==3.18
requests==2.34.2
urllib3==2.7.0