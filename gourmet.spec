Summary:	Gourmet Recipe Manager is a simple but powerful recipe-managing application
Summary(hu.UTF-8):	Gourmet Recipe Manager egy egyszerű, de hatékony recept-nyilvántartó alkalmazás
Name:		gourmet
Version:	0.14.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.gz
# Source0-md5:	81c4fbae57afebd165344519ad142357
URL:		http://grecipe-manager.sourceforge.net/
BuildRequires:	libglade2-devel
BuildRequires:	python-PIL-devel
BuildRequires:	python-ReportLab
BuildRequires:	python-gnome-desktop-print
BuildRequires:	python-pygtk-devel
BuildRequires:	python-sqlite
Requires:	python-ReportLab
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

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ README TODO
%attr(755,root,root) %{_bindir}/gourmet
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/recbox.png
%{py_sitescriptdir}/%{name}/*
%{py_sitescriptdir}/%{name}-%{version}*.egg-info
%dir %{_datadir}/%{name}
%dir %{py_sitescriptdir}/gourmet
%{_datadir}/%{name}/*
%{_datadir}/locale/*
