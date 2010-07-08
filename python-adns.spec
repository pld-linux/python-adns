Summary:	Python bindings to GNU adns
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNU adns
Name:		python-adns
Version:	1.2.1
Release:	3
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://adns-python.googlecode.com/files/adns-python-%{version}.tar.gz
# Source0-md5:	12cc7ad1b0ee8d818005e9ca4def758b
URL:		http://code.google.com/p/adns-python/
%pyrequires_eq	python
BuildRequires:	adns-devel >= 1.4
BuildRequires:	python-devel >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to GNU adns library.

%description -l pl.UTF-8
Interfejs do biblioteki GNU adns.

%prep
%setup -q -n adns-python-%{version}

%build
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
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py?
