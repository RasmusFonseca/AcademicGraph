

PAPERS = $(wildcard mag_papers_???.txt) $(wildcard mag_papers_??.txt)
PAPERSC = $(subst .txt,_compr.txt,$(PAPERS))

all: $(PAPERSC)

mag_papers_%.zip:
	wget https://academicgraphv1wu.blob.core.windows.net/aminer/$@

mag_papers_%.txt: mag_papers_%.zip
	unzip $<

mag_papers_%_compr.txt: mag_papers_%.txt
	python compress_mag_papers.py $< > $@

