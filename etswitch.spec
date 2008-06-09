Name: 		etswitch
Summary: 	ETSWITCH - A *nix 'minimizer' for a few games
Version: 	0.1.14
Release: 	%mkrel 4
License: 	GPLv2+
Group: 		Games/Other
Source: 	http://hem.bredband.net/b400150/etswitch/%{name}-%{PACKAGE_VERSION}.tar.gz
Url: 		http://hem.bredband.net/b400150/
BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	libxpm-devel
BuildRequires:	desktop-file-utils
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 

%description
A minimizer for all OpenGL and SDL games natively supported by GNU/Linux.

%prep
%setup -q
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
	    
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
	    
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
	    
%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/etswitch
%{_datadir}/applications/etswitch.desktop
%{_mandir}/man1/etswitch.*
%{_datadir}/pixmaps/etswitch.png
%{_datadir}/pixmaps/etswitch.xpm
