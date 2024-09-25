Summary:	Microsoft GSL: Guidelines Support Library
Summary(pl.UTF-8):	Microsoft GSL - biblioteka wspierająca wskazania C++ Foundation
Name:		microsoft-gsl
Version:	4.0.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/microsoft/GSL/releases
Source0:	https://github.com/microsoft/GSL/archive/v%{version}/GSL-%{version}.tar.gz
# Source0-md5:	4b1a5f39c5f489d2bdf3bd352548907d
URL:		https://github.com/microsoft/GSL
BuildRequires:	cmake >= 3.1.3
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Guidelines Support Library (GSL) contains functions and types that
are suggested for use by the C++ Core Guidelines
(<https://github.com/isocpp/CppCoreGuidelines>) maintained by the
Standard C++ Foundation (<https://isocpp.org/>).

This package contains Microsoft's implementation of GSL.

%description -l pl.UTF-8
Guidelines Support Library (GSL) zawiera funkcje i typy proponowane do
używania przez C++ Core Guidelines
(<https://github.com/isocpp/CppCoreGuidelines>) utrzymywane przez
Standard C++ Foundation (<https://isocpp.org/>).

Ten pakiet zawiera implementację GSL firmy Microsoft.

%package devel
Summary:	Microsoft GSL: Guidelines Support Library
Summary(pl.UTF-8):	Microsoft GSL - biblioteka wspierająca wskazania C++ Foundation
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:5

%description devel
The Guidelines Support Library (GSL) contains functions and types that
are suggested for use by the C++ Core Guidelines
(<https://github.com/isocpp/CppCoreGuidelines>) maintained by the
Standard C++ Foundation (<https://isocpp.org/>).

This package contains Microsoft's implementation of GSL.

%description devel -l pl.UTF-8
Guidelines Support Library (GSL) zawiera funkcje i typy proponowane do
używania przez C++ Core Guidelines
(<https://github.com/isocpp/CppCoreGuidelines>) utrzymywane przez
Standard C++ Foundation (<https://isocpp.org/>).

Ten pakiet zawiera implementację GSL firmy Microsoft.

%prep
%setup -q -n GSL-%{version}

%build
install -d build
cd build
# override install dir to avoid dir clash with GNU gsl
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/microsoft-gsl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md ThirdPartyNotices.txt
%{_includedir}/microsoft-gsl
%{_datadir}/cmake/Microsoft.GSL
