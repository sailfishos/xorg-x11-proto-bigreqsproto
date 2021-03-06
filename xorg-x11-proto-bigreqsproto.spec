# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       xorg-x11-proto-bigreqsproto
Summary:    X.Org X11 Protocol bigreqsproto
Version:    1.1.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-bigreqsproto.yaml
Provides:   bigreqsproto


%description
This extension defines a protocol to enable the use of requests that exceed 262140 bytes in length.



%prep
%setup -q -n bigreqsproto-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_includedir}/X11/extensions/bigreqstr.h
%{_includedir}/X11/extensions/bigreqsproto.h
%{_datadir}/pkgconfig/bigreqsproto.pc
%doc %{_docdir}/bigreqsproto/bigreq.xml
# << files


