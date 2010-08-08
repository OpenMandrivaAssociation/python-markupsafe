Name:           python-markupsafe
Version:        0.9.2
Release:        %mkrel 1
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
Group:          System/Libraries
License:        MIT
URL:            http://pypi.python.org/pypi/MarkupSafe
Source0:        http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools


%description
Implements a unicode subclass that supports HTML strings.


%prep
%setup -q -n MarkupSafe-%{version}

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}


%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%{py_platsitedir}/MarkupSafe-%{version}-py%{pyver}*
%{py_platsitedir}/markupsafe/*


