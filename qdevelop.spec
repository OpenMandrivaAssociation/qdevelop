%define name	qdevelop
%define version 0.27.1
%define release %mkrel 1

Summary:	A Development Environment for Qt4
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Development/C++
URL:		http://qdevelop.org/
Source:		http://qdevelop.org/public/release/%{name}-%{version}.tar.bz2
Source1:	qdevelop-16.png
Source2:	qdevelop-32.png
Source3:	qdevelop-48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-builtroot

BuildRequires:	cmake 
BuildRequires:	qt4-devel
Requires:		qt4-devel
Requires: 		ctags
Requires:		gdb

%description 
QDevelop is a development environment entirely dedicated to Qt4.
QDevelop requires Qt4, gcc under Linux or MinGW under Windows,
possibly gdb for program debugging and ctags for code completion.
QDevelop is available in English, French, German, Dutch, Polish,
Spanish, Chinese, Russian, Italian, Ukrainian, Czech and
Portuguese. 

QDevelop is not a Kdevelop like or reduced. It's an independent IDE
dedicated to Qt and is totally independent of KDevelop. Less complete,
but faster, light and especially multi-platforms. QDevelop and
KDevelop have different code sources.

%prep
%setup -q
chmod 0644 README.txt copying ChangeLog.txt

%build
%cmake_qt4
%make

%install
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}
%makeinstall_std -C build
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Development Environment for Qt4
Comment=Development Environment for Qt4
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
MimeType=application/x-qdevelop;
Categories=Qt;Development;IDE;
EOF
mkdir -p %{buildroot}/%{_iconsdir}
mkdir -p %{buildroot}/%{_miconsdir}
mkdir -p %{buildroot}/%{_liconsdir}
%__install %{SOURCE1} %{buildroot}/%_miconsdir/%{name}.png
%__install %{SOURCE2} %{buildroot}/%_iconsdir/%{name}.png
%__install %{SOURCE3} %{buildroot}/%_liconsdir/%{name}.png

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

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc copying
%doc ChangeLog.txt
%doc README.txt
%{_bindir}/*
%{_datadir}/applications
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
