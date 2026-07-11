%global tl_name lccaps
%global tl_revision 46432

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Lowercased (spaced) small capitals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lccaps
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lccaps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This little package serves the purpose of providing a uniform method to
use lowercased small capitals and spaced lowercased small capitals. It
relies on the iftex, textcase, and microtype packages and comes with
four new user macros: \textlcc, the main feature: lowercased small
capitals; \spacedcaps, a prefix to small capitals text commands to
slightly increase their spacing; \textslcc and \textssc, which are
shortcuts for \spacedcaps\textlcc and \spacedcaps\textsc (accordingly).

