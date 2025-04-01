Name:		python-nox
Version:	2025.2.9
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/n/nox/nox-%{version}.tar.gz
Summary:	Flexible test automation for Python
URL:		https://pypi.org/project/nox/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
nox is a command-line tool that automates testing in multiple Python
environments, similar to tox.  Unlike tox, Nox uses a standard Python file
for configuratio.

%files
%{_bindir}/nox
%{_bindir}/tox-to-nox
%{py_sitedir}/nox
%{py_sitedir}/nox-*.*-info
