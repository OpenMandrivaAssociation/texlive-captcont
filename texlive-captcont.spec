%global tl_name captcont
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Retain float number across several floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/captcont
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/captcont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The captcont package provides the ability to continue the numbering in
your float environment (figure, table, etc.) with minimal overhead. This
package adds three commands: \caption*, \captcont, and \captcont*. Along
with the \caption command, these give full control over the caption
numbering, caption text and the entries in the list-of pages. The
\caption and \captcont commands generate list-of page entries. The
\caption and \caption* commands increment the figure or table counter.
Captcont also fully supports the subfigure package.

