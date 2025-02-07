Name: llvm-cmake-utils
Version: 18.1.2
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/cmake-%{version}.src.tar.xz
Release: 2
Summary: llvm-cmake-utils - CMake utilities shared across LLVM subprojects
License: LGPL
%description
%{summary}.

%install
mkdir -p %{buildroot}%{_datadir}
cd %{buildroot}%{_datadir}
tar -xf %{SOURCE0}
mv cmake-%{version}.src cmake

%files
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/*.cmake
%ghost %{_datadir}/cmake/README.rst

