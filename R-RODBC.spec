%global packname  RODBC
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.9
Release:          1
Summary:          ODBC Database Access
Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/RODBC_1.3-9.tar.gz
Requires:         R-utils 
Requires:         R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils
BuildRequires:    R-stats 
BuildRequires:    unixODBC-devel

%description
An ODBC database interface

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/tests.R

