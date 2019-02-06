Name:           ros-indigo-plotjuggler
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS plotjuggler package

Group:          Development/Libraries
License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtdeclarative-devel
Requires:       qt5-qtsvg-devel
Requires:       ros-indigo-ros-type-introspection
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rosbag-storage
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-rostime
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
BuildRequires:  binutils-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ros-type-introspection
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-rosbag-storage
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-topic-tools

%description
PlotJuggler: juggle with data

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Feb 06 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.0-0
- Autogenerated by Bloom

* Fri Jan 25 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.3-1
- Autogenerated by Bloom

* Fri Jan 25 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.3-0
- Autogenerated by Bloom

* Thu Jan 24 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.2-0
- Autogenerated by Bloom

* Mon Jan 21 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.1-0
- Autogenerated by Bloom

* Sun Jan 20 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.0-0
- Autogenerated by Bloom

* Mon Nov 12 2018 Davide Faconti <davide.faconti@gmail.com> - 1.9.0-0
- Autogenerated by Bloom

* Mon Sep 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.4-0
- Autogenerated by Bloom

* Fri Aug 24 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.3-0
- Autogenerated by Bloom

* Sun Aug 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.2-0
- Autogenerated by Bloom

* Sat Aug 18 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.1-0
- Autogenerated by Bloom

* Fri Aug 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.0-0
- Autogenerated by Bloom

* Sun Aug 12 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.3-0
- Autogenerated by Bloom

* Fri Aug 10 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.2-0
- Autogenerated by Bloom

* Mon Jul 23 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.1-1
- Autogenerated by Bloom

* Sun Jul 22 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.1-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.0-0
- Autogenerated by Bloom

* Sat May 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.6.2-0
- Autogenerated by Bloom

* Tue May 15 2018 Davide Faconti <davide.faconti@gmail.com> - 1.6.1-0
- Autogenerated by Bloom

* Tue May 01 2018 Davide Faconti <davide.faconti@gmail.com> - 1.6.0-0
- Autogenerated by Bloom

* Tue Apr 24 2018 Davide Faconti <davide.faconti@gmail.com> - 1.5.2-0
- Autogenerated by Bloom

* Wed Feb 14 2018 Davide Faconti <davide.faconti@gmail.com> - 1.5.1-0
- Autogenerated by Bloom

* Tue Nov 28 2017 Davide Faconti <davide.faconti@gmail.com> - 1.5.0-0
- Autogenerated by Bloom

* Mon Nov 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.4.2-0
- Autogenerated by Bloom

* Sun Nov 19 2017 Davide Faconti <davide.faconti@gmail.com> - 1.4.1-0
- Autogenerated by Bloom

* Tue Nov 14 2017 Davide Faconti <davide.faconti@gmail.com> - 1.4.0-0
- Autogenerated by Bloom

* Thu Oct 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.3.0-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Davide Faconti <davide.faconti@gmail.com> - 1.2.1-0
- Autogenerated by Bloom

* Tue Aug 29 2017 Davide Faconti <davide.faconti@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

* Tue Jul 11 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.3-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.2-0
- Autogenerated by Bloom

* Mon Jun 26 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.8-0
- Autogenerated by Bloom

* Fri May 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri May 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

* Sun May 07 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Sun Apr 30 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Wed Apr 26 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

* Sat Apr 22 2017 Davide Faconti <davide.faconti@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Davide Faconti <davide.faconti@gmail.com> - 0.18.0-0
- Autogenerated by Bloom

* Sun Apr 02 2017 Davide Faconti <davide.faconti@gmail.com> - 0.17.0-0
- Autogenerated by Bloom

* Wed Mar 22 2017 Davide Faconti <davide.faconti@gmail.com> - 0.16.0-0
- Autogenerated by Bloom

* Wed Mar 22 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.3-0
- Autogenerated by Bloom

* Wed Mar 22 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.2-0
- Autogenerated by Bloom

* Mon Mar 20 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.1-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.0-1
- Autogenerated by Bloom

* Fri Mar 17 2017 Davide Faconti <davide.faconti@gmail.com> - 0.15.0-0
- Autogenerated by Bloom

* Thu Mar 16 2017 Davide Faconti <davide.faconti@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Wed Mar 15 2017 Davide Faconti <davide.faconti@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Wed Mar 15 2017 Davide Faconti <davide.faconti@gmail.com> - 0.14.0-0
- Autogenerated by Bloom

* Tue Mar 14 2017 Davide Faconti <davide.faconti@gmail.com> - 0.13.1-0
- Autogenerated by Bloom

* Sun Mar 12 2017 Davide Faconti <davide.faconti@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Fri Mar 10 2017 Davide Faconti <davide.faconti@gmail.com> - 0.12.3-0
- Autogenerated by Bloom

* Fri Mar 10 2017 Davide Faconti <davide.faconti@gmail.com> - 0.12.2-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Davide Faconti <davide.faconti@gmail.com> - 0.12.1-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Davide Faconti <davide.faconti@gmail.com> - 0.11.0-1
- Autogenerated by Bloom

* Thu Feb 23 2017 Davide Faconti <davide.faconti@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.3-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.1-0
- Autogenerated by Bloom

* Sun Feb 12 2017 Davide Faconti <davide.faconti@gmail.com> - 0.10.0-0
- Autogenerated by Bloom

* Thu Feb 09 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.1-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-2
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-1
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <davide.faconti@gmail.com> - 0.9.0-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.0-3
- Autogenerated by Bloom

* Mon Jan 23 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.0-2
- Autogenerated by Bloom

* Mon Jan 23 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.0-1
- Autogenerated by Bloom

* Mon Jan 23 2017 Davide Faconti <davide.faconti@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

