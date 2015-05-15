Summary:	An implementation of the Wacom Tablet Plugin
Name:		browser-plugin-wacom
Version:	0.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://github.com/ZaneA/WacomWebPlugin/archive/v%{version}.tar.gz
# Source0-md5:	ac25285a639280cb9d92a912e0ee6b63
BuildRequires:	iceweasel-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# directory where you store the plugin
%define		_plugindir	%{_libdir}/browser-plugins

%description
An implementation of the Wacom Tablet Plugin for modern browsers on
Linux.

%prep
%setup -q -n WacomWebPlugin-%{version}
sed -i -e 's#/usr/include/firefox#%{_includedir}/iceweasel#g' Makefile
sed -i -e 's#gcc#%{__cc} %{rpmcflags} %{rpmcppflags}#g' Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D npWacomWebPlugin.so $RPM_BUILD_ROOT%{_plugindir}/npWacomWebPlugin.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = "0" ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_plugindir}/npWacomWebPlugin.so
