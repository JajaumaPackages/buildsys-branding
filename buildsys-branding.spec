%global branding .jajauma
%global rpm_macros_dir /etc/rpm

Name:           buildsys-branding
Version:        1.0.0
Release:        1%{?dist}
Summary:        Build system branding

License:        MIT

BuildArch:      noarch
BuildRequires:  centos-release
Requires:       centos-release

%description
This packages provided branded versions of standard rpm macros.


%prep


%build


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{rpm_macros_dir}
cat >> %{buildroot}%{rpm_macros_dir}/macros.dist%{branding} << EOF
%%dist .el%{rhel}%{branding}
EOF


%files
%{rpm_macros_dir}/macros.dist%{branding}


%changelog
* Sat Aug 05 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1.el7.centos
- Initial release
