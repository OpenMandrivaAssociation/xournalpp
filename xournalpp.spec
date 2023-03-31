Name:           xournalpp
Version:        1.1.3
Release:        2
Summary:        Notetaking software designed around a tablet
License:        GPLv2+
Group:          Office/Utilities
Url:            https://github.com/xournalpp/xournalpp
Source0:        https://github.com/xournalpp/xournalpp/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  texlive
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gettext

# Optional, disable it if any problems arise (angry)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(lua)

Requires: hicolor-icon-theme

%description
Xournal++ is a hand note taking software.
It supports pen input, e.g. Wacom tablets.

%prep
%autosetup -p1

%build
%cmake  -DENABLE_CPPUNIT=ON
%make_build

%install
%make_install -C build

%find_lang xournalpp

%files -f xournalpp.lang
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/xournalpp
%{_bindir}/xournalpp-thumbnailer
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/*.xml
%{_datadir}/applications/com.github.xournalpp.xournalpp.desktop
%{_datadir}/metainfo/com.github.xournalpp.xournalpp.appdata.xml
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/xournalpp/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/thumbnailers/*.thumbnailer
