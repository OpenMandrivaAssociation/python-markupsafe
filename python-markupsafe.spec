%define	eggname	MarkupSafe
%define	modname	markupsafe
%define	enable_tests 0

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-%{modname}
Version:	0.12
Release:	%mkrel 1
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/%{eggname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-setuptools
%if %enable_tests
BuildRequires:	python-nose
%endif
BuildRequires:	python-devel

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%prep
%setup -q -n %{eggname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%check
%if %enable_tests
nosetests
%endif

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.rst
%dir %{py_platsitedir}/%{modname}
%{py_platsitedir}/%{modname}/*.py*
%{py_platsitedir}/%{modname}/*.so
%{py_platsitedir}/%{modname}/*.c
%dir %{py_platsitedir}/%{eggname}-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/%{eggname}-%{version}-py%{py_ver}.egg-info/*
