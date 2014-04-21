%define tarname MarkupSafe

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-markupsafe
Version:	0.18
Release:	3
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRequires:	python-distribute
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%package -n python3-markupsafe
Summary:	XML/HTML/XHTML markup safe string package for Python
Group:		Development/Python

%description -n python3-markupsafe
This package implements a XML/HTML/XHTML markup safe string for Python3.

%prep
%setup -q -n %{tarname}-%{version}
rm -rf %{py3dir}
cp -a . %{py3dir}
2to3 --write --nobackups %{py3dir}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd

%install
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}/%{python3_sitearch}/markupsafe/*.c
popd

%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# C code errantly gets installed
rm %{buildroot}/%{python_sitearch}/markupsafe/*.c

%files
%doc AUTHORS LICENSE README.rst
%{python_sitearch}/*

%files -n python3-markupsafe
%doc AUTHORS LICENSE README.rst
%{python3_sitearch}/*
