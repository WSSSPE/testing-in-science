test:
	test -v

clean:
	cd tests && rm -f *.aux *.log *bbl *.blg *log *pdf *.log
	rm -rf tests/.cache tests/__pycache__
	rm -f *.aux *.log *bbl *.blg *log *pdf *.log
	rm -rf .cache __pycache__

summary.pdf: summary.tex papers.bib
	pdflatex summary.tex
	bibtex summary
	pdflatex summary.tex
	pdflatex summary.tex


