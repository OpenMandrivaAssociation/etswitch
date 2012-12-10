Name:		etswitch
Summary:	ETSWITCH - A *nix 'minimizer' for a few games
Version:	0.1.14
Release:	%mkrel 9
License:	GPLv2+
Group:		Games/Other
Url:		http://hem.bredband.net/b400150/
Source:		http://hem.bredband.net/b400150/etswitch/%{name}-%{PACKAGE_VERSION}.tar.gz
Patch0:		etswitch-0.1.14-missing-argument-in-open.patch
BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	libxpm-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-root 

%description
A minimizer for all OpenGL and SDL games natively supported by GNU/Linux.

%prep
%setup -q
%patch0 -p1

sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{name}.desktop.in

%build
%configure2_5x \
	--enable-debug=no \
	--disable-debug

%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
	--remove-category="Tool" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/etswitch
%{_datadir}/applications/etswitch.desktop
%{_mandir}/man1/etswitch.*
%{_datadir}/pixmaps/etswitch.png
%{_datadir}/pixmaps/etswitch.xpm


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.14-9mdv2011.0
+ Revision: 610393
- rebuild

* Sun Feb 14 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-8mdv2010.1
+ Revision: 505665
- Patch0: fix open syntax

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-4mdv2008.1
+ Revision: 102425
- new license policy
- drop patch 0, use desktop-file-install for tuning up
- do not hardcode icon extension in desktop file

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%{_datadir}/man by %%{_mandir}!
    - fix man pages


* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-3mdv2007.0
+ Revision: 133956
- rebuild

* Wed Dec 06 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-2mdv2007.1
+ Revision: 91795
- fix xdg menu entry

* Tue Dec 05 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-1mdv2007.1
+ Revision: 90857
- Fixed build requires
- Add missing build requires
- import etswitch
- Import etswitch

* Sun Dec 03 2006 Tomasz pawe Gajc <tpg at mandriva dot org> 0.1.14-1mdv2007.1
- initial package for mdv

