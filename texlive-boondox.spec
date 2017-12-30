Name:		texlive-boondox
Version:	1.02d
Release:	1
Summary:	Mathematical alphabets derived from the STIX fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/boondox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains a number of PostScript fonts derived from
the STIX OpenType fonts, that may be used in maths mode in
regular and bold weights for calligraphic, fraktur and double-
struck alphabets. Virtual fonts with metrics suitable for maths
mode are provided, as are LaTeX support files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/boondox
%{_texmfdistdir}/fonts/tfm/public/boondox
%{_texmfdistdir}/fonts/type1/public/boondox
%{_texmfdistdir}/fonts/vf/public/boondox
%{_texmfdistdir}/tex/latex/boondox
%doc %{_texmfdistdir}/doc/fonts/boondox

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
