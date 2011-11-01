Name:		texlive-captcont
Version:	2.0
Release:	1
Summary:	Retain float number across several floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/captcont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
