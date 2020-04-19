Name:           xournalpp
Version:        1.0.16
Release:        %mkrel 3
Summary:        Notetaking software designed around a tablet
License:        GPLv2+
Group:          Office/Utilities
Url:            https://github.com/xournalpp/xournalpp
Source0:        https://github.com/xournalpp/xournalpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  texlive
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gettext

%description
Xournal++ is a hand note taking software.
It supports pen input, e.g. Wacom tablets.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang xournalpp

# REMOVE UNNECESSARY SCRIPTS update-icon-cache IS TAKEN CARE OF BY RPM FILE TRIGGERS
rm %{buildroot}%{_datadir}/%{name}/ui/*/hicolor/update-icon-cache.sh

%files -f xournalpp.lang
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/xournal-thumbnailer
%{_bindir}/xournalpp
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/*.xml
%{_datadir}/applications/com.github.xournalpp.xournalpp.desktop
%{_datadir}/metainfo/com.github.xournalpp.xournalpp.appdata.xml
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/xournalpp/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/thumbnailers/*.thumbnailer
