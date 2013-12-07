%define	eggname	MarkupSafe
%define	modname	markupsafe
%define	enable_tests 0

# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-%{modname}
Version:	0.18
Release:	5
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRequires:	python-distribute
BuildRequires:	python3-distribute
%if %{enable_tests}
BuildRequires:	python-nose
BuildRequires:	python3-nose
%endif
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%package -n python3-%{modname}
Summary:	XML/HTML/XHTML markup safe string package for Python3

%description -n python3-%{modname}
This package implements a XML/HTML/XHTML markup safe string for Python3.

%prep
%setup -q -c

mv %{eggname}-%{version} python2
cp -r python2 python3

%build
pushd python2
PYTHONDONTWRITEBYTECODE= python setup.py build
popd

pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py install --root=%{buildroot}
rm -rf %{buildroot}/%{py3_platsitedir}/%{modname}/__pycache__
popd

%check
%if %{enable_tests}
pushd python2
nosetests
popd

pushd python3
nosetests
popd
%endif

%files
%doc python2/AUTHORS python2/LICENSE python2/README.rst
%dir %{py_platsitedir}/%{modname}
%{py_platsitedir}/%{modname}/*.py*
%{py_platsitedir}/%{modname}/*.so
%{py_platsitedir}/%{modname}/*.c
%dir %{py_platsitedir}/%{eggname}-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/%{eggname}-%{version}-py%{py_ver}.egg-info/*

%files -n python3-%{modname}
%doc python3/AUTHORS python3/LICENSE python3/README.rst
%dir %{py3_platsitedir}/%{modname}
%{py3_platsitedir}/%{modname}/*.py*
%{py3_platsitedir}/%{modname}/*.so
%{py3_platsitedir}/%{modname}/*.c
%dir %{py3_platsitedir}/%{eggname}-%{version}-py%{py3_ver}.egg-info
%{py3_platsitedir}/%{eggname}-%{version}-py%{py3_ver}.egg-info/*

