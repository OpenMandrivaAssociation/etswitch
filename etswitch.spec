Name:		etswitch
Summary:	ETSWITCH - A *nix 'minimizer' for a few games
Version:	0.1.14
Release:	%mkrel 8
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
