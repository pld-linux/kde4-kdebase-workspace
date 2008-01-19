
# Conditional build:
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden' & '--fvisibility-inlines-hidden' to g++
#
%define		oname		kdebase-workspace
%define		_state		stable
%define		_minlibsevr	9:4.0.0

Summary:	K Desktop Environment - core files
Summary(es.UTF-8):   K Desktop Environment - archivos básicos
Summary(ja.UTF-8):   KDEデスクトップ環境 - 基本ファイル
Summary(ko.UTF-8):   KDE - 기본 파일
Summary(pl.UTF-8):   K Desktop Environment - pliki środowiska
Summary(pt_BR.UTF-8):   K Desktop Environment - arquivos básicos
Summary(ru.UTF-8):   K Desktop Environment - базовые файлы
Summary(uk.UTF-8):   K Desktop Environment - базові файли
Summary(zh_CN.UTF-8):   KDE核心
Name:		kdebase4-workspace
Version:	4.0.0
Release:	0.1
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{oname}-%{version}.tar.bz2
Source4:	kdebase-kdm.init
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

%package -n kde-decoration-b2
Summary:	KDE Window Decoration - B2
Summary(pl.UTF-8):	Dekoracja okna dla KDE - B2
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

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

%package -n kde-decoration-keramik
Summary:	KDE Window Decoration - keramik
Summary(pl.UTF-8):	Dekoracja okna dla KDE - keramik
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Conflicts:	kdebase-desktop < 9:3.3.91

%description -n kde-decoration-keramik
KDE Window Decoration - keramik.

%description -n kde-decoration-keramik -l pl.UTF-8
Dekoracja okna dla KDE - keramik.

%package -n kde-decoration-laptop
Summary:	KDE Window Decoration - Laptop
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Laptop
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-modernsys
A window decoration with small, top-aligned window buttons and a
window title with gray lines surronding the text of the title. Also
with a convex resize handle on the bottom-right window corner.

%description -n kde-decoration-modernsys -l pl.UTF-8
Dekoracja okna z małymi, wyrównanymi do góry przyciskami okna oraz
tytułem okna otoczonym szarymi liniami. Ma również wypukły uchwyt
służący do zmiany rozmiaru w prawym dolnym rogu okna.

%package -n kde-decoration-quartz
Summary:	KDE Window Decoration - Quartz
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Quartz
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-decoration-redmond
A window decoration resembling the one from Windows 98.

%description -n kde-decoration-redmond -l pl.UTF-8
Dekoracja okna przypominająca tę z Windows 98.

%package -n kde-decoration-web
Summary:	KDE Window Decoration - Web
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Web
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

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
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde-kgreet-classic
Tools for asking for passwords in the classic, default look.

%description -n kde-kgreet-classic -l pl.UTF-8
Narzędzia służące do zapytań o hasło - klasyczny, domyślny motyw
wyglądu.

%package -n kde-kgreet-winbind
Summary:	KDE greeter libraries
Summary(pl.UTF-8):	Biblioteki służące do zapytań o hasło
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kde-kgreet
Conflicts:	kdm <= 3.2.90.040503-1

%description -n kde-kgreet-winbind
Tools for asking for passwords - winbind.

%description -n kde-kgreet-winbind -l pl.UTF-8
Narzędzia służące do zapytań o hasło - winbind.

%package -n kde-kio-ldap
Summary:	KDE LDAP protocol service
Summary(pl.UTF-8):	Obsługa protokołu LDAP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	konqueror < 9:3.2.90.040210

%description -n kde-kio-ldap
KDE LDAP protocol service.

%description -n kde-kio-ldap -l pl.UTF-8
Obsługa protokołu LDAP.

%package -n kde-kio-nntp
Summary:	KDE NNTP protocol service
Summary(pl.UTF-8):	Obsługa protokołu NNTP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-nntp
KDE NNTP protocol service.

%description -n kde-kio-nntp -l pl.UTF-8
Obsługa protokołu NNTP.

%package -n kde-kio-pop3
Summary:	KDE POP3 protocol service
Summary(pl.UTF-8):	Obsługa protokołu POP3
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-pop3
KDE POP3 protocol service.

%description -n kde-kio-pop3 -l pl.UTF-8
Obsługa protokołu POP3.

%package -n kde-kio-smtp
Summary:	KDE SMTP protocol service
Summary(pl.UTF-8):	Obsługa protokołu SMTP
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-mailnews

%description -n kde-kio-smtp
KDE SMTP protocol service.

%description -n kde-kio-smtp -l pl.UTF-8
Obsługa protokołu SMTP.

%package -n kde-kside-default
Summary:	Default kicker sidebar
Summary(pl.UTF-8):	Domyślny boczny pasek do menu KDE
Group:		Themes
Requires:	kdebase-desktop >= 9:3.2.90.040424-2
Provides:	kde-kside
Obsoletes:	kde-kside

%description -n kde-kside-default
Default kicker sidebar with a gear and the K Desktop Environment text.

%description -n kde-kside-default -l pl.UTF-8
Domyślny boczny pasek do menu KDE z turbinką oraz napisem K Desktop
Environment.

%package -n kde-logoutpic-default
Summary:	KDE "Logout" picture
Summary(pl.UTF-8):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Requires:	%{name}-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-PLD

%description -n kde-logoutpic-default
Default "Logout" picture with a KDE logo.

%description -n kde-logoutpic-default -l pl.UTF-8
Standardowy obrazek okna "Wyloguj" z logiem KDE.

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

%package -n kde-splashplugin-Redmond
Summary:	ksplash plugin Redmond
Summary(pl.UTF-8):	Wtyczka ksplash Redmond
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Obsoletes:	kde-splashplugin-XpLike

%description -n kde-splashplugin-Redmond
A splash screen plugin that resembles the Windows XP post login
animations.

%description -n kde-splashplugin-Redmond -l pl.UTF-8
Wtyczka ekranu powitalnego KDE, podobna do animacji, które w Windows
XP mają miejsce po zalogowaniu.

%package -n kde-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl.UTF-8):	Wtyczka ksplash Standard
Group:		X11/Amusements
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splashplugin-Standard
A standard splash screen plugin for KDE. It is themable and shows
splashscreens on the center of the screen. The splash themes for this
plugin consist of a main picture and two icon bars that are shown
under it. For every step of the loading process a different icon is
highlighted.

%description -n kde-splashplugin-Standard -l pl.UTF-8
Standardowa wtyczka uruchamiana podczas startu KDE. Obsługuje motywy i
pokazuje ekrany startowe na środku ekranu. Motywy startowe dla tej
wtyczki składają się z głównego obrazka i dwóch pasków ikon pod nim
pokazywanych. Dla każdego kroku procesu ładowania podświetlana jest
inna ikona.

%package common-filemanagement
Summary:	Common Files for kate and konqueror
Summary(pl.UTF-8):	Pliki wspólne dla kate i konquerora
Group:		X11/Libraries
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description common-filemanagement
Thumbnail and file sharing libraries for kate and konqueror.

%description common-filemanagement -l pl.UTF-8
Biblioteki służące do tworzenia podglądu i wymiany plików dla kate i
konquerora.

%package common-konsole
Summary:	Common files for konsole and konsolepart
Summary(pl.UTF-8):	Pliki wspólne dla konsole i konsolepart
Group:		X11/Applications
Requires(post,postun):	fontpostinst
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase < 3.0.9-2.4
Obsoletes:	kdebase-fonts

%description common-konsole
Color schemes, icons, fonts and shell profiles for konsole.

%description common-konsole -l pl.UTF-8
Schematy kolorów, ikony, czcionki oraz profile sesji dla konsole.

%package core
Summary:	KDE Core Apps
Summary(pl.UTF-8):	Podstawowe aplikacje KDE
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Requires:	xdg-menus
Suggests:	sudo
Obsoletes:	kdebase < 8:3.2-0.030428.1
Obsoletes:	kdebase-helpcenter
Obsoletes:	kdebase-kcontrol
Obsoletes:	kdebase-khelpcenter
Conflicts:	kttsd <= 040609

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

%package desktop
Summary:	KDesktop - handling of desktop icons, popup menus etc.
Summary(pl.UTF-8):	KDesktop - obsługa ikon na pulpicie, menu itp.
Group:		X11/Applications
Requires:	%{name}-desktop-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kdialog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kfind = %{epoch}:%{version}-%{release}
Requires:	%{name}-kjobviewer = %{epoch}:%{version}-%{release}
Requires:	%{name}-kpager = %{epoch}:%{version}-%{release}
Requires:	eject
Requires:	kde-kgreet
Requires:	kde-kside
Requires:	kde-logoutpic
Requires:	kde-splash-Default
Requires:	konqueror = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.99.7.1
Requires:	xorg-app-xmessage
Requires:	xorg-app-xprop
Provides:	kdebase-kicker
Obsoletes:	kde-decoration-plastik
Obsoletes:	kde-theme-keramik
Obsoletes:	kdebase
Obsoletes:	kdebase-fonts
Obsoletes:	kdebase-kcheckpass
Obsoletes:	kdebase-kdesktop
Obsoletes:	kdebase-kdesktop_lock
Obsoletes:	kdebase-khelpcenter
Obsoletes:	kdebase-kicker
Obsoletes:	kdebase-kioslave
Obsoletes:	kdebase-kmenuedit
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-ksystraycmd
Obsoletes:	kdebase-kwin
Obsoletes:	kdebase-kwin_plugin
Obsoletes:	kdebase-kwmtheme
Obsoletes:	kdebase-kxmlrpc
Obsoletes:	kdebase-screensaver
Obsoletes:	kdebase-static
Obsoletes:	kdebase-wallpapers
Obsoletes:	khotkeys
Conflicts:	kdeedu-libkdeeduui < 8:3.4.0

%description desktop
KDesktop is the program that handles the desktop icons, the popup
menus for the desktop, the mac menubar, and the screensaver system.

%description desktop -l pl.UTF-8
KDesktop to program obsługujący ikony na pulpicie, menu dla pulpitu,
pasek menu oraz system wygaszacza ekranu.

%package desktop-libs
Summary:	KDesktop libraries
Summary(pl.UTF-8):	Biblioteki KDesktop
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 9:3.1.92.031006
Obsoletes:	kdebase-kicker-libs

%description desktop-libs
KDesktop libraries (taskbar, splash themes and window decorations).

%description desktop-libs -l pl.UTF-8
Biblioteki KDesktop (pasek zadań, obsługa motywów obrazków startowych
i dekoracji okna).

%package infocenter
Summary:	KDE Info Center
Summary(pl.UTF-8):	Centrum informacji o systemie dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	pciutils

%description infocenter
Application for displaying information about your system.

%description infocenter -l pl.UTF-8
Centrum informacji o systemie dla KDE.

%package kappfinder
Summary:	Menu Updating Tool
Summary(pl.UTF-8):	Narzędzie do aktualizacji menu
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase =< 8:3.2-0.030418.2

%description kappfinder
The tool for finding installed application and adding them to your
menu.

%description kappfinder -l pl.UTF-8
Narzędzie do wyszukiwania zainstalowanych aplikacji i dodawania ich do
menu.

%package kate
Summary:	KDE Advanced Text Editor
Summary(pl.UTF-8):	Zaawansowany edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kate
Conflicts:	kttsd <= 040609

%description kate
KDE advanced text editor featuring among others:
- fast opening/editing of files even the big ones (opens a 50MB file
  in a few seconds)
- powerful syntaxhighlighting engine, extensible via XML files
- Code Folding capabilities for C++, C, PHP and more
- Dynamic Word Wrap - long lines are wrapped at the window border on
  the fly for better overview
- multiple views allows you to view more instances of the same
  document and/or more documents at one time
- support for different encodings globally and at write time
- built in dockable terminal emulation
- sidebars with a list of open documents, a directory viewer with a
  directory chooser, a filter chooser and more
- a plugin interface to allow third party plugins
- a "Filter" command allows you to run selected text through a shell
  command

%description kate -l pl.UTF-8
Kate (KDE advanced text editor) to zaawansowany edytor tekstu KDE o
możliwościach obejmujących m.in.:
- szybkie otwieranie i edycję nawet dużych plików (otwiera plik 50MB w
  parę sekund)
- potężny silnik podświetlania składni, rozszerzalny za pomocą plików
  XML
- możliwość zwijania kodu dla C++, C, PHP i innych języków
- dynamiczne zawijanie wierszy - długie linie są zawijane na granicy
  okna w locie dla lepszej widoczności
- wiele widoków pozwalających oglądać więcej instancji tego samego
  dokumentu i/lub więcej dokumentów w tym samym czasie
- obsługę różnych kodowań globalnie i w czasie zapisu
- wbudowaną emulację dokowalnego terminala
- paski z listą otwartych dokumentów, przeglądarkę katalogów z
  możliwością wybierania katalogu i filtrów
- interfejs wtyczek obsługujący zewnętrzne wtyczki
- polecenie "Filtr" pozwalające przepuszczać zaznaczony tekst przez
  polecenie powłoki

%package kdeprintfax
Summary:	KDE Fax Tool
Summary(pl.UTF-8):	Narzędzie do faksowania dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	efax
Requires:	enscript

%description kdeprintfax
Support for sending faxes via the KDE print system.

%description kdeprintfax -l pl.UTF-8
Wsparcie wysyłania faksów dla systemu drukowania KDE.

%package kdcop
Summary:	Graphic DCOP browser/client
Summary(pl.UTF-8):	Graficzna przegladarka/klient DCOP
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 9:3.1.91.030911

%description kdcop
Graphic DCOP browser/client. Actually useful only for developers and
very advanced users.

%description kdcop -l pl.UTF-8
Graficzna przeglądarka/klient DCOP. Przydatna głównie developerom i
bardzo zaawansowanym użytkownikom.

%package kdialog
Summary:	A KDE version of dialog
Summary(pl.UTF-8):	Wersja KDE dialogu
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase < 8:3.2-0.030423.2

%description kdialog
Kdialog allows to display window dialogs with KDE widgets from shell
scripts.

%description kdialog -l pl.UTF-8
Kdialog umożliwia wyświetlanie komunikatów w okienkach KDE z poziomu
skryptów powłoki.

%package kfind
Summary:	KDE Find Tool
Summary(pl.UTF-8):	Narzędzie do wyszukiwania plików dla KDE
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	kfind

%description kfind
A tool for find files for KDE.

%description kfind -l pl.UTF-8
Narzędzie do wyszukiwania plików dla KDE.

%package kfontinst
Summary:	K Font Installer
Summary(pl.UTF-8):	Instalator fontów dla KDE
Group:		X11/Applications
#Requires:	konqueror = %{epoch}:%{version}-%{release}
# for /usr/share/doc/kde/HTML/en/kcontrol, probably stupid
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase-desktop < 3.1.90.030720

%description kfontinst
KDE font installer.

%description kfontinst -l pl.UTF-8
Instalator czcionek dla KDE.

%package kjobviewer
Summary:	Print Job Viewer
Summary(pl.UTF-8):	Podgląd zadań drukowania
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description kjobviewer
KDE print queue viewer.

%description kjobviewer -l pl.UTF-8
Przeglądarka kolejki drukowania dla KDE.

%package klipper
Summary:	Clipboard Tool
Summary(pl.UTF-8):	Narzędzie schowka
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description klipper
A tool extending the clipboard support for KDE. Note that it requires
a powerful computer.

%description klipper -l pl.UTF-8
Narzędzie rozszerzające obsługę schowka dla KDE. Wymaga ono szybkiego
systemu.

%package konsole
Summary:	KDE Terminal Emulator
Summary(pl.UTF-8):	Emulator terminala dla KDE
Group:		X11/Applications
Requires:	%{name}-common-konsole = %{epoch}:%{version}-%{release}
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	konsole

%description konsole
KDE Terminal Emulator.

%description konsole -l pl.UTF-8
Emulator terminala dla KDE.

%package kpager
Summary:	Desktop Pager
Summary(pl.UTF-8):	Przełącznik biurek
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase =< 8:3.2-0.030418.2

%description kpager
KDE Desktop Pager.

%description kpager -l pl.UTF-8
Przełącznik biurek dla KDE.

%package kpersonalizer
Summary:	KDE desktop settings wizard
Summary(pl.UTF-8):	Kreator ustawień środowiska KDE
Group:		X11/Applications
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}
Requires:	%{name}-klipper = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 9:3.1.92.031021

%description kpersonalizer
KDE desktop settings wizard.

%description kpersonalizer -l pl.UTF-8
Kreator ustawień środowiska KDE.

%package ksysguard
Summary:	System Guard
Summary(pl.UTF-8):	Strażnik systemu
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksgrd = %{epoch}:%{version}-%{release}

%description ksysguard
KDE System Guard.

%description ksysguard -l pl.UTF-8
Strażnik systemu dla KDE.

%package kwrite
Summary:	KDE Text Editor
Summary(pl.UTF-8):	Edytor tekstu dla KDE
Group:		X11/Applications/Editors
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkate = %{epoch}:%{version}-%{release}
Obsoletes:	kwrite

%description kwrite
KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description kwrite -l pl.UTF-8
KWrite to prosty edytor tekstu z podświetlaniem składni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest lżejszą wersją Kate,
szybszą dla mniejszych zadań.

%package kwrited
Summary:	KDE write messaging daemon
Summary(pl.UTF-8):	Demon do KDE obsługujący wymianę wiadomości za pomocą write
Group:		X11/Applications
# With functional reasons
Requires:	kdebase-core = %{epoch}:%{version}-%{release}
Obsoletes:	kdebase < 8:3.2-0.030423.1

%description kwrited
A kde daeomn that watches for messages from local users sent with
write or wall.

%description kwrited -l pl.UTF-8
Demon KDE, który monitoruje wiadomości jakie lokalni użytkownicy
wysyłają za pomocą komend write lub wall.

%package libkate
Summary:	A libraries for KDE text editors
Summary(pl.UTF-8):	Biblioteki dla edytorów tekstu KDE
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-kate < 8:3.2-0.030423.1
Obsoletes:	kdebase-libkmultitabbar

%description libkate
A libraries shared between KDE text editors. They provide an
embeddable kate interface.

%description libkate -l pl.UTF-8
Biblioteki współdzielone między edytorami tekstu w KDE. Dostarczają
interfejs kate, który można osadzać w innych aplikacjach.

%package libksgrd
Summary:	ksgrd library
Summary(pl.UTF-8):	Biblioteka ksgrd
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-ksysguard-libs
Obsoletes:	ksysguard < 9:3.1.92.031012

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
Requires:	%{name}-desktop = %{epoch}:%{version}-%{release}

%description screensavers
KDE screensavers.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu desktopu KDE.

%description screensavers -l ru.UTF-8
Некоторые 3D хранители экрана для K Desktop Environment.

%package useraccount
Summary:	User Account
Summary(pl.UTF-8):	Konto użytkownika
Group:		X11/Applications
Obsoletes:	kdeutils-kdepasswd
Obsoletes:	kdeutils-userinfo

%description useraccount
useraccount changes user account information. This module contains
kdepasswd program functionality.

%description useraccount -l pl.UTF-8
useraccount zmienia informacje o koncie użytkownika. Ten moduł zawiera
funkcjonalność programu kdepasswd.

%package -n kdm
Summary:	KDE Display Manager
Summary(pl.UTF-8):	Zarządca ekranów KDE
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	kde-kgreet
Requires:	pam >= 0.99.7.1
Requires:	rc-scripts
Requires:	xorg-app-sessreg
Provides:	XDM
Obsoletes:	kdebase-kdm
Obsoletes:	kdebase-pam

%description -n kdm
A program used for managing X11 sessions on local or remote computers.
Also provides graphical login method.

%description -n kdm -l pl.UTF-8
Program służący do zarządzania zarówno lokalnymi jak i zdalnymi
sesjami X11. Udostępnia także graficzny tryb logowania.

%package -n konqueror
Summary:	Konqueror - web browser and file manager
Summary(pl.UTF-8):	Konqueror - przeglądarka WWW i zarządca plików
Group:		X11/Applications
Requires:	%{name}-common-filemanagement = %{epoch}:%{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	konqueror-libs = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	kdebase-konqueror
Obsoletes:	kdebase-libkmultitabbar

%description -n konqueror
Konqueror is the file manager for the K Desktop Environment. It
supports basic file management on local UNIX filesystems, from simple
cut/copy and paste operations to advanced remote and local network
file browsing.

Konqueror is the canvas for all the latest KDE technology, from KIO
slaves (which provide mechanisms for file access) to component
embedding via the KParts object interface, and it is one of the most
customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2, as
well as Netscape plugins (for example, Flash or RealVideo plugins).

Konqueror is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without ever
launching another application.

%description -n konqueror -l pl.UTF-8
Konqueror to zarządca plików dla środowiska KDE. Obsługuje podstawowe
zarządzanie plikami w lokalnych uniksowych systemach plików, od
prostych operacji wycinania/kopiowania i wklejania do zaawansowanego
przeglądania plików z sieci zdalnych i lokalnych.

Konqueror to podstawa dla wszystkich nowych technologii KDE, od usług
KIO (dostarczających mechanizmy dostępu do plików) po osadzanie
komponentów poprzez interfejs obiektowy KParts i jest jedną z
najbardziej poddających się dostosowaniu do własnych potrzeb
dostępnych aplikacji.

Konqueror jest także przeglądarką WWW o otwartych źródłach, zgodną z
HTML 4.0, obsługującą aplety Javy, JavaScript, CSS1 i (częściowo)
CSS2, a także wtyczki Netscape'a (na przykład Flash i RealAudio).

Konqueror jest uniwersalną aplikacją do przeglądania, umożliwiającą
osadzenie w niej komponentów do przeglądania aby oglądać dokumenty bez
uruchamiania innej aplikacji.

%package -n konqueror-libs
Summary:	konqueror shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone konquerora
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdebase-konqueror-libs
Obsoletes:	kdebase-libkickermain
Obsoletes:	kdebase-libkonq
Obsoletes:	kdebase-libkonqsidebarplugin
Obsoletes:	konqueror < 9:3.1.92.031006

%description -n konqueror-libs
Konqueror shared libraries.

%description -n konqueror-libs -l pl.UTF-8
Biblioteki współdzielone konquerora.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):	Dokumentacja API
Group:		Documentation
Requires:	kdelibs >= 9:3.2.90

%description apidocs
Annotated reference of konqueror,kate,kicker,kcontrol and other
kdebase programming interfaces including:
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsów programowania konquerora, kate, kickera,
kcontrol i innych z kdebase z przypisami. Zawiera:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)


%prep
%setup -q -n %{oname}-%{version}

%build
export QTDIR=%{_prefix}
mkdir build
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

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d/kdm

install %{SOURCE4}	$RPM_BUILD_ROOT/etc/rc.d/init.d/kdm

%clean
rm -rf $RPM_BUILD_ROOT

%files ksysguard
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ksysguarddrc
%attr(755,root,root) %{_bindir}/ksysguard
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%attr(755,root,root) %{_libdir}/libkdeinit4_ksysguard.so
%{_desktopdir}/kde4/ksysguard.desktop
%{_datadir}/apps/kicker/applets/ksysguardapplet.desktop
%{_datadir}/apps/ksysguard
%{_iconsdir}/*/*/apps/ksysguardd.png
%{_kdedocdir}/en/ksysguard/index.cache.bz2
%{_kdedocdir}/en/ksysguard/index.docbook

%files -n kdm
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kdm
%attr(755,root,root) %{_bindir}/genkdmconf
%attr(755,root,root) %{_bindir}/kdm
%attr(755,root,root) %{_bindir}/kdmctl
%attr(755,root,root) %{_libdir}/kde4/kcm_kdm.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_config
%attr(755,root,root) %{_libdir}/kde4/libexec/kdm_greet
%{_datadir}/apps/doc/kdm/README
%{_datadir}/apps/doc/kdm/greeter.dtd
%{_datadir}/apps/kdm/pics/kdelogo-crystal.png
%{_datadir}/apps/kdm/pics/kdelogo.png
%{_datadir}/apps/kdm/pics/shutdown.jpg
%{_datadir}/apps/kdm/pics/users/default1.png
%{_datadir}/apps/kdm/pics/users/default2.png
%{_datadir}/apps/kdm/pics/users/default3.png
%{_datadir}/apps/kdm/pics/users/root1.png
%{_datadir}/apps/kdm/sessions/*.desktop
%{_datadir}/apps/kdm/themes/circles/KdmGreeterTheme.desktop
%{_datadir}/apps/kdm/themes/circles/background.svg
%{_datadir}/apps/kdm/themes/circles/circles.xml
%{_datadir}/apps/kdm/themes/circles/flower.png
%{_datadir}/apps/kdm/themes/circles/help.png
%{_datadir}/apps/kdm/themes/circles/options.png
%{_datadir}/apps/kdm/themes/circles/screenshot.png
%{_datadir}/config/kdm.knsrc
%{_kdedocdir}/en/kdm/index.cache.bz2
%{_kdedocdir}/en/kdm/index.docbook
%{_kdedocdir}/en/kdm/kdmrc-ref.docbook
%{_kdedocdir}/en/kdm/theme-ref.docbook
%{_datadir}/kde4/services/kdm.desktop

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%attr(755,root,root) %{_libdir}/kde4/kcm_screensaver.so
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*
%{_datadir}/config.kcfg/kscreensaversettings.kcfg
%{_datadir}/dbus-1/interfaces/org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kde4/services/ScreenSavers/kblank.desktop
%{_datadir}/kde4/services/ScreenSavers/krandom.desktop
%{_datadir}/kde4/services/screensaver.desktop
%{_datadir}/kde4/servicetypes/screensaver.desktop

%files kfontinst
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_libdir}/kde4/fontthumbnail.so
%attr(755,root,root) %{_libdir}/kde4/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/kde4/kcm_fonts.so
%attr(755,root,root) %{_libdir}/kde4/kfontviewpart.so
%attr(755,root,root) %{_libdir}/kde4/kio_fonts.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kfontprint
%attr(755,root,root) %{_libdir}/kde4/libexec/kio_fonts_helper
%attr(755,root,root) %{_libdir}/libkfontinst.so.*
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*
%attr(755,root,root) %{_libdir}/strigi/strigita_font.so
%{_desktopdir}/kde4/kfontview.desktop
%{_datadir}/apps/kfontinst/icons/*/*/actions/*.png
%{_datadir}/apps/kfontinst/icons/*/scalable/actions/*.svgz
%{_datadir}/apps/kfontinst/kfontviewpart.rc
%{_datadir}/apps/kfontview/kfontviewui.rc
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
%{_datadir}/kde4/services/fontthumbnail.desktop
%{_datadir}/kde4/services/kfontviewpart.desktop

%files klipper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_libdir}/libkdeinit4_klipper.so
%{_desktopdir}/kde4/klipper.desktop
%{_datadir}/autostart/klipper.desktop
%{_datadir}/config/klipperrc
%{_kdedocdir}/en/klipper/index.cache.bz2
%{_kdedocdir}/en/klipper/index.docbook
%{_kdedocdir}/en/klipper/screenshot.png

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
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Code_Poets_Dream/contents/screenshot.png
%{_datadir}/wallpapers/Code_Poets_Dream/metadata.desktop
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Colorado_Farm/contents/screenshot.png
%{_datadir}/wallpapers/Colorado_Farm/metadata.desktop
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Curls_on_Green/contents/screenshot.png
%{_datadir}/wallpapers/Curls_on_Green/metadata.desktop
%{_datadir}/wallpapers/EOS/contents/images/1024x768.jpg
%{_datadir}/wallpapers/EOS/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/EOS/contents/images/1280x800.jpg
%{_datadir}/wallpapers/EOS/contents/images/1440x900.jpg
%{_datadir}/wallpapers/EOS/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/EOS/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/EOS/contents/screenshot.png
%{_datadir}/wallpapers/EOS/metadata.desktop
%{_datadir}/wallpapers/Emotion/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Emotion/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Emotion/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Emotion/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Emotion/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Emotion/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Emotion/contents/screenshot.png
%{_datadir}/wallpapers/Emotion/metadata.desktop
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1280x1024.JPG
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1280x800.JPG
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1440x900.JPG
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1600x1200.JPG
%{_datadir}/wallpapers/Fields_of_Peace/contents/images/1920x1200.JPG
%{_datadir}/wallpapers/Fields_of_Peace/contents/screenshot.png
%{_datadir}/wallpapers/Fields_of_Peace/metadata.desktop
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Finally_Summer_in_Germany/contents/screenshot.png
%{_datadir}/wallpapers/Finally_Summer_in_Germany/metadata.desktop
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Fresh_Morning/contents/screenshot.png
%{_datadir}/wallpapers/Fresh_Morning/metadata.desktop
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Golden_Ripples/contents/screenshot.png
%{_datadir}/wallpapers/Golden_Ripples/metadata.desktop
%{_datadir}/wallpapers/Green_Concentration/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Green_Concentration/contents/screenshot.png
%{_datadir}/wallpapers/Green_Concentration/metadata.desktop
%{_datadir}/wallpapers/Ladybuggin/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/images/1600-1200.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Ladybuggin/contents/screenshot.png
%{_datadir}/wallpapers/Ladybuggin/metadata.desktop
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Leafs_Labyrinth/contents/screenshot.png
%{_datadir}/wallpapers/Leafs_Labyrinth/metadata.desktop
%{_datadir}/wallpapers/Red_Leaf/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Red_Leaf/contents/screenshot.png
%{_datadir}/wallpapers/Red_Leaf/metadata.desktop
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1024x768.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1280x800.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1440x900.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/Skeeter_Hawk/contents/screenshot.png
%{_datadir}/wallpapers/Skeeter_Hawk/metadata.desktop
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1024x768.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1280x800.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1440x900.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1600x1200.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/images/1920x1200.jpg
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/contents/screenshot.png
%{_datadir}/wallpapers/There_is_Rain_on_the_Table/metadata.desktop

%files libksgrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksgrd.so.*

%files infocenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_info.so
%{_kdedocdir}/en/kinfocenter/devices/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/devices/index.docbook
%{_kdedocdir}/en/kinfocenter/dma/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/dma/index.docbook
%{_kdedocdir}/en/kinfocenter/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/index.docbook
%{_kdedocdir}/en/kinfocenter/interrupts/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/interrupts/index.docbook
%{_kdedocdir}/en/kinfocenter/ioports/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/ioports/index.docbook
%{_kdedocdir}/en/kinfocenter/memory/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/memory/index.docbook
%{_kdedocdir}/en/kinfocenter/nics/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/nics/index.docbook
%{_kdedocdir}/en/kinfocenter/opengl/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/opengl/index.docbook
%{_kdedocdir}/en/kinfocenter/partitions/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/partitions/index.docbook
%{_kdedocdir}/en/kinfocenter/pci/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/pci/index.docbook
%{_kdedocdir}/en/kinfocenter/pcmcia/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/pcmcia/index.docbook
%{_kdedocdir}/en/kinfocenter/processor/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/processor/index.docbook
%{_kdedocdir}/en/kinfocenter/protocols/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/protocols/index.docbook
%{_kdedocdir}/en/kinfocenter/samba/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/samba/index.docbook
%{_kdedocdir}/en/kinfocenter/scsi/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/scsi/index.docbook
%{_kdedocdir}/en/kinfocenter/sound/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/sound/index.docbook
%{_kdedocdir}/en/kinfocenter/usb/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/usb/index.docbook
%{_kdedocdir}/en/kinfocenter/xserver/index.cache.bz2
%{_kdedocdir}/en/kinfocenter/xserver/index.docbook

%files desktop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemsettingsrc
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/kstartupconfig4
%attr(755,root,root) %{_bindir}/ksystraycmd
%attr(755,root,root) %{_bindir}/startkde

# kaccess
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_libdir}/libkdeinit4_kaccess.so
%{_datadir}/apps/kaccess/kaccess.notifyrc
%{_datadir}/kde4/services/kaccess.desktop

# khotkeys
%attr(755,root,root) %{_bindir}/khotkeys
%{_libdir}/kconf_update_bin/khotkeys_update
%attr(755,root,root) %{_libdir}/kde4/kcm_khotkeys.so
%attr(755,root,root) %{_libdir}/kde4/kded_khotkeys.so
%attr(755,root,root) %{_libdir}/libkdeinit4_khotkeys.so
%{_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{_datadir}/apps/khotkeys/kde32b1.khotkeys
%{_datadir}/apps/khotkeys/konqueror_gestures_kde321.khotkeys
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_iconsdir}/*/*/apps/khotkeys.png
%{_datadir}/kde4/services/kded/khotkeys.desktop
%{_datadir}/kde4/services/khotkeys.desktop

# kmenuedit
%attr(755,root,root) %{_bindir}/kmenuedit
%attr(755,root,root) %{_libdir}/libkdeinit4_kmenuedit.so
%{_desktopdir}/kde4/kmenuedit.desktop
%{_datadir}/apps/kmenuedit/icons/*/*/actions/menu_new.png
%{_datadir}/apps/kmenuedit/kmenueditui.rc
%{_kdedocdir}/en/kmenuedit/done.png
%{_kdedocdir}/en/kmenuedit/index.cache.bz2
%{_kdedocdir}/en/kmenuedit/index.docbook
%{_kdedocdir}/en/kmenuedit/itemname.png
%{_kdedocdir}/en/kmenuedit/kmenueditmain.png
%{_kdedocdir}/en/kmenuedit/new.png
%{_kdedocdir}/en/kmenuedit/selecticon.png
%{_kdedocdir}/en/kmenuedit/selectinternet.png
%{_iconsdir}/*/*/apps/kmenuedit.png

# krandrtray
%attr(755,root,root) %{_bindir}/krandrtray
%{_desktopdir}/kde4/krandrtray.desktop

# krunner
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_bindir}/krunner_lock
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
%{_datadir}/apps/ksplash/Themes/None/Theme.rc
%{_iconsdir}/*/*/apps/ksplash.png
%{_datadir}/kde4/services/ksplashthememgr.desktop

# ktip
%attr(755,root,root) %{_bindir}/ktip
%{_desktopdir}/kde4/ktip.desktop
%{_datadir}/autostart/ktip.desktop

# kwin
%attr(755,root,root) %{_bindir}/kwin
%attr(755,root,root) %{_bindir}/kwin_killer_helper
%attr(755,root,root) %{_bindir}/kwin_rules_dialog
%{_libdir}/kconf_update_bin/kwin_update_default_rules
%{_libdir}/kconf_update_bin/kwin_update_window_settings
%attr(755,root,root) %{_libdir}/kde4/kcm_kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwincompositing.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindecoration.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwindesktop.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/kde4/kwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/libkwineffects.so.*
%attr(755,root,root) %{_libdir}/libkwinnvidiahack.so.*
%{_datadir}/apps/kwin/blur-render.frag
%{_datadir}/apps/kwin/blur-render.vert
%{_datadir}/apps/kwin/blur.frag
%{_datadir}/apps/kwin/blur.vert
%{_datadir}/apps/kwin/circle-edgy.png
%{_datadir}/apps/kwin/circle.png
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
%{_datadir}/kde4/services/kwindecoration.desktop
%{_datadir}/kde4/services/kwinfocus.desktop
%{_datadir}/kde4/services/kwinmoving.desktop
%{_datadir}/kde4/services/kwinoptions.desktop
%{_datadir}/kde4/services/kwinrules.desktop

# kxkb
%attr(755,root,root) %{_bindir}/kxkb
%attr(755,root,root) %{_libdir}/libkdeinit4_kxkb.so
%{_kdedocdir}/en/kxkb/index.cache.bz2
%{_kdedocdir}/en/kxkb/index.docbook
%{_iconsdir}/*/*/apps/kxkb.png

# plasma
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
%attr(755,root,root) %{_libdir}/libplasma.so
%attr(755,root,root) %{_libdir}/libplasma.so.1
%attr(755,root,root) %{_libdir}/libplasma.so.1.0.0
%{_datadir}/apps/kwin/default_rules/plasma_desktop_containment.kwinrules
%{_datadir}/apps/plasmoidviewer/checker.png
%{_datadir}/autostart/plasma.desktop
%{_kdedocdir}/en/plasma/index.cache.bz2
%{_kdedocdir}/en/plasma/index.docbook
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

# systemsettings
%attr(755,root,root) %{_bindir}/systemsettings
%{_desktopdir}/kde4/systemsettings.desktop
%{_datadir}/apps/systemsettings/systemsettingsui.rc
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
%{_datadir}/apps/desktoptheme/default/colors
%{_datadir}/apps/desktoptheme/default/dialogs/background.svg
%{_datadir}/apps/desktoptheme/default/dialogs/shutdowndialog.svg
%{_datadir}/apps/desktoptheme/default/widgets/analog_meter.svg
%{_datadir}/apps/desktoptheme/default/widgets/background.svg
%{_datadir}/apps/desktoptheme/default/widgets/bar_meter_horizontal.svg
%{_datadir}/apps/desktoptheme/default/widgets/bar_meter_vertical.svg
%{_datadir}/apps/desktoptheme/default/widgets/battery-oxygen.svg
%{_datadir}/apps/desktoptheme/default/widgets/battery.svg
%{_datadir}/apps/desktoptheme/default/widgets/clock.svg
%{_datadir}/apps/desktoptheme/default/widgets/connection-established.svg
%{_datadir}/apps/desktoptheme/default/widgets/iconbutton.svg
%{_datadir}/apps/desktoptheme/default/widgets/panel-background.svg
%{_datadir}/apps/desktoptheme/default/widgets/plot-background.svg
%{_datadir}/apps/desktoptheme/default/widgets/toolbox-button.svg
%{_datadir}/apps/desktoptheme/metadata.desktop
%{_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{_datadir}/apps/kthememanager/themes/HighContrastDark-big/HighContrastDark-big.preview.png
%{_datadir}/apps/kthememanager/themes/HighContrastDark-big/HighContrastDark-big.xml
%{_datadir}/apps/kthememanager/themes/HighContrastDark/HighContrastDark.preview.png
%{_datadir}/apps/kthememanager/themes/HighContrastDark/HighContrastDark.xml
%{_datadir}/apps/kthememanager/themes/HighContrastLight-big/HighContrastLight-big.preview.png
%{_datadir}/apps/kthememanager/themes/HighContrastLight-big/HighContrastLight-big.xml
%{_datadir}/apps/kthememanager/themes/HighContrastLight/HighContrastLight.preview.png
%{_datadir}/apps/kthememanager/themes/HighContrastLight/HighContrastLight.xml
%{_datadir}/apps/kthememanager/themes/KDE_Classic/KDE_Classic.preview.png
%{_datadir}/apps/kthememanager/themes/KDE_Classic/KDE_Classic.xml
%{_datadir}/apps/kthememanager/themes/Keramik/Keramik.preview.png
%{_datadir}/apps/kthememanager/themes/Keramik/Keramik.xml
%{_datadir}/apps/kthememanager/themes/Plastik/Plastik.preview.png
%{_datadir}/apps/kthememanager/themes/Plastik/Plastik.xml
%{_datadir}/apps/kthememanager/themes/Platinum/Platinum.preview.png
%{_datadir}/apps/kthememanager/themes/Platinum/Platinum.xml
%{_datadir}/apps/kthememanager/themes/Redmond/Redmond.preview.png
%{_datadir}/apps/kthememanager/themes/Redmond/Redmond.xml
%{_datadir}/apps/kthememanager/themes/Sunshine/Sunshine.preview.png
%{_datadir}/apps/kthememanager/themes/Sunshine/Sunshine.xml
%{_datadir}/apps/kthememanager/themes/YellowOnBlue-big/YellowOnBlue-big.preview.png
%{_datadir}/apps/kthememanager/themes/YellowOnBlue-big/YellowOnBlue-big.xml
%{_datadir}/apps/kthememanager/themes/YellowOnBlue/YellowOnBlue.preview.png
%{_datadir}/apps/kthememanager/themes/YellowOnBlue/YellowOnBlue.xml
%{_datadir}/kde4/services/installktheme.desktop
%{_datadir}/kde4/services/kthememanager.desktop


%files core
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kcontroledit
%attr(755,root,root) %{_bindir}/kdostartupconfig4
%attr(755,root,root) %{_bindir}/solidshell
%attr(755,root,root) %{_libdir}/libkdecorations.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kcminit_startup.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kcontroledit.so
%{_datadir}/apps/color-schemes/Honeycomb.colors
%{_datadir}/apps/color-schemes/Norway.colors
%{_datadir}/apps/color-schemes/ObsidianCoast.colors
%{_datadir}/apps/color-schemes/Oxygen.colors
%{_datadir}/apps/color-schemes/Steel.colors
%{_datadir}/apps/color-schemes/WontonSoup.colors

# styles
%attr(755,root,root) %{_libdir}/kde4/kcm_style.so
%attr(755,root,root) %{_libdir}/kde4/kstyle_keramik_config.so
%{_datadir}/kde4/services/style.desktop

# solid
%attr(755,root,root) %{_libdir}/kde4/kcm_solid.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakebluetooth.so
%attr(755,root,root) %{_libdir}/kde4/solid_fakenet.so
%attr(755,root,root) %{_libdir}/kde4/solid_hal_power.so
%attr(755,root,root) %{_libdir}/libsolidcontrol.so.*
%attr(755,root,root) %{_libdir}/libsolidcontrolifaces.so.*
%{_datadir}/apps/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/apps/solidfakebluetoothbackend/fakebluetooth.xml
%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml
%{_datadir}/kde4/services/kcm_solid.desktop
%{_datadir}/kde4/services/solidbackends/solid_fakebluetooth.desktop
%{_datadir}/kde4/services/solidbackends/solid_fakenet.desktop
%{_datadir}/kde4/services/solidbackends/solid_hal_power.desktop
%{_datadir}/kde4/servicetypes/solidbluetoothmanager.desktop
%{_datadir}/kde4/servicetypes/solidnetworkmanager.desktop
%{_datadir}/kde4/servicetypes/solidpowermanager.desktop

#
# don't know yet == have no idea
#
%attr(755,root,root) %{_libdir}/kde4/ion_bbcukmet.so
%attr(755,root,root) %{_libdir}/kde4/ion_envcan.so
%attr(755,root,root) %{_libdir}/kde4/ion_noaa.so
%attr(755,root,root) %{_libdir}/kde4/kcm_access.so
%attr(755,root,root) %{_libdir}/kde4/kcm_accessibility.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bell.so
%attr(755,root,root) %{_libdir}/kde4/kcm_clock.so
%attr(755,root,root) %{_libdir}/kde4/kcm_colors.so
%attr(755,root,root) %{_libdir}/kde4/kcm_display.so
%attr(755,root,root) %{_libdir}/kde4/kcm_energy.so
%attr(755,root,root) %{_libdir}/kde4/kcm_input.so
%attr(755,root,root) %{_libdir}/kde4/kcm_joystick.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keyboard_layout.so
%attr(755,root,root) %{_libdir}/kde4/kcm_keys.so
%attr(755,root,root) %{_libdir}/kde4/kcm_launch.so
%attr(755,root,root) %{_libdir}/kde4/kcm_nic.so
%attr(755,root,root) %{_libdir}/kde4/kcm_randr.so
%attr(755,root,root) %{_libdir}/kde4/kcm_smserver.so
%attr(755,root,root) %{_libdir}/kde4/kcm_usb.so
%attr(755,root,root) %{_libdir}/kde4/kcm_view1394.so
%attr(755,root,root) %{_libdir}/kde4/kcm_xinerama.so
%attr(755,root,root) %{_libdir}/kde4/kded_networkstatus.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kcheckpass
%attr(755,root,root) %{_libdir}/kde4/libexec/krootimage
%attr(755,root,root) %{_libdir}/kde4/libexec/test_kcm_xinerama
%attr(755,root,root) %{_libdir}/libkworkspace.so
%attr(755,root,root) %{_libdir}/libkworkspace.so.4
%attr(755,root,root) %{_libdir}/libkworkspace.so.4.0.0
%attr(755,root,root) %{_libdir}/libprocesscore.so
%attr(755,root,root) %{_libdir}/libprocesscore.so.4
%attr(755,root,root) %{_libdir}/libprocesscore.so.4.0.0
%attr(755,root,root) %{_libdir}/libprocessui.so
%attr(755,root,root) %{_libdir}/libprocessui.so.4
%attr(755,root,root) %{_libdir}/libprocessui.so.4.0.0
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so.4
%attr(755,root,root) %{_libdir}/libtaskmanager.so.4.0.0
%attr(755,root,root) %{_libdir}/libweather_ion.so
%attr(755,root,root) %{_libdir}/libweather_ion.so.4
%attr(755,root,root) %{_libdir}/libweather_ion.so.4.0.0
%{_datadir}/apps/kcminput/cursor_large_black.pcf.gz
%{_datadir}/apps/kcminput/cursor_large_white.pcf.gz
%{_datadir}/apps/kcminput/cursor_small_white.pcf.gz
%{_datadir}/apps/kcminput/pics/mouse_lh.png
%{_datadir}/apps/kcminput/pics/mouse_rh.png
%{_datadir}/apps/kcmusb/usb.ids
%{_datadir}/apps/kcmview1394/oui.db
%{_datadir}/apps/kconf_update/convertShortcuts.pl
%{_datadir}/apps/kconf_update/kaccel.upd
%{_datadir}/apps/kconf_update/kcmdisplayrc.upd
%{_datadir}/apps/kconf_update/konqueror_gestures_kde321_update.upd
%{_datadir}/apps/kconf_update/kwin.upd
%{_datadir}/apps/kconf_update/kwin3_plugin.pl
%{_datadir}/apps/kconf_update/kwin3_plugin.upd
%{_datadir}/apps/kconf_update/kwin_focus1.sh
%{_datadir}/apps/kconf_update/kwin_focus1.upd
%{_datadir}/apps/kconf_update/kwin_focus2.sh
%{_datadir}/apps/kconf_update/kwin_focus2.upd
%{_datadir}/apps/kconf_update/kwin_fsp_workarounds_1.upd
%{_datadir}/apps/kconf_update/kwin_on_off.upd
%{_datadir}/apps/kconf_update/kwiniconify.upd
%{_datadir}/apps/kconf_update/kwinsticky.upd
%{_datadir}/apps/kconf_update/kwinupdatewindowsettings.upd
%{_datadir}/apps/kconf_update/move_session_config.sh
%{_datadir}/apps/kconf_update/on-off_to_true-false.sh
%{_datadir}/apps/kconf_update/pluginlibFix.pl
%{_datadir}/apps/kcontrol/pics/anchor.png
%{_datadir}/apps/kcontrol/pics/energybig.png
%{_datadir}/apps/kcontrol/pics/lo-energy.png
%{_datadir}/apps/kcontrol/pics/logo.png
%{_datadir}/apps/kcontrol/pics/mini-world.png
%{_datadir}/apps/kcontrol/pics/monitor.png
%{_datadir}/apps/kcontroledit/icons/crystalsvg/22x22/actions/menu_new.png
%{_datadir}/apps/kcontroledit/icons/crystalsvg/22x22/actions/menu_new_sep.png
%{_datadir}/apps/kcontroledit/icons/crystalsvg/32x32/actions/menu_new.png
%{_datadir}/apps/kcontroledit/icons/crystalsvg/32x32/actions/menu_new_sep.png
%{_datadir}/apps/kcontroledit/kcontroleditui.rc
%{_datadir}/apps/kdewizard/tips
%{_datadir}/apps/kdisplay/app-defaults/AAAAAAGeneral.ad
%{_datadir}/apps/kdisplay/app-defaults/AAAMotif.ad
%{_datadir}/apps/kdisplay/app-defaults/AAATk.ad
%{_datadir}/apps/kdisplay/app-defaults/AAAXaw.ad
%{_datadir}/apps/kdisplay/app-defaults/AcroRead.ad
%{_datadir}/apps/kdisplay/app-defaults/Editres.ad
%{_datadir}/apps/kdisplay/app-defaults/Emacs.ad
%{_datadir}/apps/kdisplay/app-defaults/GV.ad
%{_datadir}/apps/kdisplay/app-defaults/ML.ad
%{_datadir}/apps/kdisplay/app-defaults/Nedit.ad
%{_datadir}/apps/kdisplay/app-defaults/Netscape.ad
%{_datadir}/apps/kdisplay/app-defaults/RVPlayer.ad
%{_datadir}/apps/kdisplay/app-defaults/WPerfect.ad
%{_datadir}/apps/kdisplay/app-defaults/XCalc.ad
%{_datadir}/apps/kdisplay/app-defaults/XOsview.ad
%{_datadir}/apps/kdisplay/app-defaults/XTerm.ad
%{_datadir}/apps/kdisplay/app-defaults/XV.ad
%{_datadir}/apps/kdisplay/app-defaults/Xawtv.ad
%{_datadir}/apps/kdisplay/app-defaults/Xdvi.ad
%{_datadir}/apps/kdisplay/app-defaults/Xpdf.ad
%{_datadir}/config.kcfg/klaunch.kcfg
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
%{_datadir}/desktop-directories/kde-utilities-accessibility.directory
%{_datadir}/desktop-directories/kde-utilities-desktop.directory
%{_datadir}/desktop-directories/kde-utilities-file.directory
%{_datadir}/desktop-directories/kde-utilities-peripherals.directory
%{_datadir}/desktop-directories/kde-utilities-pim.directory
%{_datadir}/desktop-directories/kde-utilities-xutils.directory
%{_datadir}/desktop-directories/kde-utilities.directory
%{_iconsdir}/oxygen/128x128/apps/kcmkwm.png
%{_iconsdir}/oxygen/16x16/apps/computer.png
%{_iconsdir}/oxygen/16x16/apps/daemon.png
%{_iconsdir}/oxygen/16x16/apps/kcmkwm.png
%{_iconsdir}/oxygen/16x16/apps/kdeapp.png
%{_iconsdir}/oxygen/16x16/apps/kernel.png
%{_iconsdir}/oxygen/16x16/apps/running.png
%{_iconsdir}/oxygen/16x16/apps/shell.png
%{_iconsdir}/oxygen/16x16/apps/unknownapp.png
%{_iconsdir}/oxygen/16x16/apps/waiting.png
%{_iconsdir}/oxygen/22x22/apps/kcmkwm.png
%{_iconsdir}/oxygen/32x32/apps/kcmkwm.png
%{_iconsdir}/oxygen/48x48/apps/kcmkwm.png
%{_iconsdir}/oxygen/64x64/apps/kcmkwm.png
%{_iconsdir}/oxygen/scalable/apps/kcmkwm.svgz
%{_datadir}/kde4/services/accessibility.desktop
%{_datadir}/kde4/services/bell.desktop
%{_datadir}/kde4/services/clock.desktop
%{_datadir}/kde4/services/colors.desktop
%{_datadir}/kde4/services/desktop.desktop
%{_datadir}/kde4/services/devices.desktop
%{_datadir}/kde4/services/display.desktop
%{_datadir}/kde4/services/dma.desktop
%{_datadir}/kde4/services/energy.desktop
%{_datadir}/kde4/services/interrupts.desktop
%{_datadir}/kde4/services/ion-bbcukmet.desktop
%{_datadir}/kde4/services/ion-envcan.desktop
%{_datadir}/kde4/services/ion-noaa.desktop
%{_datadir}/kde4/services/ioports.desktop
%{_datadir}/kde4/services/joystick.desktop
%{_datadir}/kde4/services/kcmaccess.desktop
%{_datadir}/kde4/services/kcmlaunch.desktop
%{_datadir}/kde4/services/kcmsmserver.desktop
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
%{_datadir}/kde4/services/randr.desktop
%{_datadir}/kde4/services/scsi.desktop
%{_datadir}/kde4/services/sound.desktop
%{_datadir}/kde4/services/xinerama.desktop
%{_datadir}/kde4/services/xserver.desktop
%{_datadir}/kde4/servicetypes/kwineffect.desktop
%{_datadir}/kde4/servicetypes/weather_ion.desktop
%{_datadir}/sounds/pop.wav


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
%{_datadir}/apps/cmake/modules/FindLibXKlavier.cmake
%{_datadir}/apps/cmake/modules/FindPAM.cmake
%{_datadir}/apps/cmake/modules/FindRAW1394.cmake
%{_datadir}/apps/cmake/modules/FindSensors.cmake
%{_datadir}/apps/cmake/modules/UnixAuth.cmake
%{_includedir}/KDE/Plasma/AbstractRunner
%{_includedir}/KDE/Plasma/Animator
%{_includedir}/KDE/Plasma/Applet
%{_includedir}/KDE/Plasma/AppletBrowser
%{_includedir}/KDE/Plasma/ConfigXml
%{_includedir}/KDE/Plasma/Containment
%{_includedir}/KDE/Plasma/Corona
%{_includedir}/KDE/Plasma/DataContainer
%{_includedir}/KDE/Plasma/DataEngine
%{_includedir}/KDE/Plasma/DataEngineManager
%{_includedir}/KDE/Plasma/Dialog
%{_includedir}/KDE/Plasma/GLApplet
%{_includedir}/KDE/Plasma/Package
%{_includedir}/KDE/Plasma/PackageMetadata
%{_includedir}/KDE/Plasma/PackageStructure
%{_includedir}/KDE/Plasma/Phase
%{_includedir}/KDE/Plasma/Plasma
%{_includedir}/KDE/Plasma/ScriptEngine
%{_includedir}/KDE/Plasma/SearchContext
%{_includedir}/KDE/Plasma/SearchMatch
%{_includedir}/KDE/Plasma/Svg
%{_includedir}/KDE/Plasma/Theme
%{_includedir}/KDE/Plasma/UiLoader
%{_includedir}/KDE/Plasma/View
%{_includedir}/kcommondecoration.h
%{_includedir}/kdecoration.h
%{_includedir}/kdecorationfactory.h
%{_includedir}/kgreeterplugin.h
%{_includedir}/kscreensaver.h
%{_includedir}/kscreensaver_vroot.h
%{_includedir}/ksgrd/SensorAgent.h
%{_includedir}/ksgrd/SensorClient.h
%{_includedir}/ksgrd/SensorManager.h
%{_includedir}/ksgrd/SensorShellAgent.h
%{_includedir}/ksgrd/SensorSocketAgent.h
%{_includedir}/ksysguard/ProcessFilter.h
%{_includedir}/ksysguard/ProcessModel.h
%{_includedir}/ksysguard/ksysguardprocesslist.h
%{_includedir}/ksysguard/process.h
%{_includedir}/ksysguard/processes.h
%{_includedir}/kwinconfig.h
%{_includedir}/kwineffects.h
%{_includedir}/kwinglobals.h
%{_includedir}/kworkspace/kwindowlistmenu.h
%{_includedir}/kworkspace/kworkspace.h
%{_includedir}/plasma/abstractrunner.h
%{_includedir}/plasma/animator.h
%{_includedir}/plasma/applet.h
%{_includedir}/plasma/appletbrowser.h
%{_includedir}/plasma/configxml.h
%{_includedir}/plasma/containment.h
%{_includedir}/plasma/corona.h
%{_includedir}/plasma/datacontainer.h
%{_includedir}/plasma/dataengine.h
%{_includedir}/plasma/dataenginemanager.h
%{_includedir}/plasma/dialog.h
%{_includedir}/plasma/glapplet.h
%{_includedir}/plasma/layouts/borderlayout.h
%{_includedir}/plasma/layouts/boxlayout.h
%{_includedir}/plasma/layouts/fliplayout.h
%{_includedir}/plasma/layouts/flowlayout.h
%{_includedir}/plasma/layouts/freelayout.h
%{_includedir}/plasma/layouts/hboxlayout.h
%{_includedir}/plasma/layouts/layout.h
%{_includedir}/plasma/layouts/layoutanimator.h
%{_includedir}/plasma/layouts/layoutitem.h
%{_includedir}/plasma/layouts/nodelayout.h
%{_includedir}/plasma/layouts/vboxlayout.h
%{_includedir}/plasma/package.h
%{_includedir}/plasma/packagemetadata.h
%{_includedir}/plasma/packagestructure.h
%{_includedir}/plasma/phase.h
%{_includedir}/plasma/plasma.h
%{_includedir}/plasma/plasma_export.h
%{_includedir}/plasma/scriptengine.h
%{_includedir}/plasma/searchcontext.h
%{_includedir}/plasma/searchmatch.h
%{_includedir}/plasma/shadowitem_p.h
%{_includedir}/plasma/svg.h
%{_includedir}/plasma/theme.h
%{_includedir}/plasma/uiloader.h
%{_includedir}/plasma/view.h
%{_includedir}/plasma/widgets/checkbox.h
%{_includedir}/plasma/widgets/flash.h
%{_includedir}/plasma/widgets/icon.h
%{_includedir}/plasma/widgets/label.h
%{_includedir}/plasma/widgets/lineedit.h
%{_includedir}/plasma/widgets/meter.h
%{_includedir}/plasma/widgets/progressbar.h
%{_includedir}/plasma/widgets/pushbutton.h
%{_includedir}/plasma/widgets/radiobutton.h
%{_includedir}/plasma/widgets/signalplotter.h
%{_includedir}/plasma/widgets/widget.h
%{_includedir}/solid/control/authentication.h
%{_includedir}/solid/control/bluetoothinputdevice.h
%{_includedir}/solid/control/bluetoothinterface.h
%{_includedir}/solid/control/bluetoothmanager.h
%{_includedir}/solid/control/bluetoothremotedevice.h
%{_includedir}/solid/control/bluetoothsecurity.h
%{_includedir}/solid/control/ifaces/authentication.h
%{_includedir}/solid/control/ifaces/bluetoothinputdevice.h
%{_includedir}/solid/control/ifaces/bluetoothinterface.h
%{_includedir}/solid/control/ifaces/bluetoothmanager.h
%{_includedir}/solid/control/ifaces/bluetoothremotedevice.h
%{_includedir}/solid/control/ifaces/network.h
%{_includedir}/solid/control/ifaces/networkinterface.h
%{_includedir}/solid/control/ifaces/networkmanager.h
%{_includedir}/solid/control/ifaces/powermanager.h
%{_includedir}/solid/control/ifaces/wirelessnetwork.h
%{_includedir}/solid/control/network.h
%{_includedir}/solid/control/networking.h
%{_includedir}/solid/control/networkinterface.h
%{_includedir}/solid/control/networkmanager.h
%{_includedir}/solid/control/powermanager.h
%{_includedir}/solid/control/singletondefs.h
%{_includedir}/solid/control/solid_control_export.h
%{_includedir}/solid/control/wirelessnetwork.h
%{_includedir}/taskmanager/startup.h
%{_includedir}/taskmanager/task.h
%{_includedir}/taskmanager/taskmanager.h
