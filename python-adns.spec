Summary:	Python bindings to GNU adns
Summary(pl):	Wi±zania Pythona do biblioteki GNU adns
Name:		python-adns
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dustman.net/andy/python/adns-python/%{version}/adns-python-%{version}.tar.gz
# Source0-md5:	f7a3e7e81f6c13859261b40a9b5dc130
Patch0:		%{name}-build.patch
URL:		http://dustman.net/andy/python/adns-python/
%pyrequires_eq	python
BuildRequires:	adns-devel >= 1.0
BuildRequires:	python-devel >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to GNU adns library.

%description -l pl
Interfejs do biblioteki GNU adns.

%prep
%setup -q -n adns-python-%{version}
%patch0 -p1

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
