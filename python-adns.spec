%include	/usr/lib/rpm/macros.python
Summary:	Python bindings to GNU adns
Name:		python-adns
Version:	1.0.0
Release:	0.1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dustman.net/andy/python/adns-python/%{version}/adns-python-%{version}.tar.gz
URL:		http://dustman.net/andy/python/adns-python/
%pyrequires_eq	python
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	adns-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to GNU adns library.

%prep
%setup -q -n adns-python-%{version}

python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitedir}/*.py?
%{py_sitedir}/*.so
