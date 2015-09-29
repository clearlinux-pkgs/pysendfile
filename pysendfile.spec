#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysendfile
Version  : 2.0.0
Release  : 13
URL      : https://pypi.python.org/packages/source/p/pysendfile/pysendfile-2.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pysendfile/pysendfile-2.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pysendfile
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===========
Quick links
===========
* Home page: http://code.google.com/p/pysendfile
* Download: http://code.google.com/p/pysendfile/downloads/list

%prep
%setup -q -n pysendfile-2.0.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)
