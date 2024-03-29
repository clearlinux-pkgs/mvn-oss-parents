#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-oss-parents
Version  : 38
Release  : 19
URL      : https://github.com/sonatype/oss-parents/archive/forge-parent-38.tar.gz
Source0  : https://github.com/sonatype/oss-parents/archive/forge-parent-38.tar.gz
Source1  : https://repo.maven.apache.org/maven2/net/java/jvnet-parent/1/jvnet-parent-1.pom
Source2  : https://repo.maven.apache.org/maven2/net/java/jvnet-parent/3/jvnet-parent-3.pom
Source3  : https://repo.maven.apache.org/maven2/net/java/jvnet-parent/4/jvnet-parent-4.pom
Source4  : https://repo.maven.apache.org/maven2/net/java/jvnet-parent/5/jvnet-parent-5.pom
Source5  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/10/oss-parent-10.pom
Source6  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/11/oss-parent-11.pom
Source7  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/16/oss-parent-16.pom
Source8  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/23/oss-parent-23.pom
Source9  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/24/oss-parent-24.pom
Source10  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/25/oss-parent-25.pom
Source11  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/27/oss-parent-27.pom
Source12  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/28/oss-parent-28.pom
Source13  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/30/oss-parent-30.pom
Source14  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/33/oss-parent-33.pom
Source15  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/34/oss-parent-34.pom
Source16  : https://repo1.maven.org/maven2/com/fasterxml/oss-parent/4/oss-parent-4.pom
Source17  : https://repo1.maven.org/maven2/org/codehaus/codehaus-parent/1/codehaus-parent-1.pom
Source18  : https://repo1.maven.org/maven2/org/codehaus/codehaus-parent/3/codehaus-parent-3.pom
Source19  : https://repo1.maven.org/maven2/org/codehaus/codehaus-parent/4/codehaus-parent-4.pom
Source20  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/10/forge-parent-10.pom
Source21  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/11/forge-parent-11.pom
Source22  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/12/forge-parent-12.pom
Source23  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/3/forge-parent-3.pom
Source24  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/4/forge-parent-4.pom
Source25  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
Source26  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/6/forge-parent-6.pom
Source27  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/7/forge-parent-7.pom
Source28  : https://repo1.maven.org/maven2/org/sonatype/forge/forge-parent/9/forge-parent-9.pom
Source29  : https://repo1.maven.org/maven2/org/sonatype/oss/oss-parent/3/oss-parent-3.pom
Source30  : https://repo1.maven.org/maven2/org/sonatype/oss/oss-parent/5/oss-parent-5.pom
Source31  : https://repo1.maven.org/maven2/org/sonatype/oss/oss-parent/6/oss-parent-6.pom
Source32  : https://repo1.maven.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
Source33  : https://repo1.maven.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
Source34  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/10/spice-parent-10.pom
Source35  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/11/spice-parent-11.pom
Source36  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/12/spice-parent-12.pom
Source37  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
Source38  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/16/spice-parent-16.pom
Source39  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/17/spice-parent-17.pom
Source40  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/18/spice-parent-18.pom
Source41  : https://repo1.maven.org/maven2/org/sonatype/spice/spice-parent/20/spice-parent-20.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-oss-parents-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-oss-parents package.
Group: Data

%description data
data components for the mvn-oss-parents package.


%prep
%setup -q -n oss-parents-forge-parent-38

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/1/jvnet-parent-1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/3/jvnet-parent-3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/4/jvnet-parent-4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/java/jvnet-parent/5/jvnet-parent-5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/10
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/10/oss-parent-10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/11
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/11/oss-parent-11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/16
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/16/oss-parent-16.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/23
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/23/oss-parent-23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/24
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/24/oss-parent-24.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/25
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/25/oss-parent-25.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/27
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/27/oss-parent-27.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/28
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/28/oss-parent-28.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/30
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/30/oss-parent-30.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/33
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/33/oss-parent-33.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/34
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/34/oss-parent-34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4/oss-parent-4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/1
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/1/codehaus-parent-1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/3
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/3/codehaus-parent-3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/4
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/4/codehaus-parent-4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/10
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/10/forge-parent-10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/11
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/11/forge-parent-11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/12
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/12/forge-parent-12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/3
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/3/forge-parent-3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/4
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/4/forge-parent-4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/5
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/5/forge-parent-5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/6
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/6/forge-parent-6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/7
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/7/forge-parent-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/9
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/9/forge-parent-9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/3
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/3/oss-parent-3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/5
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/5/oss-parent-5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/6
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/6/oss-parent-6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/7
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/7/oss-parent-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/9
cp %{SOURCE33} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/9/oss-parent-9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/10
cp %{SOURCE34} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/10/spice-parent-10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/11
cp %{SOURCE35} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/11/spice-parent-11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/12
cp %{SOURCE36} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/12/spice-parent-12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/15
cp %{SOURCE37} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/15/spice-parent-15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/16
cp %{SOURCE38} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/16/spice-parent-16.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/17
cp %{SOURCE39} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/17/spice-parent-17.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/18
cp %{SOURCE40} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/18/spice-parent-18.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/20
cp %{SOURCE41} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/20/spice-parent-20.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/10/oss-parent-10.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/11/oss-parent-11.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/16/oss-parent-16.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/23/oss-parent-23.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/24/oss-parent-24.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/25/oss-parent-25.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/27/oss-parent-27.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/28/oss-parent-28.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/30/oss-parent-30.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/33/oss-parent-33.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/34/oss-parent-34.pom
/usr/share/java/.m2/repository/com/fasterxml/oss-parent/4/oss-parent-4.pom
/usr/share/java/.m2/repository/net/java/jvnet-parent/1/jvnet-parent-1.pom
/usr/share/java/.m2/repository/net/java/jvnet-parent/3/jvnet-parent-3.pom
/usr/share/java/.m2/repository/net/java/jvnet-parent/4/jvnet-parent-4.pom
/usr/share/java/.m2/repository/net/java/jvnet-parent/5/jvnet-parent-5.pom
/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/1/codehaus-parent-1.pom
/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/3/codehaus-parent-3.pom
/usr/share/java/.m2/repository/org/codehaus/codehaus-parent/4/codehaus-parent-4.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/10/forge-parent-10.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/11/forge-parent-11.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/12/forge-parent-12.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/3/forge-parent-3.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/4/forge-parent-4.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/6/forge-parent-6.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/7/forge-parent-7.pom
/usr/share/java/.m2/repository/org/sonatype/forge/forge-parent/9/forge-parent-9.pom
/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/3/oss-parent-3.pom
/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/5/oss-parent-5.pom
/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/6/oss-parent-6.pom
/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
/usr/share/java/.m2/repository/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/10/spice-parent-10.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/11/spice-parent-11.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/12/spice-parent-12.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/16/spice-parent-16.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/17/spice-parent-17.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/18/spice-parent-18.pom
/usr/share/java/.m2/repository/org/sonatype/spice/spice-parent/20/spice-parent-20.pom
