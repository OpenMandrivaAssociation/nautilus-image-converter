Summary:	Nautilus extension to mass resize or rotate images
Name:		nautilus-image-converter
Version:	0.3.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-image-converter/%{name}-%{version}.tar.bz2
URL:		http://www.bitron.ch/software/nautilus-image-converter.php
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	nautilus-devel >= 2.6.0
Requires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-

%description
Nautilus extension which allows you to mass resize or rotate images.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nautilus-image-*.glade

