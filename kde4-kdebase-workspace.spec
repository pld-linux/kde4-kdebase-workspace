# TODO:
# - subpackage PolicyKit-kde and O: PolicyKit-kde
%define		orgname		kde-workspace
%define		_state		stable
%define		qtver		4.8.3

Summary:	KDE 4 base workspace components
Summary(pl.UTF-8):	Podstawowe komponenty środowiska KDE 4
Name:		kde4-kdebase-workspace
Version:	4.9.4
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b26cc75639cada6de8c96ee752c0291b
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
Patch100:	%{name}-branch.diff
Patch0:		%{name}-rootprivs.patch
Patch1:		%{name}-kdmconfig.patch
Patch2:		%{name}-kdm_revertcrashlogic.patch
Patch3:		kde4-kdebase-workspace-brightness.patch
URL:		http://www.kde.org/
BuildRequires:	ConsoleKit-devel
BuildRequires:	Mesa-libGLES-devel
BuildRequires:	NetworkManager-devel >= 0.8.999
BuildRequires:	OpenGL-devel
BuildRequires:	akonadi-devel >= 1.3.80
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eet-devel
BuildRequires:	google-gadgets-qt >= 0.11.0
BuildRequires:	gpsd-devel
BuildRequires:	kde4-kactivities-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libcaptury-devel
BuildRequires:	libdbusmenu-qt-devel >= 0.6.0
BuildRequires:	libdmtx-devel
BuildRequires:	libggadget-qt-devel >= 0.11.0
BuildRequires:	libqalculate-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtirpc-devel
BuildRequires:	libusb-compat-devel
BuildRequires:	libxklavier-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	pciutils-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	polkit-qt-1-gui-devel >= 0.99.0
BuildRequires:	python-sip-devel
BuildRequires:	qedje-devel >= 0.4.0
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qzion-devel >= 0.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	strigi-devel >= 0.7.0
BuildRequires:	utempter-devel
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	kde4-icons-oxygen >= %{version}
Requires:	kde4-kdebase-workspace-solid >= %{version}
Requires:	rc-scripts
Requires:	xorg-app-setxkbmap
Requires:	xorg-app-xmessage
Requires:	xorg-app-xprop
Requires:	xorg-app-xset
Requires:	xorg-app-xsetroot
Suggests:	fontconfig
Suggests:	kde4-decoration-oxygen >= %{version}
Suggests:	kde4-style-oxygen >= %{version}
Obsoletes:	kde4-decoration-ozone
Obsoletes:	kde4-kdebase-workspace-core
Obsoletes:	kde4-kdebase-workspace-kde4-decoration-libs
Obsoletes:	kde4-kdebase-workspace-wallpapers
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
Pakiet zawiera pliki nagłówkowe niezbędne do programowania aplikacji
KDE.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos que usem bibliotecas do kdebase.

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
#Requires:	pciutils
Obsoletes:	kde4-kdebase-infocenter

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.

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
Requires:	%{name}-solid = %{version}-%{release}
Requires:	%{name}-ksysguard = %{version}-%{release}
Requires:	libdbusmenu-qt >= 0.6.0
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
Suggests:	udisks
Suggests:	upower

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
A kde daemon that watches for messages from local users sent with
write or wall.

%description kwrited -l pl.UTF-8
Demon KDE, który monitoruje wiadomości jakie lokalni użytkownicy
wysyłają za pomocą komend write lub wall.

%package -n kde4-kdm
Summary:	KDE Display Manager
Summary(pl.UTF-8):	Zarządca ekranów KDE
Group:		X11/Applications
Requires:	/usr/bin/X
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post,postun):	systemd-units >= 38
Requires:	/etc/X11/xinit/Xclients
Requires:	dbus-x11
Requires:	kde4-kgreet
Requires:	pam >= 0.99.7.1
Requires:	rc-scripts
Requires:	systemd-units >= 0.38
Requires:	xinitrc-ng >= 1.0
Provides:	XDM
Provides:	user(kdm)
Obsoletes:	kde4-kdm-systemd
Obsoletes:	kdm < 9:3.0.0
Obsoletes:	kdm >= 4.0.0

%description -n kde4-kdm
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kde4-kdm -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.

%package -n kde4-decoration-aurorae
Summary:	KDE Window Decoration Engine - Aurorae
Summary(pl.UTF-8):	Silnik Dekoracji okien dla KDE - Aurorae
Group:		X11/Amusements

%description -n kde4-decoration-aurorae
Aurorae is a theme engine for KWin window decorations.

%description -n kde4-decoration-aurorae -l pl.UTF-8
Aurorae jest silnikiem dekoracji dla okien KWin.

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

%package -n kde4-decoration-nitrogen
Summary:	KDE Window Decoration - nitrogen
Summary(pl.UTF-8):	Dekoracja okna dla KDE - nitrogen
Group:		X11/Amusements

%description -n kde4-decoration-nitrogen
KDE Window Decoration - nitrogen.

%description -n kde4-decoration-nitrogen -l pl.UTF-8
Dekoracja okna dla KDE - nitrogen.

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

%package -n python-plasma
Summary:	Python plasma for KDE
Group:		Libraries/Python
Requires:	%{name}-plasma = %{version}-%{release}
Requires:	python-PyKDE4

%description -n python-plasma
Python plasma for KDE.

%package -n kde4-style-oxygen
Summary:	KDE Oxygen Style
Summary(pl.UTF-8):	Styl Oxygen dla KDE
Group:		Themes
Obsoletes:	kde-style-oxygen

%description -n kde4-style-oxygen
KDE Oxygen Style.

%description -n kde4-style-oxygen -l pl.UTF-8
Styl Oxygen dla KDE.

%package -n PolicyKit-kde
Summary:	KDE PolicyKit
Summary(pl.UTF-8):	PolicyKit dla KDE
Group:		X11/Applications

%description -n PolicyKit-kde
PolicyKit-kde provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -n PolicyKit-kde -l pl.UTF-8
PolicyKit-kde dostarcza sesję D-BUSa, która używana jest do okienek
dialogowych mających na celu rozszerzenie przywilejów użytkownika.

%prep
%setup -q -n %{orgname}-%{version}
#%%patch100 -p1
%patch0 -p1
%patch1 -p1
# https://bugs.kde.org/show_bug.cgi?id=281862
#%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake \
	-DLIBEXEC_INSTALL_DIR=%{_libdir}/kde4/libexec \
	-DKDE4_KDM_PAM_SERVICE=kdm \
	-DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
	-DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
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

install %{SOURCE16} $RPM_BUILD_ROOT%{_bindir}/kde4-session
install %{SOURCE15} $RPM_BUILD_ROOT/etc/X11/sessions/kde4.desktop

$RPM_BUILD_ROOT%{_bindir}/genkdmconf --in $RPM_BUILD_ROOT%{_datadir}/config/kdm
rm -rf $RPM_BUILD_ROOT%{_datadir}/config/kdm

touch $RPM_BUILD_ROOT/etc/security/blacklist.kdm

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
# don't clean .py files!

# systemd
install -d $RPM_BUILD_ROOT/%{systemdunitdir}
ln -s /dev/null $RPM_BUILD_ROOT/%{systemdunitdir}/kdm.service

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n kde4-style-oxygen	-p /sbin/ldconfig
%postun	-n kde4-style-oxygen	-p /sbin/ldconfig

%post	libksgrd	-p /sbin/ldconfig
%postun	libksgrd	-p /sbin/ldconfig

%post	-n PolicyKit-kde	-p /sbin/ldconfig
%postun	-n PolicyKit-kde	-p /sbin/ldconfig

%pre -n kde4-kdm
%groupadd -g 252 kdm
%useradd -u 252 -d /etc/X11/kdm -g kdm -c "KDE Display Manager User" kdm

%postun -n kde4-kdm
if [ "$1" = "0" ]; then
        %userremove kdm
        %groupremove kdm
fi
%systemd_reload

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
%systemd_reload

%preun -n kde4-kdm
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del kdm
fi

%files
%defattr(644,root,root,755)
# dirs
%dir %{_datadir}/apps/kcontrol
%dir %{_datadir}/apps/kcontrol/pics
%dir %{_datadir}/apps/konqsidebartng/
%dir %{_datadir}/apps/konqsidebartng/virtual_folders
%dir %{_datadir}/apps/konqsidebartng/virtual_folders/services
#
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemsettingsrc
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kdesktop
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kstartupconfig4
%attr(755,root,root) %{_bindir}/ksystraycmd
%attr(755,root,root) %{_bindir}/startkde
#%attr(755,root,root) %{_bindir}/safestartkde
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kdostartupconfig4
%attr(755,root,root) %{_bindir}/ksplashqml
%attr(755,root,root) %{_bindir}/oxygen-demo
%attr(755,root,root) %{_bindir}/oxygen-settings
%attr(755,root,root) %{_bindir}/oxygen-shadow-demo
#%attr(755,root,root) %{_bindir}/setscheduler
%attr(755,root,root) %{_libdir}/libkdecorations.so.*
%attr(755,root,root) %{_libdir}/libksignalplotter.so.*
%attr(755,root,root) %{_libdir}/libkworkspace.so.*
%attr(755,root,root) %{_libdir}/libprocesscore.so.*
%attr(755,root,root) %{_libdir}/libprocessui.so.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*
%attr(755,root,root) %{_libdir}/libweather_ion.so.*
%attr(755,root,root) %{_libdir}/libkwinglutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwinglutils.so.?
%attr(755,root,root) %{_libdir}/libkwinglesutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwinglesutils.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit_startup.so
%attr(755,root,root) %{_libdir}/libplasmagenericshell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasmagenericshell.so.?
%attr(755,root,root) %{_libdir}/libkickoff.so
#%attr(755,root,root) %ghost %{_libdir}/libpolkitkdeprivate.so.?
#%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libtime_solar.so.?
#%attr(755,root,root) %{_libdir}/libtime_solar.so.*.*.*

%dir %{_libdir}/kde4/plugins/gui_platform
%attr(755,root,root) %{_libdir}/kde4/plugins/gui_platform/libkde.so

# workspace options
%attr(755,root,root) %{_libdir}/kde4/kcm_workspaceoptions.so
%{_datadir}/kde4/services/workspaceoptions.desktop

# standard actions
%attr(755,root,root) %{_libdir}/kde4/kcm_standard_actions.so
%{_datadir}/kde4/services/standard_actions.desktop
#%{_datadir}/kde4/services/settings-input-actions.desktop

# remotewidgets
%attr(755,root,root) %{_bindir}/remote-widgets-browser
#%{_datadir}/kde4/services/remotewidgets.desktop

# autostart
%attr(755,root,root) %{_libdir}/kde4/kcm_autostart.so
%{_datadir}/kde4/services/autostart.desktop

# kaccess
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_libdir}/libkdeinit4_kaccess.so
%{_datadir}/apps/kaccess
%{_datadir}/kde4/services/kaccess.desktop

# polkit-1 policies
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

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
%{_datadir}/apps/kcmkeyboard
%{_datadir}/apps/kcmkeys
#%{_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{_datadir}/apps/khotkeys
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
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
%attr(755,root,root) %{_libdir}/libkdeinit4_krunner.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_krunner_shell.so
%attr(755,root,root) %{_libdir}/kde4/kcm_krunner_kill.so
%attr(755,root,root) %{_libdir}/kde4/krunner_activities.so
%attr(755,root,root) %{_libdir}/kde4/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_calculatorrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_kill.so
%attr(755,root,root) %{_libdir}/kde4/krunner_locations.so
%attr(755,root,root) %{_libdir}/kde4/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/kde4/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_plasma-desktop.so
%attr(755,root,root) %{_libdir}/kde4/krunner_powerdevil.so
%attr(755,root,root) %{_libdir}/kde4/krunner_services.so
%attr(755,root,root) %{_libdir}/kde4/krunner_sessions.so
%attr(755,root,root) %{_libdir}/kde4/krunner_shell.so
%attr(755,root,root) %{_libdir}/kde4/krunner_solid.so
%attr(755,root,root) %{_libdir}/kde4/krunner_windows.so
%attr(755,root,root) %{_libdir}/kde4/krunner_nepomuksearchrunner.so
%attr(755,root,root) %{_libdir}/kde4/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/kde4/krunner_windowedwidgets.so
%attr(755,root,root) %{_libdir}/kde4/classic_mode.so
%attr(755,root,root) %{_libdir}/kde4/icon_mode.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_pkk_authorization.so
%attr(755,root,root) %{_libdir}/kde4/kded_statusnotifierwatcher.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kscreenlocker
#%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-manager
#%attr(755,root,root) %{_libdir}/kde4/libexec/krunner_lock
%{_datadir}/kde4/services/recentdocuments.desktop
%{_datadir}/autostart/krunner.desktop
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/kde4/services/plasma-runner-plasma-desktop.desktop
%{_datadir}/kde4/services/plasma-runner-kill.desktop
%{_datadir}/kde4/services/plasma-runner-kill_config.desktop
%{_datadir}/kde4/services/plasma-runner-nepomuksearch.desktop
%{_datadir}/kde4/services/plasma-runner-windows.desktop
%{_datadir}/kde4/services/plasma-applet-panelspacer-internal.desktop
%{_datadir}/kde4/services/plasma-applet-sm_ram.desktop
%{_datadir}/kde4/services/plasma-dataengine-calendar.desktop
%{_datadir}/kde4/services/plasma-dataengine-geolocation.desktop
%{_datadir}/kde4/services/plasma-engine-akonadi.desktop
%{_datadir}/kde4/services/plasma-engine-searchlaunch.desktop
%{_datadir}/kde4/services/plasma-engine-metadata.desktop
%{_datadir}/kde4/services/plasma-geolocation-gps.desktop
%{_datadir}/kde4/services/plasma-geolocation-ip.desktop
#%{_datadir}/kde4/services/kcm_pkk_authorization.desktop
%{_datadir}/kde4/services/graphicalinfocategory.desktop
%{_datadir}/kde4/services/kded/kephal.desktop
%{_datadir}/kde4/services/kded/statusnotifierwatcher.desktop
%{_datadir}/kde4/servicetypes/plasma-geolocationprovider.desktop
%dir %{_datadir}/apps/plasma-desktop
%{_datadir}/apps/plasma-desktop/plasma-desktop.notifyrc
%{_datadir}/apps/plasma-desktop/init
%{_datadir}/apps/plasma-desktop/updates

# ksmserver
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_libdir}/libkdeinit4_ksmserver.so
%{_datadir}/apps/kconf_update/ksmserver.upd
%{_datadir}/apps/kconf_update/ksmserver_shortcuts.upd
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/apps/ksmserver

# kscreenlocker
%dir %{_datadir}/apps/kscreenlocker
%{_datadir}/apps/kscreenlocker/kscreenlocker.notifyrc

# ksplash
%attr(755,root,root) %{_bindir}/ksplashsimple
%attr(755,root,root) %{_bindir}/ksplashx
%attr(755,root,root) %{_bindir}/ksplashx_scale
%attr(755,root,root) %{_libdir}/kde4/kcm_ksplashthemes.so
%{_datadir}/apps/ksplash
%{_datadir}/config/ksplash.knsrc
%{_datadir}/kde4/services/ksplashthememgr.desktop
%{_iconsdir}/*/*/apps/ksplash.png

# ktip
#%attr(755,root,root) %{_bindir}/ktip
#%{_datadir}/autostart/ktip.desktop
#%{_desktopdir}/kde4/ktip.desktop

# kxkb
#%attr(755,root,root) %{_bindir}/kxkb
#%attr(755,root,root) %{_libdir}/libkdeinit4_kxkb.so
#%lang(en) %{_kdedocdir}/en/kxkb
#%{_iconsdir}/*/*/apps/kxkb.png

# systemsettings
%attr(755,root,root) %{_bindir}/systemsettings
%attr(755,root,root) %{_libdir}/libsystemsettingsview.so.?
%{_datadir}/apps/systemsettings
%{_datadir}/applications/kde4/kdesystemsettings.desktop
%{_datadir}/kde4/services/lostfoundcategory.desktop
%{_datadir}/kde4/services/networkinfocategory.desktop
%{_datadir}/kde4/services/settings-accessibility.desktop
%{_datadir}/kde4/services/settings-account-details.desktop
%{_datadir}/kde4/services/settings-application-and-system-notifications.desktop
%{_datadir}/kde4/services/settings-application-appearance-and-behavior.desktop
%{_datadir}/kde4/services/settings-application-appearance.desktop
%{_datadir}/kde4/services/settings-audio-and-video.desktop
%{_datadir}/kde4/services/settings-bluetooth.desktop
%{_datadir}/kde4/services/settings-classic-view.desktop
%{_datadir}/kde4/services/settings-desktop-appearance.desktop
%{_datadir}/kde4/services/settings-display.desktop
%{_datadir}/kde4/services/settings-hardware.desktop
%{_datadir}/kde4/services/settings-icon-view.desktop
%{_datadir}/kde4/services/settings-input-devices.desktop
%{_datadir}/kde4/services/settings-locale.desktop
%{_datadir}/kde4/services/settings-lost-and-found.desktop
%{_datadir}/kde4/services/settings-network-and-connectivity.desktop
%{_datadir}/kde4/services/settings-network-settings.desktop
%{_datadir}/kde4/services/settings-permissions.desktop
%{_datadir}/kde4/services/settings-personal-information.desktop
%{_datadir}/kde4/services/settings-removable-devices.desktop
%{_datadir}/kde4/services/settings-sharing.desktop
%{_datadir}/kde4/services/settings-shortcuts-and-gestures.desktop
%{_datadir}/kde4/services/settings-startup-and-shutdown.desktop
%{_datadir}/kde4/services/settings-system-administration.desktop
%{_datadir}/kde4/services/settings-window-behaviour.desktop
%{_datadir}/kde4/services/settings-workspace-appearance-and-behavior.desktop
%{_datadir}/kde4/services/settings-workspace-behavior.desktop
%{_datadir}/kde4/servicetypes/systemsettingscategory.desktop
%{_datadir}/kde4/servicetypes/systemsettingsexternalapp.desktop
%{_datadir}/kde4/servicetypes/systemsettingsview.desktop
%{_desktopdir}/kde4/systemsettings.desktop
%{_kdedocdir}/en/systemsettings

# themes
%{_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{_datadir}/apps/kthememanager
%{_datadir}/apps/desktoptheme/default/widgets/
# split this ?
%{_datadir}/apps/desktoptheme/air-netbook

# styles
%attr(755,root,root) %{_libdir}/kde4/kcm_style.so
#%attr(755,root,root) %{_libdir}/kde4/kstyle_keramik_config.so
%{_datadir}/apps/kstyle/themes/qtcde.themerc
%{_datadir}/apps/kstyle/themes/qtcleanlooks.themerc
%{_datadir}/apps/kstyle/themes/qtgtk.themerc
%{_datadir}/apps/kstyle/themes/qtmotif.themerc
%{_datadir}/apps/kstyle/themes/qtplastique.themerc
%{_datadir}/apps/kstyle/themes/qtwindows.themerc
%{_datadir}/kde4/services/style.desktop
%dir %{_libdir}/kde4/plugins/styles

# powerdevil
%attr(755,root,root) %{_libdir}/kde4/libexec/backlighthelper
%attr(755,root,root) %{_libdir}/kde4/kcm_powerdevilactivitiesconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_powerdevilglobalconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_powerdevilprofilesconfig.so
%attr(755,root,root) %{_libdir}/kde4/powerdevilbrightnesscontrolaction_config.so
%attr(755,root,root) %{_libdir}/kde4/powerdevildimdisplayaction_config.so
%attr(755,root,root) %{_libdir}/kde4/powerdevildpmsaction.so
%attr(755,root,root) %{_libdir}/kde4/powerdevildpmsaction_config.so
%attr(755,root,root) %{_libdir}/kde4/powerdevilhandlebuttoneventsaction_config.so
%attr(755,root,root) %{_libdir}/kde4/powerdevilrunscriptaction_config.so
%attr(755,root,root) %{_libdir}/kde4/powerdevilsuspendsessionaction_config.so
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so.0
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so.*.*
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so.4
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so.*.*
%attr(755,root,root) %{_libdir}/libpowerdevilui.so.4
%attr(755,root,root) %{_libdir}/libpowerdevilui.so.*.*
%attr(755,root,root) %{_libdir}/libpowerdevilui.so
/etc/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%dir %{_datadir}/apps/powerdevil
%{_datadir}/apps/powerdevil/powerdevil.notifyrc
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/kde4/services/powerdevilactivitiesconfig.desktop
%{_datadir}/kde4/services/powerdevilbrightnesscontrolaction.desktop
%{_datadir}/kde4/services/powerdevildimdisplayaction.desktop
%{_datadir}/kde4/services/powerdevildpmsaction.desktop
%{_datadir}/kde4/services/powerdevilglobalconfig.desktop
%{_datadir}/kde4/services/powerdevilhandlebuttoneventsaction.desktop
%{_datadir}/kde4/services/powerdevilprofilesconfig.desktop
%{_datadir}/kde4/services/powerdevilrunscriptaction.desktop
%{_datadir}/kde4/services/powerdevilsuspendsessionaction.desktop
%{_datadir}/kde4/services/settings-power-management.desktop
%{_datadir}/kde4/servicetypes/powerdevilaction.desktop

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
%attr(755,root,root) %{_libdir}/kde4/ion_debianweather.so
%attr(755,root,root) %{_libdir}/kde4/ion_envcan.so
%attr(755,root,root) %{_libdir}/kde4/ion_noaa.so
%attr(755,root,root) %{_libdir}/kde4/ion_wettercom.so
%{_datadir}/kde4/services/ion-bbcukmet.desktop
%{_datadir}/kde4/services/ion-debianweather.desktop
%{_datadir}/kde4/services/ion-envcan.desktop
%{_datadir}/kde4/services/ion-noaa.desktop
%{_datadir}/kde4/services/ion-wettercom.desktop

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
/etc/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service

# fontthumbnail
%attr(755,root,root) %{_libdir}/kde4/fontthumbnail.so
%{_datadir}/kde4/services/fontthumbnail.desktop

# colors
%attr(755,root,root) %{_libdir}/kde4/kcm_colors.so
%{_datadir}/kde4/services/colors.desktop
%{_datadir}/apps/color-schemes

# energy
#%attr(755,root,root) %{_libdir}/kde4/kcm_energy.so
#%{_datadir}/kde4/services/energy.desktop

# randr
%attr(755,root,root) %{_bindir}/krandrstartup
%{_datadir}/kde4/services/randr.desktop
%attr(755,root,root) %{_libdir}/kde4/kcm_randr.so

# smserver
%attr(755,root,root) %{_libdir}/kde4/kcm_smserver.so
%{_datadir}/kde4/services/kcmsmserver.desktop

# xinerama
#%attr(755,root,root) %{_libdir}/kde4/kcm_xinerama.so
#%attr(755,root,root) %{_libdir}/kde4/libexec/test_kcm_xinerama
#%{_datadir}/kde4/services/xinerama.desktop

# input, hw
%attr(755,root,root) %{_libdir}/kde4/kcm_input.so
%attr(755,root,root) %{_libdir}/kde4/kcm_joystick.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/kded_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/keyboard_layout_widget.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keys.so
%{_datadir}/kde4/services/kcm_keyboard.desktop
%{_datadir}/kde4/services/kded/keyboard.desktop
%{_datadir}/apps/kcminput/cursor_large_black.pcf.gz
%{_datadir}/apps/kcminput/cursor_large_white.pcf.gz
%{_datadir}/apps/kcminput/cursor_small_white.pcf.gz
%{_datadir}/apps/kcminput/pics/mouse_lh.png
%{_datadir}/apps/kcminput/pics/mouse_rh.png
# ?
%attr(755,root,root) %{_libdir}/kde4/kded_freespacenotifier.so
#%attr(755,root,root) %{_libdir}/kde4/kded_networkstatus.so
%attr(755,root,root) %{_libdir}/kde4/kded_powerdevil.so
%attr(755,root,root) %{_libdir}/kde4/libexec/krootimage
%attr(755,root,root) %{_libdir}/kde4/libexec/kcmdatetimehelper

# krandr monitor
%attr(755,root,root) %{_libdir}/kde4/kded_randrmonitor.so
%{_datadir}/kde4/services/kded/randrmonitor.desktop

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
#%{_datadir}/apps/kconf_update/kwin3_plugin.upd
%{_datadir}/apps/kconf_update/kwin_remove_delay_focus.upd
%{_datadir}/apps/kconf_update/kwin_update_tabbox_qml_settings.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/convertShortcuts.pl
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kwin3_plugin.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/move_session_config.sh
#%attr(755,root,root) %{_datadir}/apps/kconf_update/on-off_to_true-false.sh
#%attr(755,root,root) %{_datadir}/apps/kconf_update/pluginlibFix.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kwin_remove_delay_focus.sh
%{_datadir}/config/background.knsrc
%{_datadir}/config/colorschemes.knsrc
%{_datadir}/config/wallpaper.knsrc
%{_datadir}/config/xcursor.knsrc
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
#%{_datadir}/kde4/services/kded/networkstatus.desktop
%{_datadir}/kde4/services/kded/powerdevil.desktop
%{_datadir}/kde4/services/kded/freespacenotifier.desktop
#%{_datadir}/kde4/services/keyboard.desktop
#%{_datadir}/kde4/services/keyboard_layout.desktop
%{_datadir}/kde4/services/keys.desktop
%{_datadir}/kde4/services/mouse.desktop
%{_datadir}/sounds/pop.wav
# old decoration libs
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindecoration.so
%{_datadir}/kde4/services/kwindecoration.desktop
# kephal
%attr(755,root,root) %{_libdir}/kde4/kded_kephal.so
%attr(755,root,root) %{_libdir}/libkephal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkephal.so.?
#%{_datadir}/kde4/services/kded/kded_kephal.desktop
%{_datadir}/config.kcfg/plasma-shell-desktop.kcfg
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/apps/freespacenotifier

%{_datadir}/wallpapers/stripes.png
%{_datadir}/wallpapers/stripes.png.desktop

#%files -n PolicyKit-kde
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/polkit-kde-authorization
#%attr(755,root,root) %ghost %{_libdir}/libpolkitkdeprivate.so.?
#%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/kcm_pkk_authorization.so
#%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-manager
#%{_datadir}/kde4/services/kcm_pkk_authorization.desktop
#%{_datadir}/dbus-1/services/kde-org.freedesktop.PolicyKit.AuthenticationAgent.service
#%{_datadir}/dbus-1/services/org.kde.PolicyKit.service
#%{_kdedocdir}/en/PolicyKit-kde

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
%attr(755,root,root) %{_libdir}/libkwinglutils.so
%attr(755,root,root) %{_libdir}/libkwinglesutils.so
#%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so
%attr(755,root,root) %{_libdir}/libkworkspace.so
%attr(755,root,root) %{_libdir}/libksignalplotter.so
%attr(755,root,root) %{_libdir}/libplasmaclock.so
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so
%attr(755,root,root) %{_libdir}/libplasma_applet-system-monitor.so
%attr(755,root,root) %{_libdir}/libplasmagenericshell.so
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so
%attr(755,root,root) %{_libdir}/libprocesscore.so
%attr(755,root,root) %{_libdir}/libprocessui.so
%attr(755,root,root) %{_libdir}/libsolidcontrol.so
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so
%attr(755,root,root) %{_libdir}/libsystemsettingsview.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libweather_ion.so
%attr(755,root,root) %{_libdir}/liblsofui.so
#%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so
%attr(755,root,root) %{_libdir}/liboxygenstyle.so
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig.so
%{_libdir}/cmake/KDE4Workspace
%{_includedir}/KDE/Plasma/Weather
%{_includedir}/plasma/geolocation
%{_includedir}/plasma/weather
%{_includedir}/*.h
%{_includedir}/kworkspace
%{_includedir}/ksgrd
%{_includedir}/ksysguard
%{_includedir}/solid
%{_includedir}/systemsettingsview
%{_includedir}/taskmanager
%{_includedir}/plasmaclock
%{_datadir}/apps/cmake/modules/*.cmake

%files infocenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%attr(755,root,root) %{_libdir}/kde4/kcm_usb.so
%attr(755,root,root) %{_libdir}/kde4/kcm_nic.so
%attr(755,root,root) %{_libdir}/kde4/kcm_info.so
%attr(755,root,root) %{_libdir}/kde4/kcm_infosummary.so
%attr(755,root,root) %{_libdir}/kde4/kcm_opengl.so
%attr(755,root,root) %{_libdir}/kde4/kcm_memory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_pci.so
%attr(755,root,root) %{_libdir}/kde4/kcm_samba.so
%attr(755,root,root) %{_libdir}/kde4/kcm_view1394.so
%{_datadir}/apps/kinfocenter
%{_datadir}/kde4/services/kcm_infosummary.desktop
%{_datadir}/kde4/services/kcmview1394.desktop
%{_datadir}/kde4/services/kcmusb.desktop
%{_datadir}/kde4/services/nic.desktop
%{_datadir}/kde4/services/opengl.desktop
%{_datadir}/kde4/services/scsi.desktop
%{_datadir}/kde4/services/xserver.desktop
%{_datadir}/kde4/services/dma.desktop
%{_datadir}/kde4/services/interrupts.desktop
%{_datadir}/kde4/services/ioports.desktop
%{_datadir}/kde4/services/kcm_memory.desktop
%{_datadir}/kde4/services/kcm_pci.desktop
%{_datadir}/kde4/services/smbstatus.desktop
%{_datadir}/kde4/servicetypes/kinfocentercategory.desktop
%{_desktopdir}/kde4/kinfocenter.desktop
%dir %{_datadir}/apps/kcmview1394
%dir %{_datadir}/apps/kcmusb
%{_datadir}/apps/kcmview1394/oui.db
%{_datadir}/apps/kcmusb/usb.ids
%lang(en) %{_kdedocdir}/en/kinfocenter

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
%attr(755,root,root) %{_libdir}/kde4/libexec/fontinst
%attr(755,root,root) %{_libdir}/kde4/libexec/fontinst_x11
%attr(755,root,root) %{_libdir}/strigi/strigita_font.so
%attr(755,root,root) %{_libdir}/kde4/libexec/fontinst_helper
%{_desktopdir}/kde4/kfontview.desktop
%{_datadir}/apps/kfontinst
%{_datadir}/apps/kfontview
%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/config/kfontinst.knsrc
%{_datadir}/kde4/services/ServiceMenus/installfont.desktop
%{_datadir}/kde4/services/fontinst.desktop
%{_datadir}/kde4/services/fonts.desktop
%{_datadir}/kde4/services/fonts.protocol
%{_datadir}/kde4/services/kfontviewpart.desktop
%{_iconsdir}/*/*/apps/kfontview.png
%{_iconsdir}/*/*/mimetypes/fonts-package.png
/etc/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%lang(en) %{_kdedocdir}/en/kfontview

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
%attr(755,root,root) %{_libdir}/kde4/libexec/ksysguardprocesslist_helper
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksignalplotterwidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so
%{_desktopdir}/kde4/ksysguard.desktop
%{_datadir}/apps/ksysguard
%{_iconsdir}/*/*/apps/ksysguardd.png
%{_datadir}/config/ksysguard.knsrc
%lang(en) %{_kdedocdir}/en/ksysguard

/etc/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service


%files kwin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kwin_gles
%attr(755,root,root) %{_libdir}/libkwineffects.so.*
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin_gles.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwin_scripts.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwincompositing.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindesktop.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwintabbox.so
%attr(755,root,root) %{_libdir}/kde4/kcm_cursortheme.so
%attr(755,root,root) %{_libdir}/kde4/kcm_desktoppaths.so
%attr(755,root,root) %{_libdir}/kde4/kcm_desktoptheme.so
%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_gles_builtins.so
%attr(755,root,root) %{_libdir}/kde4/kwin_oxygen_config.so
#%attr(755,root,root) %{_libdir}/kde4/kwin3_tabstrip.so
#%attr(755,root,root) %{_libdir}/kde4/kwin_tabstrip_config.so
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_default_rules
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_tabbox_settings
#%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_window_settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma-add-shortcut-to-menu
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma-to-plasma-desktop
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_tabbox_qml_settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin_update_settings_49
%attr(755,root,root) %{_libdir}/kde4/libexec/kwin_killer_helper
%attr(755,root,root) %{_libdir}/kde4/libexec/kwin_opengl_test
%attr(755,root,root) %{_libdir}/kde4/libexec/kwin_rules_dialog
%dir %{_datadir}/apps/kwin
%{_datadir}/apps/kwin/*.glsl
%{_datadir}/apps/kwin/*.png
%{_datadir}/apps/kwin/*.frag
%{_datadir}/apps/kwin/*.vert
%dir %{_datadir}/apps/kwin/default_rules
%{_datadir}/apps/kwin/default_rules/fsp_workarounds_1.kwinrules
%{_datadir}/apps/kwin/effects
%{_datadir}/apps/kwin/kcm_*
%{_datadir}/apps/kwin/kwin.notifyrc
%{_datadir}/apps/kwin/scripts
%{_datadir}/apps/kwin/tabbox
%{_datadir}/config/kwinscripts.knsrc
%{_datadir}/config/kwinswitcher.knsrc
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%dir %{_datadir}/kde4/services/kwin
%{_datadir}/kde4/services/cursortheme.desktop
%{_datadir}/kde4/services/desktoppath.desktop
%{_datadir}/kde4/services/desktoptheme.desktop
%{_datadir}/kde4/services/kwintabbox.desktop
%{_datadir}/kde4/services/kwin-script-desktopchangeosd.desktop
%{_datadir}/kde4/services/kwin-script-synchronizeskipswitcher.desktop
%{_datadir}/kde4/services/kwin-script-videowall.desktop
%{_datadir}/kde4/services/kwin/boxswitch.desktop
%{_datadir}/kde4/services/kwin/boxswitch_config.desktop
%{_datadir}/kde4/services/kwin/coverswitch.desktop
%{_datadir}/kde4/services/kwin/coverswitch_config.desktop
%{_datadir}/kde4/services/kwin/cubeslide_config.desktop
%{_datadir}/kde4/services/kwin/dashboard.desktop
%{_datadir}/kde4/services/kwin/dashboard_config.desktop
%{_datadir}/kde4/services/kwin/desktopgrid.desktop
%{_datadir}/kde4/services/kwin/desktopgrid_config.desktop
%{_datadir}/kde4/services/kwin/dialogparent.desktop
%{_datadir}/kde4/services/kwin/diminactive.desktop
%{_datadir}/kde4/services/kwin/diminactive_config.desktop
%{_datadir}/kde4/services/kwin/dimscreen.desktop
%{_datadir}/kde4/services/kwin/explosion.desktop
#%{_datadir}/kde4/services/kwin/fade.desktop
%{_datadir}/kde4/services/kwin/fallapart.desktop
%{_datadir}/kde4/services/kwin/invert.desktop
%{_datadir}/kde4/services/kwin/invert_config.desktop
%{_datadir}/kde4/services/kwin/login.desktop
%{_datadir}/kde4/services/kwin/login_config.desktop
#%{_datadir}/kde4/services/kwin/logout.desktop
%{_datadir}/kde4/services/kwin/lookingglass.desktop
%{_datadir}/kde4/services/kwin/lookingglass_config.desktop
%{_datadir}/kde4/services/kwin/magnifier.desktop
%{_datadir}/kde4/services/kwin/magnifier_config.desktop
%{_datadir}/kde4/services/kwin/minimizeanimation.desktop
%{_datadir}/kde4/services/kwin/mousemark.desktop
%{_datadir}/kde4/services/kwin/mousemark_config.desktop
%{_datadir}/kde4/services/kwin/outline.desktop
%{_datadir}/kde4/services/kwin/presentwindows.desktop
%{_datadir}/kde4/services/kwin/presentwindows_config.desktop
%{_datadir}/kde4/services/kwin/resize.desktop
%{_datadir}/kde4/services/kwin/resize_config.desktop
%{_datadir}/kde4/services/kwin/scalein.desktop
%{_datadir}/kde4/services/kwin/screenshot.desktop
#%{_datadir}/kde4/services/kwin/shadow.desktop
#%{_datadir}/kde4/services/kwin/shadow_config.desktop
#%{_datadir}/kde4/services/kwin/sharpen.desktop
#%{_datadir}/kde4/services/kwin/sharpen_config.desktop
%{_datadir}/kde4/services/kwin/showfps.desktop
%{_datadir}/kde4/services/kwin/showpaint.desktop
%{_datadir}/kde4/services/kwin/slide.desktop
%{_datadir}/kde4/services/kwin/slidingpopups.desktop
%{_datadir}/kde4/services/kwin/startupfeedback.desktop
%{_datadir}/kde4/services/kwin/thumbnailaside.desktop
%{_datadir}/kde4/services/kwin/thumbnailaside_config.desktop
%{_datadir}/kde4/services/kwin/trackmouse.desktop
%{_datadir}/kde4/services/kwin/trackmouse_config.desktop
%{_datadir}/kde4/services/kwin/windowgeometry.desktop
%{_datadir}/kde4/services/kwin/windowgeometry_config.desktop
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
#%{_datadir}/kde4/services/kwin/snow.desktop
#%{_datadir}/kde4/services/kwin/snow_config.desktop
%{_datadir}/kde4/services/kwin/showfps_config.desktop
%{_datadir}/kde4/services/kwin/wobblywindows.desktop
%{_datadir}/kde4/services/kwin/wobblywindows_config.desktop
%{_datadir}/kde4/services/kwin/cube.desktop
%{_datadir}/kde4/services/kwin/cube_config.desktop
%{_datadir}/kde4/services/kwin/magiclamp.desktop
%{_datadir}/kde4/services/kwin/taskbarthumbnail.desktop
%{_datadir}/kde4/services/kwin/cubeslide.desktop
#%{_datadir}/kde4/services/kwin/fadedesktop.desktop
%{_datadir}/kde4/services/kwin/highlightwindow.desktop
%{_datadir}/kde4/services/kwin/magiclamp_config.desktop
%{_datadir}/kde4/services/kwin/sheet.desktop
%{_datadir}/kde4/services/kwin/slideback.desktop
%{_datadir}/kde4/services/kwin/snaphelper.desktop
%{_datadir}/kde4/services/kwin/translucency.desktop
%{_datadir}/kde4/services/kwin/translucency_config.desktop
%{_datadir}/kde4/services/kwinscreenedges.desktop
%{_datadir}/kde4/services/kwin/blur.desktop
%{_datadir}/kde4/services/kwin/blur_config.desktop
%{_datadir}/kde4/services/kwin/glide.desktop
%{_datadir}/kde4/services/kwin/glide_config.desktop
%{_datadir}/kde4/services/kwin/kwin4_*.desktop
%{_datadir}/kde4/services/kwin/logout.desktop
%{_datadir}/kde4/services/kwinscripts.desktop
%{_datadir}/kde4/servicetypes/kwineffect.desktop
%{_datadir}/kde4/servicetypes/kwinscript.desktop
%{_datadir}/kde4/servicetypes/kwinwindowswitcher.desktop
%{_datadir}/apps/kconf_update/plasma-add-shortcut-to-menu.upd
%{_datadir}/apps/kconf_update/krdb_libpathwipe.upd
#%{_datadir}/apps/kconf_update/kwin.upd
#%{_datadir}/apps/kconf_update/kwin_focus1.sh
#%{_datadir}/apps/kconf_update/kwin_focus1.upd
#%{_datadir}/apps/kconf_update/kwin_focus2.sh
#%{_datadir}/apps/kconf_update/kwin_focus2.upd
%{_datadir}/apps/kconf_update/kwin_fsp_workarounds_1.upd
#%{_datadir}/apps/kconf_update/kwin_on_off.upd
%{_datadir}/apps/kconf_update/kwin_remove_effects.upd
#%{_datadir}/apps/kconf_update/kwin_window_shortcuts.sh
#%{_datadir}/apps/kconf_update/kwin_window_shortcuts.upd
#%{_datadir}/apps/kconf_update/kwiniconify.upd
#%{_datadir}/apps/kconf_update/kwinsticky.upd
#%{_datadir}/apps/kconf_update/kwinupdatewindowsettings.upd
%{_datadir}/apps/kconf_update/plasma-to-plasmadesktop-shortcuts.upd
%{_datadir}/apps/kconf_update/plasmarc-to-plasmadesktoprc.upd
%{_datadir}/apps/kconf_update/kwin_update_tabbox_settings.upd
%{_datadir}/apps/kconf_update/kwin_update_49.upd
#%{_datadir}/apps/kconf_update/kwin_blacklist.sh
#%{_datadir}/apps/kconf_update/kwin_blacklist.upd
#%{_datadir}/apps/kconf_update/khotkeys_printscreen.upd
%{_iconsdir}/oxygen/16x16/apps/kwin.png
%{_iconsdir}/oxygen/32x32/apps/kwin.png
%{_iconsdir}/oxygen/48x48/apps/kwin.png
%{_iconsdir}/Oxygen_Black
%{_iconsdir}/Oxygen_Blue
%{_iconsdir}/Oxygen_White
%{_iconsdir}/Oxygen_Yellow
%{_iconsdir}/Oxygen_Zion

%files plasma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-desktop
%attr(755,root,root) %{_bindir}/plasma-netbook
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmawallpaperviewer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%attr(755,root,root) %{_bindir}/plasma-overlay
%attr(755,root,root) %{_bindir}/plasma-windowed
%attr(755,root,root) %{_libdir}/libkdeinit4_plasma-desktop.so
%attr(755,root,root) %{_libdir}/libkdeinit4_plasma-netbook.so
%attr(755,root,root) %{_libdir}/libkdeinit4_plasma-windowed.so
%attr(755,root,root) %{_libdir}/kde4/plasma_animator_default.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_battery.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_currentappcontrol.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_dig_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_icon.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_launcher.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lockout.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_pager.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_quicklaunch.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_searchbox.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_showActivityManager.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_simplelauncher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_systemtray.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_trash.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_windowlist.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_appletscript_qedje.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_appletscript_simple_javascript.so
%attr(755,root,root) %{_libdir}/kde4/plasma_appletscriptengine_dashboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_appletscriptengine_webapplet.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_notifications.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_package_qedje.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_dashboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_web.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_applauncher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_contextmenu.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_minimalcontextmenu.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_paste.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_switchactivity.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_switchdesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containmentactions_switchwindow.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_desktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_netpanel.so
#%attr(755,root,root) %{_libdir}/kde4/plasma_containment_newspaper.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_panel.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_sal.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_color.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_image.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_activitybar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_calendar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_cpu.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_hdd.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_hdd_activity.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_hwinfo.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_net.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_temperature.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_system-monitor.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_webbrowser.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_saverdesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_activities.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_akonadi.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_apps.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_applicationjobs.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_calendar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_dict.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_executable.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_favicons.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_filebrowser.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_geolocation.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_hotplug.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_keystate.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_metadata.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mouse.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_network.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_nowplaying.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_notifications.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_places.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_powermanagement.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mpris2.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_rss.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_searchlaunch.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_share.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_systemmonitor.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_tasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_weather.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_devicenotifications.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_statusnotifieritem.so
%attr(755,root,root) %{_libdir}/kde4/plasma_package_ggl.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_share.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_ggl.so
%attr(755,root,root) %{_libdir}/kde4/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/kde4/plasma-geolocation-ip.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_panelspacer_internal.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_sm_ram.so
%attr(755,root,root) %{_libdir}/kde4/plasma_toolbox_desktoptoolbox.so
%attr(755,root,root) %{_libdir}/kde4/plasma_toolbox_nettoolbox.so
%attr(755,root,root) %{_libdir}/kde4/plasma_toolbox_paneltoolbox.so
%dir %{_datadir}/
%attr(755,root,root) %ghost %{_libdir}/libplasma-geolocation-interface.so.?
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasma_applet-system-monitor.so.?
%attr(755,root,root) %{_libdir}/libplasma_applet-system-monitor.so.*.*.*
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
%{_datadir}/kde4/services/plasma-applet-org.kde.showActivityManager.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-imgsusepasteorg.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-kde.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-desktop.SaL.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-desktop.desktopIcons.desktop
%{_datadir}/kde4/services/plasma-runner-activityrunner.desktop
%{_datadir}/kde4/services/plasma-scriptengine-ruby-applet.desktop
%{_datadir}/kde4/services/plasma-scriptengine-ruby-dataengine.desktop
%{_datadir}/kde4/services/plasma-applet-batterymonitor.desktop
%{_datadir}/kde4/services/plasma-applet-sm_hdd_activity.desktop
%{_datadir}/kde4/services/plasma-dataengine-mpris2.desktop
%dir %{_datadir}/apps/plasma/services
%{_datadir}/apps/plasma/packages/org.kde.desktop.activitymanager
%{_datadir}/apps/plasma/packages/org.kde.desktop.widgetexplorer
%{_datadir}/apps/plasma/plasmoids/battery
%{_datadir}/apps/plasma/plasmoids/lockout
%{_datadir}/apps/plasma/plasmoids/notifier
%{_datadir}/apps/plasma/plasmoids/org.kde.showActivityManager
%{_datadir}/apps/plasma/services/activities.operations
%{_datadir}/apps/plasma/services/applicationjobs.operations
%{_datadir}/apps/plasma/services/apps.operations
%{_datadir}/apps/plasma/services/hotplug.operations
%{_datadir}/apps/plasma/services/modifierkeystate.operations
%{_datadir}/apps/plasma/services/notifications.operations
%{_datadir}/apps/plasma/services/nowplaying.operations
%{_datadir}/apps/plasma/services/org.kde.places.operations
%{_datadir}/apps/plasma/services/powermanagementservice.operations
%{_datadir}/apps/plasma/services/share.operations
%{_datadir}/apps/plasma/services/tasks.operations
%{_datadir}/apps/plasma/services/searchlaunch.operations
%{_datadir}/apps/plasma/services/statusnotifieritem.operations
%{_datadir}/apps/plasma/services/mpris2.operations
%dir %{_datadir}/apps/plasma/shareprovider
%{_datadir}/apps/plasma/shareprovider/imgsusepasteorg
%{_datadir}/apps/plasma/shareprovider/imgur
%{_datadir}/apps/plasma/shareprovider/kde
%{_datadir}/apps/plasma/shareprovider/pastebincom
%{_datadir}/apps/plasma/shareprovider/pasteopensuseorg
%{_datadir}/apps/plasma/shareprovider/pasteubuntucom
%{_datadir}/apps/plasma/shareprovider/privatepastecom
%{_datadir}/apps/plasma/shareprovider/simplestimagehosting
%{_datadir}/apps/plasma/shareprovider/wklej
%{_datadir}/apps/plasma/shareprovider/wstaw
%{_datadir}/apps/plasma/layout-templates
%{_datadir}/kde4/services/plasma-animator-default.desktop
%{_datadir}/kde4/services/plasma-applet-analogclock.desktop
%{_datadir}/kde4/services/plasma-applet-currentappcontrol.desktop
%{_datadir}/kde4/services/plasma-applet-devicenotifier.desktop
%{_datadir}/kde4/services/plasma-applet-digitalclock.desktop
#%{_datadir}/kde4/services/plasma-applet-ggl-analog-clock.desktop
%{_datadir}/kde4/services/plasma-applet-icon.desktop
%{_datadir}/kde4/services/plasma-applet-launcher.desktop
%{_datadir}/kde4/services/plasma-applet-lockout.desktop
%{_datadir}/kde4/services/plasma-applet-quicklaunch.desktop
%{_datadir}/kde4/services/plasma-applet-searchbox.desktop
%{_datadir}/kde4/services/plasma-applet-simplelauncher.desktop
%{_datadir}/kde4/services/plasma-applet-systemtray.desktop
%{_datadir}/kde4/services/plasma-applet-trash.desktop
%{_datadir}/kde4/services/plasma-applet-activitybar.desktop
%{_datadir}/kde4/services/plasma-applet-calendar.desktop
#%{_datadir}/kde4/services/plasma-appletscript-qedje.desktop
%{_datadir}/kde4/services/plasma-applet-sm_cpu.desktop
%{_datadir}/kde4/services/plasma-applet-sm_hdd.desktop
%{_datadir}/kde4/services/plasma-applet-sm_hwinfo.desktop
%{_datadir}/kde4/services/plasma-applet-sm_net.desktop
%{_datadir}/kde4/services/plasma-applet-sm_temperature.desktop
%{_datadir}/kde4/services/plasma-applet-system-monitor.desktop
%{_datadir}/kde4/services/plasma-applet-webbrowser.desktop
%{_datadir}/kde4/services/plasma-applet-windowlist.desktop
%{_datadir}/kde4/services/plasma-packagestructure-dashboard.desktop
#%{_datadir}/kde4/services/plasma-packagestructure-qedje.desktop
%{_datadir}/kde4/services/plasma-packagestructure-web.desktop
%{_datadir}/kde4/services/plasma-scriptengine-applet-dashboard.desktop
%{_datadir}/kde4/services/plasma-scriptengine-applet-web.desktop
#%{_datadir}/kde4/services/plasma-scriptengine-applet-simple-javascript.desktop
#%{_datadir}/kde4/services/plasma-battery-default.desktop
%{_datadir}/kde4/services/plasma-containmentactions-applauncher.desktop
%{_datadir}/kde4/services/plasma-containmentactions-contextmenu.desktop
%{_datadir}/kde4/services/plasma-containmentactions-paste.desktop
%{_datadir}/kde4/services/plasma-containmentactions-switchactivity.desktop
%{_datadir}/kde4/services/plasma-containmentactions-switchdesktop.desktop
%{_datadir}/kde4/services/plasma-containmentactions-switchwindow.desktop
%{_datadir}/kde4/services/plasma-containment-desktop.desktop
%{_datadir}/kde4/services/plasma-containment-netpanel.desktop
#%{_datadir}/kde4/services/plasma-containment-newspaper.desktop
%{_datadir}/kde4/services/plasma-containment-panel.desktop
%{_datadir}/kde4/services/plasma-containment-sal.desktop
%{_datadir}/kde4/services/plasma-dataengine-applicationjobs.desktop
%{_datadir}/kde4/services/plasma-dataengine-favicons.desktop
%{_datadir}/kde4/services/plasma-dataengine-keystate.desktop
%{_datadir}/kde4/services/plasma-dataengine-notifications.desktop
%{_datadir}/kde4/services/plasma-dataengine-nowplaying.desktop
%{_datadir}/kde4/services/plasma-dataengine-systemmonitor.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-imgur.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-pastebincom.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-pasteopensuseorg.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-pasteubuntucom.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-privatepastecom.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-simplestimagehosting.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-wklej.desktop
%{_datadir}/kde4/services/plasma-dataengine-share-addon-wstaw.desktop
%{_datadir}/kde4/services/plasma-dataengine-share.desktop
%{_datadir}/kde4/services/plasma-dataengine-apps.desktop
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
%{_datadir}/kde4/services/plasma-engine-activities.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-desktop.findWidgets.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-desktop.photoActivity.desktop
%{_datadir}/kde4/services/plasma-packagestructure-share.desktop
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
%{_datadir}/kde4/services/plasma-runner-solid.desktop
%{_datadir}/kde4/services/plasma-tasks-default.desktop
%{_datadir}/kde4/services/plasma-toolbox-desktoptoolbox.desktop
%{_datadir}/kde4/services/plasma-toolbox-nettoolbox.desktop
%{_datadir}/kde4/services/plasma-toolbox-paneltoolbox.desktop
%{_datadir}/kde4/services/plasma-containment-saverdesktop.desktop
%{_datadir}/kde4/services/plasma-wallpaper-color.desktop
%{_datadir}/kde4/services/plasma-wallpaper-image.desktop
#%{_datadir}/kde4/services/plasma-applet-ggl-photos.desktop
#%{_datadir}/kde4/services/plasma-applet-ggl-rss.desktop
%{_datadir}/kde4/services/plasma-packagestructure-googlegadgets.desktop
%{_datadir}/kde4/services/plasma-scriptengine-googlegadgets.desktop
%{_datadir}/kde4/services/plasma-sal-bookmarks.desktop
%{_datadir}/kde4/services/plasma-sal-contacts.desktop
%{_datadir}/kde4/services/plasma-sal-education.desktop
%{_datadir}/kde4/services/plasma-sal-games.desktop
%{_datadir}/kde4/services/plasma-sal-graphics.desktop
%{_datadir}/kde4/services/plasma-sal-internet.desktop
%{_datadir}/kde4/services/plasma-sal-multimedia.desktop
%{_datadir}/kde4/services/plasma-sal-office.desktop
%{_datadir}/kde4/services/plasma-sal-system.desktop
%{_datadir}/kde4/services/plasma-sal-utility.desktop
%{_datadir}/kde4/services/plasma-applet-notifications.desktop
%{_datadir}/kde4/services/plasma-containment-desktopdashboard.desktop
%{_datadir}/kde4/services/plasma-containmentactions-minimalcontextmenu.desktop
%{_datadir}/kde4/services/plasma-dataengine-devicenotifications.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-desktop.defaultPanel.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-netbook.defaultPage.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-netbook.defaultPanel.desktop
%{_datadir}/kde4/services/plasma-layout-org.kde.plasma-netbook.defaultSal.desktop
%{_datadir}/kde4/services/plasma-runner-windowedwidgets.desktop
%{_datadir}/kde4/services/plasma-sal-development.desktop
%{_datadir}/kde4/services/plasma_applet_keyboard.desktop
%{_datadir}/kde4/services/plasma_engine_statusnotifieritem.desktop
%{_datadir}/kde4/servicetypes/plasma-sal-menu.desktop
%{_datadir}/kde4/servicetypes/plasma-layout-template.desktop
%{_datadir}/kde4/servicetypes/plasma_shareprovider.desktop
%dir %{_datadir}/apps/desktoptheme/default/system-monitor
%{_datadir}/apps/desktoptheme/default/system-monitor/hdd_panel.svgz
%dir %{_datadir}/apps/desktoptheme/default/calendar
%{_datadir}/apps/desktoptheme/default/calendar/mini-calendar.svgz
%{_datadir}/autostart/plasma-desktop.desktop
%{_datadir}/apps/plasma-netbook
%dir %{_datadir}/apps/katepart
%{_datadir}/apps/katepart/syntax/plasma-desktop-js.xml
%{_datadir}/config/activities.knsrc
%lang(en) %{_kdedocdir}/en/plasma-desktop
%{_mandir}/man1/plasmapkg.1*
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*

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
#%attr(755,root,root) %{_bindir}/solid-bluetooth
%attr(755,root,root) %{_bindir}/solid-network
#%attr(755,root,root) %{_bindir}/solid-powermanagement
%attr(755,root,root) %{_libdir}/libsolidcontrol.so.*
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so.*
%attr(755,root,root) %{_libdir}/kde4/devinfo.so
%attr(755,root,root) %{_libdir}/kde4/kcm_solid.so
%attr(755,root,root) %{_libdir}/kde4/kcm_solid_actions.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakenet.so
%attr(755,root,root) %{_libdir}/kde4/solid_modemmanager04.so
#%attr(755,root,root) %{_libdir}/kde4/solid_hal_power.so
#%attr(755,root,root) %{_libdir}/kde4/solid_bluez.so
%attr(755,root,root) %{_libdir}/kde4/solid_wicd.so
#%attr(755,root,root) %{_libdir}/kde4/solid_lirc.so
%dir %{_datadir}/apps/solid
%dir %{_datadir}/apps/solid/actions
%dir %{_datadir}/apps/solid/devices
%{_datadir}/apps/solid/devices/*.desktop
%dir %{_datadir}/apps/solidfakenetbackend
%{_datadir}/apps/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml
%{_datadir}/apps/plasma/services/soliddevice.operations
%{_datadir}/kde4/services/deviceinfocategory.desktop
%{_datadir}/kde4/services/devinfo.desktop
%{_datadir}/kde4/services/kcm_solid.desktop
%{_datadir}/kde4/services/solidbackends
%{_datadir}/kde4/services/solid-actions.desktop
%{_datadir}/kde4/servicetypes/solidmodemmanager.desktop
%{_datadir}/kde4/servicetypes/solidnetworkmanager.desktop
#%{_datadir}/kde4/servicetypes/solidpowermanager.desktop
%{_datadir}/kde4/servicetypes/solid-device-type.desktop
#%{_datadir}/kde4/servicetypes/solidremotecontrolmanager.desktop
%dir %{_datadir}/apps/kcmsolidactions
%{_datadir}/apps/kcmsolidactions/solid-action-template.desktop

%files networkmanager
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/solid_networkmanager07.so
%attr(755,root,root) %{_libdir}/kde4/solid_networkmanager09_fake.so
%{_iconsdir}/*/*x*/apps/networkmanager.png

%files kwrited
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_kwrited.so
%{_datadir}/kde4/services/kded/kwrited.desktop
%dir %{_datadir}/apps/kwrited
%{_datadir}/apps/kwrited/kwrited.notifyrc

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
%attr(755,root,root) %{_libdir}/kde4/libexec/kcmkdmhelper
/etc/X11/sessions
# XXX move dir below elsewhere
%dir %{_datadir}/apps/doc
%{_datadir}/apps/doc/kdm
%dir %{_datadir}/apps/kdm
%{_datadir}/apps/kdm/*
%{_datadir}/config/kdm.knsrc
%{_datadir}/kde4/services/kdm.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkdm.service
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%lang(en) %{_kdedocdir}/en/kdm
%{systemdunitdir}/kdm.service

%files svg-icons
%defattr(644,root,root,755)
%{_iconsdir}/*/scalable/apps/kcmkwm.svgz
%{_iconsdir}/*/scalable/apps/kfontview.svgz
%{_iconsdir}/*/scalable/apps/preferences-desktop-font-installer.svgz
%{_iconsdir}/*/scalable/mimetypes/fonts-package.svgz
%{_iconsdir}/*/scalable/apps/kwin.svgz

%files -n kde4-decoration-aurorae
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_aurorae.so
%{_datadir}/config/aurorae.knsrc
%{_datadir}/apps/kwin/aurorae.desktop
%{_datadir}/apps/kwin/aurorae

%files -n kde4-decoration-b2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_b2.so
%attr(755,root,root) %{_libdir}/kde4/kwin_b2_config.so
%{_datadir}/apps/kwin/b2.desktop

%files -n kde4-decoration-laptop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_laptop.so
%{_datadir}/apps/kwin/laptop.desktop

%files -n kde4-decoration-oxygen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_oxygen.so
%{_datadir}/apps/kwin/oxygenclient.desktop

%files -n kde4-decoration-plastic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_plastik.so
%attr(755,root,root) %{_libdir}/kde4/kwin_plastik_config.so
%{_datadir}/apps/kwin/plastik.desktop

%files -n kde4-kgreet-classic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_classic.so

%files -n kde4-kgreet-generic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_generic.so

%files -n kde4-kgreet-winbind
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgreet_winbind.so

%files -n kde4-style-oxygen
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/liboxygenstyle.so.?
%attr(755,root,root) %{_libdir}/liboxygenstyle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboxygenstyleconfig.so.?
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kstyle_oxygen_config.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/oxygen.so
%{_datadir}/apps/kstyle/themes/oxygen.themerc

%files -n python-plasma
%defattr(644,root,root,755)
%{py_sitedir}/PyKDE4/plasmascript.py[co]
%dir %{_datadir}/apps/plasma_scriptengine_python
%{_datadir}/apps/plasma_scriptengine_python/*.py
%{_datadir}/apps/plasma_scriptengine_python/*.py[co]
%{_datadir}/kde4/services/plasma*python*.desktop
