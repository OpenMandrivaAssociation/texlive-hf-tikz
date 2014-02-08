# revision 27457
# category Package
# catalog-ctan /graphics/pgf/contrib/hf-tikz
# catalog-date 2012-08-19 10:23:26 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-hf-tikz
Version:	0.1
Release:	3
Summary:	A simple way to highlight formulas and formula parts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/hf-tikz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hf-tikz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hf-tikz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hf-tikz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a way to highlight formulas and formula
parts in both documents and presentations, us TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hf-tikz/hf-tikz.sty
%doc %{_texmfdistdir}/doc/latex/hf-tikz/README
%doc %{_texmfdistdir}/doc/latex/hf-tikz/hf-tikz.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hf-tikz/hf-tikz.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
