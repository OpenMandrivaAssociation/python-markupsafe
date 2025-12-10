%define tarname markupsafe

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-markupsafe
Version:	3.0.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/project/MarkupSafe/
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
%rename python3-markupsafe
Obsoletes:	python2-markupsafe < %{EVRD}

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%files
%{py_platsitedir}/*
