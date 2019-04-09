%define tarname MarkupSafe

Summary:	XML/HTML/XHTML markup safe string package for Python


Name:		python-markupsafe
Version:	1.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/b9/2e/64db92e53b86efccfaea71321f597fa2e1b2bd3853d8ce658568f7a13094/MarkupSafe-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python3-distribute
%rename python3-markupsafe

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%package -n python2-markupsafe
Summary:	XML/HTML/XHTML markup safe string package for Python 2
Group:		Development/Python
BuildRequires:	python2-distribute

%description -n python2-markupsafe
This package implements a XML/HTML/XHTML markup safe string for Python
2.x.

%prep
%setup -q -n %{tarname}-%{version}
rm -rf ../python3
cp -a . ../python3

%build
CFLAGS="%{optflags}" python2 setup.py build
pushd ../python3
CFLAGS="%{optflags}" python setup.py build
popd

%install
pushd ../python3
python setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}/%{py_platsitedir}/markupsafe/*.c
popd

python2 setup.py install -O1 --skip-build --root %{buildroot}
# C code errantly gets installed
rm %{buildroot}/%{py2_platsitedir}/markupsafe/*.c

%files
%doc README.rst
%{py_platsitedir}/*

%files -n python2-markupsafe
%doc AUTHORS LICENSE README.rst
%{py2_platsitedir}/*
