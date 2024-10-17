Name:		texlive-lccaps
Version:	46432
Release:	2
Summary:	Lowercased (spaced) small capitals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lccaps
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This little package serves the purpose of providing a uniform
method to use lowercased small capitals and spaced lowercased
small capitals. It relies on the iftex, textcase, and microtype
packages and comes with four new user macros: \textlcc, the
main feature: lowercased small capitals; \spacedcaps, a prefix
to small capitals text commands to slightly increase their
spacing; \textslcc and \textssc, which are shortcuts for
\spacedcaps\textlcc and \spacedcaps\textsc (accordingly).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lccaps
%{_texmfdistdir}/tex/latex/lccaps
%doc %{_texmfdistdir}/doc/latex/lccaps

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
