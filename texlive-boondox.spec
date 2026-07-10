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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a number of PostScript fonts derived from the STIX
OpenType fonts that may be used in maths mode in regular and bold
weights for calligraphic, fraktur and double-struck alphabets. Virtual
fonts with metrics suitable for maths mode are provided, as are LaTeX
support files.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/boondox
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/boondox
%dir %{_datadir}/texmf-dist/fonts/map/dvips/boondox
%dir %{_datadir}/texmf-dist/fonts/tfm/public/boondox
%dir %{_datadir}/texmf-dist/fonts/type1/public/boondox
%dir %{_datadir}/texmf-dist/fonts/vf/public/boondox
%doc %{_datadir}/texmf-dist/doc/fonts/boondox/README
%doc %{_datadir}/texmf-dist/doc/fonts/boondox/boondox-doc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/boondox/boondox-doc.tex
%{_datadir}/texmf-dist/fonts/map/dvips/boondox/boondox.map
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-b-cal.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-b-calo.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-b-ds.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-b-frak.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-r-cal.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-r-calo.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-r-ds.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOX-r-frak.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOXUprScr-Bold.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/BOONDOXUprScr-Regular.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbf7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbf8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbl7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbl8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbow7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbw7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxbw8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrf7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrf8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrl7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrl8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrow7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrw7z.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/boondox/zxxrw8a.tfm
%{_datadir}/texmf-dist/fonts/type1/public/boondox/BOONDOXUprScr-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/BOONDOXUprScr-Regular.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxbf8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxbl8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxbw8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxrf8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxrl8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/boondox/zxxrw8a.pfb
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-b-cal.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-b-calo.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-b-ds.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-b-frak.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-r-cal.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-r-calo.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-r-ds.vf
%{_datadir}/texmf-dist/fonts/vf/public/boondox/BOONDOX-r-frak.vf
%{_datadir}/texmf-dist/tex/latex/boondox/BOONDOX-cal.sty
%{_datadir}/texmf-dist/tex/latex/boondox/BOONDOX-calo.sty
%{_datadir}/texmf-dist/tex/latex/boondox/BOONDOX-ds.sty
%{_datadir}/texmf-dist/tex/latex/boondox/BOONDOX-frak.sty
%{_datadir}/texmf-dist/tex/latex/boondox/BOONDOX-uprscr.sty
%{_datadir}/texmf-dist/tex/latex/boondox/uboondox-cal.fd
%{_datadir}/texmf-dist/tex/latex/boondox/uboondox-calo.fd
%{_datadir}/texmf-dist/tex/latex/boondox/uboondox-ds.fd
%{_datadir}/texmf-dist/tex/latex/boondox/uboondox-frak.fd
%{_datadir}/texmf-dist/tex/latex/boondox/uboondoxuprscr.fd
