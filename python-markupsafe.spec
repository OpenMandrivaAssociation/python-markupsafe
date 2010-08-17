%define tarname MarkupSafe
%define name	python-markupsafe
%define version 0.9.3
%define release %mkrel 1

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/MarkupSafe
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d

%description
This package implements a XML/HTML/XHTML markup safe string for Python.

%prep
%setup -q -n %{tarname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS LICENSE README.rst
