# TODO:
# - subpackage PolicyKit-kde and O: PolicyKit-kde
%define		oname		kdebase-workspace
%define		_state		unstable
%define		qt4brver	4.5.1
%define		svn		979380

Summary:	KDE 4 base workspace components
Summary(pl.UTF-8):	Podstawowe komponenty środowiska KDE 4
Name:		kde4-kdebase-workspace
Version:	4.2.95
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{oname}-%{version}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{oname}-%{version}.tar.bz2
# Source0-md5:	fd95cf684f517bf45f8c26e0896d0593
Source1:	kdebase-kdesktop.pam
Source2:	kdebase-kdm.pam
Source3:	kdebase-kdm-np.pam
Source4:	kdebase-kdm.init
Source5:	kdebase-kdm.sysconfig
Source6:	kdebase-kdm_pldlogo.png
Source7:	kdebase-kdm_pldwallpaper.png
Source8:	kdebase-kde.pam
Source9:	%{name}-kcheckpass.pam
Source10:	%{name}-kscreensaver.pam
Source11:	kdebase-kdm.Xsession
Source15:	%{name}.desktop
Source16:	%{name}-session
Patch0:		%{name}-rootprivs.patch
Patch1:		%{name}-kdmconfig.patch
#Patch100: %{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:	ConsoleKit-devel
BuildRequires:	NetworkManager-devel >= 0.7.0-0.svn4027.1
BuildRequires:	OpenGL-devel
BuildRequires:	Qt3Support-devel >= %{qt4brver}
BuildRequires:	QtDesigner-devel >= %{qt4brver}
BuildRequires:	QtGui-devel >= %{qt4brver}
BuildRequires:	QtScript-devel >= %{qt4brver}
BuildRequires:	QtSvg-devel >= %{qt4brver}
BuildRequires:	QtTest-devel >= %{qt4brver}
BuildRequires:	QtUiTools-devel >= %{qt4brver}
BuildRequires:	QtWebKit-devel >= %{qt4brver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.3
BuildRequires:	google-gadgets-qt >= 0.10.5
BuildRequires:	gpsd-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdelibs-experimental-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libcaptury-devel
BuildRequires:	libggadget-qt-devel >= 0.10.5
BuildRequires:	libtirpc-devel
BuildRequires:	libusb-devel
BuildRequires:	libxklavier-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	polkit-qt-devel
BuildRequires:	python-sip-devel
BuildRequires:	qedje-devel >= 0.4.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qt4brver}
BuildRequires:	qzion-devel >= 0.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	soprano-devel >= 2.1.68
BuildRequires:	strigi-devel
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	kde4-icons-oxygen >= %{version}
Requires:	kde4-kdebase-workspace-solid >= %{version}
Requires:	xorg-app-xmessage
Requires:	xorg-app-xprop
Requires:	xorg-app-xset
Requires:	xorg-app-xsetroot
Suggests:	kde4-style-oxygen >= %{version}
Obsoletes:	PolicyKit-kde
Obsoletes:	kde4-kdebase-workspace-core
Obsoletes:	kde4-kdebase-workspace-kde4-decoration-libs
Obsoletes:	kdebase-desktop
Obsoletes:	kdebase4-workspace
Conflicts:	kdebase-core
Conflicts:	kdebase-desktop
Conflicts:	kdebase4-workspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains KDE base system which includes:
- KDE Control Centre with modules
- KWin window manager and several decorations
- KDE splash themes and plugins
- many more.

%description -l pl.UTF-8
Ten pakiet zawiera podstawowe aplikacje KDE:
- Centrum sterowania z modułami
- zarządcę okien Kwin wraz z dekoracjami
- ekrany startowe KDE
- wiele innych elementów.

%package libksgrd
Summary:	ksgrd library
Summary(pl.UTF-8):	Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig

%description libksgrd
A library containing functions for the system monitor KSysGuard.

%description libksgrd -l pl.UTF-8
Biblioteka zawierające funkcje monitora systemu - KSysGuard.

%package devel
Summary:	Include files to develop KDE applications
Summary(pl.UTF-8):	Pliki nagłówkowe potrzebne do tworzenia aplikacji KDE
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicativos que usem bibliotecas do kdebase
Group:		X11/Development/Libraries
Requires:	%{name}-plasma = %{version}-%{release}
Requires:	kde4-kdebase-workspace-libksgrd = %{version}-%{release}
Requires:	kde4-kdebase-workspace-screensavers = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains header files needed to develop KDE applications.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do programowania
aplikacji KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários
para compilar aplicativos que usem bibliotecas do kdebase.

%package kfontinst
Summary:	K Font Installer
Summary(pl.UTF-8):	Instalator fontów dla KDE
Group:		X11/Applications
Conflicts:	kdebase-kfontinst

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

%package kwin
Summary:	KWin - KDE 4 window manager
Summary(pl.UTF-8):	KWin - zarządca okien KDE 4
Group:		X11/Applications

%description kwin
KWin - KDE 4 window manager.

%description kwin -l pl.UTF-8
KWin - zarządca okien KDE 4.

%package plasma
Summary:	Plasma - KDE 4 panels and desktop work area
Summary(pl.UTF-8):	Plasma - panele i pulpit KDE 4
Group:		X11/Applications
Suggests:	google-gadgets-qt >= 0.10.4

%description plasma
Plasma - KDE 4 panels and desktop work area.

%description plasma -l pl.UTF-8
Plasma - panele i pulpit KDE 4.

%package screensavers
Summary:	KDE screensavers
Summary(pl.UTF-8):	Wygaszacze ekranu KDE
Summary(ru.UTF-8):	хранители экрана для KDE
Summary(uk.UTF-8):	зберігачі екрану для KDE
Group:		X11/Applications

%description screensavers
KDE screensavers.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu KDE.

%description screensavers -l ru.UTF-8
Некоторые 3D хранители экрана для K Desktop Environment.

%package solid
Summary:	Solid - KDE 4 hardware configuration
Summary(pl.UTF-8):	Solid - konfiguracja sprzętu w KDE 4
Group:		X11/Applications

%description solid
Solid - KDE 4 hardware configuration.

%description solid -l pl.UTF-8
Solid - konfiguracja sprzętu w KDE 4.

%package networkmanager
Summary:	Solid NetworkManager - network management using the NetworkManager daemon
Summary(pl.UTF-8):	Solid NetworkManager - zarządzanie siecią przy użyciu demona NetworkManager
Group:		X11/Applications
Requires:	%{name}-solid = %{version}-%{release}

%description networkmanager
Solid NetworkManager - network management using the NetworkManager
daemon.

%description networkmanager -l pl.UTF-8
Solid NetworkManager - zarządzanie siecią przy użyciu demona
NetworkManager.

%package kwrited
Summary:	KDE write messaging daemon
Summary(pl.UTF-8):	Demon do KDE obsługujący wymianę wiadomości za pomocą write
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdebase-kwrited

%description kwrited
A kde daeomn that watches for messages from local users sent with
write or wall.

%description kwrited -l pl.UTF-8
Demon KDE, który monitoruje wiadomości jakie lokalni użytkownicy
wysyłają za pomocą komend write lub wall.

%package wallpapers
Summary:	KDE 4 wallpapers
Summary(pl.UTF-8):	Tapety KDE 4
Group:		X11/Applications

%description wallpapers
KDE 4 wallpapers.

%description wallpapers -l pl.UTF-8
Tapety KDE 4.

%package -n kde4-kdm
Summary:	KDE Display Manager
Summary(pl.UTF-8):	Zarządca ekranów KDE
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	kde4-kgreet
Requires:	pam >= 0.99.7.1
Requires:	rc-scripts
Provides:	XDM
Obsoletes:	kdm < 9:3.0.0
Obsoletes:	kdm >= 4.0.0

%description -n kde4-kdm
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kde4-kdm -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.

%package -n kde4-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - B2
Group:		X11/Amusements

%description -n kde4-decoration-b2
A Beos like window decoration with rectangular window title to the
left. The actual window decoration does not take more than 20-30% of
the screen width and if two window titles overlap each other, they are
aligned next to each other.

%description -n kde4-decoration-b2 -l pl.UTF-8
Podobna do Beos dekoracja okien z prostokątnym tytułem okna po lewej
stronie. Nie zajmuje ona więcej niż 20-30% szerokości ekranu, a w
przypadkach gdyby dwie dekoracje się zasłaniały, są one układane obok
siebie.

%package -n kde4-decoration-kde2
Summary:	KDE Window Decoration - kde2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - kde2
Group:		X11/Amusements

%description -n kde4-decoration-kde2
KDE Window Decoration - kde2.

%description -n kde4-decoration-kde2 -l pl.UTF-8
Dekoracja okna dla KDE - kde2.

%package -n kde4-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl.UTF-8):	Dekoracja okna dla KDE - keramik
Group:		X11/Amusements

%description -n kde4-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde4-decoration-keramik -l pl.UTF-8
Dekoracja okna dla KDE - keramik.

%package -n kde4-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements

%description -n kde4-decoration-laptop
A window decoration with stripped window title and lightly convex
window buttons.

%description -n kde4-decoration-laptop -l pl.UTF-8
Dekoracja okna z paskowanym tytułem okna oraz lekko wypukłymi
przyciskami okna.

%package -n kde4-decoration-modernsys
Summary:	KDE Window Decoration - ModernSys
Summary(pl.UTF-8):	Dekoracja okna dla KDE - ModernSys
Group:		X11/Amusements

%description -n kde4-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde4-decoration-modernsys -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde4-decoration-oxygen
Summary:	KDE Window Decoration - Oxygen
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Oxygen
Group:		X11/Amusements

%description -n kde4-decoration-oxygen
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde4-decoration-oxygen -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde4-decoration-ozone
Summary:	KDE Window Decoration - Ozone
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Ozone
Group:		X11/Amusements
Requires:	kde4-kdebase-workspace-kwin >= %{version}

%description -n kde4-decoration-ozone
A window decoration Ozone.

%description -n kde4-decoration-ozone -l pl.UTF-8
Dekoracja okna Ozone.

%package -n kde4-decoration-plastic
Summary:	KDE Window Decoration - Plastic
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Plastic
Group:		X11/Amusements

%description -n kde4-decoration-plastic
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde4-decoration-plastic -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde4-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements

%description -n kde4-decoration-quartz
A window decoration with solid borders. The window caption consists of
a lighter area for the window title and a darker area for window
buttons. Between the two area there is a stylish transition.

%description -n kde4-decoration-quartz -l pl.UTF-8
Dekoracja okna z pełnymi krawędziami. Nagłówek okna składa się z
jasnego obszaru dla tytułu okna i ciemniejszego dla przycisków. Między
obszarami jest stylowy przejście.

%package -n kde4-decoration-redmond
Summary:	KDE Window Decoration - Redmond
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Redmond
Group:		X11/Amusements

%description -n kde4-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde4-decoration-redmond -l pl.UTF-8
Dekoracja okna przypominająca tę z Windows 98.

%package -n kde4-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements

%description -n kde4-decoration-web
A completely flat window decoration with rounded corners and visible,
thin borders.

%description -n kde4-decoration-web -l pl.UTF-8
Zupełnie płaska dekoracja okna z zaokrąglonymi brzegami oraz
widocznymi, cienkimi krawędziami.

%package -n kde4-kgreet-classic
Summary:	KDE greeter libraries - classic version
Summary(pl.UTF-8):	Biblioteki KDE służące do zapytań o hasło - wersja klasyczna
Group:		X11/Libraries
Provides:	kde4-kgreet

%description -n kde4-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde4-kgreet-classic -l pl.UTF-8
Narzędzia służące do zapytań o hasło - klasyczny, domyślny motyw
wyglądu.

%package -n kde4-kgreet-generic
Summary:	KDE greeter libraries - generic version
Summary(pl.UTF-8):	Biblioteki KDE służące do zapytań o hasło - wersja zwykła
Group:		X11/Libraries
Provides:	kde4-kgreet

%description -n kde4-kgreet-generic
Tools for asking for passwords in the generic, default look.

%description -n kde4-kgreet-generic -l pl.UTF-8
Narzędzia służące do zapytań o hasło - zwykły, domyślny motyw wyglądu.

%package -n kde4-kgreet-winbind
Summary:	KDE greeter libraries - winbind version
Summary(pl.UTF-8):	Biblioteki służące do zapytań o hasło - wersja winbind
Group:		X11/Libraries
Provides:	kde4-kgreet

%description -n kde4-kgreet-winbind
Tools for asking for passwords - winbind version.

%description -n kde4-kgreet-winbind -l pl.UTF-8
Narzędzia służące do zapytań o hasło - wersja winbind.

%package -n kde4-splash-Default
Summary:	Default clasic KDE splashscreen
Summary(pl.UTF-8):	Domyślny klasyczny ekran startowy KDE
Group:		X11/Amusements
Requires:	%{name} >= %{version}

%description -n kde4-splash-Default
Default splashscreen that came with this version of KDE.

%description -n kde4-splash-Default -l pl.UTF-8
Domyślny ekran powitalny dostarczony w tej wersji KDE.

%package -n kde4-splash-Simple
Summary:	KDE Simple splashscreen
Summary(pl.UTF-8):	Ekran powitalny KDE Simple
Group:		X11/Amusements
Requires:	%{name} >= %{version}

%description -n kde4-splash-Simple
KDE Simple splashcreen.

%description -n kde4-splash-Simple -l pl.UTF-8
Ekran powitalny KDE Simple.

%package -n kde4-splash-SimpleSmall
Summary:	KDE SimpleSmall splashscreen
Summary(pl.UTF-8):	Ekran powitalny KDE SimpleSmall
Group:		X11/Amusements
Requires:	%{name} >= %{version}

%description -n kde4-splash-SimpleSmall
KDE SimpleSmall splashcreen.

%description -n kde4-splash-SimpleSmall -l pl.UTF-8
Ekran powitalny KDE SimpleSmall.

%package svg-icons
Summary:	KDE SVG icons - oxygen
Summary(pl.UTF-8):	Motyw ikon SVG do KDE - oxygen
Group:		Themes
Requires:	kde4-icons-oxygen-svg

%description svg-icons
KDE icons - oxygen. This package contains SVG icons.

%description svg-icons -l pl.UTF-8
Motyw ikon do KDE - oxygen. Ten pakiet zawiera ikony SVG.

%prep
%setup -q -n %{oname}-%{version}
#%patch100 -p1
#%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DKDE4_KDM_PAM_SERVICE=kdm \
	-DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
	-DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT/etc/{X11/kdm,pam.d,security}
install -d $RPM_BUILD_ROOT%{_datadir}/config/kdm \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqueror \
	$RPM_BUILD_ROOT%{_datadir}/apps/kcontrol \
	$RPM_BUILD_ROOT%{_datadir}/apps/kcontrol/pics \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqsidebartng/virtual_folders/services

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/pam.d/kdesktop
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/kdm
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/pam.d/kdm-np
install %{SOURCE8}	$RPM_BUILD_ROOT/etc/pam.d/kde
install %{SOURCE9}	$RPM_BUILD_ROOT/etc/pam.d/kcheckpass
install %{SOURCE10}	$RPM_BUILD_ROOT/etc/pam.d/kscreensaver
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/sysconfig/kdm

install %{SOURCE11}	$RPM_BUILD_ROOT/etc/X11/kdm/Xsession

install %{SOURCE6}	$RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/pldlogo.png
install %{SOURCE7}	$RPM_BUILD_ROOT%{_datadir}/wallpapers/kdm_pld.png

install %{SOURCE16} $RPM_BUILD_ROOT%{_bindir}/kde4-session
install %{SOURCE15} $RPM_BUILD_ROOT/etc/X11/sessions/kde4.desktop

$RPM_BUILD_ROOT%{_bindir}/genkdmconf --in $RPM_BUILD_ROOT%{_datadir}/config/kdm
rm -f $RPM_BUILD_ROOT%{_datadir}/config/kdm/README
rm -f $RPM_BUILD_ROOT%{_datadir}/config/kdm/*.bak

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post -n kde4-kdm
/sbin/chkconfig --add kdm
if [ -f /var/lock/subsys/kdm ]; then
	%banner kde4-kdm -e <<EOF
 ***************************************************
 *                                                 *
 * NOTE:                                           *
 * To make sure that new version of KDM is running *
 * You should restart KDM with:                    *
 * "/sbin/service kdm restart".                    *
 *                                                 *
 * WARNING:                                        *
 * Restarting KDM will terminate any X session     *
 * started by it!                                  *
 *                                                 *
 ***************************************************

EOF
else
	%banner kde4-kdm -e <<EOF
Run "/sbin/service kdm start" to start kdm.

EOF
fi

%preun -n kde4-kdm
if [ "$1" = "0" ]; then
	%service kdm stop
	/sbin/chkconfig --del kdm
fi

%files
%defattr(644,root,root,755)
# dirs
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/kcontrol
%dir %{_datadir}/apps/kcontrol/pics
%dir %{_datadir}/apps/konqsidebartng/
%dir %{_datadir}/apps/konqsidebartng/virtual_folders
%dir %{_datadir}/apps/konqsidebartng/virtual_folders/services
%dir %{_datadir}/apps/ksplash/Themes
#
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemsettingsrc
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdesktop
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kstartupconfig4
%attr(755,root,root) %{_bindir}/ksystraycmd
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/safestartkde
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kdostartupconfig4
%attr(755,root,root) %{_bindir}/setscheduler
#%attr(755,root,root) %{_bindir}/polkit-kde-authorization
%attr(755,root,root) %{_libdir}/libkworkspace.so.*
%attr(755,root,root) %{_libdir}/libprocesscore.so.*
%attr(755,root,root) %{_libdir}/libprocessui.so.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*
%attr(755,root,root) %{_libdir}/libweather_ion.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit_startup.so
%attr(755,root,root) %{_libdir}/libkdeinit4_plasma-desktop.so
%attr(755,root,root) %{_libdir}/libkickoff.so
#%attr(755,root,root) %ghost %{_libdir}/libpolkitkdeprivate.so.?
#%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/libsystemsettingsview.so
%attr(755,root,root) %ghost %{_libdir}/libtime_solar.so.?
%attr(755,root,root) %{_libdir}/libtime_solar.so.*.*.*

# standard actions
%attr(755,root,root) %{_libdir}/kde4/kcm_standard_actions.so
%{_datadir}/kde4/services/standard_actions.desktop
%{_datadir}/kde4/services/settings-input-actions.desktop

# autostart
%attr(755,root,root) %{_libdir}/kde4/kcm_autostart.so
%{_datadir}/kde4/services/autostart.desktop

# kaccess
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_libdir}/libkdeinit4_kaccess.so
%{_datadir}/apps/kaccess
%{_datadir}/kde4/services/kaccess.desktop

# kcontrol
%{_datadir}/apps/kcontrol/pics/anchor.png
#%{_datadir}/apps/kcontrol/pics/energybig.png
#%{_datadir}/apps/kcontrol/pics/lo-energy.png
%{_datadir}/apps/kcontrol/pics/logo.png
%{_datadir}/apps/kcontrol/pics/mini-world.png
%{_datadir}/apps/kcontrol/pics/monitor.png
%{_kdedocdir}/en/kcontrol/*

# khotkeys
%attr(755,root,root) %{_libdir}/libkhotkeysprivate.so.?
%attr(755,root,root) %{_libdir}/libkhotkeysprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kcm_hotkeys.so
%attr(755,root,root) %{_libdir}/kde4/kded_khotkeys.so
#%attr(755,root,root) %{_libdir}/kconf_update_bin/khotkeys_update
%attr(755,root,root) %{_libdir}/kconf_update_bin/krdb_clearlibrarypath
%{_datadir}/apps/kcmkeys
#%{_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{_datadir}/apps/khotkeys
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_datadir}/kde4/services/kded/khotkeys.desktop
%{_datadir}/kde4/services/khotkeys.desktop
#%{_datadir}/dbus-1/services/kde-org.freedesktop.PolicyKit.AuthenticationAgent.service
#%{_datadir}/dbus-1/services/org.kde.PolicyKit.service

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
%attr(755,root,root) %{_libdir}/libkdeinit4_krunner.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_krunner_shell.so
%attr(755,root,root) %{_libdir}/kde4/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_calculatorrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_locations.so
%attr(755,root,root) %{_libdir}/kde4/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/kde4/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_powerdevil.so
%attr(755,root,root) %{_libdir}/kde4/krunner_services.so
%attr(755,root,root) %{_libdir}/kde4/krunner_sessions.so
%attr(755,root,root) %{_libdir}/kde4/krunner_shell.so
%attr(755,root,root) %{_libdir}/kde4/krunner_nepomuksearchrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/kde4/classic_mode.so
%attr(755,root,root) %{_libdir}/kde4/icon_mode.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_pkk_authorization.so
%attr(755,root,root) %{_libdir}/kde4/kded_notificationitemwatcher.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kscreenlocker
#%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-manager
#%attr(755,root,root) %{_libdir}/kde4/libexec/krunner_lock
%{_datadir}/kde4/services/recentdocuments.desktop
%{_datadir}/autostart/krunner.desktop
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/kde4/services/plasma-runner-nepomuksearch.desktop
%{_datadir}/kde4/services/plasma-applet-panelspacer-internal.desktop
%{_datadir}/kde4/services/plasma-applet-sm_ram.desktop
%{_datadir}/kde4/services/plasma-dataengine-calendar.desktop
%{_datadir}/kde4/services/plasma-dataengine-geolocation.desktop
%{_datadir}/kde4/services/plasma-engine-akonadi.desktop
%{_datadir}/kde4/services/plasma-engine-metadata.desktop
%{_datadir}/kde4/services/plasma-geolocation-gps.desktop
%{_datadir}/kde4/services/plasma-geolocation-ip.desktop
#%{_datadir}/kde4/services/kcm_pkk_authorization.desktop
%{_datadir}/kde4/services/kded/kephal.desktop
%{_datadir}/kde4/services/kded/notificationitemwatcher.desktop
%{_datadir}/kde4/services/settings-classic-view.desktop
%{_datadir}/kde4/services/settings-icon-view.desktop
%{_datadir}/kde4/servicetypes/systemsettingsview.desktop
%{_datadir}/kde4/servicetypes/plasma-geolocationprovider.desktop

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
%dir %{_datadir}/apps/ksplash/Themes/None
%{_datadir}/apps/ksplash/Themes/None/Theme.rc
%{_datadir}/config/ksplash.knsrc
%{_datadir}/kde4/services/ksplashthememgr.desktop
%{_iconsdir}/*/*/apps/ksplash.png

# ktip
#%attr(755,root,root) %{_bindir}/ktip
#%{_datadir}/autostart/ktip.desktop
#%{_desktopdir}/kde4/ktip.desktop

# kxkb
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_libdir}/libkdeinit4_kxkb.so
%lang(en) %{_kdedocdir}/en/kxkb
%{_iconsdir}/*/*/apps/kxkb.png

# systemsettings
%attr(755,root,root) %{_bindir}/systemsettings
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
%{_desktopdir}/kde4/systemsettings.desktop
%{_kdedocdir}/en/systemsettings
%{_kdedocdir}/en/PolicyKit-kde

# themes
%{_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{_datadir}/apps/kthememanager
%{_datadir}/apps/desktoptheme/default/widgets/

# styles
%attr(755,root,root) %{_libdir}/kde4/kcm_style.so
%attr(755,root,root) %{_libdir}/kde4/kstyle_keramik_config.so
%{_datadir}/kde4/services/style.desktop

# powerdevil
%attr(755,root,root) %{_libdir}/kde4/kcm_powerdevilconfig.so
%dir %{_datadir}/apps/powerdevil
%{_datadir}/apps/powerdevil/powerdevil.notifyrc
%{_datadir}/apps/powerdevil/default.powerdevilprofiles
%{_datadir}/kde4/services/powerdevilconfig.desktop
%{_datadir}/dbus-1/interfaces/org.kde.PowerDevil.xml

# nepomuk - FIXME
%attr(755,root,root) %{_libdir}/libnepomukquery.so
%attr(755,root,root) %{_libdir}/libnepomukquery.so.?
%attr(755,root,root) %{_libdir}/libnepomukquery.so.*.*.*
%attr(755,root,root) %{_libdir}/libnepomukqueryclient.so
%attr(755,root,root) %{_libdir}/libnepomukqueryclient.so.?
%attr(755,root,root) %{_libdir}/libnepomukqueryclient.so.*.*.*


# kdisplay
%attr(755,root,root) %{_libdir}/kde4/kcm_display.so
%{_datadir}/apps/kdisplay
%{_datadir}/apps/kconf_update/kcmdisplayrc.upd
%{_datadir}/kde4/services/display.desktop

# kdewizard
#%dir %{_datadir}/apps/kdewizard
#%{_datadir}/apps/kdewizard/tips

# ion
%attr(755,root,root) %{_libdir}/kde4/ion_bbcukmet.so
%attr(755,root,root) %{_libdir}/kde4/ion_envcan.so
%attr(755,root,root) %{_libdir}/kde4/ion_noaa.so
%{_datadir}/kde4/services/ion-bbcukmet.desktop
%{_datadir}/kde4/services/ion-envcan.desktop
%{_datadir}/kde4/services/ion-noaa.desktop
#%{_datadir}/kde4/servicetypes/weather_ion.desktop

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
%attr(755,root,root) %{_libdir}/kde4/kcm_joystick.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard_layout.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keys.so
%{_datadir}/kde4/services/kcm_keyboard.desktop
%{_datadir}/apps/kcminput/cursor_large_black.pcf.gz
%{_datadir}/apps/kcminput/cursor_large_white.pcf.gz
%{_datadir}/apps/kcminput/cursor_small_white.pcf.gz
%{_datadir}/apps/kcminput/pics/mouse_lh.png
%{_datadir}/apps/kcminput/pics/mouse_rh.png
# ?
%attr(755,root,root) %{_libdir}/kde4/kded_networkstatus.so
%attr(755,root,root) %{_libdir}/kde4/kded_powerdevil.so
%attr(755,root,root) %{_libdir}/kde4/libexec/krootimage
%attr(755,root,root) %{_libdir}/kde4/libexec/kcmdatetimehelper

# session
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kcheckpass
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kscreensaver
%attr(755,root,root) %{_bindir}/kde4-session
%attr(755,root,root) %{_libdir}/kde4/libexec/kcheckpass

# lsofui
%attr(755,root,root) %{_libdir}/liblsofui.so.?
%attr(755,root,root) %{_libdir}/liblsofui.so.*.*.*

#old core
%exclude %{_iconsdir}/oxygen/scalable
%dir %{_iconsdir}/oxygen/*/mimetypes
%dir %{_datadir}/apps/kcminput
%dir %{_datadir}/apps/kcminput/pics

%{_datadir}/apps/kconf_update/kaccel.upd
#%{_datadir}/apps/kconf_update/konqueror_gestures_kde321_update.upd
%{_datadir}/apps/kconf_update/kwin3_plugin.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/convertShortcuts.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kwin3_plugin.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/move_session_config.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/on-off_to_true-false.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/pluginlibFix.pl
%{_datadir}/config/background.knsrc
%{_datadir}/config/colorschemes.knsrc
%{_datadir}/config/wallpaper.knsrc
%{_iconsdir}/*/*/apps/kcmkwm.png
%{_iconsdir}/*/*/apps/computer.png
%{_iconsdir}/*/*/apps/daemon.png
%{_iconsdir}/*/*/apps/kdeapp.png
%{_iconsdir}/*/*/apps/kernel.png
%{_iconsdir}/*/*/apps/running.png
%{_iconsdir}/*/*/apps/shell.png
%{_iconsdir}/*/*/apps/unknownapp.png
%{_iconsdir}/*/*/apps/waiting.png

%{_datadir}/kde4/services/desktop.desktop
%{_datadir}/kde4/services/joystick.desktop
%{_datadir}/kde4/services/kded/networkstatus.desktop
%{_datadir}/kde4/services/kded/powerdevil.desktop
%{_datadir}/kde4/services/keyboard.desktop
%{_datadir}/kde4/services/keyboard_layout.desktop
%{_datadir}/kde4/services/keys.desktop
%{_datadir}/kde4/services/mouse.desktop
%{_datadir}/sounds/pop.wav
# old decoration libs
%attr(755,root,root) %{_libdir}/libkdecorations.so.*
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindecoration.so
%{_datadir}/kde4/services/kwindecoration.desktop
# kephal
%attr(755,root,root) %{_libdir}/kde4/kded_kephal.so
%attr(755,root,root) %{_libdir}/libkephal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkephal.so.?
#%{_datadir}/kde4/services/kded/kded_kephal.desktop
%{_datadir}/config.kcfg/plasma-shell-desktop.kcfg

#PolicyKit-kde
%attr(755,root,root) %{_bindir}/polkit-kde-authorization
%attr(755,root,root) %ghost %{_libdir}/libpolkitkdeprivate.so.?
%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kcm_pkk_authorization.so
%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-manager
#%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt.so.?
#%attr(755,root,root) %{_libdir}/libpolkit-qt.so.*.*.*
%{_datadir}/kde4/services/kcm_pkk_authorization.desktop
%{_datadir}/dbus-1/services/kde-org.freedesktop.PolicyKit.AuthenticationAgent.service
%{_datadir}/dbus-1/services/org.kde.PolicyKit.service

%files libksgrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksgrd.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkephal.so
%attr(755,root,root) %{_libdir}/libkdecorations.so
%attr(755,root,root) %{_libdir}/libkfontinst.so
%attr(755,root,root) %{_libdir}/libkfontinstui.so
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%attr(755,root,root) %{_libdir}/libksgrd.so
%attr(755,root,root) %{_libdir}/libkwineffects.so
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so
%attr(755,root,root) %{_libdir}/libkworkspace.so
%attr(755,root,root) %{_libdir}/libplasmaclock.so
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so
%attr(755,root,root) %{_libdir}/libprocesscore.so
%attr(755,root,root) %{_libdir}/libprocessui.so
%attr(755,root,root) %{_libdir}/libsolidcontrol.so
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libweather_ion.so
%attr(755,root,root) %{_libdir}/liblsofui.so
%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so
%attr(755,root,root) %{_libdir}/libtime_solar.so
# YES, this is wrong...
%{_libdir}/cmake/KDE4Workspace-4.2.90
#%{_libdir}/cmake/KDE4Workspace-%{version}
%{_includedir}/KDE/Plasma/Weather
%{_includedir}/plasma/geolocation
%{_includedir}/plasma/weather
%{_includedir}/*.h
%{_includedir}/kephal
%{_includedir}/kworkspace
%{_includedir}/ksgrd
%{_includedir}/ksysguard
%{_includedir}/solid
%{_includedir}/systemsettingsview
%{_includedir}/taskmanager
%{_includedir}/nepomuk
%{_includedir}/plasmaclock
%{_datadir}/apps/cmake/modules/*.cmake

%files kfontinst
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_libdir}/libkfontinst.so.*
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*
%attr(755,root,root) %{_libdir}/kde4/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/kde4/kcm_fonts.so
%attr(755,root,root) %{_libdir}/kde4/kfontviewpart.so
%attr(755,root,root) %{_libdir}/kde4/kio_fonts.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kfontprint
%attr(755,root,root) %{_libdir}/kde4/libexec/kio_fonts_helper
%attr(755,root,root) %{_libdir}/strigi/strigita_font.so
%{_desktopdir}/kde4/kfontview.desktop
%{_datadir}/apps/kfontinst
%{_datadir}/apps/kfontview
%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/kde4/services/ServiceMenus/installfont.desktop
%{_datadir}/kde4/services/fontinst.desktop
%{_datadir}/kde4/services/fonts.desktop
%{_datadir}/kde4/services/fonts.protocol
%{_datadir}/kde4/services/kfontviewpart.desktop
%{_iconsdir}/*/*/apps/kfontview.png
%{_iconsdir}/*/*/mimetypes/fonts-package.png

%files klipper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_libdir}/libkdeinit4_klipper.so
%{_datadir}/autostart/klipper.desktop
#%{_datadir}/config/klipperrc
%{_desktopdir}/kde4/klipper.desktop
%{_datadir}/apps/kconf_update/klipper-kconfigxt.upd
%lang(en) %{_kdedocdir}/en/klipper

%files ksysguard
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ksysguarddrc
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_libdir}/libkdeinit4_ksysguard.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so
%{_desktopdir}/kde4/ksysguard.desktop
%{_datadir}/apps/ksysguard
%{_iconsdir}/*/*/apps/ksysguardd.png
%{_datadir}/config/ksysguard.knsrc
%lang(en) %{_kdedocdir}/en/ksysguard

%files kwin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kwin_killer_helper
%attr(755,root,root) %{_bindir}/kwin_rules_dialog
%attr(755,root,root) %{_libdir}/libkwineffects.so.*
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwin4_effect_builtins.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kwin4_effect_videorecord.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwincompositing.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindesktop.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/kde4/kcm_desktopthemedetails.so
%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_builtins.so
#%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_videorecord.so
%attr(755,root,root) %{_libdir}/kde4/kwin_oxygen_config.so
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_default_rules
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_window_settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma-add-shortcut-to-menu
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma-to-plasma-desktop
%dir %{_datadir}/apps/kwin
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
%{_datadir}/apps/kwin/cubecap.png
%{_datadir}/apps/kwin/cylinder.frag
%{_datadir}/apps/kwin/cylinder.vert
%{_datadir}/apps/kwin/sphere.vert
%{_datadir}/apps/kwin/snow.frag
%{_datadir}/apps/kwin/snow.vert
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%dir %{_datadir}/kde4/services/kwin
%{_datadir}/kde4/services/desktopthemedetails.desktop
%{_datadir}/kde4/services/kwin/boxswitch.desktop
%{_datadir}/kde4/services/kwin/boxswitch_config.desktop
%{_datadir}/kde4/services/kwin/coverswitch.desktop
%{_datadir}/kde4/services/kwin/coverswitch_config.desktop
%{_datadir}/kde4/services/kwin/cubeslide_config.desktop
%{_datadir}/kde4/services/kwin/desktopgrid.desktop
%{_datadir}/kde4/services/kwin/desktopgrid_config.desktop
%{_datadir}/kde4/services/kwin/dialogparent.desktop
%{_datadir}/kde4/services/kwin/diminactive.desktop
%{_datadir}/kde4/services/kwin/diminactive_config.desktop
%{_datadir}/kde4/services/kwin/dimscreen.desktop
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
%{_datadir}/kde4/services/kwin/slide.desktop
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
%{_datadir}/kde4/services/kwin/showfps_config.desktop
%{_datadir}/kde4/services/kwin/wobblywindows.desktop
%{_datadir}/kde4/services/kwin/wobblywindows_config.desktop
%{_datadir}/kde4/services/kwin/cube.desktop
%{_datadir}/kde4/services/kwin/cube_config.desktop
%{_datadir}/kde4/services/kwin/magiclamp.desktop
%{_datadir}/kde4/services/kwin/taskbarthumbnail.desktop
%{_datadir}/kde4/services/kwin/cubeslide.desktop
%{_datadir}/kde4/services/kwin/fadedesktop.desktop
%{_datadir}/kde4/services/kwin/highlightwindow.desktop
%{_datadir}/kde4/services/kwin/magiclamp_config.desktop
%{_datadir}/kde4/services/kwin/sheet.desktop
%{_datadir}/kde4/services/kwin/slideback.desktop
%{_datadir}/kde4/services/kwin/snaphelper.desktop
%{_datadir}/kde4/services/kwin/translucency.desktop
%{_datadir}/kde4/services/kwin/translucency_config.desktop
%{_datadir}/kde4/services/kwinscreenedges.desktop
%{_datadir}/kde4/servicetypes/kwineffect.desktop
%{_datadir}/apps/kconf_update/plasma-add-shortcut-to-menu.upd
%{_datadir}/apps/kconf_update/krdb.upd
%{_datadir}/apps/kconf_update/kwin.upd
%{_datadir}/apps/kconf_update/kwin_focus1.sh
%{_datadir}/apps/kconf_update/kwin_focus1.upd
%{_datadir}/apps/kconf_update/kwin_focus2.sh
%{_datadir}/apps/kconf_update/kwin_focus2.upd
%{_datadir}/apps/kconf_update/kwin_fsp_workarounds_1.upd
%{_datadir}/apps/kconf_update/kwin_on_off.upd
%{_datadir}/apps/kconf_update/kwin_window_shortcuts.sh
%{_datadir}/apps/kconf_update/kwin_window_shortcuts.upd
%{_datadir}/apps/kconf_update/kwiniconify.upd
%{_datadir}/apps/kconf_update/kwinsticky.upd
%{_datadir}/apps/kconf_update/kwinupdatewindowsettings.upd
%{_datadir}/apps/kconf_update/plasma-to-plasmadesktop-shortcuts.upd
%{_datadir}/apps/kconf_update/plasmarc-to-plasmadesktoprc.upd
#%{_datadir}/apps/kconf_update/khotkeys_printscreen.upd
%{_iconsdir}/oxygen/16x16/apps/kwin.png
%{_iconsdir}/oxygen/32x32/apps/kwin.png
%{_iconsdir}/oxygen/48x48/apps/kwin.png
%{_iconsdir}/Oxygen_Black
%{_iconsdir}/Oxygen_Black_Big
%{_iconsdir}/Oxygen_Blue
%{_iconsdir}/Oxygen_Blue_Big
%{_iconsdir}/Oxygen_White
%{_iconsdir}/Oxygen_White_Big
%{_iconsdir}/Oxygen_Yellow
%{_iconsdir}/Oxygen_Yellow_Big
%{_iconsdir}/Oxygen_Zion
%{_iconsdir}/Oxygen_Zion_Big

%files plasma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-desktop
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmawallpaperviewer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%attr(755,root,root) %{_bindir}/plasma-overlay
#%attr(755,root,root) %{_libdir}/libkdeinit4_plasma.so
%attr(755,root,root) %{_libdir}/kde4/plasma_animator_default.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_battery.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_devicenotifier.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_dig_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_icon.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_launcher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lockout.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_pager.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_quicklaunch.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_simplelauncher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_systemtray.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_trash.so
%attr(755,root,root) %{_libdir}/kde4/plasma_appletscript_qedje.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_appletscript_simple_javascript.so
%attr(755,root,root) %{_libdir}/kde4/plasma_appletscriptengine_dashboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_appletscriptengine_webapplet.so
%attr(755,root,root) %{_libdir}/kde4/plasma_package_qedje.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_dashboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_web.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_desktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_panel.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_dict.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_executable.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_filebrowser.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_hotplug.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mouse.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_network.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_places.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_powermanagement.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_rss.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_weather.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_saverdesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_color.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_image.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_activitybar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_calendar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_cpu.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_hdd.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_hwinfo.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_net.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_temperature.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_system-monitor.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_webbrowser.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_applicationjobs.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_favicons.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_notifications.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_nowplaying.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_systemmonitor.so
%attr(755,root,root) %{_libdir}/kde4/plasma_package_ggl.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_ggl.so
%attr(755,root,root) %{_libdir}/kde4/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/kde4/plasma-geolocation-ip.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_panelspacer_internal.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_ram.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_akonadi.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_calendar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_geolocation.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_metadata.so
%{_datadir}/apps/plasma/plasmoids
%attr(755,root,root) %{_libdir}/libplasma_applet-system-monitor.so.*
%{_libdir}/libplasma_applet-system-monitor.so
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasma-geolocation-interface.so.?
%attr(755,root,root) %{_libdir}/libplasmaclock.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasmaclock.so.?
%dir %{_datadir}/apps/kwin/default_rules
%{_datadir}/apps/kwin/default_rules/plasma_desktop_containment.kwinrules
%dir %{_datadir}/apps/plasma
%{_datadir}/apps/plasma/dashboard
%{_datadir}/autostart/plasma.desktop
%{_datadir}/config/plasma-themes.knsrc
%{_datadir}/config/plasma-overlayrc
%dir %{_datadir}/apps/plasma_scriptengine_ruby
%{_datadir}/apps/plasma_scriptengine_ruby/applet.rb
%{_datadir}/apps/plasma_scriptengine_ruby/data_engine.rb
%{_datadir}/kde4/services/plasma-scriptengine-ruby-applet.desktop
%{_datadir}/kde4/services/plasma-scriptengine-ruby-dataengine.desktop
%dir %{_datadir}/apps/plasma/services
%{_datadir}/apps/plasma/services/applicationjobs.operations
%{_datadir}/apps/plasma/services/notifications.operations
%{_datadir}/apps/plasma/services/nowplaying.operations
%{_datadir}/apps/plasma/services/tasks.operations
%{_datadir}/kde4/services/plasma-animator-default.desktop
%{_datadir}/kde4/services/plasma-applet-analogclock.desktop
%{_datadir}/kde4/services/plasma-applet-devicenotifier.desktop
%{_datadir}/kde4/services/plasma-applet-digitalclock.desktop
%{_datadir}/kde4/services/plasma-applet-icon.desktop
%{_datadir}/kde4/services/plasma-applet-launcher.desktop
%{_datadir}/kde4/services/plasma-applet-lockout.desktop
%{_datadir}/kde4/services/plasma-applet-quicklaunch.desktop
%{_datadir}/kde4/services/plasma-applet-simplelauncher.desktop
%{_datadir}/kde4/services/plasma-applet-systemtray.desktop
%{_datadir}/kde4/services/plasma-applet-trash.desktop
%{_datadir}/kde4/services/plasma-applet-activitybar.desktop
%{_datadir}/kde4/services/plasma-applet-calendar.desktop
%{_datadir}/kde4/services/plasma-appletscript-qedje.desktop
%{_datadir}/kde4/services/plasma-applet-sm_cpu.desktop
%{_datadir}/kde4/services/plasma-applet-sm_hdd.desktop
%{_datadir}/kde4/services/plasma-applet-sm_hwinfo.desktop
%{_datadir}/kde4/services/plasma-applet-sm_net.desktop
%{_datadir}/kde4/services/plasma-applet-sm_temperature.desktop
%{_datadir}/kde4/services/plasma-applet-system-monitor.desktop
%{_datadir}/kde4/services/plasma-applet-webbrowser.desktop
%{_datadir}/kde4/services/plasma-dataengine-applicationjobs.desktop
%{_datadir}/kde4/services/plasma-dataengine-favicons.desktop
%{_datadir}/kde4/services/plasma-dataengine-notifications.desktop
%{_datadir}/kde4/services/plasma-dataengine-nowplaying.desktop
%{_datadir}/kde4/services/plasma-dataengine-systemmonitor.desktop
%{_datadir}/kde4/services/plasma-packagestructure-dashboard.desktop
%{_datadir}/kde4/services/plasma-packagestructure-qedje.desktop
%{_datadir}/kde4/services/plasma-packagestructure-web.desktop
%{_datadir}/kde4/services/plasma-scriptengine-applet-dashboard.desktop
%{_datadir}/kde4/services/plasma-scriptengine-applet-web.desktop
#%{_datadir}/kde4/services/plasma-scriptengine-applet-simple-javascript.desktop
%{_datadir}/kde4/services/plasma-battery-default.desktop
%{_datadir}/kde4/services/plasma-containment-desktop.desktop
%{_datadir}/kde4/services/plasma-containment-panel.desktop
%{_datadir}/kde4/services/plasma-dataengine-executable.desktop
%{_datadir}/kde4/services/plasma-dataengine-dict.desktop
%{_datadir}/kde4/services/plasma-dataengine-filebrowser.desktop
%{_datadir}/kde4/services/plasma-dataengine-hotplug.desktop
%{_datadir}/kde4/services/plasma-dataengine-mouse.desktop
%{_datadir}/kde4/services/plasma-dataengine-network.desktop
%{_datadir}/kde4/services/plasma-dataengine-places.desktop
%{_datadir}/kde4/services/plasma-dataengine-powermanagement.desktop
%{_datadir}/kde4/services/plasma-dataengine-rss.desktop
%{_datadir}/kde4/services/plasma-dataengine-soliddevice.desktop
%{_datadir}/kde4/services/plasma-dataengine-tasks.desktop
%{_datadir}/kde4/services/plasma-dataengine-time.desktop
%{_datadir}/kde4/services/plasma-dataengine-weather.desktop
%{_datadir}/kde4/services/plasma-pager-default.desktop
%{_datadir}/kde4/services/plasma-runner-bookmarks.desktop
%{_datadir}/kde4/services/plasma-runner-calculator.desktop
%{_datadir}/kde4/services/plasma-runner-locations.desktop
%{_datadir}/kde4/services/plasma-runner-webshortcuts.desktop
%{_datadir}/kde4/services/plasma-runner-places.desktop
%{_datadir}/kde4/services/plasma-runner-powerdevil.desktop
%{_datadir}/kde4/services/plasma-runner-services.desktop
%{_datadir}/kde4/services/plasma-runner-sessions.desktop
%{_datadir}/kde4/services/plasma-runner-shell.desktop
%{_datadir}/kde4/services/plasma-tasks-default.desktop
%{_datadir}/kde4/services/plasma-containment-saverdesktop.desktop
%{_datadir}/kde4/services/plasma-wallpaper-color.desktop
%{_datadir}/kde4/services/plasma-wallpaper-image.desktop
%{_datadir}/kde4/services/plasma-applet-ggl-photos.desktop
%{_datadir}/kde4/services/plasma-applet-ggl-rss.desktop
%{_datadir}/kde4/services/plasma-packagestructure-googlegadgets.desktop
%{_datadir}/kde4/services/plasma-scriptengine-googlegadgets.desktop
#%{_datadir}/kde4/services/plasma-scriptengine-runner-javascript.desktop
%dir %{_datadir}/apps/desktoptheme/default/system-monitor
%{_datadir}/apps/desktoptheme/default/system-monitor/hdd_panel.svgz
%dir %{_datadir}/apps/desktoptheme/default/calendar
%{_datadir}/apps/desktoptheme/default/calendar/mini-calendar.svgz
%{_datadir}/autostart/plasma-desktop.desktop
%lang(en) %{_kdedocdir}/en/plasma
%{_mandir}/man1/plasmaengineexplorer.1*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*
%attr(755,root,root) %{_libdir}/kde4/kcm_screensaver.so
%{_datadir}/config.kcfg/kscreensaversettings.kcfg
%{_datadir}/dbus-1/interfaces/org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kde4/services/ScreenSavers
%{_datadir}/kde4/services/screensaver.desktop
%{_datadir}/kde4/servicetypes/screensaver.desktop

%files solid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/solid-action-desktop-gen
%attr(755,root,root) %{_bindir}/solid-bluetooth
%attr(755,root,root) %{_bindir}/solid-network
%attr(755,root,root) %{_bindir}/solid-powermanagement
%attr(755,root,root) %{_libdir}/libsolidcontrol.so.*
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so.*
%attr(755,root,root) %{_libdir}/kde4/kcm_solid.so
%attr(755,root,root) %{_libdir}/kde4/kcm_solid_actions.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakenet.so
%attr(755,root,root) %{_libdir}/kde4/solid_hal_power.so
%attr(755,root,root) %{_libdir}/kde4/solid_bluez.so
%attr(755,root,root) %{_libdir}/kde4/solid_wicd.so
%dir %{_datadir}/apps/solid
%dir %{_datadir}/apps/solid/actions
%dir %{_datadir}/apps/solid/devices
%{_datadir}/apps/solid/devices/*.desktop
%dir %{_datadir}/apps/solidfakenetbackend
%{_datadir}/apps/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml
%{_datadir}/kde4/services/kcm_solid.desktop
%{_datadir}/kde4/services/solidbackends
%{_datadir}/kde4/services/solid-actions.desktop
%{_datadir}/kde4/servicetypes/solidbluetoothmanager.desktop
%{_datadir}/kde4/servicetypes/solidnetworkmanager.desktop
%{_datadir}/kde4/servicetypes/solidpowermanager.desktop
%dir %{_datadir}/apps/kcmsolidactions
%{_datadir}/apps/kcmsolidactions/solid-action-template.desktop

%files networkmanager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/solid_networkmanager07.so
%{_iconsdir}/*/*x*/apps/networkmanager.png

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_kwrited.so
%{_datadir}/kde4/services/kded/kwrited.desktop
%dir %{_datadir}/apps/kwrited
%{_datadir}/apps/kwrited/kwrited.notifyrc

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Air
%{_datadir}/wallpapers/Aghi
%{_datadir}/wallpapers/Atra_Dot
%{_datadir}/wallpapers/Code_Poets_Dream
%{_datadir}/wallpapers/Curls_on_Green
%{_datadir}/wallpapers/EOS
%{_datadir}/wallpapers/Evening
%{_datadir}/wallpapers/Fields_of_Peace
%{_datadir}/wallpapers/Finally_Summer_in_Germany
%{_datadir}/wallpapers/Fresh_Morning
%{_datadir}/wallpapers/Plasmalicious
%{_datadir}/wallpapers/Red_Leaf
%{_datadir}/wallpapers/Spring_Sunray
%{_datadir}/wallpapers/There_is_Rain_on_the_Table
%{_datadir}/wallpapers/The_Rings_of_Saturn
%{_datadir}/wallpapers/default_blue.jpg
%{_datadir}/wallpapers/default_blue.jpg.desktop

%files -n kde4-kdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdm-np
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.kdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kdm
%dir /etc/X11/kdm
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/kdmrc
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/backgroundrc
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xreset
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xsetup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xstartup
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xwilling
%config(noreplace) %verify(not md5 mtime size) /etc/X11/kdm/Xaccess
%attr(754,root,root) /etc/rc.d/init.d/kdm
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdmctl
%attr(755,root,root) %{_libdir}/kde4/kcm_kdm.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_config
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_greet
/etc/X11/sessions
# XXX move dir below elsewhere
%dir %{_datadir}/apps/doc
%{_datadir}/apps/doc/kdm
%dir %{_datadir}/apps/kdm
%{_datadir}/apps/kdm/*
%{_datadir}/config/kdm.knsrc
%{_datadir}/kde4/services/kdm.desktop
%{_datadir}/wallpapers/kdm_pld.png
%lang(en) %{_kdedocdir}/en/kdm

%files svg-icons
%defattr(644,root,root,755)
%{_iconsdir}/*/scalable/apps/kcmkwm.svgz
%{_iconsdir}/*/scalable/apps/kfontview.svgz
%{_iconsdir}/*/scalable/apps/preferences-desktop-font-installer.svgz
%{_iconsdir}/*/scalable/mimetypes/fonts-package.svgz
%{_iconsdir}/*/scalable/apps/kwin.svgz

%files -n kde4-decoration-b2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_b2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde4-decoration-kde2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_kde2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_kde2_config.so
%{_datadir}/apps/kwin/kde2.desktop

%files -n kde4-decoration-keramik
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_keramik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_keramik_config.so
%{_datadir}/apps/kwin/keramik.desktop

%files -n kde4-decoration-laptop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde4-decoration-modernsys
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_modernsys.so
%attr(755,root,root) %{_libdir}/kde4/kwin_modernsys_config.so
%{_datadir}/apps/kwin/modernsystem.desktop

%files -n kde4-decoration-oxygen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_oxygen.so
%{_datadir}/apps/kwin/oxygenclient.desktop

%files -n kde4-decoration-ozone
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_ozone.so
%{_datadir}/apps/kwin/ozoneclient.desktop
%attr(755,root,root) %{_libdir}/kde4/kwin_ozone_config.so

%files -n kde4-decoration-plastic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_plastik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_plastik_config.so
%{_datadir}/apps/kwin/plastik.desktop

%files -n kde4-decoration-quartz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_quartz.so
%attr(755,root,root) %{_libdir}/kde4/kwin_quartz_config.so
%{_datadir}/apps/kwin/quartz.desktop

%files -n kde4-decoration-redmond
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_redmond.so
%{_datadir}/apps/kwin/redmond.desktop

%files -n kde4-decoration-web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_web.so
%{_datadir}/apps/kwin/web.desktop

%files -n kde4-kgreet-classic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_classic.so

%files -n kde4-kgreet-generic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_generic.so

%files -n kde4-kgreet-winbind
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_winbind.so

%files -n kde4-splash-Default
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default

%files -n kde4-splash-Simple
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Simple

%files -n kde4-splash-SimpleSmall
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/SimpleSmall
