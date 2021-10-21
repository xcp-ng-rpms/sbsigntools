Summary: A signing utility for UEFI secure boot
Name: sbsigntools%{?_with_debug:-debug}
Version: 0.9.3
Release: 1
License: GPLv3
Group: Development/Tools
URL: https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
# Note: The sbsigntools tarball must contain ccan at lib/ccan.git
#   url: https://ccodearchive.net/ccan.tar.bz2
Source0: https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-%{version}.tar.gz
BuildRequires: automake
BuildRequires: binutils-devel
BuildRequires: git
BuildRequires: help2man
BuildRequires: pkgconfig

%description
Signing utility for UEFI secure boot.

%prep
%autosetup

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make -j$(nproc)

%check
make check

%install
%make_install

%files
%license COPYING
/usr/bin/sbsign
/usr/bin/sbverify
/usr/bin/sbattach
/usr/bin/sbkeysync
/usr/bin/sbsiglist
/usr/bin/sbvarsign
/usr/share/man/man1/sbsign.1.gz
/usr/share/man/man1/sbverify.1.gz
/usr/share/man/man1/sbattach.1.gz
/usr/share/man/man1/sbsiglist.1.gz
/usr/share/man/man1/sbvarsign.1.gz

%changelog
* Wed Apr 28 2021 Bobby Eshleman <bobby.eshleman@gmail.com> 0.9.4-1
- Init commit
