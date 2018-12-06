# Run tests in check section
%bcond_without check

%global goipath         github.com/google/go-cmp
Version:                0.2.0

%global common_description %{expand:
This package is intended to be a more powerful and safer alternative to 
reflect.DeepEqual for comparing whether two values are semantically equal.

The primary features of cmp are:

 - When the default behavior of equality does not suit the needs of the 
 test, custom equality functions can override the equality operation. 
 For example, an equality function may report floats as equal so long as 
 they are within some tolerance of each other.

 - Types that have an Equal method may use that method to determine equality. 
 This allows package authors to determine the equality operation for the types 
 that they define.

 - If no custom equality functions are used and no Equal method is defined, 
 equality is determined by recursively comparing the primitive kinds on both 
 values, much like reflect.DeepEqual. Unlike reflect.DeepEqual, unexported 
 fields are not compared by default; they result in panics unless suppressed 
 by using an Ignore option (see cmpopts.IgnoreUnexported) or explicitly 
 compared using the AllowUnexported option.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Package for comparing Go values in tests 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- First package for Fedora

