Summary:	Gourmet Recipe Manager is a simple but powerful recipe-managing application
Summary(hu.UTF-8):	Gourmet Recipe Manager egy egyszerű, de hatékony recept-nyilvántartó alkalmazás
Name:		gourmet
Version:	0.15.9
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.gz
# Source0-md5:	7bef5569fb4523747973d83ab69a9a79
URL:		http://grecipe-manager.sourceforge.net/
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	python-PIL-devel
BuildRequires:	python-ReportLab
BuildRequires:	python-gnome-desktop-print
BuildRequires:	python-pygtk-devel
BuildRequires:	python-sqlite
BuildRequires:	rpm-pythonprov
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-sqlite
Suggests:	python-gnome-extras-gtkspell
#Suggests:	python-poppler
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gourmet Recipe Manager is a simple but powerful recipe-managing
application. Gourmet allows you to collect, search and organize your
recipes, and to automatically generate shopping lists from your
collection.

%description -l hu.UTF-8
Gourmet Recipe Manager egy egyszerű, de hatékony recept-nyilvántartó
alkalmazás. A Gourmet-tal össze tudod gyűjteni, keresni és
rendszerezni a receptjeidet és automatikusan elkészíteni a
bevásárlólistát a gyűjteményed alapján.

%package -n python-%{name}
Summary:	Gourmet Python modules
Summary(hu.UTF-8):	Gourmet Python modulok
Summary(pl.UTF-8):	Moduły Pythona Gourmet
Group:		Development/Languages/Python
Requires:	python-ReportLab
Requires:	python-sqlalchemy-migrate
%pyrequires_eq	python-modules

%description -n python-%{name}
This package provides Gourmet Recipe Manager Python modules.

%description -n python-%{name} -l hu.UTF-8
Ez a csomag tartalmazza a Gourmet Recipe Manager Python moduljait.

%description -n python-%{name} -l pl.UTF-8
Moduły Pythona z Gourmet Recipe Manager.

%prep
%setup -q

%build
cd i18n
mv nl_NL.po nl.po
mv pt_PT.po pt.po
mv zh.po zh_CN.po
rm de.po
rm sv.po
rm sv_SE.po
for file in *.po; do
	lang=$(echo $file | cut -f 1 -d .)
	mkdir -p $lang/LC_MESSAGES
	msgfmt -o $lang/LC_MESSAGES/gourmet.mo $file
done
cd ..
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

mv $RPM_BUILD_ROOT%{_localedir}/{sv_SE,sv}
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}

# what is the other Spanish?
rm -r $RPM_BUILD_ROOT%{_localedir}/es_ES
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES FAQ README TODO
%attr(755,root,root) %{_bindir}/gourmet
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/recbox.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}*.egg-info
