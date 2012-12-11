%define name	qdevelop
%define version 0.27.2
%define release %mkrel 2

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
Patch0:		qt45.patch.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-builtroot

BuildRequires:	cmake 
BuildRequires:	qt4-devel
Requires:		qt4-devel
Requires: 		ctags
Requires:		gdb
Requires: 		qt4-designer
Requires:		qt4-assistant
Requires:		qt4-linguist

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
%patch0 -p0
chmod 0644 README.txt copying ChangeLog.txt

%build
%cmake_qt4
%make

%install
#[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}
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


%changelog
* Fri Jul 31 2009 Jerome Martin <jmartin@mandriva.org> 0.27.2-2mdv2010.0
+ Revision: 405110
- Patched to fix issue with Qt 4.5.1 (http://code.google.com/p/qdevelop/issues/detail?id=374)

* Fri Feb 27 2009 Jerome Martin <jmartin@mandriva.org> 0.27.2-1mdv2009.1
+ Revision: 345390
- 0.27.2: spanish translation update

* Thu Feb 26 2009 Jerome Martin <jmartin@mandriva.org> 0.27.1-1mdv2009.1
+ Revision: 345177
- 0.27.1

* Sat Feb 21 2009 Jerome Martin <jmartin@mandriva.org> 0.27-0.rc1.1mdv2009.1
+ Revision: 343678
- 0.27-rc1

* Sat Feb 14 2009 Jerome Martin <jmartin@mandriva.org> 0.26-0.svn393.1mdv2009.1
+ Revision: 340253
- 0.26-svn393

* Wed Feb 04 2009 Jerome Martin <jmartin@mandriva.org> 0.26-0.svn372.1mdv2009.1
+ Revision: 337567
- import qdevelop


