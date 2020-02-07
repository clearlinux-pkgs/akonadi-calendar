#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-calendar
Version  : 19.12.2
Release  : 21
URL      : https://download.kde.org/stable/release-service/19.12.2/src/akonadi-calendar-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/akonadi-calendar-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/akonadi-calendar-19.12.2.tar.xz.sig
Summary  : Akonadi calendar integration
Group    : Development/Tools
License  : LGPL-2.1
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
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev

%description
# Akonadi Calendar #
Akonadi Calendar is a library that effectively bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KCalCore library. It provides
jobs, models and other helpers to make working with events and calendars through
Akonadi easier.

%package data
Summary: data components for the akonadi-calendar package.
Group: Data

%description data
data components for the akonadi-calendar package.


%package dev
Summary: dev components for the akonadi-calendar package.
Group: Development
Requires: akonadi-calendar-lib = %{version}-%{release}
Requires: akonadi-calendar-data = %{version}-%{release}
Provides: akonadi-calendar-devel = %{version}-%{release}
Requires: akonadi-calendar = %{version}-%{release}
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
%setup -q -n akonadi-calendar-19.12.2
cd %{_builddir}/akonadi-calendar-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581088174
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581088174
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-calendar
cp %{_builddir}/akonadi-calendar-19.12.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-calendar/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang libakonadi-calendar5-serializer
%find_lang libakonadi-calendar5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
/usr/share/qlogging-categories5/akonadi-calendar.categories
/usr/share/qlogging-categories5/akonadi-calendar.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Akonadi/Calendar/BlockAlarmsAttribute
/usr/include/KF5/Akonadi/Calendar/CalendarBase
/usr/include/KF5/Akonadi/Calendar/CalendarClipboard
/usr/include/KF5/Akonadi/Calendar/ETMCalendar
/usr/include/KF5/Akonadi/Calendar/FetchJobCalendar
/usr/include/KF5/Akonadi/Calendar/FreeBusyManager
/usr/include/KF5/Akonadi/Calendar/FreeBusyProviderBase
/usr/include/KF5/Akonadi/Calendar/History
/usr/include/KF5/Akonadi/Calendar/ICalImporter
/usr/include/KF5/Akonadi/Calendar/ITIPHandler
/usr/include/KF5/Akonadi/Calendar/IncidenceChanger
/usr/include/KF5/Akonadi/Calendar/PublishDialog
/usr/include/KF5/Akonadi/Calendar/StandardCalendarActionManager
/usr/include/KF5/Akonadi/Calendar/TodoPurger
/usr/include/KF5/akonadi-calendar_version.h
/usr/include/KF5/akonadi/calendar/akonadi-calendar_export.h
/usr/include/KF5/akonadi/calendar/blockalarmsattribute.h
/usr/include/KF5/akonadi/calendar/calendarbase.h
/usr/include/KF5/akonadi/calendar/calendarclipboard.h
/usr/include/KF5/akonadi/calendar/calendarsettings.h
/usr/include/KF5/akonadi/calendar/etmcalendar.h
/usr/include/KF5/akonadi/calendar/fetchjobcalendar.h
/usr/include/KF5/akonadi/calendar/freebusymanager.h
/usr/include/KF5/akonadi/calendar/freebusyproviderbase.h
/usr/include/KF5/akonadi/calendar/history.h
/usr/include/KF5/akonadi/calendar/icalimporter.h
/usr/include/KF5/akonadi/calendar/incidencechanger.h
/usr/include/KF5/akonadi/calendar/itiphandler.h
/usr/include/KF5/akonadi/calendar/publishdialog.h
/usr/include/KF5/akonadi/calendar/standardcalendaractionmanager.h
/usr/include/KF5/akonadi/calendar/todopurger.h
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarConfig.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiCalendar/KF5AkonadiCalendarTargets.cmake
/usr/lib64/libKF5AkonadiCalendar.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiCalendar.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiCalendar.so.5
/usr/lib64/libKF5AkonadiCalendar.so.5.13.2
/usr/lib64/qt5/plugins/akonadi_serializer_kcalcore.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-calendar/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libakonadi-calendar5-serializer.lang -f libakonadi-calendar5.lang
%defattr(-,root,root,-)

