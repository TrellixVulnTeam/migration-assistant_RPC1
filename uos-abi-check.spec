%global debug_package %{nil}
Name:           uos-abi-check
Version:        0.1
Release:        1
Summary:        a tool for checking backward binary compatibility of a C/C++ software library
License:        GPL2
URL:            https://github.com/deepinlinux
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3
Requires:       perl
Requires:       gcc
Requires:       gcc-c++
Requires:       python3-distro
Requires:       python3-pandas

%description
a tool for checking backward binary compatibility of a C/C++ software library.

%package -n abi-info-collect
Summary:        collect abi info
Requires:       python3
Requires:       elfutils

%description -n abi-info-collect
a tool for collecting backward binary compatibility of a C/C++ software library.


%prep
%autosetup

%build
python3 -O -m compileall -b src

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/libexec
pushd  abi-compliance-checker-2.3
%make_install
popd
# collect module install
install -m 755 src/abi-info-collect.py  %{buildroot}/usr/bin/abi-info-collect
install -m 755 src/abi-info-collect.pyc  %{buildroot}/usr/libexec/abi-info-collect

# check module install
mkdir -p %{buildroot}/usr/share/uos-abi-check
install -m 755 src/abi-info-check.pyc  %{buildroot}/usr/libexec/abi-info-check
install -m 755 uos-abi-check           %{buildroot}/usr/bin/uos-abi-check

%files
%{_bindir}/uos-abi-check
%{_libexecdir}/abi-info-check
%{_datadir}/abi-compliance-checker/
%{_bindir}/abi-compliance-checker

%files -n abi-info-collect
%{_bindir}/abi-info-collect
%{_libexecdir}/abi-info-collect