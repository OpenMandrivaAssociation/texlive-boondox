Name:		texlive-boondox
Version:	1.0
Release:	1
Summary:	Mathematical alphabets derived from the STIX fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/boondox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boondox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package contains a number of PostScript fonts derived from
the STIX OpenType fonts, that may be used in maths mode in
regular and bold weights for calligraphic, fraktur and double-
struck alphabets. Virtual fonts with metrics suitable for maths
mode are provided, as are LaTeX support files.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/boondox/boondox.map
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-b-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-b-calo.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-b-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-b-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-r-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-r-calo.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-r-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/BOONDOX-r-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbf7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbf8a.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbl7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbl8a.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbow7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbw7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxbw8a.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrf7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrf8a.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrl7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrl8a.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrow7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrw7z.tfm
%{_texmfdistdir}/fonts/tfm/public/boondox/zxxrw8a.tfm
%{_texmfdistdir}/fonts/type1/public/boondox/zxxbf8a.pfb
%{_texmfdistdir}/fonts/type1/public/boondox/zxxbl8a.pfb
%{_texmfdistdir}/fonts/type1/public/boondox/zxxbw8a.pfb
%{_texmfdistdir}/fonts/type1/public/boondox/zxxrf8a.pfb
%{_texmfdistdir}/fonts/type1/public/boondox/zxxrl8a.pfb
%{_texmfdistdir}/fonts/type1/public/boondox/zxxrw8a.pfb
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-b-cal.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-b-calo.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-b-ds.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-b-frak.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-r-cal.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-r-calo.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-r-ds.vf
%{_texmfdistdir}/fonts/vf/public/boondox/BOONDOX-r-frak.vf
%{_texmfdistdir}/tex/latex/boondox/BOONDOX-cal.sty
%{_texmfdistdir}/tex/latex/boondox/BOONDOX-calo.sty
%{_texmfdistdir}/tex/latex/boondox/BOONDOX-ds.sty
%{_texmfdistdir}/tex/latex/boondox/BOONDOX-frak.sty
%{_texmfdistdir}/tex/latex/boondox/uboondox-cal.fd
%{_texmfdistdir}/tex/latex/boondox/uboondox-calo.fd
%{_texmfdistdir}/tex/latex/boondox/uboondox-ds.fd
%{_texmfdistdir}/tex/latex/boondox/uboondox-frak.fd
%doc %{_texmfdistdir}/doc/fonts/boondox/README
%doc %{_texmfdistdir}/doc/fonts/boondox/boondox-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/boondox/boondox-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
