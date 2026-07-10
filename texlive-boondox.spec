%global tl_name boondox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02d
Release:	%{tl_revision}.1
Summary:	Mathematical alphabets derived from the STIX fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/boondox
License:	ofl lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a number of PostScript fonts derived from the STIX
OpenType fonts that may be used in maths mode in regular and bold
weights for calligraphic, fraktur and double-struck alphabets. Virtual
fonts with metrics suitable for maths mode are provided, as are LaTeX
support files.

