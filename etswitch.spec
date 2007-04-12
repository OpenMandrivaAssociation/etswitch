Name: 		etswitch
Summary: 	ETSWITCH - A *nix 'minimizer' for a few games
Version: 	0.1.14
Release: 	%mkrel 3
License: 	GPL
Group: 		Games/Other
Source: 	http://hem.bredband.net/b400150/etswitch/%{name}-%{PACKAGE_VERSION}.tar.gz
Url: 		http://hem.bredband.net/b400150/
Patch:		%{name}-menu-entry.patch
BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	libxpm-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 

%description
A minimizer for all OpenGL and SDL games natively supported by GNU/Linux.

%prep
%setup -q %{name}-%{version}

%patch -p1 -b .%{name}-menu-entry

%build
%configure2_5x \
--enable-debug=no \
--disable-debug

%make
	    
%install
rm -rf %{buildroot}
	    
%makeinstall_std
	    
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
	    
%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif
	    
%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif
	    
%files
%defattr(644, root, root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/etswitch
%{_datadir}/applications/etswitch.desktop
%{_datadir}/man/man1/etswitch.1.bz2
%{_datadir}/pixmaps/etswitch.png
%{_datadir}/pixmaps/etswitch.xpm


