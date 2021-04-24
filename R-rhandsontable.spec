#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rhandsontable
Version  : 0.3.7
Release  : 26
URL      : https://cran.r-project.org/src/contrib/rhandsontable_0.3.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rhandsontable_0.3.7.tar.gz
Summary  : Interface to the 'Handsontable.js' Library
Group    : Development/Tools
License  : MIT
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-magrittr
Requires: R-webshot
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : R-webshot
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n rhandsontable
cd %{_builddir}/rhandsontable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589770939

%install
export SOURCE_DATE_EPOCH=1589770939
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhandsontable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhandsontable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhandsontable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rhandsontable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rhandsontable/DESCRIPTION
/usr/lib64/R/library/rhandsontable/INDEX
/usr/lib64/R/library/rhandsontable/LICENSE
/usr/lib64/R/library/rhandsontable/Meta/Rd.rds
/usr/lib64/R/library/rhandsontable/Meta/features.rds
/usr/lib64/R/library/rhandsontable/Meta/hsearch.rds
/usr/lib64/R/library/rhandsontable/Meta/links.rds
/usr/lib64/R/library/rhandsontable/Meta/nsInfo.rds
/usr/lib64/R/library/rhandsontable/Meta/package.rds
/usr/lib64/R/library/rhandsontable/Meta/vignette.rds
/usr/lib64/R/library/rhandsontable/NAMESPACE
/usr/lib64/R/library/rhandsontable/NEWS
/usr/lib64/R/library/rhandsontable/R/rhandsontable
/usr/lib64/R/library/rhandsontable/R/rhandsontable.rdb
/usr/lib64/R/library/rhandsontable/R/rhandsontable.rdx
/usr/lib64/R/library/rhandsontable/doc/index.html
/usr/lib64/R/library/rhandsontable/doc/intro_rhandsontable.R
/usr/lib64/R/library/rhandsontable/doc/intro_rhandsontable.Rmd
/usr/lib64/R/library/rhandsontable/doc/intro_rhandsontable.html
/usr/lib64/R/library/rhandsontable/help/AnIndex
/usr/lib64/R/library/rhandsontable/help/aliases.rds
/usr/lib64/R/library/rhandsontable/help/paths.rds
/usr/lib64/R/library/rhandsontable/help/rhandsontable.rdb
/usr/lib64/R/library/rhandsontable/help/rhandsontable.rdx
/usr/lib64/R/library/rhandsontable/html/00Index.html
/usr/lib64/R/library/rhandsontable/html/R.css
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/chroma/chroma.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/handsontable/all.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/handsontable/handsontable.full.min.css
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/handsontable/handsontable.full.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/numbro/languages.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/lib/sparkline/jquery.sparkline.min.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/rhandsontable.css
/usr/lib64/R/library/rhandsontable/htmlwidgets/rhandsontable.js
/usr/lib64/R/library/rhandsontable/htmlwidgets/rhandsontable.yaml
/usr/lib64/R/library/rhandsontable/rstudio/addins.dcf
