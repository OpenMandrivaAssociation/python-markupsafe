%define tarname MarkupSafe

Summary:	XML/HTML/XHTML markup safe string package for Python


Name:		python-markupsafe
Version:	2.1.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
%rename python3-markupsafe
Obsoletes:	python2-markupsafe < %{EVRD}

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%prep
%autosetup -p1 -n %{tarname}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%{py_platsitedir}/*
