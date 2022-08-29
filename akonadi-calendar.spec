#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : akonadi-calendar
Version  : 22.08.0
Release  : 47
URL      : https://download.kde.org/stable/release-service/22.08.0/src/akonadi-calendar-22.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.0/src/akonadi-calendar-22.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.0/src/akonadi-calendar-22.08.0.tar.xz.sig
Summary  : Akonadi calendar integration
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: akonadi-calendar-bin = %{version}-%{release}
Requires: akonadi-calendar-data = %{version}-%{release}
Requires: akonadi-calendar-lib = %{version}-%{release}
Requires: akonadi-calendar-license = %{version}-%{release}
Requires: akonadi-calendar-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcontacts-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kio-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev

%description
SPDX-License-Identifier: CC0-1.0

%package bin
Summary: bin components for the akonadi-calendar package.
Group: Binaries
Requires: akonadi-calendar-data = %{version}-%{release}
Requires: akonadi-calendar-license = %{version}-%{release}

%description bin
bin components for the akonadi-calendar package.


%package data
Summary: data components for the akonadi-calendar package.
Group: Data

%description data
data components for the akonadi-calendar package.


%package dev
Summary: dev components for the akonadi-calendar package.
Group: Development
Requires: akonadi-calendar-lib = %{version}-%{release}
Requires: akonadi-calendar-bin = %{version}-%{release}
Requires: akonadi-calendar-data = %{version}-%{release}
Provides: akonadi-calendar-devel = %{version}-%{release}
Requires: akonadi-calendar = %{version}-%{release}

%description dev
dev components for the akonadi-calendar package.


%package lib
Summary: lib components for the akonadi-calendar package.
Group: Libraries
Requires: akonadi-calendar-data = %{version}-%{release}
Requires: akonadi-calendar-license = %{version}-%{release}

%description lib
lib components for the akonadi-calendar package.


%package license
Summary: license components for the akonadi-calendar package.
Group: Default

%description license
license components for the akonadi-calendar package.


%package locales
Summary: locales components for the akonadi-calendar package.
Group: Default

%description locales
locales components for the akonadi-calendar package.


%prep
%setup -q -n akonadi-calendar-22.08.0
cd %{_builddir}/akonadi-calendar-22.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661784178
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1661784178
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-calendar
cp %{_builddir}/akonadi-calendar-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadi-calendar/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/akonadi-calendar-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-calendar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-calendar-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-calendar/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-calendar-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-calendar/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-calendar-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-calendar/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/akonadi-calendar-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-calendar/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/akonadi-calendar-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-calendar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/akonadi-calendar-%{version}/reminder-daemon/kalendarac.notifyrc.license %{buildroot}/usr/share/package-licenses/akonadi-calendar/e9aa865961a8cfb32e5c081920b28aa634edef10 || :
pushd clr-build
%make_install
popd
%find_lang libakonadi-calendar5-serializer
%find_lang libakonadi-calendar5
%find_lang kalendarac

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kalendarac

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
/usr/share/dbus-1/services/org.kde.kalendarac.service
/usr/share/knotifications5/kalendarac.notifyrc
/usr/share/qlogging-categories5/akonadi-calendar.categories
/usr/share/qlogging-categories5/akonadi-calendar.renamecategories
/usr/share/qlogging-categories5/org_kde_kalendarac.categories
/usr/share/xdg/autostart/org.kde.kalendarac.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiCalendar/Akonadi/BlockAlarmsAttribute
/usr/include/KF5/AkonadiCalendar/Akonadi/CalendarBase
/usr/include/KF5/AkonadiCalendar/Akonadi/CalendarClipboard
/usr/include/KF5/AkonadiCalendar/Akonadi/CalendarUtils
/usr/include/KF5/AkonadiCalendar/Akonadi/ETMCalendar
/usr/include/KF5/AkonadiCalendar/Akonadi/FetchJobCalendar
/usr/include/KF5/AkonadiCalendar/Akonadi/FreeBusyManager
/usr/include/KF5/AkonadiCalendar/Akonadi/FreeBusyProviderBase
/usr/include/KF5/AkonadiCalendar/Akonadi/History
/usr/include/KF5/AkonadiCalendar/Akonadi/ICalImporter
/usr/include/KF5/AkonadiCalendar/Akonadi/ITIPHandler
/usr/include/KF5/AkonadiCalendar/Akonadi/IncidenceChanger
/usr/include/KF5/AkonadiCalendar/Akonadi/IncidenceTreeModel
/usr/include/KF5/AkonadiCalendar/Akonadi/PublishDialog
/usr/include/KF5/AkonadiCalendar/Akonadi/StandardCalendarActionManager
/usr/include/KF5/AkonadiCalendar/Akonadi/TodoPurger
/usr/include/KF5/AkonadiCalendar/akonadi-calendar_version.h
/usr/include/KF5/AkonadiCalendar/akonadi/akonadi-calendar_export.h
/usr/include/KF5/AkonadiCalendar/akonadi/blockalarmsattribute.h
/usr/include/KF5/AkonadiCalendar/akonadi/calendarbase.h
/usr/include/KF5/AkonadiCalendar/akonadi/calendarclipboard.h
/usr/include/KF5/AkonadiCalendar/akonadi/calendarsettings.h
/usr/include/KF5/AkonadiCalendar/akonadi/calendarutils.h
/usr/include/KF5/AkonadiCalendar/akonadi/etmcalendar.h
/usr/include/KF5/AkonadiCalendar/akonadi/fetchjobcalendar.h
/usr/include/KF5/AkonadiCalendar/akonadi/freebusymanager.h
/usr/include/KF5/AkonadiCalendar/akonadi/freebusyproviderbase.h
/usr/include/KF5/AkonadiCalendar/akonadi/history.h
/usr/include/KF5/AkonadiCalendar/akonadi/icalimporter.h
/usr/include/KF5/AkonadiCalendar/akonadi/incidencechanger.h
/usr/include/KF5/AkonadiCalendar/akonadi/incidencetreemodel.h
/usr/include/KF5/AkonadiCalendar/akonadi/itiphandler.h
/usr/include/KF5/AkonadiCalendar/akonadi/publishdialog.h
/usr/include/KF5/AkonadiCalendar/akonadi/standardcalendaractionmanager.h
/usr/include/KF5/AkonadiCalendar/akonadi/todopurger.h
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarConfig.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarTargets.cmake
/usr/lib64/libKF5AkonadiCalendar.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiCalendar.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiCalendar.so.5
/usr/lib64/libKF5AkonadiCalendar.so.5.21.0
/usr/lib64/qt5/plugins/akonadi_serializer_kcalcore.so
/usr/lib64/qt5/plugins/kf5/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-calendar/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-calendar/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadi-calendar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-calendar/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-calendar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-calendar/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/akonadi-calendar/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi-calendar/e9aa865961a8cfb32e5c081920b28aa634edef10

%files locales -f libakonadi-calendar5-serializer.lang -f libakonadi-calendar5.lang -f kalendarac.lang
%defattr(-,root,root,-)

