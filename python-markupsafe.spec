%define tarname MarkupSafe
%define enable_tests 0

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-markupsafe
Version:	0.12
Release:	%mkrel 1
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/%{tarname}-%{version}.tar.gz
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
%setup -q -n %{tarname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%check
%if %enable_tests
nosetests
%endif
%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS LICENSE README.rst
