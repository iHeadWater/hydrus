FROM continuumio/miniconda3

WORKDIR /hydrus

# Create the environment:
COPY environment-Copy1.yml .
RUN conda env create -f environment-Copy1.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "hydrus", "/bin/bash", "-c"]

# Expose Jupyter port & cmd
EXPOSE 8888