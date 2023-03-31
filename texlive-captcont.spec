Name:		texlive-captcont
Version:	15878
Release:	2
Summary:	Retain float number across several floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/captcont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The captcont package provides the ability to continue the
numbering in your float environment (figure, table, etc.) with
minimal overhead. This package adds three commands: \caption*,
\captcont, and \captcont*. Along with the \caption command,
these give full control over the caption numbering, caption
text and the entries in the list-of pages. The \caption and
\captcont commands generate list-of page entries. The \caption
and \caption* commands increment the figure or table counter.
Captcont also fully supports the subfigure package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/captcont/captcont.sty
%doc %{_texmfdistdir}/doc/latex/captcont/README
%doc %{_texmfdistdir}/doc/latex/captcont/captcont.pdf
%doc %{_texmfdistdir}/doc/latex/captcont/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/captcont/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/captcont/Makefile
%doc %{_texmfdistdir}/source/latex/captcont/captcont.dtx
%doc %{_texmfdistdir}/source/latex/captcont/captcont.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
