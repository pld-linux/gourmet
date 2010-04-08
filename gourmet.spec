#
# TODO:
#	- check why more translations (including Polish) are not installed
#
Summary:	Gourmet Recipe Manager is a simple but powerful recipe-managing application
Summary(hu.UTF-8):	Gourmet Recipe Manager egy egyszerű, de hatékony recept-nyilvántartó alkalmazás
Name:		gourmet
Version:	0.15.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.gz
# Source0-md5:	018b449cbd12942fe05ed9927192604f
URL:		http://grecipe-manager.sourceforge.net/
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	python-PIL-devel
BuildRequires:	python-ReportLab
BuildRequires:	python-gnome-desktop-print
BuildRequires:	python-pygtk-devel
BuildRequires:	python-sqlite
Requires:	python-%{name} = %{version}-%{release}
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
Gourmet Recipe Manager egy egyszerű, de hatékony
recept-nyilvántartó alkalmazás. A Gourmet-tal össze tudod
gyűjteni, keresni és rendszerezni a receptjeidet és automatikusan
elkészíteni a bevásárlólistát a gyűjteményed alapján.

%package -n python-%{name}
Summary:	Gourmet Python modules
Summary(pl.UTF-8):	Moduły Pythona Gourmet
Group:		Development/Languages/Python
Requires:	python-ReportLab
Requires:	python-sqlalchemy-migrate
%pyrequires_eq	python-modules

%description -n python-%{name}
This package provides Gourumet Recipe Manager Python modules.

%description -n python-%{name} -l pl.UTF-8
Moduły Pythona z Gourmet Recipe Manager.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

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
