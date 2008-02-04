
# Conditional build:
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
#
%define		oname		kdebase-workspace
%define		_state		unstable

Summary:	K Desktop Environment - core files
Summary(es.UTF-8):   K Desktop Environment - archivos básicos
Summary(ja.UTF-8):   KDEデスクトップ環境 - 基本ファイル
Summary(ko.UTF-8):   KDE - 기본 파일
Summary(pl.UTF-8):   K Desktop Environment - pliki środowiska
Summary(pt_BR.UTF-8):   K Desktop Environment - arquivos básicos
Summary(ru.UTF-8):   K Desktop Environment - базовые файлы
Summary(uk.UTF-8):   K Desktop Environment - базові файли
Summary(zh_CN.UTF-8):   KDE核心
Name:		kde4-kdebase-workspace
Version:	4.0.60
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{oname}-%{version}.tar.bz2
# Source0-md5:	a2e11366ade39366cee569cd65b078e3
Source1:	kdebase-kdesktop.pam
Source2:	kdebase-kdm.pam
Source3:	kdebase-kdm-np.pam
Source4:	kdebase-kdm.init
Source5:	kdebase-kdm.sysconfig
Source6:	kdebase-kdm_pldlogo.png
Source7:	kdebase-kdm_pldwallpaper.png
Source8:	kdebase-kde.pam
Source15:	%{name}.desktop
Source16:	%{name}-session
BuildRequires:	NetworkManager-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake
BuildRequires:	qimageblitz-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libtirpc-devel
BuildRequires:	libxklavier-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	QtScript-devel >= 4.3
Obsoletes:	kdebase-desktop
Obsoletes:	kdebase4-workspace
Conflicts:	kdebase4-workspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains KDE base system which includes:
- KDE Control Centre with modules
- KDesktop (a desktop) and Kicker (a panel)
- KWin window manager and several decorations
- KDE splash themes and plugins
- thumbnail creation, mail, news and terminal emulation support
- many more.

%description -l ja.UTF-8
KDEデスクトップ環境用の基本アプリケーション。
以下のようなパッケージが入っています。

%description -l pl.UTF-8
Ten pakiet zawiera podstawowe aplikacje KDE:
- Centrum sterowania z modułami
- KDesktop (pulpit) i Kicker (panel)
- menedżer okien Kwin i dekoracje
- ekrany startowe KDE
- obsługę podglądu plików, protokołów poczty i news oraz emulacji
  terminala

%description -l ru.UTF-8
Базовые программы для K Desktop Environment. Включены: 
kwin (оконный менеджер), konqueror (файловый менеджер,
web-браузер, ftp-клиент, ...), konsole (замена xterm), kicker
(запускалка программ и пейджер рабочего стола), kaudio (аудиосервер),
kdehelp (программа для просмотра справочных файлов kde, файлов info и
man), kthememgr (система для управления альтернативными пакетами тем)
и другие компоненты KDE (kcheckpass, kikbd, kscreensaver, kcontrol,
kfind, kfontmanager, kmenuedit, kappfinder).

%description -l uk.UTF-8
Базові програми для K Desktop Environment. Включені: 
kwin (віконный менеджер), konqueror (файловий менеджер, web-браузер,
ftp-кліент, ...), konsole (заміна xterm), kicker (запускалка програм
та пейджер робочого столу), kaudio (аудіосервер), kdehelp (програма
для перегляду файлів довідки kde, файлів info та man), kthememgr
(система для керування альтернативними пакетами тем) та інші
компоненти KDE (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit, kappfinder).

%package devel
Summary:	Include files to develop KDE applications
Summary(pl.UTF-8):   Pliki nagłówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR.UTF-8):   Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do programowania aplikacji
KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package kde-decoration-libs
Summary:	Libraries for KDE Window Decorations
Summary(pl.UTF-8):	Biblioteki dla dekoracji okien KDE
Group:		X11/Amusements

%description kde-decoration-libs
Libraries for KDE Window Decorations.

%package -n kde-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - B2
Group:		X11/Amusements

%description -n kde-decoration-b2
A Beos like window decoration with rectangular window title to the
left. The actual window decoration does not take more than 20-30% of
the screen width and if two window titles overlap each other, they are
aligned next to each other.

%description -n kde-decoration-b2 -l pl.UTF-8
Podobna do Beos dekoracja okien z prostokątnym tytułem okna po lewej
stronie. Nie zajmuje ona więcej niż 20-30% szerokości ekranu, a w
przypadkach gdyby dwie dekoracje się zasłaniały, są one układane obok
siebie.

%package -n kde-decoration-kde2
Summary:	KDE Window Decoration - kde2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - kde2
Group:		X11/Amusements

%description -n kde-decoration-kde2
KDE Window Decoration - kde2.

%description -n kde-decoration-kde2 -l pl.UTF-8
Dekoracja okna dla KDE - kde2.

%package -n kde-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl.UTF-8):	Dekoracja okna dla KDE - keramik
Group:		X11/Amusements

%description -n kde-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde-decoration-keramik -l pl.UTF-8
Dekoracja okna dla KDE - keramik.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements

%description -n kde-decoration-laptop
A window decoration with stripped window title and lightly convex
window buttons.

%description -n kde-decoration-laptop -l pl.UTF-8
Dekoracja okna z paskowanym tytułem okna oraz lekko wypukłymi
przyciskami okna.

%package -n kde-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl.UTF-8):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements

%description -n kde-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde-decoration-modernsys -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde-decoration-oxygen
Summary:	KDE Window Decoration - Oxygen
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Oxygen
Group:		X11/Amusements

%description -n kde-decoration-oxygen
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde-decoration-oxygen -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde-decoration-plastic
Summary:	KDE Window Decoration - Plastic
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Plastic
Group:		X11/Amusements

%description -n kde-decoration-plastic
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde-decoration-plastic -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements

%description -n kde-decoration-quartz
A window decoration with solid borders. The window caption consists of
a lighter area for the window title and a darker area for window
buttons. Between the two area there is a stylish transition.

%description -n kde-decoration-quartz -l pl.UTF-8
Dekoracja okna z pełnymi krawędziami. Nagłówek okna składa się z
jasnego obszaru dla tytułu okna i ciemniejszego dla przycisków. Między
obszarami jest stylowy przejście.

%package -n kde-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements

%description -n kde-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde-decoration-redmond -l pl.UTF-8
Dekoracja okna przypominająca tę z Windows 98.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements

%description -n kde-decoration-web
A completely flat window decoration with rounded corners and visible,
thin borders.

%description -n kde-decoration-web -l pl.UTF-8
Zupełnie płaska dekoracja okna z zaokrąglonymi brzegami oraz
widocznymi, cienkimi krawędziami.

%package -n kde-kgreet-classic
Summary:	KDE greeter libraries
Summary(pl.UTF-8):	Biblioteki służące do zapytań o hasło
Group:		X11/Libraries
Provides:	kde-kgreet

%description -n kde-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde-kgreet-classic -l pl.UTF-8
Narzędzia służące do zapytań o hasło - klasyczny, domyślny motyw
wyglądu.

%package -n kde-kgreet-winbind
Summary:	KDE greeter libraries
Summary(pl.UTF-8):	Biblioteki służące do zapytań o hasło
Group:		X11/Libraries
Provides:	kde-kgreet

%description -n kde-kgreet-winbind
Tools for asking for passwords - winbind.

%description -n kde-kgreet-winbind -l pl.UTF-8
Narzędzia służące do zapytań o hasło - winbind.

%package -n kde-splash-Default
Summary:	Default clasic KDE splashscreen
Summary(pl.UTF-8):	Domyślny klasyczny ekran startowy KDE
Group:		X11/Amusements

%description -n kde-splash-Default
Default splashscreen that came with this version of KDE.

%description -n kde-splash-Default -l pl.UTF-8
Domyślny ekran powitalny dostarczony w tej wersji KDE.

%package -n kde-splash-Simple
Summary:	KDE Simple splashscreen
Summary(pl.UTF-8):	Ekran powitalny KDE Simple
Group:		X11/Amusements

%description -n kde-splash-Simple
KDE Simple splashcreen.

%description -n kde-splash-Simple -l pl.UTF-8
Ekran powitalny KDE Simple.

%package -n kde-splash-SimpleSmall
Summary:	KDE SimpleSmall splashscreen
Summary(pl.UTF-8):	Ekran powitalny KDE SimpleSmall
Group:		X11/Amusements

%description -n kde-splash-SimpleSmall
KDE SimpleSmall splashcreen.

%description -n kde-splash-SimpleSmall -l pl.UTF-8
Ekran powitalny KDE SimpleSmall.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl.UTF-8):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
#Requires(post,postun):	fontpostinst

%description common-konsole
Color schemes, icons, fonts and shell profiles for konsole.

%description common-konsole -l pl.UTF-8
Schematy kolorów, ikony, czcionki oraz profile sesji dla konsole.

%package core
Summary:	KDE Core Apps
Summary(pl.UTF-8):	Podstawowe aplikacje KDE
Group:		X11/Applications
#Requires:	xdg-menus
#Suggests:	sudo
#Conflicts:	kttsd <= 040609

%description core
KDE Core apps. This package contains:
- Control Center;
- Help Center;
- Print System;
- Crash Handlers;
- A Frontend for "su" (or "sudo") program.

%description core -l pl.UTF-8
Podstawowe aplikacje środowiska KDE. Pakiet ten zawiera:
- Centrum sterowania;
- System drukowania;
- System pomocy;
- Programy obsługi błędów;
- Frontend dla programu "su" (lub "sudo").

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
#Requires:	pciutils

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.

%package kfontinst
Summary:	K Font Installer
Summary(pl.UTF-8):	Instalator fontów dla KDE
Group:		X11/Applications

%description kfontinst
KDE font installer.

%description kfontinst -l pl.UTF-8
Instalator czcionek dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl.UTF-8):	Narzędzie schowka
Group:		X11/Applications

%description klipper
A tool extending the clipboard support for KDE. Note that it requires
a powerful computer.

%description klipper -l pl.UTF-8
Narzędzie rozszerzające obsługę schowka dla KDE. Wymaga ono szybkiego
systemu.

%package ksysguard
Summary:	System Guard
Summary(pl.UTF-8):	Strażnik systemu
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig

%description ksysguard
KDE System Guard.

%description ksysguard -l pl.UTF-8
Strażnik systemu dla KDE.

%package libksgrd
Summary:	ksgrd library
Summary(pl.UTF-8):	Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig

%description libksgrd
A library containing functions for the system monitor KSysGuard.

%description libksgrd -l pl.UTF-8
Biblioteka zawierające funkcje monitora systemu - KSysGuard.

%package screensavers
Summary:	KDE screensavers
Summary(pl.UTF-8):	Wygaszacze ekranu desktopu KDE
Summary(ru.UTF-8):	хранители экрана для KDE
Summary(uk.UTF-8):	зберігачі екрану для KDE
Group:		X11/Applications

%description screensavers
KDE screensavers.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru.UTF-8
Некоторые 3D хранители экрана для K Desktop Environment.

%package solid
Summary:	Solid
Group:		X11/Applications

%description solid
Solid.

%package networkmanager
Summary:	networkmanager
Group:		X11/Applications

%description networkmanager
Networkmanager.

%package plasma
Summary:	Plasma
Group:		X11/Applications

%description plasma
Plasma.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl.UTF-8):	Zarządca ekranów KDE
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.99.7.1
Requires:	rc-scripts
Requires:	kde-kgreet
Provides:	XDM

%description -n kdm
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kdm -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.

%package wallpapers
Summary:	KDE4 wallpapers
Summary(pl.UTF-8):	Tapety KDE4
Group:		X11/Applications

%description wallpapers
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description wallpapers -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.

%package kwin
Summary:	kwin
Group:		X11/Applications

%description kwin
kwin

%prep
%setup -q -n %{oname}-%{version}

%build
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT/etc/{X11,pam.d,security}
install -d $RPM_BUILD_ROOT%{_datadir}/config/kdm

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/pam.d/kdm-np
install %{SOURCE8}	$RPM_BUILD_ROOT/etc/pam.d/kde
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/sysconfig/kdm

install %{SOURCE6}	$RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_datadir}/wallpapers/kdm_pld.png

install %{SOURCE16} $RPM_BUILD_ROOT%{_bindir}/kde4-session
install %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/sessions/kde4.desktop

$RPM_BUILD_ROOT%{_bindir}/genkdmconf --in $RPM_BUILD_ROOT%{_datadir}/config/kdm
rm $RPM_BUILD_ROOT%{_datadir}/config/kdm/README

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

%clean
rm -rf $RPM_BUILD_ROOT

%post	kde-decoration-libs	-p /sbin/ldconfig
%postun	kde-decoration-libs	-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post -n kdm
/sbin/chkconfig --add kdm
%service kdm restart

%preun -n kdm
if [ "$1" = "0" ]; then
	%service kdm stop
	/sbin/chkconfig --del kdm
fi

%files
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemsettingsrc
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdesktop
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kstartupconfig4
%attr(755,root,root) %{_bindir}/ksystraycmd
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kdostartupconfig4
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit_startup.so

%attr(755,root,root) %{_libdir}/libkworkspace.so.*
%attr(755,root,root) %{_libdir}/libprocesscore.so.*
%attr(755,root,root) %{_libdir}/libprocessui.so.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*
%attr(755,root,root) %{_libdir}/libweather_ion.so.*
%attr(755,root,root) %{_libdir}/libplasmaclock.so.*

# kaccess
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_libdir}/libkdeinit4_kaccess.so
%{_datadir}/apps/kaccess
%{_datadir}/kde4/services/kaccess.desktop

# kcontrol
%attr(755,root,root) %{_bindir}/kcontroledit
%attr(755,root,root) %{_libdir}/libkdeinit4_kcontroledit.so
%{_datadir}/apps/kcontrol/pics/anchor.png
%{_datadir}/apps/kcontrol/pics/energybig.png
%{_datadir}/apps/kcontrol/pics/lo-energy.png
%{_datadir}/apps/kcontrol/pics/logo.png
%{_datadir}/apps/kcontrol/pics/mini-world.png
%{_datadir}/apps/kcontrol/pics/monitor.png
%{_datadir}/apps/kcontroledit

# khotkeys
%attr(755,root,root) %{_bindir}/khotkeys
%{_libdir}/kconf_update_bin/khotkeys_update
%attr(755,root,root) %{_libdir}/kde4/kcm_khotkeys.so
%attr(755,root,root) %{_libdir}/kde4/kded_khotkeys.so
%attr(755,root,root) %{_libdir}/libkdeinit4_khotkeys.so
%{_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{_datadir}/apps/khotkeys
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_iconsdir}/*/*/apps/khotkeys.png
%{_datadir}/kde4/services/kded/khotkeys.desktop
%{_datadir}/kde4/services/khotkeys.desktop

# kmenuedit
%attr(755,root,root) %{_bindir}/kmenuedit
%attr(755,root,root) %{_libdir}/libkdeinit4_kmenuedit.so
%{_desktopdir}/kde4/kmenuedit.desktop
%{_datadir}/apps/kmenuedit
%lang(en) %{_kdedocdir}/en/kmenuedit
%{_iconsdir}/*/*/apps/kmenuedit.png

# krandrtray
%attr(755,root,root) %{_bindir}/krandrtray
%{_desktopdir}/kde4/krandrtray.desktop

# krunner
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_libdir}/kde4/libexec/krunner_lock
%attr(755,root,root) %{_libdir}/kde4/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_calculatorrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_locations.so
%attr(755,root,root) %{_libdir}/kde4/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/libkdeinit4_krunner.so
%{_datadir}/autostart/krunner.desktop
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.Interface.xml

# ksmserver
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_libdir}/libkdeinit4_ksmserver.so
%{_datadir}/apps/kconf_update/ksmserver.upd
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml

# ksplash
%attr(755,root,root) %{_bindir}/ksplashsimple
%attr(755,root,root) %{_bindir}/ksplashx
%attr(755,root,root) %{_bindir}/ksplashx_scale
%attr(755,root,root) %{_libdir}/kde4/kcm_ksplashthemes.so
%dir %{_datadir}/apps/ksplash
%dir %{_datadir}/apps/ksplash/Themes
%dir %{_datadir}/apps/ksplash/Themes/None
%{_datadir}/apps/ksplash/Themes/None/Theme.rc
%{_iconsdir}/*/*/apps/ksplash.png
%{_datadir}/kde4/services/ksplashthememgr.desktop

# ktip
%attr(755,root,root) %{_bindir}/ktip
%{_desktopdir}/kde4/ktip.desktop
%{_datadir}/autostart/ktip.desktop


# kxkb
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_libdir}/libkdeinit4_kxkb.so
%lang(en) %{_kdedocdir}/en/kxkb
%{_iconsdir}/*/*/apps/kxkb.png

# systemsettings
%attr(755,root,root) %{_bindir}/systemsettings
%{_desktopdir}/kde4/systemsettings.desktop
%{_datadir}/apps/systemsettings
%{_datadir}/kde4/services/settings-about-me.desktop
%{_datadir}/kde4/services/settings-accessibility.desktop
%{_datadir}/kde4/services/settings-advanced-user-settings.desktop
%{_datadir}/kde4/services/settings-advanced.desktop
%{_datadir}/kde4/services/settings-appearance.desktop
%{_datadir}/kde4/services/settings-bluetooth.desktop
%{_datadir}/kde4/services/settings-computer-administration.desktop
%{_datadir}/kde4/services/settings-desktop.desktop
%{_datadir}/kde4/services/settings-display.desktop
%{_datadir}/kde4/services/settings-general.desktop
%{_datadir}/kde4/services/settings-keyboard-and-mouse.desktop
%{_datadir}/kde4/services/settings-look-and-feel.desktop
%{_datadir}/kde4/services/settings-network-and-connectivity.desktop
%{_datadir}/kde4/services/settings-network-settings.desktop
%{_datadir}/kde4/services/settings-notifications.desktop
%{_datadir}/kde4/services/settings-personal.desktop
%{_datadir}/kde4/services/settings-regional-and-language.desktop
%{_datadir}/kde4/services/settings-sharing.desktop
%{_datadir}/kde4/services/settings-system.desktop
%{_datadir}/kde4/services/settings-window-behaviour.desktop
%{_datadir}/kde4/servicetypes/systemsettingscategory.desktop

# themes
%attr(755,root,root) %{_bindir}/kdeinstallktheme
%attr(755,root,root) %{_libdir}/kde4/kcm_kthememanager.so
%{_datadir}/apps/desktoptheme
%{_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{_datadir}/apps/kthememanager
%{_datadir}/kde4/services/installktheme.desktop
%{_datadir}/kde4/services/kthememanager.desktop

# styles
%attr(755,root,root) %{_libdir}/kde4/kcm_style.so
%attr(755,root,root) %{_libdir}/kde4/kstyle_keramik_config.so
%{_datadir}/kde4/services/style.desktop

# kdisplay
%{_datadir}/apps/kdisplay
%attr(755,root,root) %{_libdir}/kde4/kcm_display.so
%{_datadir}/apps/kconf_update/kcmdisplayrc.upd
%{_datadir}/kde4/services/display.desktop

# kdewizard
%dir %{_datadir}/apps/kdewizard
%{_datadir}/apps/kdewizard/tips

# ion
%attr(755,root,root) %{_libdir}/kde4/ion_bbcukmet.so
%attr(755,root,root) %{_libdir}/kde4/ion_envcan.so
%attr(755,root,root) %{_libdir}/kde4/ion_noaa.so
%{_datadir}/kde4/services/ion-bbcukmet.desktop
%{_datadir}/kde4/services/ion-envcan.desktop
%{_datadir}/kde4/services/ion-noaa.desktop
%{_datadir}/kde4/servicetypes/weather_ion.desktop

# accessibility
%attr(755,root,root) %{_libdir}/kde4/kcm_accessibility.so
%{_datadir}/desktop-directories/kde-utilities-accessibility.directory
%{_datadir}/kde4/services/accessibility.desktop

# launch
%attr(755,root,root) %{_libdir}/kde4/kcm_launch.so
%{_datadir}/config.kcfg/klaunch.kcfg
%{_datadir}/kde4/services/kcmlaunch.desktop

# access
%attr(755,root,root) %{_libdir}/kde4/kcm_access.so
%{_datadir}/kde4/services/kcmaccess.desktop

# bell
%attr(755,root,root) %{_libdir}/kde4/kcm_bell.so
%{_datadir}/kde4/services/bell.desktop

# bluez
%attr(755,root,root) %{_libdir}/kde4/solid_bluez.so

# clock
%attr(755,root,root) %{_libdir}/kde4/kcm_clock.so
%{_datadir}/kde4/services/clock.desktop

# fontthumbnail
%attr(755,root,root) %{_libdir}/kde4/fontthumbnail.so
%{_datadir}/kde4/services/fontthumbnail.desktop

# colors
%attr(755,root,root) %{_libdir}/kde4/kcm_colors.so
%{_datadir}/kde4/services/colors.desktop
%{_datadir}/apps/color-schemes

# energy
%attr(755,root,root) %{_libdir}/kde4/kcm_energy.so
%{_datadir}/kde4/services/energy.desktop

# randr
%{_datadir}/kde4/services/randr.desktop
%attr(755,root,root) %{_libdir}/kde4/kcm_randr.so

# smserver
%attr(755,root,root) %{_libdir}/kde4/kcm_smserver.so
%{_datadir}/kde4/services/kcmsmserver.desktop

# xinerama
%attr(755,root,root) %{_libdir}/kde4/kcm_xinerama.so
%attr(755,root,root) %{_libdir}/kde4/libexec/test_kcm_xinerama
%{_datadir}/kde4/services/xinerama.desktop

# input, hw
%attr(755,root,root) %{_libdir}/kde4/kcm_input.so
%{_datadir}/apps/kcminput/cursor_large_black.pcf.gz
%{_datadir}/apps/kcminput/cursor_large_white.pcf.gz
%{_datadir}/apps/kcminput/cursor_small_white.pcf.gz
%{_datadir}/apps/kcminput/pics/mouse_lh.png
%{_datadir}/apps/kcminput/pics/mouse_rh.png
%attr(755,root,root) %{_libdir}/kde4/kcm_joystick.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard_layout.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keys.so
%attr(755,root,root) %{_libdir}/kde4/kcm_nic.so
%attr(755,root,root) %{_libdir}/kde4/kcm_usb.so
%attr(755,root,root) %{_libdir}/kde4/kcm_view1394.so
%{_datadir}/apps/kcmview1394/oui.db

# ?
%attr(755,root,root) %{_libdir}/kde4/kded_networkstatus.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kcheckpass
%attr(755,root,root) %{_libdir}/kde4/libexec/krootimage

# session
%attr(755,root,root) %{_bindir}/kde4-session

%files core
%dir %{_datadir}/apps/kcmview1394
%dir %{_datadir}/apps/kcmusb
%dir %{_iconsdir}/oxygen/*/mimetypes
%dir %{_datadir}/apps/kcminput
%dir %{_datadir}/apps/kcminput/pics

%{_datadir}/apps/kconf_update/kaccel.upd
%{_datadir}/apps/kconf_update/konqueror_gestures_kde321_update.upd
%{_datadir}/apps/kconf_update/kwin3_plugin.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/convertShortcuts.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kwin3_plugin.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/move_session_config.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/on-off_to_true-false.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/pluginlibFix.pl
%{_datadir}/config/background.knsrc
%{_datadir}/config/wallpaper.knsrc
%{_datadir}/desktop-directories/kde-development-translation.directory
%{_datadir}/desktop-directories/kde-development-webdevelopment.directory
%{_datadir}/desktop-directories/kde-development.directory
%{_datadir}/desktop-directories/kde-editors.directory
%{_datadir}/desktop-directories/kde-edu-languages.directory
%{_datadir}/desktop-directories/kde-edu-mathematics.directory
%{_datadir}/desktop-directories/kde-edu-miscellaneous.directory
%{_datadir}/desktop-directories/kde-edu-science.directory
%{_datadir}/desktop-directories/kde-edu-tools.directory
%{_datadir}/desktop-directories/kde-education.directory
%{_datadir}/desktop-directories/kde-games-arcade.directory
%{_datadir}/desktop-directories/kde-games-board.directory
%{_datadir}/desktop-directories/kde-games-card.directory
%{_datadir}/desktop-directories/kde-games-kids.directory
%{_datadir}/desktop-directories/kde-games-roguelikes.directory
%{_datadir}/desktop-directories/kde-games-strategy.directory
%{_datadir}/desktop-directories/kde-games.directory
%{_datadir}/desktop-directories/kde-graphics.directory
%{_datadir}/desktop-directories/kde-internet-terminal.directory
%{_datadir}/desktop-directories/kde-internet.directory
%{_datadir}/desktop-directories/kde-main.directory
%{_datadir}/desktop-directories/kde-more.directory
%{_datadir}/desktop-directories/kde-multimedia.directory
%{_datadir}/desktop-directories/kde-office.directory
%{_datadir}/desktop-directories/kde-science.directory
%{_datadir}/desktop-directories/kde-settingsmenu.directory
%{_datadir}/desktop-directories/kde-system-terminal.directory
%{_datadir}/desktop-directories/kde-system.directory
%{_datadir}/desktop-directories/kde-toys.directory
%{_datadir}/desktop-directories/kde-unknown.directory
%{_datadir}/desktop-directories/kde-utilities-desktop.directory
%{_datadir}/desktop-directories/kde-utilities-file.directory
%{_datadir}/desktop-directories/kde-utilities-peripherals.directory
%{_datadir}/desktop-directories/kde-utilities-pim.directory
%{_datadir}/desktop-directories/kde-utilities-xutils.directory
%{_datadir}/desktop-directories/kde-utilities.directory

%{_iconsdir}/*/*/apps/kcmkwm.png
%{_iconsdir}/*/scalable/apps/kcmkwm.svgz
%{_iconsdir}/*/*/apps/computer.png
%{_iconsdir}/*/*/apps/daemon.png
%{_iconsdir}/*/*/apps/kdeapp.png
%{_iconsdir}/*/*/apps/kernel.png
%{_iconsdir}/*/*/apps/running.png
%{_iconsdir}/*/*/apps/shell.png
%{_iconsdir}/*/*/apps/unknownapp.png
%{_iconsdir}/*/*/apps/waiting.png

%{_datadir}/kde4/services/desktop.desktop
%{_datadir}/kde4/services/devices.desktop
%{_datadir}/kde4/services/dma.desktop
%{_datadir}/kde4/services/interrupts.desktop
%{_datadir}/kde4/services/ioports.desktop
%{_datadir}/kde4/services/joystick.desktop
%{_datadir}/kde4/services/kcmusb.desktop
%{_datadir}/kde4/services/kcmview1394.desktop
%{_datadir}/kde4/services/kded/networkstatus.desktop
%{_datadir}/kde4/services/keyboard.desktop
%{_datadir}/kde4/services/keyboard_layout.desktop
%{_datadir}/kde4/services/keys.desktop
%{_datadir}/kde4/services/memory.desktop
%{_datadir}/kde4/services/mouse.desktop
%{_datadir}/kde4/services/nic.desktop
%{_datadir}/kde4/services/opengl.desktop
%{_datadir}/kde4/services/partitions.desktop
%{_datadir}/kde4/services/pci.desktop
%{_datadir}/kde4/services/processor.desktop
%{_datadir}/kde4/services/scsi.desktop
%{_datadir}/kde4/services/sound.desktop
%{_datadir}/kde4/services/xserver.desktop
%{_datadir}/sounds/pop.wav

%files kwin
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kwin_killer_helper
%attr(755,root,root) %{_bindir}/kwin_rules_dialog
%{_libdir}/kconf_update_bin/kwin_update_default_rules
%{_libdir}/kconf_update_bin/kwin_update_window_settings
%attr(755,root,root) %{_libdir}/kde4/kcm_kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwincompositing.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindesktop.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/libkwineffects.so.*
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so.*
%dir %{_datadir}/apps/kwin
%{_datadir}/apps/kwin/blur-render.frag
%{_datadir}/apps/kwin/blur-render.vert
%{_datadir}/apps/kwin/blur.frag
%{_datadir}/apps/kwin/blur.vert
%{_datadir}/apps/kwin/circle-edgy.png
%{_datadir}/apps/kwin/circle.png
%{_datadir}/apps/kwin/snowflake.png
%dir %{_datadir}/apps/kwin/default_rules
%{_datadir}/apps/kwin/default_rules/fsp_workarounds_1.kwinrules
%{_datadir}/apps/kwin/explosion-end.png
%{_datadir}/apps/kwin/explosion-start.png
%{_datadir}/apps/kwin/explosion.frag
%{_datadir}/apps/kwin/explosion.vert
%{_datadir}/apps/kwin/invert.frag
%{_datadir}/apps/kwin/invert.vert
%{_datadir}/apps/kwin/kwin.notifyrc
%{_datadir}/apps/kwin/lookingglass.frag
%{_datadir}/apps/kwin/lookingglass.vert
%{_datadir}/apps/kwin/shadow-texture.png
%{_datadir}/apps/kwin/sharpen.frag
%{_datadir}/apps/kwin/sharpen.vert
%{_datadir}/apps/kwin/trackmouse.png
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_iconsdir}/oxygen/16x16/apps/kwin.png
%{_iconsdir}/oxygen/32x32/apps/kwin.png
%{_iconsdir}/oxygen/48x48/apps/kwin.png
%{_iconsdir}/oxygen/scalable/apps/kwin.svgz
%dir %{_datadir}/kde4/services/kwin
%{_datadir}/kde4/services/kwin/blur.desktop
%{_datadir}/kde4/services/kwin/boxswitch.desktop
%{_datadir}/kde4/services/kwin/desktopgrid.desktop
%{_datadir}/kde4/services/kwin/desktopgrid_config.desktop
%{_datadir}/kde4/services/kwin/dialogparent.desktop
%{_datadir}/kde4/services/kwin/diminactive.desktop
%{_datadir}/kde4/services/kwin/diminactive_config.desktop
%{_datadir}/kde4/services/kwin/explosion.desktop
%{_datadir}/kde4/services/kwin/fade.desktop
%{_datadir}/kde4/services/kwin/fallapart.desktop
%{_datadir}/kde4/services/kwin/invert.desktop
%{_datadir}/kde4/services/kwin/invert_config.desktop
%{_datadir}/kde4/services/kwin/login.desktop
%{_datadir}/kde4/services/kwin/logout.desktop
%{_datadir}/kde4/services/kwin/lookingglass.desktop
%{_datadir}/kde4/services/kwin/lookingglass_config.desktop
%{_datadir}/kde4/services/kwin/magnifier.desktop
%{_datadir}/kde4/services/kwin/magnifier_config.desktop
%{_datadir}/kde4/services/kwin/maketransparent.desktop
%{_datadir}/kde4/services/kwin/maketransparent_config.desktop
%{_datadir}/kde4/services/kwin/minimizeanimation.desktop
%{_datadir}/kde4/services/kwin/mousemark.desktop
%{_datadir}/kde4/services/kwin/mousemark_config.desktop
%{_datadir}/kde4/services/kwin/presentwindows.desktop
%{_datadir}/kde4/services/kwin/presentwindows_config.desktop
%{_datadir}/kde4/services/kwin/scalein.desktop
%{_datadir}/kde4/services/kwin/shadow.desktop
%{_datadir}/kde4/services/kwin/shadow_config.desktop
%{_datadir}/kde4/services/kwin/sharpen.desktop
%{_datadir}/kde4/services/kwin/sharpen_config.desktop
%{_datadir}/kde4/services/kwin/showfps.desktop
%{_datadir}/kde4/services/kwin/showpaint.desktop
%{_datadir}/kde4/servicetypes/kwineffect.desktop
%{_datadir}/kde4/services/kwin/taskbarthumbnail.desktop
%{_datadir}/kde4/services/kwin/thumbnailaside.desktop
%{_datadir}/kde4/services/kwin/thumbnailaside_config.desktop
%{_datadir}/kde4/services/kwin/trackmouse.desktop
%{_datadir}/kde4/services/kwin/trackmouse_config.desktop
%{_datadir}/kde4/services/kwin/zoom.desktop
%{_datadir}/kde4/services/kwin/zoom_config.desktop
%{_datadir}/kde4/services/kwinactions.desktop
%{_datadir}/kde4/services/kwinadvanced.desktop
%{_datadir}/kde4/services/kwincompositing.desktop
%{_datadir}/kde4/services/kwinfocus.desktop
%{_datadir}/kde4/services/kwinmoving.desktop
%{_datadir}/kde4/services/kwinoptions.desktop
%{_datadir}/kde4/services/kwinrules.desktop
%{_datadir}/kde4/services/kwin/flipswitch.desktop
%{_datadir}/kde4/services/kwin/flipswitch_config.desktop
%{_datadir}/kde4/services/kwin/snow.desktop
%{_datadir}/kde4/services/kwin/snow_config.desktop
%{_datadir}/apps/kconf_update/kwin.upd
%{_datadir}/apps/kconf_update/kwin_focus1.sh
%{_datadir}/apps/kconf_update/kwin_focus1.upd
%{_datadir}/apps/kconf_update/kwin_focus2.sh
%{_datadir}/apps/kconf_update/kwin_focus2.upd
%{_datadir}/apps/kconf_update/kwin_fsp_workarounds_1.upd
%{_datadir}/apps/kconf_update/kwin_on_off.upd
%{_datadir}/apps/kconf_update/kwiniconify.upd
%{_datadir}/apps/kconf_update/kwinsticky.upd
%{_datadir}/apps/kconf_update/kwinupdatewindowsettings.upd
%{_datadir}/apps/kconf_update/khotkeys_printscreen.upd

%files plasma
%attr(755,root,root) %{_bindir}/plasma
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%attr(755,root,root) %{_libdir}/kde4/plasma_animator_default.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_battery.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_devicenotifier.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_dig_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_icon.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_launcher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lockout.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_pager.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_simplelauncher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_systemtray.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_desktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_panel.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_dict.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_filebrowser.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_hotplug.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mouse.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_places.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_powermanagement.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_weather.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_qscript.so
%attr(755,root,root) %{_libdir}/libkdeinit4_plasma.so
%attr(755,root,root) %{_libdir}/libplasma.so.*
%{_datadir}/apps/kwin/default_rules/plasma_desktop_containment.kwinrules
%dir %{_datadir}/apps/plasmoidviewer
%{_datadir}/apps/plasmoidviewer/checker.png
%{_datadir}/autostart/plasma.desktop
%lang(en) %{_kdedocdir}/en/plasma
%{_datadir}/kde4/services/plasma-animator-default.desktop
%{_datadir}/kde4/services/plasma-applet-analogclock.desktop
%{_datadir}/kde4/services/plasma-applet-devicenotifier.desktop
%{_datadir}/kde4/services/plasma-applet-digitalclock.desktop
%{_datadir}/kde4/services/plasma-applet-icon.desktop
%{_datadir}/kde4/services/plasma-applet-launcher.desktop
%{_datadir}/kde4/services/plasma-applet-lockout.desktop
%{_datadir}/kde4/services/plasma-applet-simplelauncher.desktop
%{_datadir}/kde4/services/plasma-applet-systemtray.desktop
%{_datadir}/kde4/services/plasma-battery-default.desktop
%{_datadir}/kde4/services/plasma-containment-desktop.desktop
%{_datadir}/kde4/services/plasma-containment-panel.desktop
%{_datadir}/kde4/services/plasma-dataengine-dict.desktop
%{_datadir}/kde4/services/plasma-dataengine-filebrowser.desktop
%{_datadir}/kde4/services/plasma-dataengine-hotplug.desktop
%{_datadir}/kde4/services/plasma-dataengine-mouse.desktop
%{_datadir}/kde4/services/plasma-dataengine-places.desktop
%{_datadir}/kde4/services/plasma-dataengine-powermanagement.desktop
%{_datadir}/kde4/services/plasma-dataengine-soliddevice.desktop
%{_datadir}/kde4/services/plasma-dataengine-tasks.desktop
%{_datadir}/kde4/services/plasma-dataengine-time.desktop
%{_datadir}/kde4/services/plasma-dataengine-weather.desktop
%{_datadir}/kde4/services/plasma-pager-default.desktop
%{_datadir}/kde4/services/plasma-runner-bookmarks.desktop
%{_datadir}/kde4/services/plasma-runner-calculator.desktop
%{_datadir}/kde4/services/plasma-runner-locations.desktop
%{_datadir}/kde4/services/plasma-runner-webshortcuts.desktop
%{_datadir}/kde4/services/plasma-scriptengine-qscript.desktop
%{_datadir}/kde4/services/plasma-tasks-default.desktop
%{_datadir}/kde4/servicetypes/plasma-animator.desktop
%{_datadir}/kde4/servicetypes/plasma-applet.desktop
%{_datadir}/kde4/servicetypes/plasma-dataengine.desktop
%{_datadir}/kde4/servicetypes/plasma-runner.desktop
%{_datadir}/kde4/servicetypes/plasma-scriptengine.desktop

%files solid
%attr(755,root,root) %{_bindir}/solidshell
%attr(755,root,root) %{_libdir}/kde4/kcm_solid.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakebluetooth.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakenet.so
%attr(755,root,root) %{_libdir}/kde4/solid_hal_power.so
%attr(755,root,root) %{_libdir}/libsolidcontrol.so.*
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so.*
%dir %{_datadir}/apps/solid
%dir %{_datadir}/apps/solid/actions
%dir %{_datadir}/apps/solidfakebluetoothbackend
%dir %{_datadir}/apps/solidfakenetbackend
%{_datadir}/apps/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/apps/solidfakebluetoothbackend/fakebluetooth.xml
%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml
%{_datadir}/kde4/services/kcm_solid.desktop
%{_datadir}/kde4/services/solidbackends
%{_datadir}/kde4/servicetypes/solidbluetoothmanager.desktop
%{_datadir}/kde4/servicetypes/solidnetworkmanager.desktop
%{_datadir}/kde4/servicetypes/solidpowermanager.desktop

%files networkmanager
%attr(755,root,root) %{_libdir}/kde4/solid_networkmanager.so
%{_iconsdir}/*/*x*/apps/networkmanager.png
            
%files kde-decoration-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindecoration.so
%{_datadir}/kde4/services/kwindecoration.desktop
%attr(755,root,root) %{_libdir}/libkdecorations.so.*

%files ksysguard
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ksysguarddrc
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%attr(755,root,root) %{_libdir}/libkdeinit4_ksysguard.so
%{_desktopdir}/kde4/ksysguard.desktop
%{_datadir}/apps/ksysguard
%{_iconsdir}/*/*/apps/ksysguardd.png
%lang(en) %{_kdedocdir}/en/ksysguard
# it looks like kde3 remains
%dir %{_datadir}/apps/kicker
%dir %{_datadir}/apps/kicker/applets
%{_datadir}/apps/kicker/applets/ksysguardapplet.desktop

%files -n kdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm-np
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kdm
%dir %{_datadir}/config/kdm
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/kdmrc
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/backgroundrc
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xsetup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xstartup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xwilling
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/config/kdm/Xaccess
%attr(754,root,root) /etc/rc.d/init.d/kdm
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdmctl
%attr(755,root,root) %{_libdir}/kde4/kcm_kdm.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_config
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_greet
# XXX move dir below elsewhere
%dir %{_datadir}/apps/doc
%{_datadir}/apps/doc/kdm
%{_datadir}/apps/kdm/*
%{_datadir}/config/kdm.knsrc
%{_datadir}/kde4/services/kdm.desktop
%{_datadir}/wallpapers/kdm_pld.png
%lang(en) %{_kdedocdir}/en/kdm

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%attr(755,root,root) %{_libdir}/kde4/kcm_screensaver.so
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*
%{_datadir}/config.kcfg/kscreensaversettings.kcfg
%{_datadir}/dbus-1/interfaces/org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kde4/services/ScreenSavers
%{_datadir}/kde4/services/screensaver.desktop
%{_datadir}/kde4/servicetypes/screensaver.desktop

%files kfontinst
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_libdir}/kde4/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/kde4/kcm_fonts.so
%attr(755,root,root) %{_libdir}/kde4/kfontviewpart.so
%attr(755,root,root) %{_libdir}/kde4/kio_fonts.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kfontprint
%attr(755,root,root) %{_libdir}/kde4/libexec/kio_fonts_helper
%attr(755,root,root) %{_libdir}/libkfontinst.so.*
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*
%dir %{_libdir}/strigi
%attr(755,root,root) %{_libdir}/strigi/strigita_font.so
%{_desktopdir}/kde4/kfontview.desktop
%{_datadir}/apps/kfontinst
%{_datadir}/apps/kfontview
%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_iconsdir}/*/*/apps/kfontview.png
%{_iconsdir}/*/scalable/apps/kfontview.svgz
%{_iconsdir}/*/scalable/apps/preferences-desktop-font-installer.svgz
%{_iconsdir}/*/*/mimetypes/fonts-package.png
%{_iconsdir}/*/scalable/mimetypes/fonts-package.svgz
%{_datadir}/kde4/services/ServiceMenus/installfont.desktop
%{_datadir}/kde4/services/fontinst.desktop
%{_datadir}/kde4/services/fonts.desktop
%{_datadir}/kde4/services/fonts.protocol
%{_datadir}/kde4/services/kfontviewpart.desktop

%files klipper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_libdir}/libkdeinit4_klipper.so
%{_desktopdir}/kde4/klipper.desktop
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%lang(en) %{_kdedocdir}/en/klipper

%files -n kde-splash-Default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default

%files -n kde-splash-Simple
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Simple

%files -n kde-splash-SimpleSmall
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/SimpleSmall

%files -n kde-kgreet-classic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_classic.so

%files -n kde-kgreet-winbind
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_winbind.so

%files -n kde-decoration-b2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_b2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde-decoration-keramik
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_keramik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_keramik_config.so
%{_datadir}/apps/kwin/keramik.desktop

%files -n kde-decoration-laptop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde-decoration-modernsys
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_modernsys.so
%attr(755,root,root) %{_libdir}/kde4/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde-decoration-quartz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_quartz.so
%attr(755,root,root) %{_libdir}/kde4/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde-decoration-redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde-decoration-web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde-decoration-kde2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_kde2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_kde2_config.so
%{_datadir}/apps/kwin/kde2.desktop

%files -n kde-decoration-oxygen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_oxygen.so
%{_datadir}/apps/kwin/oxygenclient.desktop

%files -n kde-decoration-plastic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_plastik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_plastik_config.so
%{_datadir}/apps/kwin/plastik.desktop

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Code_Poets_Dream
%{_datadir}/wallpapers/Colorado_Farm
%{_datadir}/wallpapers/Curls_on_Green
%{_datadir}/wallpapers/EOS
%{_datadir}/wallpapers/Emotion
%{_datadir}/wallpapers/Fields_of_Peace
%{_datadir}/wallpapers/Finally_Summer_in_Germany
%{_datadir}/wallpapers/Fresh_Morning
%{_datadir}/wallpapers/Golden_Ripples
%{_datadir}/wallpapers/Green_Concentration
%{_datadir}/wallpapers/Ladybuggin
%{_datadir}/wallpapers/Leafs_Labyrinth
%{_datadir}/wallpapers/Red_Leaf
%{_datadir}/wallpapers/Skeeter_Hawk
%{_datadir}/wallpapers/There_is_Rain_on_the_Table
%{_datadir}/wallpapers/default_blue.jpg
%{_datadir}/wallpapers/default_blue.jpg.desktop

%files libksgrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksgrd.so.*

%files infocenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_info.so
%lang(en) %{_kdedocdir}/en/kinfocenter/*
%{_datadir}/apps/kcmusb/usb.ids

%files devel
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%attr(755,root,root) %{_libdir}/libkfontinst.so
%attr(755,root,root) %{_libdir}/libkfontinstui.so
%attr(755,root,root) %{_libdir}/libkwineffects.so
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so
%attr(755,root,root) %{_libdir}/libkdecorations.so
%attr(755,root,root) %{_libdir}/libksgrd.so
%attr(755,root,root) %{_libdir}/libsolidcontrol.so
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so
%attr(755,root,root) %{_libdir}/libkworkspace.so
%attr(755,root,root) %{_libdir}/libprocesscore.so
%attr(755,root,root) %{_libdir}/libprocessui.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libweather_ion.so
%attr(755,root,root) %{_libdir}/libplasma.so
%attr(755,root,root) %{_libdir}/libplasmaclock.so
%{_datadir}/apps/cmake/modules/FindLibXKlavier.cmake
%{_datadir}/apps/cmake/modules/FindPAM.cmake
%{_datadir}/apps/cmake/modules/FindRAW1394.cmake
%{_datadir}/apps/cmake/modules/FindSensors.cmake
%{_datadir}/apps/cmake/modules/UnixAuth.cmake
%{_includedir}/KDE
%{_includedir}/*.h
%{_includedir}/kworkspace
%{_includedir}/plasma
%{_includedir}/solid
%{_includedir}/taskmanager
%{_includedir}/ksgrd
%{_includedir}/ksysguard
