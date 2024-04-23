FROM ollama/ollama:latest

ENV OLLAMA_ORIGINS=*
ENV OLLAMA_HOST=0.0.0.0:11434
ENV OLLAMA_MODELS=models/

COPY models models/

ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]