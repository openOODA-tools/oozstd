Name:           oozstd
Version:        0.1.0
Release:        1%{?dist}
Summary:        Ultra-fast Zstandard compression and decompression utilizing modern vector units.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oozstd
Source0:        oozstd-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oozstd is a sovereign, capability-bounded ZSTD COMPRESS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oozstd
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oozstd-uninstall

%files
/usr/bin/oozstd
/usr/bin/oozstd-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
