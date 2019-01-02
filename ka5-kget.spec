%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kget
Summary:	kget
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a8da3b691919f0a1c16df2883949bfb8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.7.0
BuildRequires:	gpgme-qt5-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcmutils-devel >= 5.44.0
BuildRequires:	kf5-kcompletion-devel >= 5.44.0
BuildRequires:	kf5-kconfig-devel >= 5.44.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.44.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.44.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.44.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.44.0
BuildRequires:	kf5-kdoctools-devel >= 5.44.0
BuildRequires:	kf5-ki18n-devel >= 5.44.0
BuildRequires:	kf5-kiconthemes-devel >= 5.44.0
BuildRequires:	kf5-kio-devel >= 5.44.0
BuildRequires:	kf5-kitemviews-devel >= 5.44.0
BuildRequires:	kf5-knotifications-devel >= 5.44.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.44.0
BuildRequires:	kf5-kparts-devel >= 5.44.0
BuildRequires:	kf5-kservice-devel >= 5.44.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.44.0
BuildRequires:	kf5-kwallet-devel >= 5.44.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.44.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.44.0
BuildRequires:	kf5-kxmlgui-devel >= 5.44.0
BuildRequires:	kf5-solid-devel >= 5.44.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGet is a versatile and user-friendly download manager.. Features.
Downloading files from FTP and HTTP(S) sources. Pausing and resuming
of downloading files, as well as the ability to restart a download.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kget.categories
%attr(755,root,root) %{_bindir}/kget
%attr(755,root,root) %{_libdir}/libkgetcore.so
%attr(755,root,root) %ghost %{_libdir}/libkgetcore.so.5
%attr(755,root,root) %{_libdir}/libkgetcore.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kget_checksumsearchfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kget_metalinkfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kget_multisegkiofactory.so
%dir %{_libdir}/qt5/plugins/kget
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_checksumsearchfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_kio.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_metalinkfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_multisegkiofactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget_browser_integration.so
%{_desktopdir}/org.kde.kget.desktop
%{_datadir}/config.kcfg/kget.kcfg
%{_datadir}/config.kcfg/kget_checksumsearchfactory.kcfg
%{_datadir}/config.kcfg/kget_mirrorsearchfactory.kcfg
%{_datadir}/config.kcfg/kget_multisegkiofactory.kcfg
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.rc
%{_iconsdir}/hicolor/128x128/apps/kget.png
%{_iconsdir}/hicolor/16x16/apps/kget.png
%{_iconsdir}/hicolor/22x22/apps/kget.png
%{_iconsdir}/hicolor/32x32/apps/kget.png
%{_iconsdir}/hicolor/48x48/apps/kget.png
%{_iconsdir}/hicolor/64x64/apps/kget.png
%{_datadir}/kconf_update/kget.upd
%{_datadir}/kconf_update/kget_limitdownloads.pl
%{_datadir}/kconf_update/kget_sensitive.pl
%{_datadir}/kget
%{_datadir}/khtml/kpartplugins/kget_plug_in.desktop
%{_datadir}/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/knotifications5/kget.notifyrc
%{_datadir}/kservices5/ServiceMenus/kget_download.desktop
%{_datadir}/kservices5/kget_checksumsearchfactory_config.desktop
%{_datadir}/kservices5/kget_metalinkfactory_config.desktop
%{_datadir}/kservices5/kget_mirrorsearchfactory_config.desktop
%{_datadir}/kservices5/kget_multisegkiofactory_config.desktop
%{_datadir}/kservicetypes5/kget_plugin.desktop
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.rc
%{_datadir}/kxmlgui5/kget
%{_datadir}/metainfo/org.kde.kget.appdata.xml
