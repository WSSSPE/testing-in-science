test:
	py.test -v

all: test summary.pdf citeall.pdf
	

clean:
	cd tests && rm -f *.aux *.log *bbl *.blg *log *pdf *.log
	rm -rf tests/.cache tests/__pycache__
	rm -f *.aux *.log *bbl *.blg *log *pdf *.log
	rm -rf .cache __pycache__
	rm -f citeall.pdf


summary.pdf: summary.tex papers.bib
	pdflatex summary.tex
	bibtex summary
	pdflatex summary.tex
	pdflatex summary.tex


citeall.pdf: tests/citeall.tex papers.bib
	cd tests && pdflatex citeall.tex
	cd tests && bibtex citeall
	cd tests && pdflatex citeall.tex
	cd tests && pdflatex citeall.tex
	cp tests/citeall.pdf citeall.pdf
	@echo "All publications from papers.bib are listed in citeall.pdf"
