#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	simplegeneric
Summary:	Simple generic functions
Summary(pl.UTF-8):	Proste funkcje generyczne
Name:		python-%{module}
Version:	0.8.1
Release:	9
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/simplegeneric/
Source0:	https://files.pythonhosted.org/packages/source/s/simplegeneric/simplegeneric-%{version}.zip
# Source0-md5:	f9c1fab00fd981be588fc32759f474e3
URL:		https://pypi.org/project/simplegeneric/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The simplegeneric module lets you define simple single-dispatch
generic functions, akin to Python's built-in generic functions like
len(), iter() and so on. However, instead of using specially-named
methods, these generic functions use simple lookup tables, akin to
those used by e.g. pickle.dump() and other generic functions found in
the Python standard library.

%description -l pl.UTF-8
Moduł simplegeneric pozwala definiować proste funkcje generyczne
pojedynczego wyboru, podobne do wbudowanych funkcji generycznych
Pythona, takich jak len(), iter() itp. Jednak, zamiast używania
specjalnie nazwanych metod, te funkcje generyczne używają
pojedynczych tabel wyszukiwania, podobnie do tych używanych przez np.
pickle.dump() czy inne funkcje generyczne w bibliotece standardowej
Pythona.

%package -n python3-%{module}
Summary:	Simple generic functions
Summary(pl.UTF-8):	Proste funkcje generyczne
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
The simplegeneric module lets you define simple single-dispatch
generic functions, akin to Python’s built-in generic functions like
len(), iter() and so on. However, instead of using specially-named
methods, these generic functions use simple lookup tables, akin to
those used by e.g. pickle.dump() and other generic functions found in
the Python standard library.

%description -n python3-%{module} -l pl.UTF-8
Moduł simplegeneric pozwala definiować proste funkcje generyczne
pojedynczego wyboru, podobne do wbudowanych funkcji generycznych
Pythona, takich jak len(), iter() itp. Jednak, zamiast używania
specjalnie nazwanych metod, te funkcje generyczne używają
pojedynczych tabel wyszukiwania, podobnie do tych używanych przez np.
pickle.dump() czy inne funkcje generyczne w bibliotece standardowej
Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/simplegeneric.py[co]
%{py_sitescriptdir}/simplegeneric-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.txt
%{py3_sitescriptdir}/simplegeneric.py
%{py3_sitescriptdir}/__pycache__/simplegeneric.cpython-*.py[co]
%{py3_sitescriptdir}/simplegeneric-%{version}-py*.egg-info
%endif
