Name: grubby
Version: 7.0.5
Release: 1%{?dist}
Summary: Command line tool for updating bootloader configs
Group: System Environment/Base
License: GPLv2+
URL: http://git.fedorahosted.org/git/grubby.git
# we only pull git snaps at the moment
# git clone git://git.fedorahosted.org/git/grubby.git
# git archive --format=tar --prefix=grubby-%{version}/ HEAD |bzip2 > grubby-%{version}.tar.bz2
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: pkgconfig glib2-devel popt-devel 
BuildRequires: libblkid-devel

%description
grubby  is  a command line tool for updating and displaying information about 
the configuration files for the grub, lilo, elilo (ia64),  yaboot (powerpc)  
and zipl (s390) boot loaders. It is primarily designed to be used from scripts
which install new kernels and need to find information about the current boot 
environment.

%prep
%setup -q


%build
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
/sbin/installkernel
/sbin/new-kernel-pkg
/sbin/grubby
%{_mandir}/man8/grubby.8*


%changelog
* Fri Sep 11 2009 Peter Jones <pjones@redhat.com> - 7.0.5-1
- Add support for plymouth as a second initrd.
  Resolves: rhbz#520515

* Wed Sep 09 2009 Hans de Goede <hdegoede@redhat.com> - 7.0.4-1
- Add --dracut cmdline argument for %post generation of dracut initrd

* Wed Aug 26 2009 Hans de Goede <hdegoede@redhat.com> - 7.0.3-1
- Silence error when no /etc/sysconfig/keyboard (#517187)

* Fri Aug  7 2009 Hans de Goede <hdegoede@redhat.com> - 7.0.2-1
- Add --add-dracut-args new-kernel-pkg cmdline option

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Jeremy Katz <katzj@redhat.com> - 7.0.1-1
- Fix blkid usage (#124246)

* Wed Jun 24 2009 Jeremy Katz <katzj@redhat.com> - 7.0-1
- BR libblkid-devel now instead of e2fsprogs-devel
- Add bits to switch to using dracut for new-kernel-pkg

* Wed Jun  3 2009 Jeremy Katz <katzj@redhat.com> - 6.0.86-2
- add instructions for checking out from git

* Tue Jun  2 2009 Jeremy Katz <katzj@redhat.com> - 6.0.86-1
- initial build after splitting out from mkinitrd

