%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kget
Summary:	kget
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c82a51da58c9e7239c969c0e45ecf9c3
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
BuildRequires:	ka5-dolphin-devel >= %{kdeappsver}
BuildRequires:	ka5-libktorrent-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-solid-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%{_libdir}/libkgetcore.so
%ghost %{_libdir}/libkgetcore.so.5
%attr(755,root,root) %{_libdir}/libkgetcore.so.*.*.*
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
%dir %{_datadir}/dolphinpart
%dir %{_datadir}/dolphinpart/kpartplugins
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/dolphinpart/kpartplugins/kget_plug_in.rc
%{_iconsdir}/hicolor/128x128/apps/kget.png
%{_iconsdir}/hicolor/16x16/apps/kget.png
%{_iconsdir}/hicolor/22x22/apps/kget.png
%{_iconsdir}/hicolor/32x32/apps/kget.png
%{_iconsdir}/hicolor/48x48/apps/kget.png
%{_iconsdir}/hicolor/64x64/apps/kget.png
%{_datadir}/kconf_update/kget.upd
%attr(755,root,root) %{_datadir}/kconf_update/kget_limitdownloads.pl
%attr(755,root,root) %{_datadir}/kconf_update/kget_sensitive.pl
%{_datadir}/kget
%dir %{_datadir}/khtml
%dir %{_datadir}/khtml/kpartplugins
%{_datadir}/khtml/kpartplugins/kget_plug_in.desktop
%{_datadir}/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/knotifications5/kget.notifyrc
%{_datadir}/kservices5/ServiceMenus/kget_download.desktop
%{_datadir}/kservices5/kget_checksumsearchfactory_config.desktop
%{_datadir}/kservices5/kget_metalinkfactory_config.desktop
%{_datadir}/kservices5/kget_mirrorsearchfactory_config.desktop
%{_datadir}/kservices5/kget_multisegkiofactory_config.desktop
%{_datadir}/kservicetypes5/kget_plugin.desktop
%dir %{_datadir}/kwebkitpart
%dir %{_datadir}/kwebkitpart/kpartplugins
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/kwebkitpart/kpartplugins/kget_plug_in.rc
%{_datadir}/kxmlgui5/kget
%{_datadir}/metainfo/org.kde.kget.appdata.xml
%{_datadir}/qlogging-categories5/kget.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kget_bittorrentfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kget/kget_bittorrent.so
%{_datadir}/kservices5/kget_bittorrentfactory_config.desktop
