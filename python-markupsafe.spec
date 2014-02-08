%define	eggname	MarkupSafe
%define	modname	markupsafe
%define	enable_tests 0

Summary:	XML/HTML/XHTML markup safe string package for Python
Name:		python-%{modname}
Version:	0.18
Release:	2
Source0:	http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdv2011.0
+ Revision: 667967
- mass rebuild

* Tue Feb 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.12-1
+ Revision: 639313
- don't use manifest, but rather explicitly provide a %%files list
- replace '%%py_requires -d' macro with a generic BuildRequires: python-devel
- new release 0.12

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.11-2mdv2011.0
+ Revision: 590386
- disable test, like for sphinx ( bootstraping for python 2.7 )
- rebuild for python 2.7

* Wed Oct 20 2010 Lev Givon <lev@mandriva.org> 0.11-1mdv2011.0
+ Revision: 587008
- Update to 0.11.

* Tue Aug 17 2010 Lev Givon <lev@mandriva.org> 0.9.3-1mdv2011.0
+ Revision: 571051
- Update to 0.9.3.

* Sun Aug 08 2010 Crispin Boylan <crisb@mandriva.org> 0.9.2-1mdv2011.0
+ Revision: 567631
- New package
- create python-markupsafe



