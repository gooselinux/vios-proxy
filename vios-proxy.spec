Name:           vios-proxy
Version:        0.1
Release:        1%{?dist}
Summary:        Network proxy between a QEMU host and QEMU guests using virtioserial channels

Group:          System Environment/Daemons
License:        Apache License, Version 2.0
URL:            http://www.redhat.com/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  boost-devel 
BuildRequires:  gcc-c++ 
BuildRequires:  cmake >= 2.6.0

%description
The vios-proxy program suite creates a network tunnel between
a server in the QEMU host and a client in a QEMU guest.
The proxied server and client programs open normal TCP network
ports on localhost and the vios-proxy tunnel connects them using
QEMU virtioserial channels.

%package host

Summary:        Network proxy using virtioserial for QEMU host
Group:          System Environment/Daemons

%description host
The vios-proxy-host daemon runs on a QEMU host. A vios-proxy-host daemon
manages all the proxy connections for a single proxied service on the host.
Multiple vios-proxy-host daemons are required to provide proxy access to
multiple services on the host. A single vios-proxy-host daemon may open
multiple proxy channels to multiple QEMU guests limited only by the
number of virtioserial connections available to each guest.

%package guest

Summary:        Network proxy using virtioserial for QEMU guest
Group:          System Environment/Daemons

%description guest
The vios-proxy-guest daemon runs on a QEMU client. A vios-proxy-guest daemon
creates a listening network socket on the guest's localhost interface. When
client programs connect to this socket then the vios-proxy-guest daemon opens
a proxy channel to the host through the tunnel.

%prep
%setup -q


%build
cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc

%files host
/usr/local/bin/vios-proxy-host

%files guest
/usr/local/bin/vios-proxy-guest

%changelog
