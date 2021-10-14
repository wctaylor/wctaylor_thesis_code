# Thesis Code README

This README is inteded to act as a reference for setting up and running
the code used in my thesis.

# Matplotlib Configuration

In order to achieve a uniform look between the $\LaTeX$ of the thesis document
and the text in plots, Matplotlib needs to be configured to use $\LaTeX$ in
the backend. This naturally requires $\LaTeX$ to be installed on the same
machine being used to generate the plots. In my case, I used the Oscar cluster
at Brown to generate my plots. I manually installed TeX Live to my home directory on Oscar. The full details of my installation can be found in `config/texlive.profile`.

## ESCAPE 2021 Summer School

This configuration is based on a presentation in the ESCAPE 2021 summer school.
The associated GitHub repo is here:

[ESCAPE 2021 Publication Quality Matplotlib Repo](https://github.com/escape2020/school2021/tree/main/matplotlib-publication-quality)

And the YouTube video going over the configuration contained in the repo 
is here:

[ESCAPE 2021 Publication Quality Matplotlib Video](https://www.youtube.com/watch?v=gfr2wzCOQYc)

## Thesis Matplotlib Configuration

Configuring Matplotlib (henceforth denoted as MPL) requires two configuration
files
* `config/mpl_thesis_rc`  
A file used to configure MPL. It adjusts a few MPL settings and tells MPL to use
TeX
* `config/mpl_thesis_settings.tex`  
A file used to configure TeX. It sets up TeX to match the thesis style. 