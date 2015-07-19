%define tarname MarkupSafe

Summary:	XML/HTML/XHTML markup safe string package for Python


Name:		python-markupsafe
Version:	0.23
Release:	6
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
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
2to3 --write --nobackups ../python3

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
%doc AUTHORS LICENSE README.rst
%{py_platsitedir}/*

%files -n python2-markupsafe
%doc AUTHORS LICENSE README.rst
%{py2_platsitedir}/*
